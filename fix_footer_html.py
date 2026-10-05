import re
html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the <p> containing <div> bug
html = html.replace('<p class="mb-2 d-flex', '<div class="mb-2 d-flex')
html = html.replace('</span>\n                    </p>', '</span>\n                    </div>')

# Fix copyright bar margin
html = html.replace('copyright text-light py-3"', 'copyright text-light py-3 mb-0" style="margin-bottom: 0 !important;"')

# Fix Vision 2030 logo
html = html.replace('https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Saudi_Vision_2030_logo.svg/1024px-Saudi_Vision_2030_logo.svg.png', 'https://www.vision2030.gov.sa/v2030/images/v2030-logo.svg')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
