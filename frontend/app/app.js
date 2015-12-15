var app = angular.module('MyApp', ['ui.router', 'appControllers', 'appServices', 'ngStorage']);

app.config(function ($stateProvider, $urlRouterProvider) {

    $urlRouterProvider
        .otherwise('/login');

    $stateProvider
        .state('login', {
            url: '/login',
            templateUrl: '/partials/login-partial.html',
            controller: 'LoginController',
            authenticate: false
        })
        .state('app', {
            url: '/app',
            templateUrl: '/partials/home.html',
            abstract: true,
            authenticate: true
        })
        .state('app.dashboard', {
            url: '/dashboard',
            templateUrl: '/partials/home-partial.html',
            controller: 'HomeController',
            authenticate: true
        });
});

app.run(function ($rootScope, Auth, $state) {

    $rootScope.$on('$stateChangeStart', function (event, toState) {
        if (toState.authenticate && Auth.isAuthenticated() === undefined) {
            event.preventDefault();
            $state.go('login');
        }
    });
});
