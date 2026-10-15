import re

html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

edu_pattern = r'(<!-- Educational Content Start -->.*?<!-- Educational Content End -->)'
match = re.search(edu_pattern, html, flags=re.DOTALL)
if match:
    edu_html = match.group(1)
    
    old_bg = 'style="background-color: var(--forest); position: relative; z-index: 10; border-top: 4px solid var(--ds-gold); border-bottom: 4px solid var(--ds-gold);"'
    new_bg = 'style="background: linear-gradient(rgba(12, 59, 46, 0.95), rgba(12, 59, 46, 0.95)), url(\'{% static \'img/rafed_image/background/3687745542.jpg\' %}\') center center no-repeat; background-size: cover; background-attachment: fixed; position: relative; z-index: 10; border-top: 4px solid var(--ds-gold); border-bottom: 4px solid var(--ds-gold); box-shadow: inset 0 0 50px rgba(0,0,0,0.5);"'
    
    edu_html = edu_html.replace(old_bg, new_bg)
    
    html = html[:match.start()] + edu_html + html[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
