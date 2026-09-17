"""Validate the built corporate site using Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote, urljoin
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'hugo/public')

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.assets = []
        self.h1s = 0
        self.alternates = {}
        self.canonical = None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1': self.h1s += 1
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.assets.append(a['src'])
        if tag == 'link':
            if a.get('rel') == 'canonical': self.canonical = a['href']
            if a.get('hreflang'): self.alternates[a['hreflang']] = a['href']
            if a.get('rel') == 'stylesheet': self.assets.append(a['href'])

routes = ['', '360/', 'media/', 'business/', 'contact/', 'thanks/']
for lang in ['', 'es/']:
    for route in routes:
        path = lang + route
        file = root / path / 'index.html'
        assert file.exists(), f'Missing page: {path}'
        text = file.read_text()
        page = Page(text)
        assert page.h1s == 1, f'{path}: expected one h1, got {page.h1s}'
        assert 'en-US' in page.alternates and 'es-PR' in page.alternates, f'{path}: missing language alternates'
        assert urlparse(page.alternates['en-US']).path == '/' + route
        assert urlparse(page.alternates['es-PR']).path == '/es/' + route
        assert page.canonical == 'https://glezper.com/' + path, f'{path}: wrong canonical'
        assert 'Powered by Publii' not in text and 'BIU' not in text
        assert 'data:image' not in text
        assert '787-377-9522' not in text and '17873779522' not in text, f'{path}: private phone exposed'
        assert '↗' not in text and '→' not in text and '➡' not in text, f'{path}: text arrow instead of SVG'
        for link in page.links + page.assets:
            u = urlparse(urljoin('https://glezper.com/' + path, link))
            if u.scheme not in ('http', 'https') or u.netloc != 'glezper.com': continue
            local = root / unquote(u.path).lstrip('/')
            assert local.is_file() or (local / 'index.html').is_file(), f'{path}: broken local link {link}'
        print(f'PASS /{path}: canonical, paired translation, assets, links, one heading')

for legacy in ['glezper-360deg.html', 'glezper-media.html', 'glezper-business.html', 'hecho-para-quienes-hacen-negocios.html']:
    assert (root / legacy).is_file(), f'Missing legacy alias: {legacy}'
assert (root / 'CNAME').read_text().strip() == 'glezper.com'
for lang in ['', 'es/']:
    text = (root / lang / 'business/index.html').read_text()
    assert 'data-delivery-enabled=false' in text or 'data-delivery-enabled="false"' in text
    assert 'action=#business-inquiry' in text or 'action="#business-inquiry"' in text
    assert '001QP00001dUhWtYAK' not in text, 'Inquiry must not go directly to a provider'
    for field in ['interest_financing', 'interest_pos', 'interest_automation', 'monthly_revenue', 'pos_goal', 'automation_process', 'contact_consent', '_honey']:
        assert f'name={field}' in text or f'name="{field}"' in text, f'Missing field {field}'
    assert 'https://glezper.com/' + lang + 'thanks/' in text
    assert '_captcha' not in text, 'Keep provider CAPTCHA enabled'
for file in root.glob('**/*.json'):
    assert '787-377-9522' not in file.read_text(), f'Private phone in {file}'
print('PASS legacy aliases, privacy, provider-neutral intake and email form configuration')
