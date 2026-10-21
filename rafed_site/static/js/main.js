(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Fixed Navbar
    $('.fixed-top').css('top', $('.top-bar').height());
    $(window).scroll(function () {
        if ($(this).scrollTop()) {
            $('.fixed-top').addClass('bg-dark').css('top', 0);
        } else {
            $('.fixed-top').removeClass('bg-dark').css('top', $('.top-bar').height());
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: false, rtl: true,
        smartSpeed: 1500,
        loop: true,
        nav: true,
        dots: false,
        responsive: { 0: { items: 1 }, 768: { items: 1 }, 992: { items: 1 } },
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ]
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    
    // Partner carousel
    $(".partner-carousel").owlCarousel({
        autoplay: true, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ],
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:3 },
            1200:{ items:4 }
        }
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ],
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:2 }
        }
    });

    
    // Video carousel
    $(".video-carousel").owlCarousel({
        autoplay: false, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ],
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:3 },
            1200:{ items:4 }
        }
    });

    // Content carousel
    $(".content-carousel").owlCarousel({
        autoplay: true, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ],
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:3 },
            1200:{ items:4 }
        }
    });

    // News carousel
    $(".news-carousel").owlCarousel({
        autoplay: true, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-right"></i>',
            '<i class="bi bi-chevron-left"></i>'
        ],
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:3 },
            1200:{ items:4 }
        }
    });

    // Services carousel (Dedicated Services Page)
    var $servicesCarousel = $(".services-carousel");
    if ($servicesCarousel.length && !$servicesCarousel.hasClass("owl-loaded")) {
        $servicesCarousel.owlCarousel({
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            rtl: true,
            smartSpeed: 700,
            loop: true,
            center: true,
            dots: true,
            nav: true,
            navText : [
                '<i class="bi bi-chevron-right"></i>',
                '<i class="bi bi-chevron-left"></i>'
            ],
            responsive: {
                0: { 
                    items: 1, 
                    margin: 15 
                },
                768: { 
                    items: 2.2, 
                    margin: 20 
                },
                1100: { 
                    items: 3, 
                    margin: 25 
                }
            }
        });

        $(document).on('click', '.services-carousel .owl-item:not(.center)', function() {
            var $this = $(this);
            var $center = $('.services-carousel .owl-item.center');
            if ($this.index() > $center.index()) {
                $servicesCarousel.trigger('next.owl.carousel');
            } else {
                $servicesCarousel.trigger('prev.owl.carousel');
            }
        });
    }

})(jQuery);
