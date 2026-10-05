import re

html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the order of Icons and Text in Contact Us
phone_old = '<span class="me-3" style="font-family: var(--font-mono); direction: ltr;">0552002057</span>\n                        <div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-phone-alt text-white"></i></div>'
phone_new = '<div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-phone-alt text-white"></i></div>\n                        <span class="me-3" style="font-family: var(--font-mono); direction: ltr;">0552002057</span>'

email_old = '<span class="me-3" style="font-family: var(--font-mono);">info@rafed.org.sa</span>\n                        <div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-envelope text-white"></i></div>'
email_new = '<div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-envelope text-white"></i></div>\n                        <span class="me-3" style="font-family: var(--font-mono);">info@rafed.org.sa</span>'

map_old = '<span class="me-3">جدة - حي الفيحاء</span>\n                        <div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-map-marker-alt text-white"></i></div>'
map_new = '<div style="min-width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-left: 15px;"><i class="fa fa-map-marker-alt text-white"></i></div>\n                        <span class="me-3">جدة - حي الفيحاء</span>'

html = html.replace(phone_old, phone_new)
html = html.replace(email_old, email_new)
html = html.replace(map_old, map_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
