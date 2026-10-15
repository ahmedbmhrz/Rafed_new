import re

html_path = 'home/templates/home/home_page.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Modify Educational Content Background and Text Colors
edu_pattern = r'(<!-- Educational Content Start -->.*?<!-- Educational Content End -->)'
match = re.search(edu_pattern, html, flags=re.DOTALL)
if match:
    edu_html = match.group(1)
    
    # Change section background
    edu_html = edu_html.replace('<div class="container-xxl py-6 bg-light" style="position: relative; z-index: 10;">',
                                '<div class="container-xxl py-6" style="background-color: var(--forest); position: relative; z-index: 10; border-top: 4px solid var(--ds-gold); border-bottom: 4px solid var(--ds-gold);">')
    
    # Change Title to White
    edu_html = edu_html.replace('<h2 class="display-6 mb-4" style="color: var(--forest);">تصاميم تثقيفية عن الأوقاف</h2>',
                                '<h2 class="display-6 mb-4" style="color: #ffffff;">تصاميم تثقيفية عن الأوقاف</h2>')
    
    # Change Button to Gold
    edu_html = edu_html.replace('style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;"',
                                'style="background-color: var(--ds-gold) !important; border-color: var(--ds-gold) !important; color: white !important; font-weight: bold;"')
    
    html = html[:match.start()] + edu_html + html[match.end():]

# 2. Modify Video Album to floating/borderless style
vid_pattern = r'(<!-- Video Album Start -->.*?<!-- Video Album End -->)'
match = re.search(vid_pattern, html, flags=re.DOTALL)
if match:
    vid_html = match.group(1)
    
    # Replace the card wrapper with a borderless wrapper
    vid_html = vid_html.replace('<div class="content-item bg-white rounded shadow-sm" style="border: 1px solid rgba(0,0,0,0.05); overflow: hidden; height: 100%;">',
                                '<div class="video-item text-center" style="height: 100%;">')
    
    # Modify the image container to have rounded corners and shadow, and margin bottom
    vid_html = vid_html.replace('<div style="position: relative; cursor: pointer;">',
                                '<div style="position: relative; cursor: pointer; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.15); margin-bottom: 20px;" class="vid-thumb-container">')
    
    # Modify the bottom text container
    vid_html = vid_html.replace('<div class="p-4 text-center">', '<div class="text-center px-2">')
    
    # Change the Button to Outline style to look different
    vid_html = vid_html.replace('style="background-color: var(--forest) !important; border-color: var(--forest) !important; color: white !important;"',
                                'style="background-color: transparent !important; border: 2px solid var(--forest) !important; color: var(--forest) !important; font-weight: bold;"')
    vid_html = vid_html.replace('class="btn btn-primary rounded py-3 px-5"', 'class="btn rounded py-3 px-5 video-btn-hover"')
    
    html = html[:match.start()] + vid_html + html[match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
