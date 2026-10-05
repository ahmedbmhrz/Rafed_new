import re
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Force the container to be an absolute full width block
html = html.replace('<div class="container-fluid py-6" style="background: linear-gradient',
                    '<div class="py-6" style="width: 100vw; margin-left: calc(-50vw + 50%); background: linear-gradient')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
