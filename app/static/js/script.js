// Toggle hamburger menu

const burgerIcon = document.querySelector('#Burger');
const navBarMenu = document.querySelector('#Nav-links')

burgerIcon.addEventListener('click', () => {
  burgerIcon.classList.toggle('is-active')
  navBarMenu.classList.toggle('is-active')
});