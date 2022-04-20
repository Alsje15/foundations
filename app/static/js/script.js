// Toggle hamburger menu

const burgerIcon = document.querySelector('#Burger');
const navBarMenu = document.querySelector('#Nav-links')

burgerIcon.addEventListener('click', () => {
  burgerIcon.classList.toggle('is-active')
  navBarMenu.classList.toggle('is-active')
});


// Adjust form input based on text
function Expand(obj){
  if (!obj.savesize) obj.savesize=obj.size;
  obj.size=Math.max(obj.savesize,obj.value.length);
 }