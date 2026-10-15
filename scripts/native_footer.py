import re
html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Completely replace the broken footer with a gorgeous template-native footer
footer_pattern = r'(<!-- Footer Start -->.*?<!-- Copyright End -->)'
match = re.search(footer_pattern, html, flags=re.DOTALL)
if match:
    new_footer = """
    <!-- Footer Start -->
    <div class="container-fluid text-light footer mt-5 pt-5 wow fadeIn" data-wow-delay="0.1s" style="background-color: var(--forest); border-top: 4px solid var(--ds-gold); padding-bottom: 0 !important;">
        <div class="container py-5">
            <div class="row g-5">
                
                <!-- Contact Us -->
                <div class="col-lg-4 col-md-6">
                    <h4 class="text-light mb-4" style="color: var(--ds-gold) !important; font-weight: bold;">إتصل بنا</h4>
                    <p class="mb-2"><i class="fa fa-phone-alt ms-3" style="color: var(--ds-gold);"></i><span style="font-family: var(--font-mono); direction: ltr; display: inline-block;">0552002057</span></p>
                    <p class="mb-2"><i class="fa fa-envelope ms-3" style="color: var(--ds-gold);"></i><span style="font-family: var(--font-mono);">info@rafed.org.sa</span></p>
                    <p class="mb-4"><i class="fa fa-map-marker-alt ms-3" style="color: var(--ds-gold);"></i>جدة - حي الفيحاء</p>
                    
                    <h5 class="text-light mb-3 mt-4" style="font-size: 16px;">تجدنا على</h5>
                    <div class="d-flex pt-2">
                        <a class="btn btn-square btn-outline-light rounded-circle ms-2" href="#"><i class="fab fa-youtube"></i></a>
                        <a class="btn btn-square btn-outline-light rounded-circle ms-2" href="#"><i class="fab fa-instagram"></i></a>
                        <a class="btn btn-square btn-outline-light rounded-circle ms-2" href="#"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="col-lg-4 col-md-6">
                    <h4 class="text-light mb-4" style="color: var(--ds-gold) !important; font-weight: bold;">الروابط السريعة</h4>
                    <a class="btn btn-link" href="#">الرئيسية</a>
                    <a class="btn btn-link" href="#">نبذة عنا</a>
                </div>

                <!-- Vision 2030 -->
                <div class="col-lg-4 col-md-6">
                    <h4 class="text-light mb-4" style="color: var(--ds-gold) !important; font-weight: bold;">رؤية 2030</h4>
                    <img src="https://upload.wikimedia.org/wikipedia/ar/thumb/4/43/Saudi_Vision_2030_logo.svg/1024px-Saudi_Vision_2030_logo.svg.png" alt="Vision 2030" style="max-width: 150px; filter: brightness(0) invert(1); opacity: 0.9;">
                </div>
            </div>
        </div>
    </div>
    
    <!-- Copyright Start -->
    <div class="container-fluid copyright text-light py-4 wow fadeIn" data-wow-delay="0.1s" style="background-color: var(--forest-3);">
        <div class="container">
            <div class="row">
                <div class="col-md-12 text-center" style="color: var(--paper); font-size: 14px;">
                    جميع الحقوق محفوظة لجمعية رافد للأوقاف &copy; 2026
                </div>
            </div>
        </div>
    </div>
    <!-- Copyright End -->
    """
    html = html[:match.start()] + new_footer + html[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
