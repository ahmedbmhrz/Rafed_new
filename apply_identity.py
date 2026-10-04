import re

file_path = 'rafed_site/static/css/style.css'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Define the new identity variables
root_css = """
:root {
  --forest: #0c3b2e;
  --forest-2: #155845;
  --forest-3: #051d15;
  --forest-pale: #1f6d57;
  --ds-gold: #c9a961;
  --ds-gold-2: #b8954b;
  --gold-pale: #efe5cb;
  --gold-deep: #876530;
  --paper: #fffdf7;
  --bg: #fffef9;
  --bg-2: #faf6ee;
  --ink: #14110a;
  --ink-2: #3d3830;
  --ink-3: #6e685c;
  --font-display: "Reem Kufi", "Tajawal", sans-serif;
  --font-sans: "Outfit", "Tajawal", ui-sans-serif, system-ui;
  --font-mono: "JetBrains Mono", "Courier New", monospace;
  
  --primary: #c9a961;
  --secondary: #0c3b2e;
  --light: #fffdf7;
  --dark: #051d15;
}
"""

# Replace all occurrences of old colors with CSS variables or new hexes
# Old gold: #B98F3E or #b98f3e
c = re.sub(r'#B98F3E', 'var(--ds-gold)', c, flags=re.IGNORECASE)
c = re.sub(r'rgba\(185,\s*143,\s*62,', 'rgba(201, 169, 97,', c) # rgb for #c9a961

# Old green: #28623F or #28623f (sometimes in rgb(40, 98, 63))
c = re.sub(r'#28623F', 'var(--forest)', c, flags=re.IGNORECASE)
c = re.sub(r'rgba\(40,\s*98,\s*63,', 'rgba(12, 59, 46,', c) # rgb for #0c3b2e

# Old cream: #FCFBF9 -> var(--bg) #fffef9
c = re.sub(r'#FCFBF9', '#fffef9', c, flags=re.IGNORECASE)

# Old Fonts -> New Fonts
c = re.sub(r"font-family: 'Tajawal', sans-serif !important;", "font-family: var(--font-sans) !important; color: var(--ink) !important;", c)
c = re.sub(r"font-family: 'Cairo', sans-serif !important;", "font-family: var(--font-display) !important; color: var(--forest) !important;", c)

# Ensure text-primary is readable (using gold-deep)
c = c + """
.text-primary { color: var(--gold-deep) !important; }
.bg-primary { background-color: var(--ds-gold) !important; }
.btn-primary { background-color: var(--forest) !important; border-color: var(--forest) !important; color: var(--paper) !important; border-radius: 8px !important; }
.btn-primary:hover { background-color: var(--forest-2) !important; border-color: var(--forest-2) !important; color: var(--paper) !important; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(12, 59, 46, 0.3) !important; }
.top-bar { border-bottom: 2px solid var(--ds-gold) !important; }
"""

# Fix SVG base64 encoding colors
# We have to decode, replace %23B98F3E with %23c9a961, and re-encode.
import base64
def update_base64_svgs(match):
    b64 = match.group(1)
    svg = base64.b64decode(b64).decode('utf-8')
    svg = svg.replace('#B98F3E', '#c9a961')
    new_b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
    return f'url("data:image/svg+xml;base64,{new_b64}")'

c = re.sub(r'url\("data:image/svg\+xml;base64,([^"]+)"\)', update_base64_svgs, c)

# Insert root variables at top
c = root_css + c

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)

# Update base.html cache
with open('rafed_site/templates/base.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('css/style.css?v=2.5', 'css/style.css?v=2.6')
with open('rafed_site/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(html)
