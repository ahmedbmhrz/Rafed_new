from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


# ==============================================================================
# 1. HOMEPAGE & INLINE CHILD SECTIONS (الصفحة الرئيسية)
# ==============================================================================

class HomePageAchievement(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=150, verbose_name="عنوان الإنجاز")
    number = models.CharField(max_length=50, verbose_name="الرقم / القيمة (مثل: 73 أو 290570)")
    unit = models.CharField(max_length=50, blank=True, verbose_name="الوحدة (مثل: لقاء، ريال، متطوع، منشور)")
    icon = models.CharField(max_length=80, default="fa-chart-line", verbose_name="أيقونة FontAwesome")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('number'),
        FieldPanel('unit'),
        FieldPanel('icon'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "إنجاز أو رقم إحصائي"
        verbose_name_plural = "إنجازاتنا"


class HomePageNews(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='news_items')
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    date_text = models.CharField(max_length=100, verbose_name="تاريخ النشر (مثل: الأربعاء، 05 أغسطس 2026)")
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="صورة الخبر")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="img/rafed_image/background/6aa0f543b127d8.21470575.png", verbose_name="مسار صورة بديلة من static")
    excerpt = models.TextField(blank=True, verbose_name="موجز الخبر أو التفاصيل")
    link = models.CharField(max_length=255, blank=True, default="#", verbose_name="رابط الخبر (اختياري)")
    is_active = models.BooleanField(default=True, verbose_name="منشور")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('excerpt'),
        FieldPanel('link'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "أخبار الجمعية والفعاليات"


class HomePageEducational(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='educational_items')
    title = models.CharField(max_length=255, verbose_name="عنوان المحتوى التثقيفي")
    date_text = models.CharField(max_length=100, verbose_name="التاريخ (مثل: الثلاثاء، 21 أكتوبر 2025)")
    image = models.ImageField(upload_to="infographics/", blank=True, null=True, verbose_name="صورة الغلاف أو التصميم")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="img/rafed_image/background/6aa0f543b127d8.21470575.png", verbose_name="مسار صورة بديلة من static")
    badge_text = models.CharField(max_length=50, default="6 صور", verbose_name="الشارة التعريفية (مثل: 6 صور، إنفوجرافيك)")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('badge_text'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "تصميم تثقيفي"
        verbose_name_plural = "تصاميم تثقيفية عن الأوقاف"


class HomePageVideo(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='video_items')
    title = models.CharField(max_length=255, verbose_name="عنوان الفيديو")
    date_text = models.CharField(max_length=100, default="الخميس، 01 أكتوبر 2026", verbose_name="تاريخ النشر")
    video_url = models.CharField(
        max_length=500, 
        default="https://www.youtube.com/watch?v=ScMzIvxBSi4", 
        verbose_name="رابط الفيديو (يوتيوب أو رابط خارجي)"
    )
    thumbnail = models.ImageField(upload_to="videos/", blank=True, null=True, verbose_name="صورة غلاف الفيديو")
    image_static_fallback = models.CharField(
        max_length=255, 
        blank=True, 
        default="img/rafed_image/background/4.jpg", 
        verbose_name="مسار صورة بديلة من static"
    )
    duration = models.CharField(max_length=50, blank=True, default="03:20", verbose_name="مدة الفيديو")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في ألبوم الفيديو")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('video_url'),
        FieldPanel('thumbnail'),
        FieldPanel('image_static_fallback'),
        FieldPanel('duration'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "فيديو"
        verbose_name_plural = "ألبوم الفيديو في الصفحة الرئيسية"

    @property
    def embed_url(self):
        url = self.video_url
        if "youtube.com/watch?v=" in url:
            vid_id = url.split("v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{vid_id}?autoplay=1"
        elif "youtu.be/" in url:
            vid_id = url.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{vid_id}?autoplay=1"
        return url


class HomePagePartner(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=150, verbose_name="اسم الشريك أو الجهة")
    logo = models.ImageField(upload_to="partners/", blank=True, null=True, verbose_name="شعار الشريك")
    logo_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    link = models.CharField(max_length=255, blank=True, default="#", verbose_name="رابط موقع الشريك (اختياري)")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في قسم الشركاء")

    panels = [
        FieldPanel('name'),
        FieldPanel('logo'),
        FieldPanel('logo_static_fallback'),
        FieldPanel('link'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "شريك نجاح"
        verbose_name_plural = "شركاء النجاح"


class HomePageTestimonial(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=150, verbose_name="صاحب التزكية / الاسم")
    author_role = models.CharField(max_length=200, verbose_name="الصفة أو المنصب")
    quote = models.TextField(verbose_name="نص التزكية أو الشهادة")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True, verbose_name="الصورة الشخصية")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة الرئيسية")

    panels = [
        FieldPanel('author_name'),
        FieldPanel('author_role'),
        FieldPanel('quote'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('is_active'),
    ]

    @property
    def author_title(self):
        return self.author_role

    class Meta:
        verbose_name = "تزكية في الصفحة الرئيسية"
        verbose_name_plural = "تزكيات الصفحة الرئيسية (قالوا عنا)"


class HomePageSlide(Orderable):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='hero_slides')
    image = models.ImageField(upload_to="hero/", blank=True, null=True, verbose_name="صورة الشريحة (Slider Image)")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    subheading = models.CharField(max_length=150, blank=True, default="جمعية رافد للأوقاف", verbose_name="العنوان التمهيدي / الفرعي")
    heading = models.CharField(max_length=200, blank=True, default="نؤسس ونطور الأوقاف بتميز", verbose_name="العنوان الرئيسي")
    text = models.TextField(blank=True, default="نسعى لتحقيق الاستدامة وتنمية الكيانات الوقفية وفق أفضل الممارسات المؤسسية.", verbose_name="النص التوضيحي")
    button_text = models.CharField(max_length=100, blank=True, default="اقرأ المزيد", verbose_name="نص الزر")
    button_url = models.CharField(max_length=255, blank=True, default="/about/", verbose_name="رابط الزر")
    is_active = models.BooleanField(default=True, verbose_name="شريحة مفعلة")

    panels = [
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('subheading'),
        FieldPanel('heading'),
        FieldPanel('text'),
        FieldPanel('button_text'),
        FieldPanel('button_url'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "شريحة في السلايدر الرئيسي"
        verbose_name_plural = "شرائح السلايدر الرئيسي (Hero Slider)"


class HomePage(Page):
    hero_subheading = models.CharField(max_length=100, default="جمعية رافد للأوقاف", verbose_name="العنوان الفرعي")
    hero_heading = models.CharField(max_length=100, default="نؤسس ونطور الأوقاف", verbose_name="العنوان الرئيسي")
    hero_text = models.CharField(max_length=255, default="جمعية تعنى بتأسيس وتطوير واستدامة الكيانات الوقفية.", verbose_name="النص")

    about_tab_text = models.TextField(
        default="جمعية تعنى بتأسيس وتطوير واستدامة الكيانات الوقفية وتقديم خدمات متنوعة للراغبين في الوقف ومنسوبي الأوقاف. مرخصة إدارياً من المركز الوطني لتنمية القطاع غير الربحي رقم ١٩٣٧ وبإشراف من الهيئة العامة للأوقاف.",
        verbose_name="نص تبويب 'من نحن' في الرئيسية"
    )

    vision_title = models.CharField(max_length=100, default="رؤيتنا", verbose_name="عنوان الرؤية")
    vision_text = models.TextField(default="أوقاف متنامية ذات أثر مجتمعي بأدوات مبتكرة.", verbose_name="نص الرؤية")
    
    mission_title = models.CharField(max_length=100, default="رسالتنا", verbose_name="عنوان الرسالة")
    mission_text = models.TextField(default="حلول إبداعية يقدمها خبراء متخصصون لتأسيس وتمكين الأوقاف سعياً لاستدامتها وتعظيم أثرها بمنطقة مكة المكرمة.", verbose_name="نص الرسالة")

    # قالوا عنا (Testimonials on Homepage)
    testimonials_eyebrow = models.CharField(max_length=100, default="قالوا عنا", verbose_name="العنوان التمهيدي لقسم قالوا عنا")
    testimonials_heading = models.CharField(max_length=150, default="سعداء دائماً بخدمتكم", verbose_name="العنوان الرئيسي لقسم قالوا عنا")
    testimonials_text = models.CharField(max_length=255, default="كلمات نعتز بها من أصحاب الفضيلة والخبراء والشركاء في مسيرة الأوقاف", verbose_name="النص التوضيحي لقسم قالوا عنا")

    content_panels = Page.content_panels + [
        InlinePanel('hero_slides', heading="🖼️ شرائح السلايدر الرئيسي (Hero Slider Images & Content)", label="شريحة"),
        MultiFieldPanel([
            FieldPanel('hero_subheading'),
            FieldPanel('hero_heading'),
            FieldPanel('hero_text'),
        ], heading="القسم الرئيسي - نصوص احتياطية (Hero Fallback)"),
        MultiFieldPanel([
            FieldPanel('about_tab_text'),
            FieldPanel('vision_title'),
            FieldPanel('vision_text'),
            FieldPanel('mission_title'),
            FieldPanel('mission_text'),
        ], heading="نبذة عن الجمعية والرؤية والرسالة"),
        InlinePanel('achievements', heading="📊 قسم إنجازاتنا والأرقام الإحصائية", label="إنجاز أو رقم إحصائي"),
        InlinePanel('news_items', heading="📰 أخبار الجمعية والفعاليات", label="خبر"),
        InlinePanel('educational_items', heading="🎨 تصاميم تثقيفية عن الأوقاف", label="تصميم تثقيفي"),
        InlinePanel('video_items', heading="🎬 ألبوم الفيديو في الصفحة الرئيسية", label="فيديو"),
        InlinePanel('partners', heading="🤝 شركاؤنا في النجاح", label="شريك نجاح"),
        MultiFieldPanel([
            FieldPanel('testimonials_eyebrow'),
            FieldPanel('testimonials_heading'),
            FieldPanel('testimonials_text'),
        ], heading="💬 نصوص ترويسة قسم قالوا عنا (تزكيات هذا القسم متزامنة تلقائياً مع صفحة قالوا عنا / سجل التزكيات)"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['hero_slides'] = self.hero_slides.filter(is_active=True)
        context['achievements'] = self.achievements.filter(is_active=True)
        context['news_items'] = self.news_items.filter(is_active=True)
        context['educational_items'] = self.educational_items.filter(is_active=True)
        context['video_items'] = self.video_items.filter(is_active=True)
        context['partners'] = self.partners.filter(is_active=True)

        # Context for projects & testimonials on homepage
        proj_page = ProjectsPage.objects.first()
        context['projects'] = proj_page.projects.filter(is_featured=True) if proj_page else []

        # Testimonials on homepage: directly synchronized with TestimonialsPage (سجل التزكيات)
        testi_page = TestimonialsPage.objects.first()
        context['testimonials'] = testi_page.testimonials.filter(is_featured=True) if testi_page else []

        contact_page = ContactPage.objects.first()
        context['site_settings'] = contact_page or SiteContactSettings.get_settings()
        return context


# ==============================================================================
# 2. ABOUT PAGE (صفحة من نحن)
# ==============================================================================

class AboutPageValue(Orderable):
    page = ParentalKey('AboutPage', on_delete=models.CASCADE, related_name='values')
    title = models.CharField(max_length=150, verbose_name="عنوان القيمة")
    description = models.TextField(verbose_name="وصف القيمة")
    icon = models.CharField(max_length=80, default="fa-balance-scale", verbose_name="أيقونة FontAwesome")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('icon'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "قيمة جوهرية"
        verbose_name_plural = "قيمنا الجوهرية"


class AboutPageGoal(Orderable):
    page = ParentalKey('AboutPage', on_delete=models.CASCADE, related_name='goals')
    serial_number = models.CharField(max_length=20, default="01", verbose_name="الرقم التسلسلي (مثال: 01)")
    title = models.CharField(max_length=150, verbose_name="عنوان الهدف")
    text = models.TextField(verbose_name="نص وتفاصيل الهدف")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('serial_number'),
        FieldPanel('title'),
        FieldPanel('text'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "هدف استراتيجي"
        verbose_name_plural = "أهدافنا الاستراتيجية"


class AboutPageStat(Orderable):
    page = ParentalKey('AboutPage', on_delete=models.CASCADE, related_name='stats')
    number = models.CharField(max_length=50, verbose_name="الرقم / النسبة (مثال: 10 أو 50 أو 10000 أو 100%)")
    label = models.CharField(max_length=150, verbose_name="عنوان الإحصائية (مثال: سنوات خبرة تراكمية)")
    icon = models.CharField(max_length=80, default="fa-certificate", verbose_name="أيقونة FontAwesome")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('number'),
        FieldPanel('label'),
        FieldPanel('icon'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "رقم إحصائي"
        verbose_name_plural = "أثرنا في أرقام"


class AboutPage(Page):
    subheading = models.CharField(max_length=100, default="جمعية رافد للأوقاف", verbose_name="العنوان الفرعي للترويسة")
    heading = models.CharField(max_length=100, default="من نحن", verbose_name="العنوان الرئيسي للترويسة")

    # Story / Overview
    story_subheading = models.CharField(max_length=100, default="نبذة عن الجمعية", verbose_name="عنوان نبذة عن الجمعية")
    story_heading = models.CharField(max_length=200, default="رواد في تأسيس وتطوير واستدامة الكيانات الوقفية", verbose_name="عنوان القصة")
    story_text = models.TextField(
        default="جمعية رافد للأوقاف هي جمعية أهلية متخصصة ومصرح لها رسمياً، تُعنى بتقديم منظومة استشارية وتطويرية متكاملة لتأسيس وتنمية واستدامة الكيانات الوقفية، وتمكين الراغبين في الوقف ومنسوبي القطاع الوقفي من إدارة أوقافهم بأعلى معايير الحوكمة والامتثال الشرعي والنظامي.",
        verbose_name="نص نبذة عن الجمعية"
    )
    story_image = models.ImageField(upload_to="about/", blank=True, null=True, verbose_name="صورة النبذة الرئيسية")
    story_image_static_fallback = models.CharField(
        max_length=255, 
        blank=True, 
        default="img/rafed_image/background/4.jpg", 
        verbose_name="مسار صورة بديلة من static"
    )
    badge_number = models.CharField(max_length=50, default="+10", verbose_name="رقم الشارة على الصورة")
    badge_text = models.CharField(max_length=100, default="سنوات من الريادة الوقفية", verbose_name="نص الشارة على الصورة")

    # Licenses / Badges
    license_1_title = models.CharField(max_length=100, default="ترخيص رسمي معتمد", verbose_name="عنوان الترخيص الأول")
    license_1_subtitle = models.CharField(max_length=150, default="المركز الوطني للقطاع غير الربحي (رقم 1937)", verbose_name="تفاصيل الترخيص الأول")
    license_2_title = models.CharField(max_length=100, default="إشراف فني متخصص", verbose_name="عنوان الإشراف الثاني")
    license_2_subtitle = models.CharField(max_length=150, default="تحت إشراف الهيئة العامة للأوقاف", verbose_name="تفاصيل الإشراف الثاني")

    # Vision & Mission
    vision_kicker = models.CharField(max_length=100, default="بوصلة المستقبل", verbose_name="شارة الرؤية")
    vision_title = models.CharField(max_length=100, default="رؤيتنا", verbose_name="عنوان الرؤية")
    vision_text = models.TextField(
        default="الريادة والتميز في تأسيس وتطوير واستدامة الأوقاف، لتكون رافداً تنموياً رائداً يسهم في نهضة المجتمع واستقرار أصوله الوقفية.",
        verbose_name="نص الرؤية"
    )
    vision_footer = models.CharField(
        max_length=200, 
        default="مرتكز استراتيجي لصناعة الأثر الوقفي المستدام عبر الأجيال", 
        verbose_name="شعار أسفل الرؤية"
    )

    mission_kicker = models.CharField(max_length=100, default="رسالتنا التنموية", verbose_name="شارة الرسالة")
    mission_title = models.CharField(max_length=100, default="رسالتنا", verbose_name="عنوان الرسالة")
    mission_text = models.TextField(
        default="تقديم خدمات استشارية ومؤسسية نوعية للمانحين والواقفين والنظار، وتمكينهم من صياغة وتأسيس وإدارة كيانات وقفية نموذجية تحقق أعلى درجات الأثر والاستدامة، بالاعتماد على كفاءات وطنية متخصصة وحوكمة دقيقة.",
        verbose_name="نص الرسالة"
    )
    mission_footer = models.CharField(
        max_length=200, 
        default="تمكين مؤسسي متكامل للواقفين والنظار", 
        verbose_name="شعار أسفل الرسالة"
    )

    # Vision 2030 Banner
    v2030_badge = models.CharField(max_length=100, default="مستهدفات وطنية", verbose_name="شارة رؤية 2030")
    v2030_heading = models.CharField(max_length=200, default="مواءمة استراتيجية مع رؤية المملكة 2030", verbose_name="عنوان رؤية 2030")
    v2030_text = models.TextField(
        default="تضع جمعية رافد مستهدفات رؤية المملكة 2030 في صميم خططها، مساهمةً في رفع مساهمة القطاع غير الربحي في الناتج المحلي الإجمالي من 1% إلى 5%، وتعزيز الأثر الاقتصادي والاجتماعي للأوقاف لضمان استمرار نفعها لأجيال قادمة.",
        verbose_name="نص مواءمة رؤية 2030"
    )

    # CTA Banner
    cta_heading = models.CharField(max_length=200, default="هل ترغب في تأسيس أو تطوير وقفك؟", verbose_name="عنوان الدعوة للتواصل (CTA)")
    cta_text = models.TextField(
        default="فريق مستشاري رافد جاهز لتقديم المشورة الشرعية والنظامية والإدارية لضمان استدامة أوقافكم ونمائها.",
        verbose_name="نص الدعوة للتواصل"
    )
    cta_btn_text = models.CharField(max_length=100, default="تواصل مع مستشارينا الآن", verbose_name="نص زر التواصل")
    cta_btn_url = models.CharField(max_length=255, default="/contact/", verbose_name="رابط زر التواصل")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subheading'),
            FieldPanel('heading'),
        ], heading="ترويسة الصفحة (Header)"),
        MultiFieldPanel([
            FieldPanel('story_subheading'),
            FieldPanel('story_heading'),
            FieldPanel('story_text'),
            FieldPanel('story_image'),
            FieldPanel('story_image_static_fallback'),
            FieldPanel('badge_number'),
            FieldPanel('badge_text'),
            FieldPanel('license_1_title'),
            FieldPanel('license_1_subtitle'),
            FieldPanel('license_2_title'),
            FieldPanel('license_2_subtitle'),
        ], heading="نبذة عن الجمعية والتراخيص الرسمية"),
        MultiFieldPanel([
            FieldPanel('vision_kicker'),
            FieldPanel('vision_title'),
            FieldPanel('vision_text'),
            FieldPanel('vision_footer'),
            FieldPanel('mission_kicker'),
            FieldPanel('mission_title'),
            FieldPanel('mission_text'),
            FieldPanel('mission_footer'),
        ], heading="الرؤية والرسالة"),
        InlinePanel('values', heading="💎 قيمنا الجوهرية", label="قيمة"),
        InlinePanel('goals', heading="🎯 أهدافنا الاستراتيجية", label="هدف"),
        MultiFieldPanel([
            FieldPanel('v2030_badge'),
            FieldPanel('v2030_heading'),
            FieldPanel('v2030_text'),
        ], heading="مواءمة رؤية المملكة 2030"),
        InlinePanel('stats', heading="📈 أثرنا في أرقام", label="رقم إحصائي"),
        MultiFieldPanel([
            FieldPanel('cta_heading'),
            FieldPanel('cta_text'),
            FieldPanel('cta_btn_text'),
            FieldPanel('cta_btn_url'),
        ], heading="قسم الدعوة للتواصل (CTA)"),
    ]

    template = "home/about_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['values'] = self.values.filter(is_active=True)
        context['goals'] = self.goals.filter(is_active=True)
        context['stats'] = self.stats.filter(is_active=True)
        return context


# ==============================================================================
# 3. SERVICES PAGE (صفحة خدماتنا)
# ==============================================================================

class ServicesPageItem(Orderable):
    page = ParentalKey('ServicesPage', on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=150, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    icon = models.CharField(max_length=80, default="fa-scroll", verbose_name="أيقونة FontAwesome")
    feature_1 = models.CharField(max_length=200, blank=True, default="", verbose_name="الميزة / النقطة الأولى")
    feature_2 = models.CharField(max_length=200, blank=True, default="", verbose_name="الميزة / النقطة الثانية")
    feature_3 = models.CharField(max_length=200, blank=True, default="", verbose_name="الميزة / النقطة الثالثة")
    action_text = models.CharField(max_length=100, default="طلب خدمة التأسيس", verbose_name="نص زر طلب الخدمة")
    action_url = models.CharField(max_length=255, default="/contact/", verbose_name="رابط زر الخدمة")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('icon'),
        FieldPanel('feature_1'),
        FieldPanel('feature_2'),
        FieldPanel('feature_3'),
        FieldPanel('action_text'),
        FieldPanel('action_url'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "خدمة وقفية"
        verbose_name_plural = "باقة الخدمات الوقفية"


class ServicesPageProcess(Orderable):
    page = ParentalKey('ServicesPage', on_delete=models.CASCADE, related_name='process_steps')
    step_number = models.CharField(max_length=50, default="المرحلة 01", verbose_name="رقم أو تسمية المرحلة")
    title = models.CharField(max_length=150, verbose_name="عنوان المرحلة")
    description = models.TextField(verbose_name="وصف المرحلة")
    icon = models.CharField(max_length=80, default="fa-clipboard-list", verbose_name="أيقونة FontAwesome")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('step_number'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('icon'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "مرحلة عمل"
        verbose_name_plural = "منهجية العمل ومراحل الخدمة"


class ServicesPageDifferentiator(Orderable):
    page = ParentalKey('ServicesPage', on_delete=models.CASCADE, related_name='differentiators')
    title = models.CharField(max_length=150, verbose_name="عنوان الميزة التنافسية")
    description = models.TextField(verbose_name="شرح وتفاصيل الميزة")
    icon = models.CharField(max_length=80, default="fa-balance-scale", verbose_name="أيقونة FontAwesome")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('icon'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "ميزة تنافسية"
        verbose_name_plural = "لماذا يختار الواقفون جمعية رافد؟"


class ServicesPage(Page):
    subheading = models.CharField(max_length=100, default="جمعية رافد للأوقاف", verbose_name="العنوان الفرعي للترويسة")
    heading = models.CharField(max_length=100, default="خدماتنا", verbose_name="العنوان الرئيسي للترويسة")

    # Overview
    overview_subheading = models.CharField(max_length=100, default="منظومة خدمات متكاملة", verbose_name="العنوان الفرعي للمقدمة")
    overview_heading = models.CharField(
        max_length=200, 
        default="حلول مؤسسية واستشارية مبتكرة لتأسيس وتنمية واستدامة الأوقاف", 
        verbose_name="العنوان الرئيسي للمقدمة"
    )
    overview_text = models.TextField(
        default="تُقدّم جمعية رافد للأوقاف حزمة شاملة من الخدمات المتخصصة الموجّهة للواقفين، والنظار، والمنشآت الوقفية القائمة والمستقبلية، بإشراف نخبة من المستشارين الشرعيين والقانونيين والخبراء الإداريين والاستثماريين، لضمان أعلى مستويات الحوكمة والأثر الوقفي المستدام.",
        verbose_name="نص المقدمة الشاملة"
    )

    # Accreditation Box
    badge_title = models.CharField(max_length=150, default="اعتماد رسمي وأمانة شرعية", verbose_name="عنوان صندوق الاعتماد")
    badge_subtitle = models.CharField(max_length=150, default="مرخصة من المركز الوطني (1937) وبإشراف هيئة الأوقاف", verbose_name="تفاصيل ترخيص الصندوق")
    badge_text = models.TextField(
        default="كافة استشاراتنا وصكوكنا تخضع لدراسة شرعية ونظامية دقيقة تضمن تحقيق شروط الواقفين وحمايتها وتعظيم منافعها التنموية للأجيال القادمة.",
        verbose_name="نص صندوق الاعتماد"
    )

    # CTA Banner
    cta_heading = models.CharField(max_length=200, default="جاهزون للبدء في تأسيس أو تطوير وقفك؟", verbose_name="عنوان الدعوة للتواصل (CTA)")
    cta_text = models.TextField(
        default="احجز جلسة استشارية أولية مع نخبة من خبرائنا الشرعيين والنظاميين لمناقشة أهدافك الوقفية ووضع خارطة طريق تنفيذية متكاملة.",
        verbose_name="نص الدعوة للتواصل"
    )
    cta_btn_text = models.CharField(max_length=100, default="احجز جلستك الاستشارية الآن", verbose_name="نص زر التواصل")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('subheading'),
            FieldPanel('heading'),
        ], heading="ترويسة الصفحة (Header)"),
        MultiFieldPanel([
            FieldPanel('overview_subheading'),
            FieldPanel('overview_heading'),
            FieldPanel('overview_text'),
            FieldPanel('badge_title'),
            FieldPanel('badge_subtitle'),
            FieldPanel('badge_text'),
        ], heading="المقدمة التنفيذية وصندوق الاعتماد"),
        InlinePanel('services', heading="💼 باقة الخدمات الوقفية الشاملة", label="خدمة وقفية"),
        InlinePanel('process_steps', heading="🔄 منهجية العمل ومراحل تقديم الخدمة", label="مرحلة عمل"),
        InlinePanel('differentiators', heading="⭐ لماذا يختار الواقفون جمعية رافد؟", label="ميزة تنافسية"),
        MultiFieldPanel([
            FieldPanel('cta_heading'),
            FieldPanel('cta_text'),
            FieldPanel('cta_btn_text'),
        ], heading="قسم الدعوة للتواصل (CTA)"),
    ]

    template = "home/services_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['services'] = self.services.filter(is_active=True)
        context['process_steps'] = self.process_steps.filter(is_active=True)
        context['differentiators'] = self.differentiators.filter(is_active=True)
        return context


# ==============================================================================
# 4. PROJECTS PAGE (صفحة مشاريعنا الوقفية)
# ==============================================================================

class ProjectsPageItem(Orderable):
    CATEGORY_CHOICES = [
        ('initiatives', 'مبادرات وبرامج وقفية'),
        ('empowerment', 'تمكين وتأهيل النظار'),
        ('governance', 'حوكمة وتنظيم الأوقاف'),
        ('investment', 'استثمار وتنمية الأصول'),
    ]

    STATUS_CHOICES = [
        ('ongoing', 'قيد التنفيذ'),
        ('completed', 'منجز ومكتمل'),
        ('continuous', 'مبادرة مستمرة'),
    ]

    page = ParentalKey('ProjectsPage', on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255, verbose_name="اسم المشروع الوقفي")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='initiatives', verbose_name="تصنيف المشروع")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ongoing', verbose_name="حالة المشروع")
    description = models.TextField(verbose_name="وصف المشروع")
    image = models.ImageField(upload_to="projects/", blank=True, null=True, verbose_name="صورة المشروع")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="img/rafed_image/background/4.jpg", verbose_name="مسار صورة بديلة من static")
    progress_percentage = models.PositiveIntegerField(default=75, verbose_name="نسبة الإنجاز %")
    target_amount = models.CharField(max_length=100, blank=True, default="", verbose_name="المستهدف المالي أو العددي (اختياري)")
    is_featured = models.BooleanField(default=True, verbose_name="ظاهر في صفحة المشاريع")

    panels = [
        FieldPanel('title'),
        FieldPanel('category'),
        FieldPanel('status'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('progress_percentage'),
        FieldPanel('target_amount'),
        FieldPanel('is_featured'),
    ]

    class Meta:
        verbose_name = "مشروع وقفي"
        verbose_name_plural = "المشاريع الوقفية"


class ProjectsPage(Page):
    subheading = models.CharField(max_length=100, default="مشاريعنا الوقفية", verbose_name="العنوان الفرعي")
    heading = models.CharField(max_length=200, default="مشاريع ومبادرات جمعية رافد للأوقاف", verbose_name="العنوان الرئيسي")
    intro_text = models.TextField(default="نعمل على تطوير وتنفيذ حزمة من المشاريع والمبادرات الوقفية الاستراتيجية التي تعزز الاستدامة المالية وتعمق الأثر المجتمعي.", verbose_name="مقدمة الصفحة")

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('heading'),
        FieldPanel('intro_text'),
        InlinePanel('projects', heading="🏗️ قائمة المشاريع الوقفية", label="مشروع وقفي"),
    ]

    template = "home/projects_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['projects'] = self.projects.filter(is_featured=True)
        return context


# ==============================================================================
# 5. TEAM PAGE (صفحة فريقنا ونخبة خبرائنا)
# ==============================================================================

class TeamPageMember(Orderable):
    CATEGORY_CHOICES = [
        ('board', 'مجلس الإدارة'),
        ('sharia', 'الهيئة الشرعية والاستشارية'),
        ('exec', 'الإدارة التنفيذية'),
    ]

    page = ParentalKey('TeamPage', on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=150, verbose_name="الاسم الكريم")
    role = models.CharField(max_length=150, verbose_name="المسمى / المنصب")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='board', verbose_name="الفئة / القسم")
    bio = models.TextField(blank=True, default="", verbose_name="نبذة عن العضو أو المؤهلات")
    image = models.ImageField(upload_to="team/", blank=True, null=True, verbose_name="الصورة الشخصية")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    initials = models.CharField(max_length=10, blank=True, default="", verbose_name="الحروف الأولى (إذا لم تتوفر صورة)")
    linkedin_url = models.CharField(max_length=255, blank=True, default="", verbose_name="رابط لينكد إن أو البريد (اختياري)")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في صفحة فريقنا")

    panels = [
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('category'),
        FieldPanel('bio'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('initials'),
        FieldPanel('linkedin_url'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "عضو في الفريق"
        verbose_name_plural = "أعضاء الفريق والخبراء"


class TeamPage(Page):
    subheading = models.CharField(max_length=100, default="كفاءات رافد", verbose_name="العنوان الفرعي")
    heading = models.CharField(max_length=200, default="الهيكل القيادي والاستشاري للجمعية", verbose_name="العنوان الرئيسي")

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('heading'),
        InlinePanel('team_members', heading="👥 قائمة أعضاء الفريق والخبراء", label="عضو في الفريق"),
    ]

    template = "home/team_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['team_members'] = self.team_members.filter(is_active=True)
        return context


# ==============================================================================
# 6. TESTIMONIALS PAGE (صفحة قالوا عنا وتزكيات الشركاء)
# ==============================================================================

class TestimonialsPageItem(Orderable):
    CATEGORY_CHOICES = [
        ('scholars', 'العلماء والأكاديميون'),
        ('nazir', 'النظار والواقفون'),
        ('partners', 'الجهات الشريكة'),
    ]

    page = ParentalKey('TestimonialsPage', on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=150, verbose_name="صاحب التزكية / الاسم")
    author_title = models.CharField(max_length=150, verbose_name="اللقب أو الصفة (مثل: رئيس محكمة، أستاذ فقه، خبير وقفي)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='scholars', verbose_name="تصنيف التزكية")
    organization = models.CharField(max_length=200, blank=True, default="", verbose_name="الجهة أو المؤسسة (اختياري)")
    quote = models.TextField(verbose_name="نص التزكية أو الشهادة")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True, verbose_name="الصورة الشخصية (اختياري)")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    rating = models.PositiveIntegerField(default=5, verbose_name="التقييم من 5")
    is_featured = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('author_name'),
        FieldPanel('author_title'),
        FieldPanel('category'),
        FieldPanel('organization'),
        FieldPanel('quote'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('rating'),
        FieldPanel('is_featured'),
    ]

    @property
    def author_role(self):
        return self.author_title

    class Meta:
        verbose_name = "تزكية أو رأي"
        verbose_name_plural = "التزكيات والآراء"


class TestimonialsPage(Page):
    subheading = models.CharField(max_length=100, default="ثقة وأثر مستدام", verbose_name="العنوان الفرعي")
    heading = models.CharField(max_length=200, default="تزكيات العلماء والخبراء وشركاء الأثر", verbose_name="العنوان الرئيسي")

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('heading'),
        InlinePanel('testimonials', heading="💬 قائمة التزكيات والآراء", label="تزكية أو رأي"),
    ]

    template = "home/testimonials_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['testimonials'] = self.testimonials.filter(is_featured=True)
        return context


# ==============================================================================
# 7. VIDEOS PAGE (صفحة ألبوم الفيديو)
# ==============================================================================

class VideosPageItem(Orderable):
    page = ParentalKey('VideosPage', on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255, verbose_name="عنوان الفيديو")
    date_text = models.CharField(max_length=100, default="الخميس، 01 أكتوبر 2026", verbose_name="تاريخ النشر")
    video_url = models.CharField(
        max_length=500, 
        default="https://www.youtube.com/watch?v=ScMzIvxBSi4", 
        verbose_name="رابط الفيديو (يوتيوب أو رابط خارجي)"
    )
    thumbnail = models.ImageField(upload_to="videos/", blank=True, null=True, verbose_name="صورة غلاف الفيديو")
    image_static_fallback = models.CharField(
        max_length=255, 
        blank=True, 
        default="img/rafed_image/background/4.jpg", 
        verbose_name="مسار صورة بديلة من static"
    )
    duration = models.CharField(max_length=50, blank=True, default="03:20", verbose_name="مدة الفيديو")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في ألبوم الفيديو")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('video_url'),
        FieldPanel('thumbnail'),
        FieldPanel('image_static_fallback'),
        FieldPanel('duration'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "فيديو"
        verbose_name_plural = "فيديوهات المكتبة المرئية"

    @property
    def embed_url(self):
        url = self.video_url
        if "youtube.com/watch?v=" in url:
            vid_id = url.split("v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{vid_id}?autoplay=1"
        elif "youtu.be/" in url:
            vid_id = url.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{vid_id}?autoplay=1"
        return url


class VideosPage(Page):
    subheading = models.CharField(max_length=100, default="المكتبة المرئية", verbose_name="العنوان الفرعي")
    heading = models.CharField(max_length=200, default="شاهد وتعرف على وثائقيات ومبادرات رافد للأوقاف", verbose_name="العنوان الرئيسي")

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('heading'),
        InlinePanel('videos', heading="🎬 مكتبة الفيديوهات والندوات", label="فيديو"),
    ]

    template = "home/videos_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        context['videos'] = self.videos.filter(is_active=True)
        return context


# ==============================================================================
# 8. CONTACT PAGE (صفحة تواصل معنا)
# ==============================================================================

class ContactPage(Page):
    subheading = models.CharField(max_length=100, default="قنوات الاتصال المباشر", verbose_name="العنوان الفرعي")
    heading = models.CharField(max_length=200, default="نسعد بخدمتكم وتلقي استفساراتكم", verbose_name="العنوان الرئيسي")

    # Main Contact Info
    phone = models.CharField(max_length=50, default="0552002057", verbose_name="رقم الهاتف الموحد")
    whatsapp = models.CharField(max_length=50, default="966552002057", verbose_name="رقم واتساب (أرقام فقط)")
    email = models.EmailField(default="info@rafed.org.sa", verbose_name="البريد الإلكتروني الرسمي")
    address = models.CharField(max_length=255, default="المملكة العربية السعودية - مدينة جدة - حي الفيحاء", verbose_name="العنوان والمقر")
    working_hours = models.CharField(max_length=255, default="الأحد - الخميس: 8:00 صباحاً حتى 4:00 مساءً", verbose_name="أوقات العمل الرسمية")

    # Social Media Links
    twitter_url = models.URLField(default="https://twitter.com/rafid_sa", verbose_name="رابط منصة إكس (تويتر)")
    linkedin_url = models.URLField(default="https://linkedin.com", verbose_name="رابط لينكد إن")
    instagram_url = models.URLField(default="https://instagram.com/rafid_sa", verbose_name="رابط إنستغرام")
    youtube_url = models.URLField(default="https://youtube.com", verbose_name="رابط قناة يوتيوب")
    telegram_url = models.URLField(default="https://t.me/rafid_sa", verbose_name="رابط قناة تيليجرام")

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('heading'),
        MultiFieldPanel([
            FieldPanel('phone'),
            FieldPanel('whatsapp'),
            FieldPanel('email'),
            FieldPanel('address'),
            FieldPanel('working_hours'),
        ], heading="📞 معلومات وأرقام التواصل"),
        MultiFieldPanel([
            FieldPanel('twitter_url'),
            FieldPanel('linkedin_url'),
            FieldPanel('instagram_url'),
            FieldPanel('youtube_url'),
            FieldPanel('telegram_url'),
        ], heading="🌐 منصات التواصل الاجتماعي"),
    ]

    template = "home/contact_page.html"


# ==============================================================================
# 9. VISITOR CONTACT INQUIRIES (صندوق الرسائل والاستفسارات)
# ==============================================================================

@register_snippet
class ContactInquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'طلب جديد 🔴'),
        ('in_progress', 'قيد المتابعة 🟡'),
        ('done', 'تم الرد والتواصل 🟢'),
    ]

    name = models.CharField(max_length=150, verbose_name="الاسم الكريم")
    phone = models.CharField(max_length=50, verbose_name="رقم الجوال")
    email = models.EmailField(blank=True, default="", verbose_name="البريد الإلكتروني")
    subject = models.CharField(max_length=150, verbose_name="نوع الطلب / الاستشارة")
    message = models.TextField(verbose_name="نص الرسالة أو الاستفسار")
    prefer_whatsapp = models.BooleanField(default=True, verbose_name="يفضل الرد عبر واتساب")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name="حالة الطلب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ ووقت الإرسال")
    admin_notes = models.TextField(blank=True, default="", verbose_name="ملاحظات الإدارة الداخلية")

    panels = [
        FieldPanel('name'),
        FieldPanel('phone'),
        FieldPanel('email'),
        FieldPanel('subject'),
        FieldPanel('message'),
        FieldPanel('prefer_whatsapp'),
        FieldPanel('status'),
        FieldPanel('admin_notes'),
    ]

    class Meta:
        verbose_name = "طلب تواصل أو استشارة"
        verbose_name_plural = "📩 صندوق رسائل واستفسارات تواصل معنا"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


# Fallback helper for legacy references if any
@register_snippet
class SiteContactSettings(models.Model):
    phone = models.CharField(max_length=50, default="0552002057", verbose_name="رقم الهاتف الموحد")
    whatsapp = models.CharField(max_length=50, default="966552002057", verbose_name="رقم واتساب")
    email = models.EmailField(default="info@rafed.org.sa", verbose_name="البريد الإلكتروني")
    address = models.CharField(max_length=255, default="المملكة العربية السعودية - جدة - حي الفيحاء", verbose_name="العنوان والمقر")
    working_hours = models.CharField(max_length=255, default="الأحد - الخميس: 8:00 صباحاً حتى 4:00 مساءً", verbose_name="أوقات العمل")
    twitter_url = models.URLField(default="https://twitter.com/rafid_sa", verbose_name="تويتر")
    linkedin_url = models.URLField(default="https://linkedin.com", verbose_name="لينكد إن")
    instagram_url = models.URLField(default="https://instagram.com/rafid_sa", verbose_name="إنستغرام")
    youtube_url = models.URLField(default="https://youtube.com", verbose_name="يوتيوب")
    telegram_url = models.URLField(default="https://t.me/rafid_sa", verbose_name="تيليجرام")

    class Meta:
        verbose_name = "إعدادات التواصل الاحتياطية"
        verbose_name_plural = "إعدادات التواصل الاحتياطية"

    @classmethod
    def get_settings(cls):
        contact_page = ContactPage.objects.first()
        if contact_page:
            return contact_page
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


# ==============================================================================
# 10. NAVBAR & TOPBAR SETTINGS (إعدادات النافبار والقائمة العلوية)
# ==============================================================================

@register_snippet
class NavbarSettings(models.Model):
    # --- 1. الشعار والهوية ---
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="شعار الجمعية في القائمة (Logo)"
    )
    logo_alt = models.CharField(max_length=150, default="جمعية رافد للأوقاف", verbose_name="النص البديل للشعار (Alt text)")

    # --- 2. زر ورقم الاتصال في النافبار ---
    phone_label = models.CharField(max_length=100, default="تواصل معنا", verbose_name="نص زر الاتصال")
    phone_number = models.CharField(max_length=50, default="0552002057", verbose_name="رقم الهاتف الظاهر")
    phone_call_url = models.CharField(max_length=50, default="0552002057", verbose_name="رقم الاتصال المباشر (tel:)")

    # --- 3. روابط التواصل الاجتماعي في الشريط العلوي ---
    twitter_url = models.URLField(blank=True, default="https://twitter.com/rafid_sa", verbose_name="رابط إكس (تويتر)")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com", verbose_name="رابط لينكد إن")
    instagram_url = models.URLField(blank=True, default="https://instagram.com/rafid_sa", verbose_name="رابط إنستغرام")
    facebook_url = models.URLField(blank=True, default="", verbose_name="رابط فيسبوك")
    youtube_url = models.URLField(blank=True, default="", verbose_name="رابط يوتيوب")
    whatsapp_url = models.CharField(max_length=200, blank=True, default="https://wa.me/966552002057", verbose_name="رابط واتساب")

    # --- 4. الروابط السريعة يمين الشريط العلوي ---
    topbar_link1_text = models.CharField(max_length=100, default="الرئيسية", verbose_name="نص الرابط 1")
    topbar_link1_url = models.CharField(max_length=255, default="/", verbose_name="مسار / رابط الرابط 1")
    topbar_link2_text = models.CharField(max_length=100, default="التوظيف", verbose_name="نص الرابط 2")
    topbar_link2_url = models.CharField(max_length=255, default="#", verbose_name="مسار / رابط الرابط 2")
    topbar_link3_text = models.CharField(max_length=100, default="الشروط", verbose_name="نص الرابط 3")
    topbar_link3_url = models.CharField(max_length=255, default="#", verbose_name="مسار / رابط الرابط 3")
    topbar_link4_text = models.CharField(max_length=100, default="الخصوصية", verbose_name="نص الرابط 4")
    topbar_link4_url = models.CharField(max_length=255, default="#", verbose_name="مسار / رابط الرابط 4")

    # --- 5. مسميات عناصر القائمة الرئيسية ---
    nav_home_label = models.CharField(max_length=100, default="الرئيسية", verbose_name="نص رابط الرئيسية")
    nav_about_label = models.CharField(max_length=100, default="من نحن", verbose_name="نص رابط من نحن")
    nav_services_label = models.CharField(max_length=100, default="خدماتنا", verbose_name="نص رابط خدماتنا")
    nav_projects_label = models.CharField(max_length=100, default="مشاريعنا", verbose_name="نص رابط مشاريعنا")
    nav_pages_label = models.CharField(max_length=100, default="صفحات", verbose_name="نص القائمة المنسدلة (صفحات)")
    nav_team_label = models.CharField(max_length=100, default="فريقنا", verbose_name="نص رابط فريقنا")
    nav_team_desc = models.CharField(max_length=150, default="نخبة خبرائنا وكفاءاتنا", verbose_name="وصف رابط فريقنا")
    nav_testimonials_label = models.CharField(max_length=100, default="قالوا عنا", verbose_name="نص رابط قالوا عنا")
    nav_testimonials_desc = models.CharField(max_length=150, default="تزكيات العلماء والشركاء", verbose_name="وصف رابط قالوا عنا")
    nav_videos_label = models.CharField(max_length=100, default="ألبوم الفيديو", verbose_name="نص رابط ألبوم الفيديو")
    nav_videos_desc = models.CharField(max_length=150, default="وثائقيات وندوات مرئية", verbose_name="وصف رابط ألبوم الفيديو")
    nav_contact_label = models.CharField(max_length=100, default="تواصل معنا", verbose_name="نص رابط تواصل معنا")

    panels = [
        MultiFieldPanel([
            FieldPanel('logo'),
            FieldPanel('logo_alt'),
        ], heading="🖼️ شعار الجمعية في القائمة العلوية"),

        MultiFieldPanel([
            FieldPanel('phone_label'),
            FieldPanel('phone_number'),
            FieldPanel('phone_call_url'),
        ], heading="📞 زر الاتصال المباشر ورقم الهاتف في النافبار"),

        MultiFieldPanel([
            FieldPanel('twitter_url'),
            FieldPanel('linkedin_url'),
            FieldPanel('instagram_url'),
            FieldPanel('facebook_url'),
            FieldPanel('youtube_url'),
            FieldPanel('whatsapp_url'),
        ], heading="🌐 روابط التواصل الاجتماعي (الشريط العلوي)"),

        MultiFieldPanel([
            FieldPanel('topbar_link1_text'),
            FieldPanel('topbar_link1_url'),
            FieldPanel('topbar_link2_text'),
            FieldPanel('topbar_link2_url'),
            FieldPanel('topbar_link3_text'),
            FieldPanel('topbar_link3_url'),
            FieldPanel('topbar_link4_text'),
            FieldPanel('topbar_link4_url'),
        ], heading="🔗 الروابط السريعة (يمين الشريط العلوي)"),

        MultiFieldPanel([
            FieldPanel('nav_home_label'),
            FieldPanel('nav_about_label'),
            FieldPanel('nav_services_label'),
            FieldPanel('nav_projects_label'),
            FieldPanel('nav_pages_label'),
            FieldPanel('nav_team_label'),
            FieldPanel('nav_team_desc'),
            FieldPanel('nav_testimonials_label'),
            FieldPanel('nav_testimonials_desc'),
            FieldPanel('nav_videos_label'),
            FieldPanel('nav_videos_desc'),
            FieldPanel('nav_contact_label'),
        ], heading="📑 عناوين عناصر القائمة الرئيسية (النافبار)"),
    ]

    class Meta:
        verbose_name = "معلومات النافبار والقائمة العلوية"
        verbose_name_plural = "🔝 معلومات النافبار والقائمة العلوية"

    def __str__(self):
        return "إعدادات النافبار والقائمة العلوية"

    @classmethod
    def get_settings(cls):
        obj = cls.objects.first()
        if not obj:
            obj = cls.objects.create()
        return obj

