"""Validate deployable paths, metadata, font cache inputs, and static reading content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json,re,struct
root=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.path=path;self.ids=[];self.links=[];self.meta={};self.canonical=None;self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag in ['script','img','link','a']:
   for k in ['src','href']:
    if k in a:self.links.append(a[k])
  if tag=='meta':self.meta[a.get('property',a.get('name'))]=a.get('content')
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='img':assert 'alt' in a,f'{self.path.name}: image without alt'
pages={p.name:Page(p) for p in root.glob('*.html')}
for name,page in pages.items():
 assert len(page.ids)==len(set(page.ids)),f'{name}: duplicate IDs'
 assert '<html lang="en"' in page.path.read_text(),f'{name}: missing language'
 assert page.canonical and page.canonical.startswith('https://pythonidaer.github.io/technical-writing/'),f'{name}: canonical'
 for key in ['description','og:title','og:description','og:url','og:image','og:image:alt','twitter:card','robots']:
  assert page.meta.get(key),f'{name}: missing {key}'
 assert page.meta['og:url']==page.canonical,f'{name}: canonical mismatch'
 image=root/page.meta['og:image'].rsplit('/',1)[1]
 data=image.read_bytes();assert data.startswith(b'\x89PNG\r\n\x1a\n')
 assert struct.unpack('>II',data[16:24])==(1200,630),'social image dimensions'
 for href in page.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  path=(page.path.parent/unquote(u.path)) if u.path else page.path
  assert path.exists(),f'{name}: missing {href}'
  if u.fragment and path.suffix=='.html' and not u.fragment.startswith('lesson-'):
   assert u.fragment in pages[path.name].ids,f'{name}: missing anchor {href}'
for sheet in root.glob('*.css'):
 for url in re.findall(r'url\([\'"]?([^\)\'\"]+)',sheet.read_text()):
  if not url.startswith(('https:', 'data:')):assert (sheet.parent/url).exists(),f'Missing CSS asset {url}'
fonts=list((root/'fonts').glob('*.woff2'));assert len(fonts)==4
for font in fonts:
 assert font.read_bytes()[:4]==b'wOF2',f'{font.name}: wrong font container'
 assert font.name in (root/'fonts.css').read_text()
 assert font.name in (root/'font-sw.js').read_text()
assert (root/'fonts/DM-Sans-OFL.txt').stat().st_size>1000
assert (root/'fonts/DM-Mono-OFL.txt').stat().st_size>1000
assert len(re.findall(r'<article id=',(root/'full-guide.html').read_text()))==10
assert len(re.findall(r'<li class="resource-item"',(root/'design-reading.html').read_text()))==50
json.loads((root/'site.webmanifest').read_text())
print(f'PASS: {len(pages)} HTML pages, local links and anchors, 4 WOFF2 faces, licenses, 1200×630 social cards, canonical/OG metadata, 10 static lessons, and 50 static resources.')
