$(document).ready(function(){
    $('.js--wp-1').waypoint(function(direction){
        $('.js--wp-1').addClass('animated slideInRight');
    },{offset:'80%'})
    $('.js--wp-2').waypoint(function(direction){
        $('.js--wp-2').addClass('animated slideInLeft');
    },{offset:'70%'})
    $('.js--wp-3').waypoint(function(direction){
        $('.js--wp-3').addClass('animated slideInRight');
    },{offset:'70%'})

});