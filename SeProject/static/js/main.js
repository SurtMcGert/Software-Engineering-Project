$(document).foundation();
$(function () {
    insertPagePaddingOnNormaPages();
    setNavbarPosition();
});

window.addEventListener("resize", setNavbarPosition);

//function to set the position of the navbar
function setNavbarPosition() {
    navbar = $(".child2");
    mainButtons = $(".mainButtons");
    leftPos = $("body,html").outerWidth() / 2;
    leftPos = leftPos - navbar.outerWidth() / 2;
    leftPos = leftPos + mainButtons.outerWidth() / 2;
    navbar.css("left", leftPos + "px");
    $("nav").css("visibility", "visible");
}
//function to insert padding at the top of normal pages so the nav bar doesnt overlap content on the page
function insertPagePaddingOnNormaPages() {
    pageArea = $(".pageArea");
    if (pageArea.is(":empty")) {
        //if there is no normal page, delete this area
        $(".normalPageBlock").remove();
    }
}
