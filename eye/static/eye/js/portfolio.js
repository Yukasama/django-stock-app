//PORTFOLIO TEMPLATE
const portfolio_form_c = document.querySelector(".portfolio_form_c");
const portfolio_createone = document.querySelector(".portfolio_createone");
const portfolio_delete = document.querySelector(".portfolio_delete");
eventHandler(portfolio_createone, portfolio_form_c, "click");
eventHandler(portfolio_delete, portfolio_form_c, "click", "hide");