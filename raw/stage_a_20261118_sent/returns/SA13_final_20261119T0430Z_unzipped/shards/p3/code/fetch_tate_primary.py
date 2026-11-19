from pathlib import Path
import urllib.request,subprocess
out=Path('work/p3_primary');out.mkdir(exist_ok=True)
for name,url in [('moretbailly1985','https://www.numdam.org/item/AST_1985__129__1_0.pdf'),('zarhin2011geometric','https://arxiv.org/pdf/1012.5083')]:
    data=urllib.request.urlopen(url,timeout=50).read();p=out/(name+'.pdf');p.write_bytes(data)
    subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
    print(name,len(data),url)
