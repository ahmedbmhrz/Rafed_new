from django.db import models
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


# ==============================================================================
# 1. SITE CONTACT & BRAND SETTINGS (إعدادات التواصل والموقع الموحدة)
# ==============================================================================
@register_snippet
class SiteContactSettings(models.Model):
    phone = models.CharField(max_length=50, default="0552002057", verbose_name="رقم الهاتف الموحد")
    whatsapp = models.CharField(max_length=50, default="966552002057", verbose_name="رقم واتساب (أرقام فقط)")
    email = models.EmailField(default="info@rafed.org.sa", verbose_name="البريد الإلكتروني الرسمي")
    address = models.CharField(max_length=255, default="المملكة العربية السعودية - جدة - حي الفيحاء", verbose_name="العنوان والمقر")
    working_hours = models.CharField(max_length=255, default="الأحد - الخميس: 8:00 صباحاً حتى 4:00 مساءً", verbose_name="أوقات العمل الرسمية")
    
    # Social Media Links
    twitter_url = models.URLField(default="https://twitter.com/rafid_sa", verbose_name="رابط منصة إكس (تويتر)")
    linkedin_url = models.URLField(default="https://linkedin.com", verbose_name="رابط لينكد إن")
    instagram_url = models.URLField(default="https://instagram.com/rafid_sa", verbose_name="رابط إنستغرام")
    youtube_url = models.URLField(default="https://youtube.com", verbose_name="رابط قناة يوتيوب")
    telegram_url = models.URLField(default="https://t.me/rafid_sa", verbose_name="رابط قناة تيليجرام")

    panels = [
        MultiFieldPanel([
            FieldPanel('phone'),
            FieldPanel('whatsapp'),
            FieldPanel('email'),
            FieldPanel('address'),
            FieldPanel('working_hours'),
        ], heading="معلومات الاتصال الأساسية"),
        MultiFieldPanel([
            FieldPanel('twitter_url'),
            FieldPanel('linkedin_url'),
            FieldPanel('instagram_url'),
            FieldPanel('youtube_url'),
            FieldPanel('telegram_url'),
        ], heading="حسابات التواصل الاجتماعي"),
    ]

    class Meta:
        verbose_name = "إعدادات التواصل والموقع"
        verbose_name_plural = "⚙️ إعدادات التواصل والموقع"

    def __str__(self):
        return f"إعدادات التواصل الرسمية ({self.phone} - {self.email})"

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


# ==============================================================================
# 2. ACHIEVEMENTS & STATISTICS (إنجازاتنا والأرقام)
# ==============================================================================
@register_snippet
class AchievementMetric(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان الإنجاز")
    number = models.CharField(max_length=50, verbose_name="الرقم / القيمة (مثل: 73 أو 290570)")
    unit = models.CharField(max_length=50, blank=True, verbose_name="الوحدة (مثل: لقاء، ريال، متطوع، منشور)")
    icon = models.CharField(max_length=80, default="fa-chart-line", verbose_name="أيقونة FontAwesome (مثل: fa-users, fa-chalkboard-teacher)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة الرئيسية")

    panels = [
        FieldPanel('title'),
        FieldPanel('number'),
        FieldPanel('unit'),
        FieldPanel('icon'),
        FieldPanel('order'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "إنجاز أو رقم إحصائي"
        verbose_name_plural = "📊 إنجازاتنا (أرقام وإحصائيات)"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} ({self.number} {self.unit})"


# ==============================================================================
# 3. NEWS & EVENTS (أخبار الجمعية والفعاليات)
# ==============================================================================
@register_snippet
class NewsItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    date_text = models.CharField(max_length=100, verbose_name="تاريخ النشر (مثل: الأربعاء، 05 أغسطس 2026)")
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="صورة الخبر")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="img/rafed_image/background/6aa0f543b127d8.21470575.png", verbose_name="مسار صورة بديلة من static")
    excerpt = models.TextField(blank=True, verbose_name="موجز الخبر أو التفاصيل")
    link = models.CharField(max_length=255, blank=True, default="#", verbose_name="رابط الخبر (اختياري)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="منشور")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('excerpt'),
        FieldPanel('link'),
        FieldPanel('order'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "📰 أخبار الجمعية والفعاليات"
        ordering = ['order', '-id']

    def __str__(self):
        return self.title


# ==============================================================================
# 4. EDUCATIONAL CONTENT (تصاميم تثقيفية عن الأوقاف)
# ==============================================================================
@register_snippet
class EducationalDesign(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان المحتوى التثقيفي")
    date_text = models.CharField(max_length=100, verbose_name="التاريخ (مثل: الثلاثاء، 21 أكتوبر 2025)")
    image = models.ImageField(upload_to="infographics/", blank=True, null=True, verbose_name="صورة الغلاف أو التصميم")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="img/rafed_image/background/6aa0f543b127d8.21470575.png", verbose_name="مسار صورة بديلة من static")
    badge_text = models.CharField(max_length=50, default="6 صور", verbose_name="الشارة التعريفية (مثل: 6 صور، إنفوجرافيك، دليل PDF)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('image'),
        FieldPanel('image_static_fallback'),
        FieldPanel('badge_text'),
        FieldPanel('order'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "تصميم تثقيفي"
        verbose_name_plural = "🎨 تصاميم تثقيفية عن الأوقاف"
        ordering = ['order', '-id']

    def __str__(self):
        return self.title


# ==============================================================================
# 5. PROJECTS (مشاريعنا الوقفية)
# ==============================================================================
@register_snippet
class ProjectItem(models.Model):
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

    title = models.CharField(max_length=255, verbose_name="اسم المشروع الوقفي")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tasees', verbose_name="تصنيف المشروع")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ongoing', verbose_name="حالة المشروع")
    description = models.TextField(verbose_name="وصف المشروع")
    image = models.ImageField(upload_to="projects/", blank=True, null=True, verbose_name="صورة المشروع")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static (اختياري)")
    progress_percentage = models.PositiveIntegerField(default=75, verbose_name="نسبة الإنجاز %")
    target_amount = models.CharField(max_length=100, blank=True, default="", verbose_name="المستهدف المالي أو العددي (اختياري)")
    is_featured = models.BooleanField(default=True, verbose_name="ظاهر في صفحة المشاريع")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")

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
        FieldPanel('order'),
    ]

    class Meta:
        verbose_name = "مشروع وقفي"
        verbose_name_plural = "🏗️ مشاريعنا الوقفية"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


# ==============================================================================
# 6. TEAM MEMBERS (فريقنا ونخبة خبرائنا)
# ==============================================================================
@register_snippet
class TeamMember(models.Model):
    CATEGORY_CHOICES = [
        ('board', 'مجلس الإدارة'),
        ('sharia', 'الهيئة الشرعية والاستشارية'),
        ('exec', 'الإدارة التنفيذية'),
    ]

    name = models.CharField(max_length=150, verbose_name="الاسم الكريم")
    role = models.CharField(max_length=150, verbose_name="المسمى / المنصب")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='board', verbose_name="الفئة / القسم")
    bio = models.TextField(blank=True, default="", verbose_name="نبذة عن العضو أو المؤهلات")
    image = models.ImageField(upload_to="team/", blank=True, null=True, verbose_name="الصورة الشخصية")
    image_static_fallback = models.CharField(max_length=255, blank=True, default="", verbose_name="مسار صورة بديلة من static")
    initials = models.CharField(max_length=10, blank=True, default="", verbose_name="الحروف الأولى (إذا لم تتوفر صورة)")
    linkedin_url = models.CharField(max_length=255, blank=True, default="", verbose_name="رابط لينكد إن أو البريد (اختياري)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
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
        FieldPanel('order'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "عضو في الفريق"
        verbose_name_plural = "👥 فريقنا (أعضاء الفريق والخبراء)"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name} - {self.role} ({self.get_category_display()})"


# ==============================================================================
# 7. TESTIMONIALS (قالوا عنا وتزكيات الشركاء)
# ==============================================================================
@register_snippet
class TestimonialItem(models.Model):
    author_name = models.CharField(max_length=150, verbose_name="صاحب التزكية / الاسم")
    author_title = models.CharField(max_length=150, verbose_name="اللقب أو الصفة (مثل: رئيس محكمة، أستاذ فقه، خبير وقفي)")
    organization = models.CharField(max_length=200, blank=True, default="", verbose_name="الجهة أو المؤسسة (اختياري)")
    quote = models.TextField(verbose_name="نص التزكية أو الشهادة")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True, verbose_name="الصورة الشخصية (اختياري)")
    rating = models.PositiveIntegerField(default=5, verbose_name="التقييم من 5")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_featured = models.BooleanField(default=True, verbose_name="ظاهر في الصفحة")

    panels = [
        FieldPanel('author_name'),
        FieldPanel('author_title'),
        FieldPanel('organization'),
        FieldPanel('quote'),
        FieldPanel('image'),
        FieldPanel('rating'),
        FieldPanel('order'),
        FieldPanel('is_featured'),
    ]

    class Meta:
        verbose_name = "تزكية أو رأي"
        verbose_name_plural = "💬 قالوا عنا (التزكيات والآراء)"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.author_name} - {self.organization}"


# ==============================================================================
# 8. CONTACT INQUIRIES (صندوق رسائل واستفسارات تواصل معنا)
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


# ==============================================================================

# ==============================================================================
# 9. VIDEO ALBUM (ألبوم الفيديو)
# ==============================================================================
@register_snippet
class VideoItem(models.Model):
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
    duration = models.CharField(max_length=50, blank=True, default="03:20", verbose_name="مدة الفيديو (مثل: 03:20)")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="ظاهر في ألبوم الفيديو")

    panels = [
        FieldPanel('title'),
        FieldPanel('date_text'),
        FieldPanel('video_url'),
        FieldPanel('thumbnail'),
        FieldPanel('image_static_fallback'),
        FieldPanel('duration'),
        FieldPanel('order'),
        FieldPanel('is_active'),
    ]

    class Meta:
        verbose_name = "فيديو"
        verbose_name_plural = "🎬 ألبوم الفيديو"
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

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

# HOMEPAGE MODEL
# ==============================================================================
class HomePage(Page):
    hero_subheading = models.CharField(max_length=100, default="جمعية رافد للأوقاف", verbose_name="العنوان الفرعي")
    hero_heading = models.CharField(max_length=100, default="نؤسس ونطور الأوقاف", verbose_name="العنوان الرئيسي")
    hero_text = models.CharField(max_length=255, default="جمعية تعنى بتأسيس وتطوير واستدامة الكيانات الوقفية.", verbose_name="النص")

    vision_title = models.CharField(max_length=100, default="رؤيتنا", verbose_name="عنوان الرؤية")
    vision_text = models.TextField(default="الريادة في تطوير واستدامة الأوقاف.", verbose_name="نص الرؤية")
    
    mission_title = models.CharField(max_length=100, default="رسالتنا", verbose_name="عنوان الرسالة")
    mission_text = models.TextField(default="تقديم خدمات متنوعة للراغبين في الوقف.", verbose_name="نص الرسالة")

    # Statistics fallbacks
    stats_years = models.IntegerField(default=10, verbose_name="سنوات الخبرة")
    stats_projects = models.IntegerField(default=50, verbose_name="المشاريع الوقفية")
    stats_beneficiaries = models.IntegerField(default=10000, verbose_name="المستفيدين")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_subheading'),
            FieldPanel('hero_heading'),
            FieldPanel('hero_text'),
        ], heading="القسم الرئيسي (Hero)"),
        MultiFieldPanel([
            FieldPanel('vision_title'),
            FieldPanel('vision_text'),
            FieldPanel('mission_title'),
            FieldPanel('mission_text'),
        ], heading="الرؤية والرسالة"),
        MultiFieldPanel([
            FieldPanel('stats_years'),
            FieldPanel('stats_projects'),
            FieldPanel('stats_beneficiaries'),
        ], heading="الإحصائيات الأساسية"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['achievements'] = AchievementMetric.objects.filter(is_active=True)
        context['news_items'] = NewsItem.objects.filter(is_active=True)
        context['educational_items'] = EducationalDesign.objects.filter(is_active=True)
        context['projects'] = ProjectItem.objects.filter(is_featured=True)
        context['testimonials'] = TestimonialItem.objects.filter(is_featured=True)
        context['video_items'] = VideoItem.objects.filter(is_active=True)
        context['site_settings'] = SiteContactSettings.get_settings()
        return context
