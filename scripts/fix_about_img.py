# -*- coding: utf-8 -*-
file_path = 'home/templates/home/home_page.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken img-twice image paths
old_path_1 = "'rafed_site/static/img/rafed_image/background/6aa0f543b127d8.21470575.png.jpg'"
new_path_1 = "'img/rafed_image/background/4.jpg'"

old_path_2 = "'img/rafed_image/background/3687745542.jpg'"
new_path_2 = "'img/rafed_image/background/6aa0f543b127d8.21470575.png'"

html = html.replace(old_path_1, new_path_1)
html = html.replace(old_path_2, new_path_2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
