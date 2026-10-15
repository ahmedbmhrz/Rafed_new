import re

# 1. HTML modifications
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

partners_pattern = r'(<!-- Partners Start -->.*?<!-- Partners End -->)'
match = re.search(partners_pattern, html, flags=re.DOTALL)
if match:
    partners_html = match.group(1)
    
    # Apply full-bleed trick to the white background
    old_div = '<div class="container-fluid py-6 bg-white" style="border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); position: relative; z-index: 10;">'
    new_div = '<div class="py-6 bg-white" style="width: 100vw; position: relative; right: 50%; margin-right: -50vw; border-top: 1px solid rgba(0,0,0,0.05); border-bottom: 1px solid rgba(0,0,0,0.05); z-index: 10;">'
    partners_html = partners_html.replace(old_div, new_div)
    
    # Fix the text squishing under logos
    partners_html = partners_html.replace('<h6 style="color: var(--ink-2); font-size: 14px;">', '<h6 style="color: var(--forest); font-size: 14px; font-weight: bold; white-space: nowrap;">')
    
    # Increase the padding around the carousel so arrows don't clip logos if they are inside
    partners_html = partners_html.replace('<div class="owl-carousel partner-carousel">', '<div class="owl-carousel partner-carousel px-4">')
    
    html = html[:match.start()] + partners_html + html[match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. CSS modifications
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove partner-carousel from the generic owl-nav rule
css = css.replace(', .partner-carousel .owl-nav {', ' {')
css = css.replace(', .partner-carousel .owl-nav .owl-prev,', ',')
css = css.replace(', .partner-carousel .owl-nav .owl-next {', ' {')
css = css.replace(', .partner-carousel .owl-nav .owl-prev:hover,', ',')
css = css.replace(', .partner-carousel .owl-nav .owl-next:hover {', ' {')

# Add specific partner-carousel rule
specific_rule = '''
.partner-carousel .owl-nav { position: absolute; top: 50%; width: 100%; transform: translateY(-50%); display: flex; justify-content: space-between; left: 0; padding: 0; pointer-events: none; }
.partner-carousel .owl-nav .owl-prev, .partner-carousel .owl-nav .owl-next { width: 35px; height: 35px; background: var(--paper) !important; color: var(--forest) !important; border: 2px solid var(--forest) !important; border-radius: 50%; display: flex; align-items: center; justify-content: center; pointer-events: auto; font-size: 16px; transition: 0.3s; }
.partner-carousel .owl-nav .owl-prev:hover, .partner-carousel .owl-nav .owl-next:hover { background: var(--forest) !important; color: white !important; }
'''

if '.partner-carousel .owl-nav {' not in css:
    css += specific_rule
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
