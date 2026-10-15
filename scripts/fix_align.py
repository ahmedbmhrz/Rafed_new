import re
# 1. Update HTML
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change text-lg-end to text-lg-start for RTL right alignment
html = html.replace('<div class="col-lg-3 text-center text-lg-end wow fadeInUp"',
                    '<div class="col-lg-3 text-center text-lg-start wow fadeInUp"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update CSS
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.partner-carousel .owl-nav { position: absolute; top: 50%; width: 100%; transform: translateY(-50%); display: flex; justify-content: space-between; left: 0; padding: 0; pointer-events: none; }',
                  '.partner-carousel .owl-nav { position: absolute; top: 50%; width: calc(100% + 60px); transform: translateY(-50%); display: flex; justify-content: space-between; left: -30px; padding: 0; pointer-events: none; }')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
