from pathlib import Path
from pypdf import PdfReader
import subprocess,json,hashlib
root=Path('reference/lecture-notes'); inventory=[]; links=[]
for n in (7,8,9):
 src=Path(f'reference/Lecture-{n:02}.pdf'); reader=PdfReader(src)
 raw=subprocess.check_output(['pdftotext','-layout',str(src),'-'],stderr=subprocess.DEVNULL).decode().split('\f')
 md=[f'# Lecture {n:02}: page-by-page source extraction\n',f'Source: [original PDF](../Lecture-{n:02}.pdf). Mechanical text extraction; equations and image-only text may be incomplete. Page previews are authoritative for layout. See the edited lecture notes for corrected formulas.\n']
 for i,p in enumerate(reader.pages,1):
  md += [f'## Page {i}\n',f'[Slide preview](pages/L{n:02}-{i:02}.jpg)\n','```text\n'+raw[i-1].strip()+'\n```\n']
  page_links=[]
  for a in p.get('/Annots',[]):
   obj=a.get_object(); act=obj.get('/A',{}); url=act.get('/URI')
   if url:
    links.append({'lecture':n,'page':i,'url':str(url)});page_links.append(str(url))
  if page_links: md+=['Embedded links:\n']+['- '+u+'\n' for u in dict.fromkeys(page_links)]
  for j,im in enumerate(p.images):
   name=f'L{n:02}-p{i:02}-{j:02}-{im.name}'; path=root/'embedded'/name;path.write_bytes(im.data)
   inventory.append({'lecture':n,'page':i,'file':str(path.relative_to(root)),'sha256':hashlib.sha256(im.data).hexdigest(),'status':'embedded slide image; upstream attribution not yet matched'})
 (root/f'Lecture-{n:02}-transcript.md').write_text('\n'.join(md))
(root/'embedded-images.json').write_text(json.dumps(inventory,indent=2))
(root/'slide-links.json').write_text(json.dumps(links,indent=2))
print(json.dumps(links,indent=2));print('Images:',len(inventory))
