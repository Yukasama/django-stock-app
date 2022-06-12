
//PROFILE
const profile = document.querySelector(".profile");
const profile_container = document.querySelector(".profile_container");
eventHandler(profile, profile_container, "click", "show");


//PORTFOLIO CREATE FIELD
const portfolio_form_c = document.querySelector(".portfolio_form_c");
const portfolio_createone = document.querySelector(".portfolio_createone");
const portfolio_delete = document.querySelector(".portfolio_delete");
eventHandler(portfolio_createone, portfolio_form_c, "click");
eventHandler(portfolio_delete, portfolio_form_c, "click", "remove");

