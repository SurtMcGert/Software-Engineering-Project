$(document).foundation();
$(function () {
    setNavbarPosition();
});

window.addEventListener("resize", setNavbarPosition);

//function to set the position of the navbar
function setNavbarPosition() {
    navbar = $(".child2");
    leftPos = $("body,html").width() / 2 - navbar.width() / 2;
    navbar.css("left", leftPos + "px");
}
