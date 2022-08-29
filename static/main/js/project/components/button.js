const icon_button = document.querySelectorAll(".icon_button");
eventHandler(icon_button, 0, "mouseover", "add", "multiple");
eventHandler(icon_button, 0, "mouseleave", "hide", "multiple");

const info = document.querySelectorAll(".info");
const info_icon = document.querySelectorAll(".info_icon");
const infodesc = document.querySelectorAll(".info_desc");
eventHandler(info, 0, "mouseover", "add", "multiple");
eventHandler(info, 0, "mouseleave", "hide", "multiple");
eventHandler(info_icon, 0, "mouseover", "add", "multiple");