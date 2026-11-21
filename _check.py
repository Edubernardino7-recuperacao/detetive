import re

for f in ['jogo.html', 'solucao.html']:
    html = open(f, encoding='utf-8').read()
    opens = len(re.findall(r'<div\b', html))
    closes = len(re.findall(r'</div>', html))
    pages = len(re.findall(r'class="page[" ]', html))
    print(f'{f}: open={opens} close={closes} delta={opens-closes} | .page divs={pages}')

    # per-page balance: walk through and track depth at each .page start
    depth = 0
    page_marks = []
    for m in re.finditer(r'<div\b|</div>', html):
        tag = m.group(0)
        if tag == '</div>':
            depth -= 1
        else:
            if 'class="page' in html[m.start():m.start()+40]:
                page_marks.append(depth)
            depth += 1
    print(f'   depth at each .page start: {page_marks}')
