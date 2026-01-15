// Function to change styles of <h1> tags - First version
const tag = () => {
    // Get the first <h1> element on the page
    var h1 = document.getElementsByTagName('h1')[0];
    h1.style.color = 'red';
    h1.style.backgroundColor = 'green';

    // Get the second <h1> element on the page
    var h2 = document.getElementsByTagName('h1')[1];
    h2.style.color = 'white';
    h2.style.backgroundColor = 'blue';
}

// Function to change styles of <h1> tags - Second version
const tag1 = () => {
    var h1 = document.getElementsByTagName('h1')[0];
    h1.style.color = 'white';
    h1.style.backgroundColor = 'blue';

    var h2 = document.getElementsByTagName('h1')[1];
    h2.style.color = 'red';
    h2.style.backgroundColor = 'green';
}

// Function to style a button with ID 'btn'
const btnclk = () => {
    var btn = document.getElementById('btn');
    btn.style.width = '100px';
    btn.style.height = '50px';
    btn.style.backgroundColor = 'blue';
    btn.style.color = 'white';
    btn.style.border = '10px solid black';
}
