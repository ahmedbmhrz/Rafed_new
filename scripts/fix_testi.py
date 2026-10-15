import re

# Fix HTML
file_path = 'home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('<div class="col-lg-4 text-center text-lg-start wow fadeInUp" data-wow-delay="0.1s">', '<div class="col-lg-4 text-center text-lg-start">')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Fix CSS
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()
css += '''
.testimonial-carousel .owl-nav .owl-next, .testimonial-carousel .owl-nav .owl-prev {
    background: transparent !important;
    width: auto !important;
    height: auto !important;
    border-radius: 0 !important;
}
.testimonial-carousel .owl-nav {
    left: auto !important;
    right: 0 !important;
    width: 100% !important;
    justify-content: flex-end !important;
}
'''
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Fix JS
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('items: 1', 'responsive: { 0: { items: 1 }, 768: { items: 1 }, 992: { items: 1 } }')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
