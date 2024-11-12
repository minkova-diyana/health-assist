const menuButtonElement = document.querySelector('#menue');
const closeMenuButtonElement = document.querySelector('#close');
const navLinksElement = document.getElementById('navLinks');
const flagElement = document.querySelector('.flag-image');


function showMenu(){
    closeMenuButtonElement.style.display = 'block';
    menuButtonElement.style.display = 'none';
    navLinksElement.style.right = '0';
    flagElement.style.display = 'block';
    flagElement.style.right = '50px';
}
function closeMenu(){
    closeMenuButtonElement.style.display = 'none';
    menuButtonElement.style.display = 'block';
    navLinksElement.style.right = '-200px';
    flagElement.style.display = 'none';
    flagElement.style.right = '-200px';
}



menuButtonElement.addEventListener('click', showMenu);
closeMenuButtonElement.addEventListener('click', closeMenu);
