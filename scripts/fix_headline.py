import re
file_path = 'home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the pill div
old_pill = r'<div style=.display:flex;align-items:center;gap:16px;margin-bottom:20px;justify-content:center;.*?>\s*<div style=.display:inline-flex;align-items:center;gap:12px;border-radius:9999px;background:var\(--ds-gold\);padding:6px 18px 6px 6px;flex-shrink:0.>\s*<span style=.width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba\(255,255,255,\.22\);color:var\(--forest-3\);font-size:14px;flex-shrink:0.>◉</span>\s*<span style=.font-family:var\(--font-display\);font-weight:700;font-size:13px;color:var\(--forest-3\).>الأخبار</span>\s*</div>\s*</div>'

new_eyebrow = r'<p class="text-primary text-uppercase mb-2 eyebrow" style="font-size: 16px; font-weight: 700; letter-spacing: 2px; color: var(--gold-deep) !important;">الأخبار</p>'

content = re.sub(old_pill, new_eyebrow, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
