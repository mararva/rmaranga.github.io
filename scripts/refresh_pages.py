"""Refresh edited pages within existing Quarto shells when Quarto is unavailable.

Preserves project listings, page paths, navigation, and bundled theme assets.
Use `quarto render` for a full site build when Quarto is installed.
"""
from pathlib import Path
import subprocess, re, json
from html import escape
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,data):self.parts.append(data)
def plain(s):
 p=Text();p.feed(s);return ' '.join(' '.join(p.parts).split())
def render(path):
 s=subprocess.check_output(['pandoc',str(ROOT/path),'-f','markdown','-t','html5'],text=True)
 return s.replace('.qmd"', '.html"').replace('.qmd#', '.html#')
updated={}
for name in ['index','about','resume']:
 source=(ROOT/(name+'.qmd')).read_text()
 title=re.search(r'^title: "([^"]+)"',source,re.M).group(1)
 desc=re.search(r'^description: "([^"]+)"',source,re.M).group(1)
 p=ROOT/'docs'/f'{name}.html';s=p.read_text()
 body=render(name+'.qmd')
 header='<header id="title-block-header" class="quarto-title-block default"><div class="quarto-title"><h1 class="title">'+escape(title)+'</h1></div></header>\n'
 s=re.sub(r'(<main\b[^>]*>).*?(</main>)',lambda m:m[1]+header+body+m[2],s,flags=re.S)
 s=re.sub(r'<title>.*?</title>','<title>'+escape(title)+' – Ryan Marangattu</title>',s)
 s=re.sub(r'<meta name="description"[^>]*>\s*','',s)
 s=s.replace('</head>','<meta name="description" content="'+escape(desc,quote=True)+'">\n</head>')
 p.write_text(s);updated[name]=(title,plain(body))
p=ROOT/'docs/posts/colonelblotto/colonelblotto.html';s=p.read_text()
if 'https://github.com/mararva/colonelblottogame' not in s:
 s=s.replace('</main>','<p><a href="https://github.com/mararva/colonelblottogame">Source code on GitHub</a></p>\n</main>');p.write_text(s)
intro='Selected work in statistical computing, visualization, and interactive applications. The original project links and dates are retained.'
p=ROOT/'docs/projects.html';s=p.read_text()
if intro not in s:s=re.sub(r'(<main\b[^>]*>)',lambda m:m[1]+'\n<p>'+intro+'</p>',s,count=1);p.write_text(s)
for p in (ROOT/'docs').rglob('*.html'):
 s=p.read_text();s=re.sub(r'(href="(?:\./|\.\./)*?)resume\.pdf("[^>]*>\s*(?:<[^>]+>\s*)*Resume\b)',r'\1resume.html\2',s)
 s=re.sub(r'(<a class="nav-link" href="[^"]*resume.html">) +',r'\1',s)
 p.write_text(s)
(ROOT/'docs/styles.css').write_bytes((ROOT/'styles.css').read_bytes())
p=ROOT/'docs/search.json';entries=json.loads(p.read_text())
for e in entries:
 name=e['href'].split('.')[0]
 if name in updated:e['title'],e['text']=updated[name]
p.write_text(json.dumps(entries,indent=2,ensure_ascii=False)+'\n')
