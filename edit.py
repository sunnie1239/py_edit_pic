from PIL import Image

image_file = Image.open('FLOWERS.jpg')
image_file = image_file.convert('L') # 轉為灰階
image_file.save('result.png')