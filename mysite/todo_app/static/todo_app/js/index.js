$(document).ready(function() {
    var $burger = $(".burger");
    var $navLinksWrapper = $(".links");
    var $navLinks = $(".nav-links  li");


    $burger.on("click", function() {
        $navLinksWrapper.toggleClass("toggle-nav");   
        $(this).toggleClass("cross");
    });
})