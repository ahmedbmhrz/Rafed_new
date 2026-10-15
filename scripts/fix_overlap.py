import re

# 1. Fix HTML: Remove Item 5 and Item 6 from Testimonial Carousel
html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

testimonial_pattern = r'(<!-- Testimonial Start -->.*?<!-- Testimonial End -->)'
match = re.search(testimonial_pattern, html, flags=re.DOTALL)
if match:
    testimonial_html = match.group(1)
    # Remove the bad items
    bad_items_pattern = r'<!-- Item 5 -->.*?<!-- Item 4 -->'
    testimonial_html_fixed = re.sub(bad_items_pattern, '<!-- Item 4 -->', testimonial_html, flags=re.DOTALL)
    
    html = html[:match.start()] + testimonial_html_fixed + html[match.end():]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
# 2. Fix CSS: Correct the broken selector
css_path = 'rafed_site/static/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I will just replace the exact broken block
broken_css_block_1 = r'\.news-carousel \.owl-nav, \.content-carousel \.owl-nav \.owl-prev, \.news-carousel \.owl-nav, \.content-carousel \.owl-nav \.owl-next \{ width: 40px;'
fixed_css_block_1 = r'.news-carousel .owl-nav .owl-prev, .content-carousel .owl-nav .owl-prev, .news-carousel .owl-nav .owl-next, .content-carousel .owl-nav .owl-next { width: 40px;'

broken_css_block_2 = r'\.news-carousel \.owl-nav, \.content-carousel \.owl-nav \.owl-prev:hover, \.news-carousel \.owl-nav, \.content-carousel \.owl-nav \.owl-next:hover \{ background: var\(--ds-gold\) !important; \}'
fixed_css_block_2 = r'.news-carousel .owl-nav .owl-prev:hover, .content-carousel .owl-nav .owl-prev:hover, .news-carousel .owl-nav .owl-next:hover, .content-carousel .owl-nav .owl-next:hover { background: var(--ds-gold) !important; }'

css = re.sub(broken_css_block_1, fixed_css_block_1, css)
css = re.sub(broken_css_block_2, fixed_css_block_2, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
