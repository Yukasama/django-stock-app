
//PROFILE EDITING
const account_name_edit = document.querySelector(".account_name_edit");
const account_name_change = document.querySelector(".account_user_change");
const account_name_hide = document.querySelector(".account_name_hide");
eventHandler(account_name_edit, account_name_change, "click", "add");
eventHandler(account_name_hide, account_name_change, "click", "hide");

const account_verification = document.querySelectorAll(".account_verification");
account_verification.forEach(element => {
    if (element.innerHTML == "Verified") {
        element.style.backgroundColor = "rgb(50, 209, 29)";
    } else {
        element.style.backgroundColor = "red";
    }
})