
//PROFILE EDITING
const account_name_edit = document.querySelector(".account_name_edit");
const account_name_change = document.querySelector(".account_name_change");
const account_name_hide = document.querySelector(".account_name_hide");
eventHandler(account_name_edit, account_name_change, "click", "add", "once", "blur");
eventHandler(account_name_hide, account_name_change, "click", "hide", "once", "blur");

const account_email_edit = document.querySelector(".account_email_edit");
const account_email_change = document.querySelector(".account_email_change");
const account_email_hide = document.querySelector(".account_email_hide");
eventHandler(account_email_edit, account_email_change, "click", "add", "once", "blur");
eventHandler(account_email_hide, account_email_change, "click", "hide", "once", "blur");


const account_biography_change = document.querySelector(".account_biography_change");
const account_biography_edit = document.querySelector(".account_biography_edit");
const account_biography_buttons = document.querySelector(".account_biography_buttons");
account_biography_edit.addEventListener("click", () => {
    account_biography_change.disabled = false;
    account_biography_buttons.classList.add("show");
})
account_biography_discard.addEventListener("click", () => {
    account_biography_change.disabled = true;
    account_biography_buttons.classList.remove("show");
})

const account_verification = document.querySelectorAll(".account_verification");
account_verification.forEach(element => {
    if (element.innerHTML == "Verified") {
        element.style.backgroundColor = "rgb(50, 209, 29)";
    } else {
        element.style.backgroundColor = "red";
    }
})