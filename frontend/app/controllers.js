var appControllers = angular.module('appControllers', []);

appControllers.controller('LoginController', ['$scope', '$state', 'Auth', function ($scope, $state, Auth) {

    if (Auth.isAuthenticated() !== undefined) {
        $state.go('app.dashboard');
    }

    $scope.login = function (user) {
        Auth.login({'username': user.name, 'password': user.password});
    };


}]);

appControllers.controller('HomeController', function ($scope) {

    $scope.message = 'Welcome Secret Message!';

});
