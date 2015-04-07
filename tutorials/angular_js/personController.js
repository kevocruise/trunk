angular.module('myApp', []).controller('personCtrl', function($scope) {
    $scope.names = [
        {name:'Kevin',country:'Canada'},
        {name:'Hannah',country:'USA'},
        {name:'Khurrum',country:'England'}
    ];
});