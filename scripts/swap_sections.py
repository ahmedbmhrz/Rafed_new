import re

file_path = 'rafed_site/home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Achievements block
achievements_pattern = r'(    <!-- Achievements Start -->.*?<!-- Achievements End -->\n)'
achievements_match = re.search(achievements_pattern, content, re.DOTALL)

# Extract About block
about_pattern = r'(    <!-- About Start -->.*?<!-- About End -->\n)'
about_match = re.search(about_pattern, content, re.DOTALL)

if achievements_match and about_match:
    achievements_html = achievements_match.group(1)
    about_html = about_match.group(1)
    
    # Replace the combined occurrence
    # They should be adjacent: Achievements then About
    combined_pattern = achievements_pattern + about_pattern
    new_combined = about_html + achievements_html
    
    content = re.sub(combined_pattern, new_combined, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully swapped Achievements and About sections.")
else:
    print("Could not find one or both sections.")
