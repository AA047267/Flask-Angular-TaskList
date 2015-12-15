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
        }
    }

}]);


appServices.service('TaskServices' ['$http', function($http) {

    $http.defaults.headers.post["Content-Type"] = "application/json";

    return {
        getTasks: function () {
            return $http.get('http://localhost:5000/api/tasks');
        },
        getTask: function (taskId) {
            return $http.get('http://localhost:5000/api/tasks/' + taskId);
        },
        postTask: function() {
            return $http.post();
        }


    }

}]);