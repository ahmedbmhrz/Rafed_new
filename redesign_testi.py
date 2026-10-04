# -*- coding: utf-8 -*-
import re

# 1. Update home_page.html
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_testimonial_html = """
    <!-- Testimonial Start -->
    <div class="container-xxl py-6" style="position: relative; z-index: 10;">
        <div class="container">
            <!-- Title -->
            <div class="text-center mx-auto mb-5">
                <p class="text-primary text-uppercase mb-2 eyebrow" style="font-size: 16px; font-weight: 700; letter-spacing: 2px; color: var(--gold-deep) !important;">قالوا عنا</p>
                <h2 class="display-6 mb-4" style="color: var(--forest);">سعداء دائما بخدمتكم</h2>
            </div>
            
            <!-- Carousel -->
            <div class="owl-carousel testimonial-carousel">
                <!-- Item 1 -->
                <div class="bg-white rounded p-4 text-center shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); height: 100%;">
                    <img class="rounded-circle mx-auto mb-4" src="{% static 'img/rafed_image/people/68ecf41bf2f63.png' %}" alt="" style="width: 100px !important; height: 100px !important; object-fit: cover; border: 4px solid var(--paper); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <h5 class="mb-1" style="color: var(--forest);">د. خالد عبدالله السريحي</h5>
                    <span class="d-block mb-3" style="font-size: 13px; color: var(--ink-2);">المدير العام للمركز الدولي للأبحاث والدراسات ( مداد )</span>
                    <i class="fa fa-quote-right fa-2x text-primary mb-3"></i>
                    <p class="fs-6 mb-0" style="color: var(--ink-2); line-height: 1.8;">بسم الله الرحمن الرحيم الحمد لله رب العالمين والصلاة والسلام على أشرف المرسلين وبعد شرفت اليوم الاثنين تسعة ربيع الأول من عام 1447 هجري بالمشاركة في ديوانية رافد... الأوقاف من خلال تقديم موضوع استشراف المستقبل الأوقاف خلال عشر سنوات قادمة وما شاهدته من التفاعل والمشاركات والمبادرات التي خرجت أثناء اللقاء وعليه فإنني أدعو جميع الفضلاء من أهل العلم وأهل التجارة بالمساهم مع الإخوة في جمعية رافد لمساعدتهم ومشاركتهم في تنفيذ مثل هذه البرامج والفعاليات والحمد لله الذي تتم بنعمته الصالحات.</p>
                </div>
                
                <!-- Item 2 -->
                <div class="bg-white rounded p-4 text-center shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); height: 100%;">
                    <img class="rounded-circle mx-auto mb-4" src="{% static 'img/rafed_image/people/68ecf45e8f69f.png' %}" alt="" style="width: 100px !important; height: 100px !important; object-fit: cover; border: 4px solid var(--paper); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <h5 class="mb-1" style="color: var(--forest);">د. أنس بن عبدالوهاب</h5>
                    <span class="d-block mb-3" style="font-size: 13px; color: var(--ink-2);">أكاديمي وباحث في شؤون الأوقاف</span>
                    <i class="fa fa-quote-right fa-2x text-primary mb-3"></i>
                    <p class="fs-6 mb-0" style="color: var(--ink-2); line-height: 1.8;">الحمد لله رب العالمين، والصلاة والسلام على أشرف الأنبياء والمرسلين نبينا محمد وعلى آله وصحبه أجمعين، لقد سررت هذا المساء بلقاء ثلة من الفضلاء والمهتمين بالعمل الوقفي، في ديوانية رافد للأوقاف بمكة المكرمة والتي كان لها دور بارز في نشر ثقافة الوقف والتوعية بأهميته في المجتمع.</p>
                </div>

                <!-- Item 3 -->
                <div class="bg-white rounded p-4 text-center shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); height: 100%;">
                    <img class="rounded-circle mx-auto mb-4" src="{% static 'img/rafed_image/people/68ecf49e3c05a.png' %}" alt="" style="width: 100px !important; height: 100px !important; object-fit: cover; border: 4px solid var(--paper); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <h5 class="mb-1" style="color: var(--forest);">الشيخ صالح بن عواد المغامسي</h5>
                    <span class="d-block mb-3" style="font-size: 13px; color: var(--ink-2);">إمام وخطيب مسجد قباء سابقاً</span>
                    <i class="fa fa-quote-right fa-2x text-primary mb-3"></i>
                    <p class="fs-6 mb-0" style="color: var(--ink-2); line-height: 1.8;">الحمد لله الذي بنعمته تتم الصالحات، نشكر الإخوة في جمعية رافد على جهودهم المباركة في إحياء سنة الوقف وتنمية الموارد المالية للمشاريع الخيرية، ونسأل الله أن يبارك في جهودهم ويجعلها في ميزان حسناتهم يوم القيامة.</p>
                </div>

                <!-- Item 4 -->
                <div class="bg-white rounded p-4 text-center shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); height: 100%;">
                    <img class="rounded-circle mx-auto mb-4" src="{% static 'img/rafed_image/people/68ecf550ed5e2.png' %}" alt="" style="width: 100px !important; height: 100px !important; object-fit: cover; border: 4px solid var(--paper); box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <h5 class="mb-1" style="color: var(--forest);">أ.د. سليمان بن عبدالله أبا الخيل</h5>
                    <span class="d-block mb-3" style="font-size: 13px; color: var(--ink-2);">مدير جامعة الإمام محمد بن سعود الإسلامية سابقاً</span>
                    <i class="fa fa-quote-right fa-2x text-primary mb-3"></i>
                    <p class="fs-6 mb-0" style="color: var(--ink-2); line-height: 1.8;">سرني كثيراً ما رأيته من تنظيم وعمل دؤوب في جمعية رافد للأوقاف، والتي تسعى لتقديم نموذج مؤسسي متميز في إدارة الأوقاف وتنميتها، وفق أحدث المعايير العالمية، وهذا يعكس حرصهم على تحقيق الاستدامة المالية للقطاع غير الربحي.</p>
                </div>
            </div>
            
            <div class="text-center mt-5">
                <a href="#" class="btn btn-primary rounded py-3 px-5" style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;">عرض كافة التزكيات</a>
            </div>
        </div>
    </div>
    <!-- Testimonial End -->
"""

old_pattern = r'<!-- Testimonial Start -->.*?<!-- Testimonial End -->'
html = re.sub(old_pattern, new_testimonial_html, html, flags=re.DOTALL)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# 3. Update main.js
js_path = 'rafed_site/static/js/main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

old_js_pattern = r'\$\(\"\.testimonial-carousel\"\)\.owlCarousel\(\{.*?\}\);'
new_js = """$(".testimonial-carousel").owlCarousel({
        autoplay: true, rtl: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: false,
        dots: true,
        nav: false,
        responsive: {
            0:{ items:1 },
            768:{ items:2 },
            992:{ items:2 }
        }
    });"""
js = re.sub(old_js_pattern, new_js, js, flags=re.DOTALL)
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
