"""Build the PDF from resume.qmd; requires pandoc and reportlab."""
from pathlib import Path
import json, subprocess
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('PortfolioSans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PortfolioSans-Bold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('PortfolioSans',normal='PortfolioSans',bold='PortfolioSans-Bold',italic='PortfolioSans',boldItalic='PortfolioSans-Bold')
ROOT = Path(__file__).resolve().parents[1]
ast = json.loads(subprocess.check_output(['pandoc', str(ROOT/'resume.qmd'), '-f', 'markdown', '-t', 'json']))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle('Name', fontName='PortfolioSans-Bold', fontSize=20, leading=23, textColor=HexColor('#263746'), spaceAfter=5))
styles.add(ParagraphStyle('Section',fontName='PortfolioSans-Bold',fontSize=11,leading=13,spaceBefore=9,spaceAfter=4,keepWithNext=True,textColor=HexColor('#263746')))
styles.add(ParagraphStyle('Role',fontName='PortfolioSans-Bold',fontSize=9.4,leading=11.5,spaceBefore=5,spaceAfter=3,keepWithNext=True))
styles.add(ParagraphStyle('Copy',fontName='PortfolioSans',fontSize=9,leading=11.8,spaceAfter=4))
styles.add(ParagraphStyle('Item',parent=styles['Copy'],leftIndent=10,firstLineIndent=-7,spaceAfter=2))
def inline(xs):
 out=''
 for x in xs:
  t=x['t']; c=x.get('c')
  if t=='Str': out+=escape(c)
  elif t in ('Space','SoftBreak','LineBreak'):out+=' '
  elif t=='Strong':out+='<b>'+inline(c)+'</b>'
  elif t=='Emph':out+='<i>'+inline(c)+'</i>'
  elif t=='Link':
   label=inline(c[1]);url=c[2][0]
   if url.endswith('.qmd'):url=url[:-4]+'.html'
   if not url.startswith('http'):url='https://ryan.marangatwo.com/'+url
   out+='<a color="#923c17" href="'+escape(url,quote=True)+'">'+label+'</a>'
 return out
story=[Paragraph('Ryan Marangattu',styles['Name']),Paragraph('Los Angeles, CA | ryanmarangattu@gmail.com | <a href="https://github.com/mararva">github.com/mararva</a> | <a href="https://ryan.marangatwo.com">ryan.marangatwo.com</a>',styles['Copy'])]
for b in ast['blocks']:
 if b['t']=='Header':
  level,_,text=b['c'];story.append(Paragraph(inline(text), styles['Section' if level==2 else 'Role']))
 elif b['t']=='Para':
  text=inline(b['c'])
  if 'Download resume' in text or 'View all projects' in text:continue
  story.append(Paragraph(text,styles['Copy']))
 elif b['t']=='BulletList':
  for item in b['c']:
   for p in item:
    story.append(Paragraph('&#8226; '+inline(p['c']),styles['Item']))
def footer(canvas,doc):
 canvas.setTitle('Ryan Marangattu - Analytics and Research Resume')
 canvas.setAuthor('Ryan Marangattu')
 canvas.setFont('PortfolioSans',8);canvas.setFillColor(HexColor('#53606b'))
 canvas.drawRightString(576,24,str(doc.page))
SimpleDocTemplate(str(ROOT/'resume.pdf'),pagesize=(612,792),rightMargin=36,leftMargin=36,topMargin=30,bottomMargin=34).build(story,onFirstPage=footer,onLaterPages=footer)
(ROOT/'docs/resume.pdf').write_bytes((ROOT/'resume.pdf').read_bytes())
