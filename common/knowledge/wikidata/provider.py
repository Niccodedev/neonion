from common.knowledge.provider import Provider
from os import path, makedirs
import config
import wd_download
import wd_extract
import wd_import
import logging


class Wikidata(Provider):

    def __init__(self, elastic_search_url, root_folder):
        self.elastic_search_url = elastic_search_url
        self.root_folder = root_folder
        self.dumps_folder = path.join(self.root_folder, 'dumps')
        self.extract_folder = path.join(self.root_folder, 'extracted_data')

        if not path.exists(self.root_folder):    makedirs(self.root_folder)
        if not path.exists(self.dumps_folder):   makedirs(self.dumps_folder)
        if not path.exists(self.extract_folder): makedirs(self.extract_folder)

        print( path.abspath(self.root_folder) )

    def index(self):
        return 'wikidata'

    def dump(self, types={'person':'http://www.wikidata.org/entity/Q5', 'institute': 'http://www.wikidata.org/entity/Q15916302'}):

        # set up logging to file
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=path.join(self.root_folder, 'maintenance.log'),
                            filemode='a')

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s', "%H:%M:%S")
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        wd_download.download_wd_dump(
            self.dumps_folder,
            logging.getLogger('download'))
        wd_extract.extract_from_wd_dump(
            self.dumps_folder,
            self.extract_folder,
            logging.getLogger('extract'))
        wd_import.import_json_into_es(
            self.extract_folder,
            logging.getLogger('import'))

    def create(self, uri):
        pass

    def edit(self, uri):
        pass

    def delete(self, uri):
        pass