// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code can go here

    // Example: Display an alert when a job listing is clicked
    const jobLinks = document.querySelectorAll('ul li a');
    jobLinks.forEach(link => {
        link.addEventListener('click', function() {
            alert('You clicked on a job listing!');
        });
    });
});
