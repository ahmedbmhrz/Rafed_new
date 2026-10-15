import re

# 1. Update home_page.html
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_content_html = """
    <!-- Educational Content Start -->
    <div class="container-xxl py-6 bg-light" style="position: relative; z-index: 10;">
        <div class="container">
            <!-- Title -->
            <div class="text-center mx-auto mb-5 wow fadeInUp" data-wow-delay="0.1s">
                <p class="text-primary text-uppercase mb-2 eyebrow" style="font-size: 16px; font-weight: 700; letter-spacing: 2px; color: var(--gold-deep) !important;">المحتوى التوعوي</p>
                <h2 class="display-6 mb-4" style="color: var(--forest);">تصاميم تثقيفية عن الأوقاف</h2>
            </div>
            
            <!-- Carousel -->
            <div class="owl-carousel content-carousel wow fadeInUp" data-wow-delay="0.3s">
                
                <!-- Item 1 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/ads/ads1.jpg' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 6 صور
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">مسابقة أوقاف الوطن 3 لعام 2025</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الثلاثاء, 21 أكتوبر 2025</span>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/ads/ads2.jpg' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 4 صور
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">مسابقة أوقاف الوطن 2 لعام 2024</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الثلاثاء, 21 أكتوبر 2024</span>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/background/4.jpg' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 13 صورة
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">مسابقة أوقاف الوطن 1 لعام 2023</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الثلاثاء, 21 أكتوبر 2023</span>
                    </div>
                </div>

                <!-- Item 4 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/background/3687745542.jpg' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 11 صورة
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">درر وقفية وغايات الأوقاف</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الأربعاء, 27 أغسطس 2025</span>
                    </div>
                </div>

            </div>
            
            <div class="text-center mt-5">
                <a href="#" class="btn btn-primary rounded py-3 px-5" style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;">عرض كافة الألبومات</a>
            </div>
        </div>
    </div>
    <!-- Educational Content End -->
"""

# Insert between News End and Testimonial Start
insert_pattern = r'(<!-- News End -->\n)'
html = re.sub(insert_pattern, r'\1' + new_content_html + '\n', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update JS
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
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
"""
if '.content-carousel' not in js:
    js = js.replace('// News carousel', new_js + '\n    // News carousel')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

# 3. Update CSS to share arrow styling
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make the news-carousel styles apply to content-carousel too
css = css.replace('.news-carousel .owl-nav', '.news-carousel .owl-nav, .content-carousel .owl-nav')
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

