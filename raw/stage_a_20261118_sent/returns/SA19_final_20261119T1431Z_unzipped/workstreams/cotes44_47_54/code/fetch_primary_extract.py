"""Fetch a primary PDF rejected by web parser for size; retain selected text only."""
from pathlib import Path
import urllib.request,subprocess,sys,hashlib,re,json
root=Path(__file__).resolve().parents[1]
label,url,patterns=sys.argv[1:4]
pdf=root/'research'/f'{label}_temporary.pdf'
data=urllib.request.urlopen(url,timeout=90).read()
pdf.write_bytes(data)
text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True)
pdf.unlink()
lines=text.splitlines(); out=[]
for pat in patterns.split('|'):
    hits=[i for i,l in enumerate(lines) if re.search(pat,l,re.I)]
    out.append({'pattern':pat,'hits':len(hits),'contexts':[{'line':i+1,'text':'\n'.join(lines[max(0,i-4):i+32])} for i in hits[:20]]})
result={'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'retrieval':'HTTP 200 using urllib; complete PDF parsed with pdftotext; temporary original removed after extraction','patterns':out}
(root/'research'/f'{label}_extract.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
