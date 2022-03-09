// array to store what needs to be hidden later. Need to start off these divs to be block and not hidden for the rest of this code to work properly
let hiddenContainers = [
    document.querySelector('.tops-carousel'),
    document.querySelector('.bottoms-carousel'),
    document.querySelector('.onepieces-carousel'),
    document.querySelector('.shoes-carousel'),
    document.querySelector('.accessories-carousel'),
];

document.querySelectorAll('.carousel').forEach(container => {
    const id = container.id;

    const track = document.querySelector(`.${id}-carousel__track`);
    const slides = Array.from(track.children);
    // solves issue when there are no pieces in an outfit
    if(slides.length === 0) {
        return;
    };
    const nextButton = document.querySelector(`.${id}-carousel__button--right`);
    const prevButton = document.querySelector(`.${id}-carousel__button--left`);
    const dotsNav = document.querySelector(`.${id}-carousel__nav`);
    const dots = Array.from(dotsNav.children);
    const slideWidth = slides[0].getBoundingClientRect().width;
    // arrange the slides next to one another
    const setSlidePosition = (slide, index) => {
        slide.style.left = slideWidth * index + 'px';
    };
    slides.forEach(setSlidePosition);

    const moveToSlide = (track, currentSlide, targetSlide) => {
        // move to next slide
        track.style.transform = 'translateX(-' + targetSlide.style.left + ')';
        currentSlide.classList.remove(`${id}-current-slide`);
        currentSlide.classList.remove('current-slide');
        targetSlide.classList.add(`${id}-current-slide`);
        targetSlide.classList.add('current-slide');
    };
    
    const updateDots = (currentDot, targetDot) => {
        currentDot.classList.remove(`${id}-current-slide`);
        currentDot.classList.remove('current-slide');
        targetDot.classList.add(`${id}-current-slide`);
        targetDot.classList.add('current-slide');
    };
    
    const hideShowArrows = (slides, prevButton, nextButton, targetIndex) => {
        if (targetIndex === 0) {
            prevButton.classList.add(`${id}-is-hidden`);
            prevButton.classList.add('is-hidden');
            nextButton.classList.remove(`${id}-is-hidden`);
            nextButton.classList.remove('is-hidden');
        } else if (targetIndex === slides.length - 1) {
            prevButton.classList.remove(`${id}-is-hidden`);
            prevButton.classList.remove('is-hidden');
            nextButton.classList.add(`${id}-is-hidden`);
            nextButton.classList.add('is-hidden');
        } else {
            prevButton.classList.remove(`${id}-is-hidden`);
            prevButton.classList.remove('is-hidden');
            nextButton.classList.remove(`${id}-is-hidden`);
            nextButton.classList.remove('is-hidden');
        }
    };
    if (prevButton){
        // click left
        prevButton.addEventListener('click', e => {
            const currentSlide = track.querySelector(`.${id}-current-slide`);
            const prevSlide = currentSlide.previousElementSibling;
            const currentDot = dotsNav.querySelector(`.${id}-current-slide`);
            const prevDot = currentDot.previousElementSibling;
            const prevIndex = slides.findIndex(slide => slide === prevSlide);
            moveToSlide(track, currentSlide, prevSlide)
            updateDots(currentDot, prevDot)
            hideShowArrows(slides, prevButton, nextButton, prevIndex);
        })   ;     
    };
    if (nextButton){
        // click right
        nextButton.addEventListener('click', e => {
            const currentSlide = track.querySelector(`.${id}-current-slide`);
            const nextSlide = currentSlide.nextElementSibling;
            const currentDot = dotsNav.querySelector(`.${id}-current-slide`);
            const nextDot = currentDot.nextElementSibling;
            const nextIndex = slides.findIndex(slide => slide === nextSlide);
            moveToSlide(track, currentSlide, nextSlide);
            updateDots(currentDot, nextDot)
            hideShowArrows(slides, prevButton, nextButton, nextIndex);
        });
        
    };
    
    if (dotsNav){
        // click nav indicators
        dotsNav.addEventListener('click', e => {
            // what indicator was clicked
            const targetDot = e.target.closest('button');
            
            if (!targetDot) return;
            
            const currentSlide = track.querySelector(`.${id}-current-slide`);
            const currentDot = dotsNav.querySelector(`.${id}-current-slide`);
            const targetIndex = dots.findIndex(dot => dot === targetDot)
            const targetSlide = slides[targetIndex];
            moveToSlide(track, currentSlide, targetSlide);
            updateDots(currentDot, targetDot);
            hideShowArrows(slides, prevButton, nextButton, targetIndex);
            
        });
    };
});

// outfit pages has this div that needs to be hidden after all carousels are set up
if (document.querySelector('#all-pieces')) {
    document.querySelector('#all-pieces').style.display = "none";
};
// return divs back to hidden
hiddenContainers.forEach(container => container.style.display = 'none');