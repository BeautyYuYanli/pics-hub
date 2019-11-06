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
# main
with open('datebase.qwq', 'r') as f:
    datebase = f.read().split(';')
if datebase[-1] == '':
    datebase.pop()
for i, j, k in os.walk('origin'):
    for l in k:
        if l.split('.')[0] in datebase:
            continue
        try:
            convert(l)
            datebase.append(l.split('.')[0])
            print(l)
        except:
            print('convert failed: ' + l)
with open('datebase.qwq', 'w') as f:
    for i in datebase:
        f.write(i + ';')