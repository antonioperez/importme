var app = angular.module('importme', ['ngRoute', 'ngSanitize']);

app.directive('topNav', function(){
	return {
		restrict: 'A', 
		templateUrl: '/static/app/views/shared/navi/top_nav.html', 
		controller: function ($scope, $location){
			$scope.isActive === $location.path();
		},
		controllerAs:'navi'
	};
});


app.controller('UserController', ['$scope', '$http', '$location',  function($scope, $http, $location){
	$scope.user = {};
	$scope.loginInfo = {};
	$scope.errorMessage = '';
	this.loginUser = function(){

		$http.post('/login/', $scope.loginInfo).success(function(data){
			$scope.user = data;
			$scope.errorMessage = data['message'];
			$location.path( "/" );
		})
		.error (function(data, status){
			console.log(data['message']);
			$scope.errorMessage = data['message'];
		});
	}

}]);

app.controller('PortfolioController', ['$scope', '$http', '$location',  function($scope, $http, $location){
	$scope.projects = {};
	$scope.errorMessage = '';
	this.getProjects = function(){
		$http.get('/portfolio/projects/').success(function(data){
			$scope.projects = data;
			$scope.errorMessage = data['message'];
		})
		.error (function(data, status){
			console.log(data['message']);
			$scope.errorMessage = data['message'];
		});
	}

}]);

app.controller('BlogController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
	
	$scope.posts = [];
	$scope.tagOpts = [];
	
  	var username = $routeParams.username;
  	var postTitle = $routeParams.id;

	this.getPosts = function(){

		var url = '/blog/posts/';
		if (postTitle) {
			url = url + postTitle +'/';
		}

		console.log(url);

		$http.get(url).success(function(data, status){
			$scope.posts = data;
		})
		.error(function(data, status){


		});
	}

	this.getTags = function(){
		$http.get('/blog/tags/').success(function(data, status){
			$scope.tagOpts = data;
		})
	}

	$scope.newPost = {
		tags : []
	}
	this.createPost = function(){
		$http.post('/blog/posts/', $scope.newPost).success(function(data, status){
			$scope.posts.push(data);
			$scope.newPost = {};
			$location.path( "/" );
		}).error(function(data, status){

		});
	}
}]);


app.config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	$routeProvider
	.when('/', 
		{
			templateUrl:'/static/app/views/blog/front.html', 
			controller: 'BlogController'
		})
	.when('/:username/posts/:id', 
		{
			templateUrl:'/static/app/views/blog/front.html', 
			controller: 'BlogController'

		})
	.when('/create/post', 
		{
			templateUrl:'/static/app/views/blog/create_post.html', 
			controller: 'BlogController'

		})
	.when('/login', 
		{
			templateUrl:'/static/app/views/user/login.html', 
			controller: 'UserController'

		})
	.when('/portfolio', 
		{
			templateUrl:'/static/app/views/portfolio/portfolio.html', 
			controller: 'PortfolioController'

		})
	//.otherwise({ redirectTo: '/' });

}]);







