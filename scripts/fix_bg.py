import re

html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

edu_pattern = r'(<!-- Educational Content Start -->.*?<!-- Educational Content End -->)'
match = re.search(edu_pattern, html, flags=re.DOTALL)
if match:
    edu_html = match.group(1)
    
    # Make background full-width
    edu_html = edu_html.replace('<div class="container-xxl py-6" style="background: linear-gradient',
                                '<div class="container-fluid py-6" style="background: linear-gradient')
    
    # Fix the text color being overridden
    edu_html = edu_html.replace('style="color: #ffffff;"', 'style="color: #ffffff !important;"')
    
    html = html[:match.start()] + edu_html + html[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
