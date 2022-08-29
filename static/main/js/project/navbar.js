//Navbar is already declared in event.js
eventHandler(window, navbar, "scroll", "show"); //SCROLL-STICKY NAVBAR

const profile = document.querySelector(".profile");
const profile_wrapper = document.querySelector(".profile_wrapper");
eventHandler(profile, profile_wrapper, "click", "show");
eventHandler(profile_wrapper, 0, "mouseleave", "hide"); //PROFILE CONTAINER