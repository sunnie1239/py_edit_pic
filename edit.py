from PIL import Image
import os

for pic in os.listdir('.'):
    if pic.endswith('.jpg'):
        image_file = Image.open(pic)
        image_file = image_file.convert('L') # 轉為灰階
        image_file.save('res_'+ pic) 