{% load staticfiles %}
var count=0;
$(document).ready(function(){
    // Activate Carousel
    $("#myCarousel").carousel();
    
    // Enable Carousel Indicators
    $(".item1").click(function(){
        $("#myCarousel").carousel(0);
    });
    //count+
    count++;
    $(".item2").click(function(){
        $("#myCarousel").carousel(1);
    });
    count++;
    $(".item3").click(function(){
        $("#myCarousel").carousel(2);
    });
