"""OCR selected pages of a primary reference, only to navigate and read it.
No manuscript ink is interpreted by this program. Files remain outside the dossier.
"""
import pathlib,subprocess,sys
pdf=pathlib.Path(sys.argv[1]); first,last=map(int,sys.argv[2:4])
target=pdf.parent/(pdf.stem+'_ocr');target.mkdir(exist_ok=True)
out=[]
for page in range(first,last+1):
    prefix=target/f'p{page}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2200','-png',str(pdf),str(prefix)],check=True)
    subprocess.run(['tesseract',str(prefix)+'.png',str(prefix),'-l','eng'],check=True,stderr=subprocess.DEVNULL)
    out+=['\nPDF_PAGE '+str(page)+'\n'+prefix.with_suffix('.txt').read_text()]
alltext=target/'selected.txt';alltext.write_text('\n'.join(out))
print('OCR text:',alltext,'pages',first,last)
