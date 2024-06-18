const headerMenu = document.querySelector('[data-header="menu"]')

function AnimateMenuScroll() {
    const windowTop = window.pageYOffset;
    if (windowTop > 0) {
        headerMenu.classList.add('menu-shadow')
    }
    else {
        headerMenu.classList.remove('menu-shadow')
    }
}

window.addEventListener('scroll', function() {
    AnimateMenuScroll();
})