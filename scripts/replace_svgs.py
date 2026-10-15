import re
import base64

# Read official SVGs
with open('rafed_site/static/img/rafed_image/rafid-identity/assets/leaf.svg', 'r', encoding='utf-8') as f:
    leaf_svg = f.read()

with open('rafed_site/static/img/rafed_image/rafid-identity/assets/wheat.svg', 'r', encoding='utf-8') as f:
    wheat_svg = f.read()

# Replace hardcoded colors with gold #c9a961
leaf_svg = re.sub(r'fill="[^"]+"', 'fill="#c9a961"', leaf_svg)
# In leaf.svg, let's also ensure there's an opacity to make it a subtle watermark
leaf_svg = leaf_svg.replace('<svg ', '<svg opacity="0.08" ')

wheat_svg = re.sub(r'style="fill:[^;]+;"', 'style="fill:#c9a961;"', wheat_svg)
wheat_svg = wheat_svg.replace('<svg ', '<svg opacity="0.08" ')

# Base64 encode
leaf_b64 = base64.b64encode(leaf_svg.encode('utf-8')).decode('utf-8')
wheat_b64 = base64.b64encode(wheat_svg.encode('utf-8')).decode('utf-8')

# Update CSS
file_path = 'rafed_site/static/css/style.css'
with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Find the background-image rule in body, .bg-light
# It looks like: background-image: \n url("..."),\n url("..."),\n url("...") !important;
pattern = r'(background-image:\s*\n\s*url\("data:image/svg\+xml;base64,[^"]+"\),\s*\n\s*url\("data:image/svg\+xml;base64,)([^"]+)("\),\s*\n\s*url\("data:image/svg\+xml;base64,)([^"]+)("\) !important;)'

match = re.search(pattern, css)
if match:
    new_bg = match.group(1) + leaf_b64 + match.group(3) + wheat_b64 + match.group(5)
    css = css[:match.start()] + new_bg + css[match.end():]
    
    # We should also adjust the background-size. The leaf is big, wheat is smaller.
    # Currently: background-size: 80px 80px, 400px 400px, 400px 400px !important;
    css = re.sub(r'background-size: 80px 80px, 400px 400px, 400px 400px !important;', 'background-size: 80px 80px, 800px 800px, 400px 400px !important;', css)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Replaced SVGs.")
else:
    print("Could not find background pattern.")

# Update base.html cache
with open('rafed_site/templates/base.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('css/style.css?v=2.7', 'css/style.css?v=2.8')
with open('rafed_site/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(html)
