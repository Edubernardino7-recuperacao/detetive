from PIL import Image
import os

files = sorted(os.listdir('_pages'))
files = [f for f in files if f.startswith('jogo_')]
cols, rows = 6, 6
tw, th = 220, 311
sheet = Image.new('RGB', (cols * tw, rows * th), 'white')
for idx, f in enumerate(files):
    im = Image.open(os.path.join('_pages', f)).resize((tw, th))
    sheet.paste(im, ((idx % cols) * tw, (idx // cols) * th))
sheet.save('_pages/_sheet_jogo.png')
print('sheet', len(files))
