from PIL import Image
import os
def convert(name):
    img = Image.open('origin/' + name).convert('RGB')
    hei, wid = img.size
    max_size = 400
    if max(hei, wid) <= max_size:
        pass
    else:
        img.thumbnail((max_size, max_size))
    img.save('midsize/' + name.split('.')[0] + '_md.jpg')
for i, j, k in os.walk('origin'):
    for l in k:
        try:
            convert(l)
        except:
            print('convert failed: ' + l)