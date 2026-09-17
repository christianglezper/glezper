"""Reproducibly import the three English service pages from the backed-up export.

Mechanical content conversion only. Does not change the source HTML files.
"""
from html.parser import HTMLParser
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

class ContentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.parts = []
        self.href = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'div':
            if self.depth:
                self.depth += 1
            elif 'content__entry' in attrs.get('class', '').split():
                self.depth = 1
            return
        if not self.depth:
            return
        if tag in ('h1', 'h2', 'h3'):
            self.parts.append('\n\n' + ('## ' if tag in ('h1', 'h2') else '### '))
        elif tag == 'p':
            self.parts.append('\n\n')
        elif tag == 'strong':
            self.parts.append('**')
        elif tag == 'br':
            self.parts.append('  \n')
        elif tag == 'a' and attrs.get('href'):
            self.href = attrs['href']
            self.parts.append('[')

    def handle_endtag(self, tag):
        if tag == 'div' and self.depth:
            self.depth -= 1
            return
        if not self.depth:
            return
        if tag == 'strong':
            self.parts.append('**')
        elif tag == 'a' and self.href:
            self.parts.append('](' + self.href + ')')
            self.href = None

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

pages = [
    ('glezper-360deg.html', '360', 'Glezper 360°', 'Strategic communications, public relations, brand messaging, digital presence and Media Budget Allocation.'),
    ('glezper-media.html', 'media', 'Glezper Media', 'Editorial brands, advertising and brand partnerships for distinct Puerto Rican audiences.'),
    ('glezper-business.html', 'business', 'Glezper Business', 'Business solutions, commercial strategy and access to capital for qualifying businesses.'),
]

for source, slug, title, description in pages:
    parser = ContentParser()
    parser.feed((ROOT / source).read_text())
    body = ''.join(parser.parts).strip()
    body = body.replace('**christianglezper@gmail.com**', '**[christianglezper@gmail.com](mailto:christianglezper@gmail.com)**')
    body = body.replace('**787-377-9522**', '**[787-377-9522](tel:+17873779522)**')
    front = f'---\ntitle: {json.dumps(title, ensure_ascii=False)}\ndescription: {json.dumps(description)}\ntranslationKey: {slug}\naliases: ["/{source}"]\n---\n\n'
    target = ROOT / 'hugo/content/en' / (slug + '.md')
    target.write_text(front + body + '\n')
    print(target.relative_to(ROOT))
