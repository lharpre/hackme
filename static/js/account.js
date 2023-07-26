/** Login & Account Variables */
const login_Form = document.getElementById("form-login");
const register_Form = document.getElementById("form-reg");
const register_Password = document.getElementById("reg-pass");

function register() {
    hideElement(login_Form);
    hideElement(register_Password);
    showElement(register_Form);
}

function newRegister() {
    showElement(login_Form);
    showElement(register_Password);
    hideElement(register_Form);
}

function hideElement(e) {
    e.style.display = "none";
}
function showElement(e) {
    e.style.display = "flex";
}