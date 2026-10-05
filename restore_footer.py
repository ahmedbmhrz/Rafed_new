import re

html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace footer section
footer_pattern = r'(<!-- Footer Start -->.*?<!-- Copyright End -->)'
match = re.search(footer_pattern, html, flags=re.DOTALL)
if match:
    restored_footer = """
    <!-- Footer Start -->
    <div class="py-4 mt-5" style="width: 100vw; position: relative; right: 50%; margin-right: calc(-50vw + 50%); background-color: var(--forest); z-index: 10;">
        <div class="container text-light">
            <div class="row g-3">
                
                <!-- Contact Us -->
                <div class="col-lg-4 col-md-6 text-start">
                    <h4 class="text-white mb-3" style="font-weight: bold; padding-bottom: 5px; font-size: 20px;">إتصل بنا</h4>
                    <div class="mb-2 d-flex align-items-center justify-content-start" style="font-size: 14px;">
                        <div style="min-width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-phone-alt text-white"></i></div>
                        <span class="me-3" style="font-family: var(--font-mono); direction: ltr;">0552002057</span>
                    </div>
                    <div class="mb-2 d-flex align-items-center justify-content-start" style="font-size: 14px;">
                        <div style="min-width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-envelope text-white"></i></div>
                        <span class="me-3" style="font-family: var(--font-mono);">info@rafed.org.sa</span>
                    </div>
                    <div class="mb-2 d-flex align-items-center justify-content-start" style="font-size: 14px;">
                        <div style="min-width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-map-marker-alt text-white"></i></div>
                        <span class="me-3">جدة - حي الفيحاء</span>
                    </div>
                    
                    <h5 class="text-white mb-3 mt-4" style="font-size: 15px;">تجدنا على</h5>
                    <div class="d-flex justify-content-start">
                        <a class="btn btn-square rounded me-2 d-flex align-items-center justify-content-center" href="#" style="background: #ff0000; color: white; border: none; width: 32px; height: 32px;"><i class="bi bi-youtube"></i></a>
                        <a class="btn btn-square rounded me-2 d-flex align-items-center justify-content-center" href="#" style="background: #405de6; color: white; border: none; width: 32px; height: 32px;"><i class="bi bi-instagram"></i></a>
                        <a class="btn btn-square rounded d-flex align-items-center justify-content-center" href="#" style="background: #1da1f2; color: white; border: none; width: 32px; height: 32px;"><i class="bi bi-twitter"></i></a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="col-lg-4 col-md-6 text-center">
                    <h4 class="text-white mb-3" style="font-weight: bold; padding-bottom: 5px; font-size: 20px;">الروابط السريعة</h4>
                    <div class="d-flex flex-column align-items-center">
                        <a class="text-light mb-3" href="#" style="text-decoration: none; font-size: 15px; transition: 0.3s;"><i class="bi bi-chevron-left me-2" style="color: var(--forest-pale);"></i>الرئيسية</a>
                        <a class="text-light mb-3" href="#" style="text-decoration: none; font-size: 15px; transition: 0.3s;"><i class="bi bi-chevron-left me-2" style="color: var(--forest-pale);"></i>نبذة عنا</a>
                    </div>
                </div>

                <!-- Vision 2030 -->
                <div class="col-lg-4 col-md-6 text-end">
                    <h4 class="text-white mb-3" style="font-weight: bold; padding-bottom: 5px; font-size: 20px;">نبذة عنا</h4>
                    <br>
                    <img src="https://www.vision2030.gov.sa/v2030/images/v2030-logo.svg" alt="Vision 2030" style="max-width: 140px; filter: brightness(0) invert(1);">
                </div>

            </div>
        </div>
    </div>
    
    <!-- Copyright Start -->
    <div class="copyright text-light py-3 mb-0" style="margin-bottom: 0 !important; background: var(--forest-3); width: 100vw; position: relative; right: 50%; margin-right: calc(-50vw + 50%); z-index: 10;">
        <div class="container">
            <div class="row">
                <div class="col-md-12 text-center mb-3 mb-md-0" style="color: var(--paper); font-size: 14px;">
                    جميع الحقوق محفوظة لجمعية رافد للأوقاف &copy; 2026
                </div>
            </div>
        </div>
    </div>
    <!-- Copyright End -->
    """
    html = html[:match.start()] + restored_footer + html[match.end():]
    
    html = re.sub(r'js/main\.js\?v=\d+\.\d+', 'js/main.js?v=8.0', html)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
