const icon = document.querySelector('.navbar-icon');
const menu = document.querySelector('.navbar-menu');
const span = document.querySelector('.span')

function toggleNavbar() {
    menu.classList.toggle('active');
    icon.classList.toggle('active');
}

document.querySelector('.navbar-toggle-btn').addEventListener('click', function () {
    toggleNavbar();
});