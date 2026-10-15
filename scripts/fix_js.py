import re
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
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
"""
if '.partner-carousel' not in js:
    js = js.replace('// Testimonials carousel', new_js + '\n    // Testimonials carousel')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)
