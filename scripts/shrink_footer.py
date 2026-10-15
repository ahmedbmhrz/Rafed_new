import re

html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make overall padding smaller
html = html.replace('class="py-6 mt-5"', 'class="py-4 mt-5"')

# Make grid gaps smaller
html = html.replace('row g-5', 'row g-3')

# Shrink headings
html = html.replace('mb-4" style="font-weight: bold; padding-bottom: 5px;"', 'mb-3" style="font-weight: bold; padding-bottom: 5px; font-size: 20px;"')

# Shrink Contact Us text rows
html = html.replace('mb-4 d-flex align-items-center justify-content-end"', 'mb-2 d-flex align-items-center justify-content-end"')
html = html.replace('style="font-size: 15px;"', 'style="font-size: 14px;"')

# Shrink icon boxes
html = html.replace('min-width: 35px; height: 35px;', 'min-width: 28px; height: 28px;')

# Shrink social icons
html = html.replace('width: 40px; height: 40px;', 'width: 32px; height: 32px;')

# Make vision logo smaller
html = html.replace('max-width: 200px;', 'max-width: 140px;')

# Shrink copyright padding
html = html.replace('copyright text-light py-4', 'copyright text-light py-3')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
