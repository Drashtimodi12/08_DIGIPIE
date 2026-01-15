// This function will run when the form is submitted
function validateForm() {
    // Get the value entered in the "name" input field
    let name = document.getElementById("name").value.trim();

    // Get the value entered in the "age" input field
    let age = document.getElementById("age").value.trim();

    // Get the value entered in the "email" input field
    let email = document.getElementById("email").value.trim();

    // Check if the name is empty
    if (name === "") {
        alert("Please enter your name."); // Show error message
        return false; // Stop form submission
    }

    // Check if the age is empty OR not a number OR less than 1
    if (age === "" || isNaN(age) || Number(age) <= 0) {
        alert("Please enter a valid age.");
        return false;
    }

    // Check if the email is empty OR does not contain "@"
    if (email === "" || !email.includes("@")) {
        alert("Please enter a valid email."); // Show error message
        return false; // Stop form submission
    }

    // If both name and email are valid, allow the form to submit
    return true;
}
