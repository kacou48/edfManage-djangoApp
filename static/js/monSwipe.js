var swiper = new Swiper(".reviews-slider", {
  spaceBetween: 20,
  loop: true,
  /*centeredSlide: 'true',*/
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  
  breakpoints:{
      0: {
        slidesPerView: 1,
      },
      450: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
});


var swiper = new Swiper(".blog-slider", {
  spaceBetween: 20,
  loop: true,
  /*centeredSlide: 'true',*/
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  
  breakpoints:{
      0: {
        slidesPerView: 1,
      },
      450: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
});



var swiper = new Swiper(".mySwiper", {
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    renderBullet: function (index, className) {
      return '<span class="' + className + '">' + (index + 1) + "</span>";
    },
  },
});