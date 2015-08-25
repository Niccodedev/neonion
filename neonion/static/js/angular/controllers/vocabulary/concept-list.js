neonionApp.controller('ConceptListCtrl', ['$scope', '$sce', 'CommonService', 'ConceptService', 'PropertyService',
        function ($scope, $sce, CommonService, ConceptService, PropertyService) {
            "use strict";

            $scope.style = {
                compact: true
            }
            $scope.locales = {
                // TODO localize
                create: "New Concept"
            };

            $scope.queryConcepts = function () {
                return ConceptService.query(function (data) {
                    $scope.resources = data;
                }).$promise;
            };

            $scope.queryProperties = function () {
                return PropertyService.query(function (data) {
                    $scope.properties = data;
                }).$promise;
            };

            $scope.getItemHeader = function (resource) {
                return $sce.trustAsHtml(resource.label);
            };

            $scope.getItemSubHeader = function (resource) {
                return "";
            };

            $scope.getItemDescription = function (resource) {
                return $sce.trustAsHtml(resource.comment);
            };

            $scope.filterResources = function (resource) {
                if (CommonService.filter.query.length > 0) {
                    return resource.label.toLowerCase().indexOf(CommonService.filter.query.toLowerCase()) != -1;
                    ;
                }
                return true;
            }

            // execute promise chain
            $scope.queryConcepts();

        }]
);