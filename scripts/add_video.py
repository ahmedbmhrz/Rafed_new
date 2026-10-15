import re

# 1. Update HTML
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

video_section_html = """
    <!-- Video Album Start -->
    <div class="container-xxl py-6" style="position: relative; z-index: 10;">
        <div class="container">
            <!-- Title -->
            <div class="text-center mx-auto mb-5 wow fadeInUp" data-wow-delay="0.1s">
                <p class="text-primary text-uppercase mb-2 eyebrow" style="font-size: 16px; font-weight: 700; letter-spacing: 2px; color: var(--gold-deep) !important;">ألبوم الفيديو</p>
                <h2 class="display-6 mb-4" style="color: var(--forest);">شاهد احدث الفيديوهات</h2>
            </div>
            
            <!-- Carousel -->
            <div class="owl-carousel video-carousel wow fadeInUp" data-wow-delay="0.3s">
                
                <!-- Item 1 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative; cursor: pointer;">
                        <img src="{% static 'img/rafed_image/background/4.jpg' %}" alt="" style="width: 100%; height: 200px; object-fit: cover;">
                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); transition: 0.3s;"></div>
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s;" class="play-btn">
                            <i class="fa fa-play" style="color: var(--forest); font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700; font-size: 16px;">الفيلم التعريفي لجمعية رافد</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الخميس, 01 أكتوبر 2026</span>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative; cursor: pointer;">
                        <img src="{% static 'img/rafed_image/people/68ecf550ed5e2.png' %}" alt="" style="width: 100%; height: 200px; object-fit: cover; background: var(--paper);">
                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); transition: 0.3s;"></div>
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s;" class="play-btn">
                            <i class="fa fa-play" style="color: var(--forest); font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700; font-size: 16px;">دور الذكاء الاصطناعي في تمكين الأوقاف</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الخميس, 01 أكتوبر 2026</span>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative; cursor: pointer;">
                        <img src="{% static 'img/rafed_image/background/3687745542.jpg' %}" alt="" style="width: 100%; height: 200px; object-fit: cover;">
                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); transition: 0.3s;"></div>
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s;" class="play-btn">
                            <i class="fa fa-play" style="color: var(--forest); font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700; font-size: 16px;">صياغة وتوثيق الوصايا والأوقاف</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الاثنين, 04 مارس 2024</span>
                    </div>
                </div>

                <!-- Item 4 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative; cursor: pointer;">
                        <img src="{% static 'img/rafed_image/people/68ecf45e8f69f.png' %}" alt="" style="width: 100%; height: 200px; object-fit: cover; background: var(--paper);">
                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); transition: 0.3s;"></div>
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s;" class="play-btn">
                            <i class="fa fa-play" style="color: var(--forest); font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700; font-size: 16px;">اللوائح التنظيمية للأوقاف</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الاثنين, 04 مارس 2024</span>
                    </div>
                </div>

                <!-- Item 5 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative; cursor: pointer;">
                        <img src="{% static 'img/rafed_image/background/6aa0f543b127d8.21470575.png' %}" alt="" style="width: 100%; height: 200px; object-fit: cover;">
                        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); transition: 0.3s;"></div>
                        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: rgba(255,255,255,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s;" class="play-btn">
                            <i class="fa fa-play" style="color: var(--forest); font-size: 20px; margin-left: 4px;"></i>
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700; font-size: 16px;">حوكمة الأوقاف</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الاثنين, 04 مارس 2024</span>
                    </div>
                </div>

            </div>
            
            <div class="text-center mt-5">
                <a href="#" class="btn btn-primary rounded py-3 px-5" style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;">عرض كافة الفيديوهات</a>
            </div>
        </div>
    </div>
    <style>
        .video-carousel .content-item:hover .play-btn { transform: translate(-50%, -50%) scale(1.1); background: var(--ds-gold); color: white; }
        .video-carousel .content-item:hover .play-btn i { color: white !important; }
    </style>
    <!-- Video Album End -->
"""

insert_pattern = r'(<!-- Educational Content End -->\n)'
html = re.sub(insert_pattern, r'\1' + video_section_html + '\n', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update JS
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
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
"""
if '.video-carousel' not in js:
    js = js.replace('// Content carousel', new_js + '\n    // Content carousel')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js)

# 3. Update CSS
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add video-carousel to the owl-nav styles
css = css.replace('.content-carousel .owl-nav .owl-prev,', '.content-carousel .owl-nav .owl-prev, .video-carousel .owl-nav .owl-prev,')
css = css.replace('.content-carousel .owl-nav .owl-next {', '.content-carousel .owl-nav .owl-next, .video-carousel .owl-nav .owl-next {')
css = css.replace('.content-carousel .owl-nav .owl-prev:hover,', '.content-carousel .owl-nav .owl-prev:hover, .video-carousel .owl-nav .owl-prev:hover,')
css = css.replace('.content-carousel .owl-nav .owl-next:hover {', '.content-carousel .owl-nav .owl-next:hover, .video-carousel .owl-nav .owl-next:hover {')
css = css.replace('.news-carousel .owl-nav, .content-carousel .owl-nav {', '.news-carousel .owl-nav, .content-carousel .owl-nav, .video-carousel .owl-nav {')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

