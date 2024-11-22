'''
移除图片背景
'''
from rembg import remove
from PIL import Image

img_path = 'data/1.jpeg'
out_path = 'data/1.png'
inp = Image.open(img_path)
out = remove(inp)
out.save(out_path)
Image.open(out_path)