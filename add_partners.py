import re

html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

partners_html = """
    <!-- Partners Start -->
    <div class="container-fluid py-6 bg-white" style="border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); position: relative; z-index: 10;">
        <div class="container">
            <div class="row g-5 align-items-center">
                
                <!-- Right Side: Text & Button (col-lg-4) -->
                <div class="col-lg-3 text-center text-lg-end wow fadeInUp" data-wow-delay="0.1s">
                    <div class="d-flex align-items-center justify-content-center justify-content-lg-start mb-2">
                        <div style="flex: 1; height: 1px; background: var(--ds-gold); opacity: 0.5;"></div>
                        <h2 class="display-6 mx-3 mb-0" style="color: var(--forest); white-space: nowrap;">شركاؤنا</h2>
                        <div style="flex: 1; height: 1px; background: var(--ds-gold); opacity: 0.5;"></div>
                    </div>
                    <p class="text-uppercase mb-4 eyebrow" style="font-size: 16px; font-weight: 700; letter-spacing: 1px; color: var(--ink-3) !important;">شركاء النجاح</p>
                    <a href="#" class="btn btn-primary rounded py-3 px-4 w-100" style="font-weight: bold;">عرض كافة الشركاء</a>
                </div>

                <!-- Left Side: Carousel (col-lg-9) -->
                <div class="col-lg-9 wow fadeInUp" data-wow-delay="0.3s">
                    <div class="owl-carousel partner-carousel">
                        <!-- Partner 1 -->
                        <div class="partner-item text-center">
                            <img class="img-fluid mx-auto mb-3" src="{% static 'img/rafed_image/partners/675acf3938b1f.png' %}" alt="" style="height: 90px; width: auto; object-fit: contain;">
                            <h6 style="color: var(--ink-2); font-size: 14px;">الهيئة العامة للأوقاف</h6>
                        </div>
                        <!-- Partner 2 -->
                        <div class="partner-item text-center">
                            <img class="img-fluid mx-auto mb-3" src="{% static 'img/rafed_image/partners/675acf7988383.png' %}" alt="" style="height: 90px; width: auto; object-fit: contain;">
                            <h6 style="color: var(--ink-2); font-size: 14px;">جمعية الشقائق</h6>
                        </div>
                        <!-- Partner 3 -->
                        <div class="partner-item text-center">
                            <img class="img-fluid mx-auto mb-3" src="{% static 'img/rafed_image/partners/675acfa128973.png' %}" alt="" style="height: 90px; width: auto; object-fit: contain;">
                            <h6 style="color: var(--ink-2); font-size: 14px;">شركة التحول التقني</h6>
                        </div>
                        <!-- Partner 4 -->
                        <div class="partner-item text-center">
                            <img class="img-fluid mx-auto mb-3" src="{% static 'img/rafed_image/partners/675acfc2140c4.png' %}" alt="" style="height: 90px; width: auto; object-fit: contain;">
                            <h6 style="color: var(--ink-2); font-size: 14px;">السبيعي الخيرية</h6>
                        </div>
                        <!-- Partner 5 -->
                        <div class="partner-item text-center">
                            <img class="img-fluid mx-auto mb-3" src="{% static 'img/rafed_image/partners/675acfd1d1b20.png' %}" alt="" style="height: 90px; width: auto; object-fit: contain;">
                            <h6 style="color: var(--ink-2); font-size: 14px;">مؤسسة سليمان الراجحي</h6>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
    <!-- Partners End -->
"""

insert_pattern = r'(<!-- Video Album End -->\n)'
html = re.sub(insert_pattern, r'\1\n' + partners_html + '\n', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# Update JS
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
    js = js.replace('// Testimonial carousel', new_js + '\n    // Testimonial carousel')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)


# Update CSS to share the arrow styles
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I will just write a specific style block for partner-carousel to keep it clean, 
# because adding it to the massive comma-separated selector might get messy, but actually the comma separated selector is fine.
# Wait, let's just use the exact string replacement to be safe.
css = css.replace('.video-carousel .owl-nav {', '.video-carousel .owl-nav, .partner-carousel .owl-nav {')
css = css.replace('.video-carousel .owl-nav .owl-prev,', '.video-carousel .owl-nav .owl-prev, .partner-carousel .owl-nav .owl-prev,')
css = css.replace('.video-carousel .owl-nav .owl-next {', '.video-carousel .owl-nav .owl-next, .partner-carousel .owl-nav .owl-next {')
css = css.replace('.video-carousel .owl-nav .owl-prev:hover,', '.video-carousel .owl-nav .owl-prev:hover, .partner-carousel .owl-nav .owl-prev:hover,')
css = css.replace('.video-carousel .owl-nav .owl-next:hover {', '.video-carousel .owl-nav .owl-next:hover, .partner-carousel .owl-nav .owl-next:hover {')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

