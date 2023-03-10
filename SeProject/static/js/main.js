$(document).foundation();
$(function () {
    setProjectLogoCell();
});
//function to resize an element
function resizeElem(elem, newWidth) {
    elem.width = newWidth;
}
//function to set the hight of the cell for projectLogo
function setProjectLogoCell() {
    const cell = document.getElementById("projectLogoCell");
    const logos = document.getElementsByClassName("projectLogo");
    if (cell != null && logos != null) {
        var height;
        var width;
        for (var logo of logos) {
            if (window.getComputedStyle(logo).display != "none") {
                height = logo.height;
                width = logo.width + 10;
            }
        }
        cell.setAttribute("style", "height: " + height + "px!important; " + "width: " + width + "px!important;");
    }
}

window.addEventListener("resize", setProjectLogoCell);