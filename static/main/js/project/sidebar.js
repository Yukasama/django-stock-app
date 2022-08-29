const sidenavbar = document.querySelector(".sidenavbar");
const hamburger1 = document.querySelector(".hamburger1");
eventHandler(hamburger1, sidenavbar, "click", "window"); //SIDENAVBAR (MOBILE NAVBAR)
const sidenav_header = document.querySelectorAll(".sidenav_header")
activeLooper(sidenav_header, "list"); //SIDENAVBAR ACTIVE HOVER ANIMATION

if ($(document.querySelector(".sidebar")).is(":visible")) {
  var sidebar = document.querySelector(".sidebar");
  var content = document.querySelector(".content");
  content.classList.add("sidebar_active");
  eventHandler(sidebar, content, "mouseover", "add");
  eventHandler(sidebar, content, "mouseleave", "hide");
} else {
  console.log("No Sidebar detected.");
}

const side_link = document.querySelectorAll(".side_link");
const view = document.querySelectorAll(".view");
activeLooper(side_link, "navtabs", view);