$(document).ready(function() {
    var $burger = $(".burger");
    var $navLinksWrapper = $(".links");
    var $username = $("#id_username");
    var $email = $("#id_email");
    var $password1 = $("#id_password1");
    var $password2 = $("#id_password2");
    var $login_password = $("#id_password");





    $burger.on("click", function() {
        $navLinksWrapper.toggleClass("toggle-nav");   
        $(this).toggleClass("cross");
    });

    $username.attr({
        "placeholder": "Username"
    });
    $email.attr({
        "placeholder": "Email"
    });
    $password1.attr({
        "placeholder": "Password"
    });
    $password2.attr({
        "placeholder": "Confirm Password"
    })
    $login_password.attr({
        "placeholder": "Password"
    });

    window.addEventListener("load", () => {
        $username.focus();
        $(".todo-form-wrapper .form .form-group div input").focus();
    });

})