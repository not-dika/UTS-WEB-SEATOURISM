// Navbar Scroll Effect
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Form Submission
    const bookingForm = document.getElementById('bookingForm');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simple form validation
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const destination = document.getElementById('destination').value;
            const additional = document.getElementById('additional').value;

            if (name && email && destination) {
                Swal.fire({
                    icon: 'success',
                    title: 'Booking Submitted!',
                    text: `Thank you, ${name}! We'll contact you about your ${destination} trip soon.`,
                    confirmButtonText: 'Great!'
                }).then(() => {
                    // Send POST request after the alert is confirmed
                    fetch('/bookings', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ name, email, destination, additional})
                    })
                    .then(response => {
                        if (response.ok) {
                            // Optionally handle successful response
                            console.log('Booking successfully sent!');
                        } else {
                            // Handle error response
                            console.error('Error sending booking:', response.statusText);
                        }
                    })
                    .catch(error => {
                        console.error('Error sending booking:', error);
                    });
    
                    // Reset the form
                    this.reset();
                });
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Please fill in all required fields!'
                });
            }
        });
    }

    // Add animation to elements on load
    const animateElements = document.querySelectorAll('.animate-on-load');
    animateElements.forEach(el => {
        el.classList.add('animate-on-load');
    });
});