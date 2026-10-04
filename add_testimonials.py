import re

# 1. Update home_page.html
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_testimonial_html = """
    <!-- Testimonial Start -->
    <div class="container-xxl py-6" style="position: relative; z-index: 10;">
        <div class="container">
            <div class="row g-5 align-items-center">
                <!-- Title Column (Right in RTL) -->
                <div class="col-lg-4 text-center text-lg-start wow fadeInUp" data-wow-delay="0.1s">
                    <h2 class="display-5 mb-3" style="color: var(--forest); font-family: var(--font-display); font-weight: 700;">قالوا عنا</h2>
                    <p class="mb-4" style="color: var(--ink-2); font-size: 18px; font-weight: 500;">سعداء دائما بخدمتكم</p>
                    <a href="#" class="btn btn-primary rounded py-3 px-4" style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;">عرض كافة التزكيات</a>
                </div>
                
                <!-- Carousel Column (Left in RTL) -->
                <div class="col-lg-8 wow fadeInUp" data-wow-delay="0.3s">
                    <div class="owl-carousel testimonial-carousel">
                        <!-- Item 1 -->
                        <div class="testimonial-card">
                            <img class="testimonial-img" src="{% static 'img/rafed_image/people/68ecf41bf2f63.png' %}" alt="">
                            <div class="testimonial-header-info text-end">
                                <h5 class="mb-1 text-primary" style="font-family: var(--font-sans); font-weight: 700; color: var(--gold-deep) !important;">د. خالد عبدالله السريحي</h5>
                                <span style="font-size: 13px; color: var(--ink-2);">المدير العام للمركز الدولي للأبحاث والدراسات ( مداد )</span>
                            </div>
                            <div class="testimonial-content">
                                <div class="text-end mb-3">
                                    <i class="fa fa-quote-right fa-4x text-primary quote-icon"></i>
                                </div>
                                <p class="fs-6 mb-0 text-end" style="color: var(--ink-2); line-height: 1.8;">بسم الله الرحمن الرحيم الحمد لله رب العالمين والصلاة والسلام على أشرف المرسلين وبعد شرفت اليوم الاثنين تسعة ربيع الأول من عام 1447 هجري بالمشاركة في ديوانية رافد... الأوقاف من خلال تقديم موضوع استشراف المستقبل الأوقاف خلال عشر سنوات قادمة وما شاهدته من التفاعل والمشاركات والمبادرات التي خرجت أثناء اللقاء وعليه فإنني أدعو جميع الفضلاء من أهل العلم وأهل التجارة بالمساهم مع الإخوة في جمعية رافد لمساعدتهم ومشاركتهم في تنفيذ مثل هذه البرامج والفعاليات والحمد لله الذي تتم بنعمته الصالحات.</p>
                            </div>
                        </div>
                        
                        <!-- Item 2 -->
                        <div class="testimonial-card">
                            <img class="testimonial-img" src="{% static 'img/rafed_image/people/68ecf45e8f69f.png' %}" alt="">
                            <div class="testimonial-header-info text-end">
                                <h5 class="mb-1 text-primary" style="font-family: var(--font-sans); font-weight: 700; color: var(--gold-deep) !important;">د. أنس بن عبدالوهاب</h5>
                                <span style="font-size: 13px; color: var(--ink-2);">أكاديمي وباحث في شؤون الأوقاف</span>
                            </div>
                            <div class="testimonial-content">
                                <div class="text-end mb-3">
                                    <i class="fa fa-quote-right fa-4x text-primary quote-icon"></i>
                                </div>
                                <p class="fs-6 mb-0 text-end" style="color: var(--ink-2); line-height: 1.8;">الحمد لله رب العالمين، والصلاة والسلام على أشرف الأنبياء والمرسلين نبينا محمد وعلى آله وصحبه أجمعين، لقد سررت هذا المساء بلقاء ثلة من الفضلاء والمهتمين بالعمل الوقفي، في ديوانية رافد للأوقاف بمكة المكرمة والتي كان لها دور بارز في نشر ثقافة الوقف والتوعية بأهميته في المجتمع.</p>
                            </div>
                        </div>

                        <!-- Item 3 -->
                        <div class="testimonial-card">
                            <img class="testimonial-img" src="{% static 'img/rafed_image/people/68ecf49e3c05a.png' %}" alt="">
                            <div class="testimonial-header-info text-end">
                                <h5 class="mb-1 text-primary" style="font-family: var(--font-sans); font-weight: 700; color: var(--gold-deep) !important;">الشيخ صالح بن عواد المغامسي</h5>
                                <span style="font-size: 13px; color: var(--ink-2);">إمام وخطيب مسجد قباء سابقاً</span>
                            </div>
                            <div class="testimonial-content">
                                <div class="text-end mb-3">
                                    <i class="fa fa-quote-right fa-4x text-primary quote-icon"></i>
                                </div>
                                <p class="fs-6 mb-0 text-end" style="color: var(--ink-2); line-height: 1.8;">الحمد لله الذي بنعمته تتم الصالحات، نشكر الإخوة في جمعية رافد على جهودهم المباركة في إحياء سنة الوقف وتنمية الموارد المالية للمشاريع الخيرية، ونسأل الله أن يبارك في جهودهم ويجعلها في ميزان حسناتهم يوم القيامة.</p>
                            </div>
                        </div>

                        <!-- Item 4 -->
                        <div class="testimonial-card">
                            <img class="testimonial-img" src="{% static 'img/rafed_image/people/68ecf550ed5e2.png' %}" alt="">
                            <div class="testimonial-header-info text-end">
                                <h5 class="mb-1 text-primary" style="font-family: var(--font-sans); font-weight: 700; color: var(--gold-deep) !important;">أ.د. سليمان بن عبدالله أبا الخيل</h5>
                                <span style="font-size: 13px; color: var(--ink-2);">مدير جامعة الإمام محمد بن سعود الإسلامية سابقاً</span>
                            </div>
                            <div class="testimonial-content">
                                <div class="text-end mb-3">
                                    <i class="fa fa-quote-right fa-4x text-primary quote-icon"></i>
                                </div>
                                <p class="fs-6 mb-0 text-end" style="color: var(--ink-2); line-height: 1.8;">سرني كثيراً ما رأيته من تنظيم وعمل دؤوب في جمعية رافد للأوقاف، والتي تسعى لتقديم نموذج مؤسسي متميز في إدارة الأوقاف وتنميتها، وفق أحدث المعايير العالمية، وهذا يعكس حرصهم على تحقيق الاستدامة المالية للقطاع غير الربحي.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Testimonial End -->
"""

# Replace the existing Testimonial section
old_pattern = r'<!-- Testimonial Start -->.*?<!-- Testimonial End -->'
html = re.sub(old_pattern, new_testimonial_html, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Custom Testimonial Card */
.testimonial-card {
    position: relative;
    background-color: var(--paper);
    border: 1px solid rgba(20, 17, 10, 0.08);
    border-radius: 8px;
    padding: 30px 40px;
    margin-left: 55px; /* Space for the floating image */
    margin-top: 20px;
    margin-bottom: 20px;
    z-index: 1;
    overflow: visible;
}

.testimonial-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    /* Optional geometric watermark background */
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2M5YTk2MSIgb3BhY2l0eT0iMC4wNSIgZD0iTTEyIDBMNiA2bDYgNiA2LTZ6bTAgMTJsLTYgNmwtNi02bDYtNnptMTIgMGwtNiA2bC02LTZsNi02eiIvPjwvc3ZnPg==");
    background-size: 60px;
    background-repeat: repeat;
    z-index: -1;
    border-radius: 8px;
}

.testimonial-header-info {
    padding-bottom: 15px;
    border-bottom: 1px solid rgba(20, 17, 10, 0.05);
    margin-bottom: 20px;
}

.testimonial-img {
    position: absolute !important;
    top: -20px;
    left: -55px;
    width: 110px !important;
    height: 110px !important;
    border-radius: 50%;
    border: 6px solid var(--paper);
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    object-fit: cover;
    z-index: 5;
}

.quote-icon {
    color: var(--forest) !important;
    opacity: 0.9;
}

.testimonial-carousel .owl-dots {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}
.testimonial-carousel .owl-dot {
    width: 12px;
    height: 12px;
    margin: 0 5px;
    background: #e0d8c3 !important;
    border-radius: 50%;
    transition: 0.3s;
}
.testimonial-carousel .owl-dot.active {
    background: var(--forest) !important;
}

/* Float the arrow inside the card, on the right edge */
.testimonial-carousel .owl-nav {
    position: absolute;
    top: 50%;
    right: 15px;
    transform: translateY(-50%);
    pointer-events: none;
}
.testimonial-carousel .owl-nav .owl-next {
    font-size: 30px !important;
    color: #a0a0a0 !important;
    pointer-events: auto;
}
.testimonial-carousel .owl-nav .owl-next:hover { color: var(--forest) !important; }
.testimonial-carousel .owl-nav .owl-prev { display: none !important; } /* Only show next arrow as per screenshot */

/* Ensure owl-stage-outer doesn't clip the floating image */
.testimonial-carousel .owl-stage-outer {
    overflow: visible !important;
    padding-left: 60px;
    margin-left: -60px;
}
"""

if '.testimonial-card {' not in css:
    css += new_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)


# 3. Update main.js
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the existing testimonial-carousel initialization
old_js_pattern = r'\$\(\"\.testimonial-carousel\"\)\.owlCarousel\(\{.*?\}\);'
new_js = """$(".testimonial-carousel").owlCarousel({
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
        items: 1
    });"""

js = re.sub(old_js_pattern, new_js, js, flags=re.DOTALL)
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Testimonial section updated successfully.")
