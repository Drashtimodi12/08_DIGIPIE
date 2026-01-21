// This function will run when the form is submitted
function validateForm() {
    // Get the value entered in the "name" input field
    let name = document.getElementById("name").value;

    // Get the value entered in the "email" input field
    let email = document.getElementById("email").value;

    // Check if the name is empty
    if (name === "") {
        alert("Please enter your name."); // Show error message
        return false; // Stop form submission
    }

    // Check if the email is empty OR does not contain "@"
    if (email === "" || !email.includes("@")) {
        alert("Please enter a valid email."); // Show error message
        return false; // Stop form submission
    }

    // If both name and email are valid, allow the form to submit
    return true;
}
