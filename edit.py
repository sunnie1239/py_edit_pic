from PIL import Image
import os

for pic in os.listdir('original'):
    if pic.endswith('.jpg'):
        image_file = Image.open(os.path.join('original', pic))
        image_file = image_file.convert('L') # 轉為灰階
        image_file.save(os.path.join('result', pic[:-4] + '_res.jpg'))