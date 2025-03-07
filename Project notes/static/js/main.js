// change navbar styles on scroll

window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle
    ('window-scroll',window.scrollY > 0)
})

////show/hide faq answer

const faqs = document.querySelectorAll('.faq');

faqs.forEach(faq => {
    faq.addEventListener('click',() => {
        faq.classList.toggle('open');

        // change icon
        const icon = faq.querySelector('.faq__icon i');
        if(icon.className === 'fa-solid fa-plus'){
            icon.className = "fa-solid fa-minus";
        } else{
            icon.className = "fa-solid fa-plus";
        }
    })
})
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});