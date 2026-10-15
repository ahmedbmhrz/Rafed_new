# -*- coding: utf-8 -*-
import re

# Fix HTML
file_path = 'home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace adblock-triggering images with safe background images
html = html.replace('img/rafed_image/ads/ads1.jpg', 'img/rafed_image/background/6aa0f543b127d8.21470575.png')
html = html.replace('img/rafed_image/ads/ads2.jpg', 'img/rafed_image/background/3687745542.jpg')

# Find the end of the content carousel and duplicate items to ensure arrows show
pattern = r'(<div class="content-item bg-white rounded shadow-sm".*?</div>\s*</div>)'
matches = re.findall(pattern, html, flags=re.DOTALL)

# Let's just manually append two more items before the closing tag of the owl-carousel
if '<!-- Item 4 -->' in html:
    extra_items = """
                <!-- Item 5 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/background/4.jpg' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 8 صور
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">دليل الهوية البصرية</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الإثنين, 15 سبتمبر 2025</span>
                    </div>
                </div>
                
                <!-- Item 6 -->
                <div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">
                    <div style="position: relative;">
                        <img src="{% static 'img/rafed_image/background/6aa0f543b127d8.21470575.png' %}" alt="" style="width: 100%; height: 220px; object-fit: cover;">
                        <div style="position: absolute; top: 15px; left: 15px; background: var(--ds-gold); color: var(--paper); padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 700; font-family: var(--font-mono); box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
                            <i class="fa fa-images me-1"></i> 3 صور
                        </div>
                    </div>
                    <div class="p-4 text-center">
                        <h5 class="mb-2" style="color: var(--forest); font-family: var(--font-sans); font-weight: 700;">تقرير الإنجازات السنوي</h5>
                        <span class="d-block" style="font-size: 13px; color: var(--ink-3); font-family: var(--font-mono);">الخميس, 1 يناير 2026</span>
                    </div>
                </div>
    """
    html = html.replace('<!-- Item 4 -->', extra_items + '\n                <!-- Item 4 -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
