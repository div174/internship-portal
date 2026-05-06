document.addEventListener('DOMContentLoaded', () => {
    // Delete Confirmation with SweetAlert2
    const deleteForms = document.querySelectorAll('.delete-form');
    
    deleteForms.forEach(form => {
        const btn = form.querySelector('.delete-btn');
        if (btn) {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                
                Swal.fire({
                    title: 'Are you sure?',
                    text: "You won't be able to revert this!",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#ef4444',
                    cancelButtonColor: '#64748b',
                    confirmButtonText: 'Yes, delete it!',
                    background: '#ffffff',
                    borderRadius: '12px',
                }).then((result) => {
                    if (result.isConfirmed) {
                        form.submit();
                    }
                });
            });
        }
    });

    // Animate numbers on dashboard
    const counters = document.querySelectorAll('.counter');
    const speed = 50;

    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.innerText;
            const count = +counter.getAttribute('data-count') || 0;
            const inc = target / speed;

            if (count < target) {
                counter.setAttribute('data-count', Math.ceil(count + inc));
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };

        const targetText = counter.innerText;
        counter.innerText = '0';
        counter.innerText = targetText; 
        updateCount();
    });
});
