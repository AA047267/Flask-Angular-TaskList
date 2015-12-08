angular.module('MyApp', ['ui.router'])
  .config(function($stateProvider, $urlRouterProvider) {


        $urlRouterProvider
            .otherwise('/home');

         $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: '/partials/home-partial.html',
            controller: 'HomeCtrl'
        });

  });