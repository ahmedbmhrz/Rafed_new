import re

def fix_colors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Original orange-gold
    content = re.sub(r'#EAA636', '#c9a961', content, flags=re.IGNORECASE)
    content = re.sub(r'234,\s*166,\s*54', '201, 169, 97', content)
    
    # Original green
    content = re.sub(r'#32C36C', '#0c3b2e', content, flags=re.IGNORECASE)
    content = re.sub(r'50,\s*195,\s*108', '12, 59, 46', content)

    # Some old text-primary could still have the #c9a961 which fails contrast, but we'll let our style.css !important handle it

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_colors('rafed_site/static/css/bootstrap.min.css')
fix_colors('rafed_site/static/css/style.css')

# Update cache buster
with open('rafed_site/templates/base.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('css/bootstrap.min.css', 'css/bootstrap.min.css?v=2.9')
html = html.replace('css/style.css?v=2.9', 'css/style.css?v=3.0')
with open('rafed_site/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Colors forcefully eradicated.")
