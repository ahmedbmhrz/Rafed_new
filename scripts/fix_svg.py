import base64
import re

svg1 = "<svg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'><g fill='#B98F3E' fill-opacity='0.04'><path d='M40 0l-7.5 15-15-7.5 7.5 15H15v15l-15-7.5 7.5 15-7.5 15 15-7.5v15h15l-7.5 15 15-7.5 7.5 15 7.5-15 15 7.5-7.5-15h15V40l15 7.5-7.5-15 7.5-15-15 7.5V15H55l7.5-15-15 7.5L40 0zm-15 25l15 7.5L55 25l-7.5 15 7.5 15-15-7.5L25 55l7.5-15L25 25z'/></g></svg>"
svg2 = "<svg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'><g fill='none' stroke='#B98F3E' stroke-width='4' stroke-linecap='round' opacity='0.08'><path d='M50 100 L50 20 M50 90 Q 70 70 50 50 M50 90 Q 30 70 50 50 M50 70 Q 70 50 50 30 M50 70 Q 30 50 50 30 M50 50 Q 70 30 50 10 M50 50 Q 30 30 50 10 M50 30 Q 60 10 50 0 M50 30 Q 40 10 50 0'/></g></svg>"

b64_1 = base64.b64encode(svg1.encode('utf-8')).decode('utf-8')
b64_2 = base64.b64encode(svg2.encode('utf-8')).decode('utf-8')

new_rule = f"""body, .bg-light {{ 
    background-color: #FCFBF9 !important; 
    background-image: 
        url("data:image/svg+xml;base64,{b64_1}"),
        url("data:image/svg+xml;base64,{b64_2}"),
        url("data:image/svg+xml;base64,{b64_2}") !important;
    background-size: 80px 80px, 400px 400px, 400px 400px !important;
    background-position: center, -100px bottom, calc(100% + 100px) 150px !important;
    background-repeat: repeat, no-repeat, no-repeat !important;
    background-attachment: scroll, fixed, fixed !important;
}}"""

file_path = 'rafed_site/static/css/style.css'
with open(file_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the broken rule
c = re.sub(r'body, \.bg-light \{ \n    background-color: #FCFBF9 !important;.*?background-attachment: scroll, fixed, fixed !important;\n\}', new_rule, c, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(c)

# Update base.html
with open('rafed_site/templates/base.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('css/style.css?v=2.1', 'css/style.css?v=2.2')
with open('rafed_site/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(html)
