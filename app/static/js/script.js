// Navigation active state
document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.style.opacity = '0.5';
        }
    });
});

// Form submission handler
function submitForm(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Images uploaded successfully!');
        form.reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error uploading images');
    });
}
