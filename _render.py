import pypdfium2 as pdfium
import os, re

os.makedirs('_pages', exist_ok=True)
for f in os.listdir('_pages'):
    os.remove(os.path.join('_pages', f))

for tag, f in [('jogo', 'Caso_Mansao_Blackwood_JOGO.pdf'), ('sol', 'Caso_Mansao_Blackwood_SOLUCAO.pdf')]:
    pdf = pdfium.PdfDocument(f)
    n = len(pdf)
    print(f'{f}: {n} pages')
    for i in range(n):
        page = pdf[i]
        img = page.render(scale=1.2).to_pil()
        img.save(f'_pages/{tag}_{i+1:02d}.png')
    pdf.close()
print('done')
