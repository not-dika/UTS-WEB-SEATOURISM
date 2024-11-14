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
            const name = this.querySelector('input[type="text"]').value;
            const email = this.querySelector('input[type="email"]').value;
            const destination = this.querySelector('select').value;

            if (name && email && destination) {
                Swal.fire({
                    icon: 'success',
                    title: 'Booking Submitted!',
                    text: `Thank you, ${name}! We'll contact you about your ${destination} trip soon.`,
                    confirmButtonText: 'Great!'
                });
                this.reset();
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