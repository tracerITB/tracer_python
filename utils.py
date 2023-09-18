import os
import base64
from bs4 import BeautifulSoup

def replace_image():
    html_dir = 'cache'
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    with open('navbar.html') as file:
        original_html = file.read()
    soup = BeautifulSoup(original_html, 'html.parser')
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_src = img_tag['src']
        with open(img_src, 'rb') as image_file:
            base64_data = base64.b64encode(image_file.read()).decode('utf-8')
        img_tag['src'] = f'data:image/jpeg;base64,{base64_data}'
    with open(html_dir + '/navbar.html', 'w') as cache_file:
        cache_file.write(str(soup))
    print("HTML file has been modified and saved to " + html_dir + "/navbar.html.")