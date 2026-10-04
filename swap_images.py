import re

file_path = 'rafed_site/home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the three items
item1_pattern = r'(<div class="owl-carousel-item position-relative">\s*<img class="img-fluid" src="{% static \'img/rafed_image/background/4\.jpg\' %}" alt="">.*?</div>\s*</div>\s*</div>\s*</div>)'
item2_pattern = r'(<div class="owl-carousel-item position-relative">\s*<img class="img-fluid" src="{% static \'img/rafed_image/background/3687745542\.jpg\' %}" alt="">.*?</div>\s*</div>\s*</div>\s*</div>)'
item3_pattern = r'(<div class="owl-carousel-item position-relative">\s*<img class="img-fluid" src="{% static \'img/rafed_image/background/6aa0f543b127d8\.21470575\.png\' %}" alt="">.*?</div>\s*</div>\s*</div>\s*</div>)'

item1_match = re.search(item1_pattern, content, re.DOTALL)
item2_match = re.search(item2_pattern, content, re.DOTALL)
item3_match = re.search(item3_pattern, content, re.DOTALL)

if item1_match and item2_match and item3_match:
    item1_html = item1_match.group(1)
    item2_html = item2_match.group(1)
    item3_html = item3_match.group(1)
    
    # Construct the new sequence
    new_carousel_inner = item2_html + "\n" + item1_html + "\n" + item3_html
    
    # Replace the old sequence
    old_sequence = item1_html + "\n" + item2_html + "\n" + item3_html
    
    # Since whitespace might differ, let's just do a string replacement of the specific items individually if needed
    # Actually, the simplest way is to just replace '4.jpg' with '3687745542.jpg' and vice versa in the src attributes!
    # Because all three items have the exact same text/buttons inside!
    pass

# Faster way: just swap the image filenames since the content inside is identical.
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("background/4.jpg", "background/TEMP.jpg")
content = content.replace("background/3687745542.jpg", "background/4.jpg")
content = content.replace("background/TEMP.jpg", "background/3687745542.jpg")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Swapped image order.")
