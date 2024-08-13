let lastScrollTop = 0;
const header = document.getElementById('header');

window.addEventListener('scroll', () => {
  let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

  if (currentScroll > lastScrollTop) {
    // Scrolling down
    header.style.top = '-120px'; // Adjust this value to the height of the header
    // header.style.backdropFilter = 'blur(10px)';
  } else {
    // Scrolling up
    header.style.top = '0';
    // header.style.background ='#222';
  }

  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // For Mobile or negative scrolling
});
