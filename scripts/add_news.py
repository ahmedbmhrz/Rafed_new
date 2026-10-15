import re

# 1. Update main.js
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

news_carousel_js = """
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
"""

if '.news-carousel' not in js_content:
    js_content += news_carousel_js
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)


# 2. Update style.css to add some padding/styling to news cards
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

news_css = """
/* News Carousel */
.news-item { border: 1px solid rgba(20, 17, 10, 0.1); border-radius: 12px; overflow: hidden; background: var(--paper); transition: all 0.3s ease; height: 100%; display: flex; flex-direction: column; }
.news-item:hover { box-shadow: 0 10px 30px rgba(12, 59, 46, 0.1); transform: translateY(-5px); }
.news-item img { height: 200px; width: 100%; object-fit: cover; }
.news-content { padding: 20px; flex-grow: 1; display: flex; flex-direction: column; }
.news-content h5 { font-family: var(--font-sans) !important; color: var(--forest); font-size: 16px; font-weight: 700; line-height: 1.5; margin-bottom: 10px; }
.news-content .date { font-family: var(--font-mono); font-size: 12px; color: var(--ink-3); margin-top: auto; }
.news-carousel .owl-nav { position: absolute; top: 50%; width: 100%; transform: translateY(-50%); display: flex; justify-content: space-between; left: 0; padding: 0 20px; pointer-events: none; }
.news-carousel .owl-nav .owl-prev, .news-carousel .owl-nav .owl-next { width: 40px; height: 40px; background: var(--forest) !important; color: #ffffff !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; pointer-events: auto; font-size: 18px; transition: 0.3s; }
.news-carousel .owl-nav .owl-prev:hover, .news-carousel .owl-nav .owl-next:hover { background: var(--ds-gold) !important; }
"""
if '.news-item' not in css_content:
    css_content += news_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 3. Update home_page.html
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

news_html = """
    <!-- News Start -->
    <div class="container-xxl py-6" style="position: relative; z-index: 10;">
        <div class="container">
            <div class="text-center mx-auto mb-5 wow fadeInUp" data-wow-delay="0.1s" style="max-width: 500px;">
                <div style="display:flex;align-items:center;gap:16px;margin-bottom:20px;justify-content:center;">
                  <div style="display:inline-flex;align-items:center;gap:12px;border-radius:9999px;background:var(--ds-gold);padding:6px 18px 6px 6px;flex-shrink:0">
                    <span style="width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,.22);color:var(--forest-3);font-size:14px;flex-shrink:0">◉</span>
                    <span style="font-family:var(--font-display);font-weight:700;font-size:13px;color:var(--forest-3)">الأخبار</span>
                  </div>
                </div>
                <h2 class="display-6 mb-4" style="color: var(--forest);">تعرف على آخر أخبار الجمعية</h2>
            </div>
            <div class="owl-carousel news-carousel wow fadeInUp" data-wow-delay="0.1s">
                <div class="news-item">
                    <img src="{% static 'img/rafed_image/background/3687745542.jpg' %}" alt="News Image">
                    <div class="news-content">
                        <h5>زيارة جمعية رافد للأوقاف لجمعية الدعوة والإرشاد وتوعية الجاليات في الشرائع بمكة المكرمة</h5>
                        <div class="date">الأربعاء, 05 أغسطس 2026</div>
                    </div>
                </div>
                <div class="news-item">
                    <img src="{% static 'img/rafed_image/background/6aa0f543b127d8.21470575.png' %}" alt="News Image">
                    <div class="news-content">
                        <h5>شكر وامتنان لصندوق دعم الجمعيات على دعمهم لمنحة دعم البرامج والمشاريع 2026</h5>
                        <div class="date">الخميس, 10 سبتمبر 2026</div>
                    </div>
                </div>
                <div class="news-item">
                    <img src="{% static 'img/rafed_image/background/4.jpg' %}" alt="News Image">
                    <div class="news-content">
                        <h5>شكر وامتنان لصندوق دعم الجمعيات على دعمهم لمنحة دعم رأس المال البشري 2026</h5>
                        <div class="date">الخميس, 10 سبتمبر 2026</div>
                    </div>
                </div>
                <div class="news-item">
                    <img src="{% static 'img/rafed_image/background/3687745542.jpg' %}" alt="News Image">
                    <div class="news-content">
                        <h5>شراكة وقضية بين «رافد» ولجنة نظار ما وراء النهر</h5>
                        <div class="date">الثلاثاء, 21 يوليو 2026</div>
                    </div>
                </div>
                <div class="news-item">
                    <img src="{% static 'img/rafed_image/background/4.jpg' %}" alt="News Image">
                    <div class="news-content">
                        <h5>ديوانية الأوقاف تستضيف مدير عام الإدارة العامة للأوقاف بمكة المكرمة</h5>
                        <div class="date">الأربعاء, 15 يوليو 2026</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- News End -->
"""

# Replace old unused bakery sections (Product Start through Team End) with the News Section
old_sections_pattern = r'(    <!-- Product Start -->.*?<!-- Team End -->\n)'
html = re.sub(old_sections_pattern, news_html, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added News Section successfully.")
