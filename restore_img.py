# -*- coding: utf-8 -*-
import re

file_path = 'home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Isolate the About Start section
about_pattern = r'(<!-- About Start -->.*?<!-- About End -->)'
match = re.search(about_pattern, html, flags=re.DOTALL)
if match:
    about_html = match.group(1)
    # Replace the PNG with the building JPG
    about_html = about_html.replace('img/rafed_image/background/6aa0f543b127d8.21470575.png', 'img/rafed_image/background/3687745542.jpg')
    
    html = html[:match.start()] + about_html + html[match.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Reverted image successfully.")
