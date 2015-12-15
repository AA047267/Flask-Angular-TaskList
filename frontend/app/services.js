var appServices = angular.module('appServices', []);


appServices.factory('Auth', ['$http', '$localStorage', function ($http, $localStorage) {

    return {
        isAuthenticated: function () {
            return $localStorage.accessToken;
        },
        login: function (credentials) {
            $http.post('http://localhost:5000/api/auth/access_token', credentials)
            .success(function (result) {
                alert('Logged in! result: ' + result);
                $localStorage.accessToken = JSON.stringify(result);
            }).error(function (error) {
                alert('error: ' + error);
            })
        },
        logout: function () {
            // REMEMBER: The backend doesn't care about logouts, delete the token and you're good to go.
            // todo
        }
    }

}]);