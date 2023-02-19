import requests, lxml, re, urllib.parse, base64
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

img_tags = soup.find_all('img')

#    echo '<img src="data:image/jpeg;base64,'.base64_encode($row['imagem']).'"/>';
#img_matches = re.findall(r"s='data:image/jpeg;base64,(.*?)';", str(img_tags))

#print(len(img_tags))


for index, elemento in enumerate(img_tags):
    try:
        print(index)
        img_data = elemento['src']
        img_matches = img_data.replace("data:image/jpeg;base64,","")
        #print(img_matches)
        final_image = Image.open(BytesIO(base64.b64decode(str(img_matches))))
        final_image.save(f'./inline_image_{index}.jpg', 'JPEG')
    except:
        pass