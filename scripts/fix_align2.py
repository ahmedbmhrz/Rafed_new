import re

html_path = 'rafed_site/templates/base.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix alignment for Contact Us
html = html.replace('<!-- Right Column: Contact Us -->\n                <div class="col-lg-4 col-md-6 text-end">',
                    '<!-- Right Column: Contact Us -->\n                <div class="col-lg-4 col-md-6 text-start">')
html = html.replace('justify-content-end', 'justify-content-start')

# Fix alignment for About Us
html = html.replace('<!-- Left Column: About/Vision -->\n                <div class="col-lg-4 col-md-6 text-start">',
                    '<!-- Left Column: About/Vision -->\n                <div class="col-lg-4 col-md-6 text-end">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
