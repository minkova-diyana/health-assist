const menuButtonElement = document.querySelector('#menue');
const closeMenuButtonElement = document.querySelector('#close');
const navLinksElement = document.getElementById('navLinks');
const flagElement = document.querySelector('.flag-image');
const showMoreButtonElement = document.querySelectorAll('.show-more');
const hidenTextElement = document.querySelectorAll('.hiden-info');
const showLessElementBtn = document.querySelectorAll('.show-less');

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

function showMore(event){
    const parent = event.target.closest('.news-container');
    const hiddenText = parent.querySelector('.hiden-info');
    const showLessButton = parent.querySelector('.show-less');
    const showMoreButton = event.target;

    hiddenText.style.display = 'block';
    showLessButton.style.display = 'block';
    showMoreButton.style.display = 'none';
}

function showLess(event){
    const parent = event.target.closest('.news-container');
    const hiddenText = parent.querySelector('.hiden-info');
    const showLessButton = event.target;
    const showMoreButton = parent.querySelector('.show-more');

    hiddenText.style.display = 'none';
    showLessButton.style.display = 'none';
    showMoreButton.style.display = 'block';
}

menuButtonElement.addEventListener('click', showMenu);
closeMenuButtonElement.addEventListener('click', closeMenu);
showMoreButtonElement.forEach((element) => {
    element.addEventListener('click', showMore)
});
showLessElementBtn.forEach((element) => {
    element.addEventListener('click', showLess)
});
