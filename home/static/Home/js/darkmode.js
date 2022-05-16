
//DARK MODE
let darkMode = localStorage.getItem("darkMode");
const nav_icon_dark = document.querySelector(".nav_icon_dark");
const nav_icon_light = document.querySelector(".nav_icon_light");
const side_item1 = document.querySelector(".side_item1");
const pageicon = document.querySelector(".pageicon");

const enableDarkMode = () => {
    document.body.classList.add("dark");
    localStorage.setItem("darkMode", "enabled");
    pageicon.classList.add("dark");
    nav_icon_dark.classList.add("hide_dark");
    nav_icon_light.classList.add("hide_dark");
};
const disableDarkMode = () => {
    document.body.classList.remove("dark");
    localStorage.setItem("darkMode", null);
    pageicon.classList.remove("dark");
    nav_icon_dark.classList.remove("hide_dark");
    nav_icon_light.classList.remove("hide_dark");
};
if(darkMode === "enabled") {
    enableDarkMode();
};
nav_icon_dark.addEventListener("click", function() {
    darkMode = localStorage.getItem("darkMode");
    if(darkMode !== "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});
nav_icon_light.addEventListener("click", function() {
    darkMode = localStorage.getItem("darkMode");
    if(darkMode !== "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});
side_item1.addEventListener("click", function() {
    darkMode = localStorage.getItem("darkMode");
    if(darkMode !== "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});