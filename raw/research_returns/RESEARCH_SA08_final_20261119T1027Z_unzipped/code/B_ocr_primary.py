"""OCR a specified page range solely for locating primary-source passages."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import argparse, subprocess, time, json

parser=argparse.ArgumentParser()
parser.add_argument('stem')
parser.add_argument('first',type=int)
parser.add_argument('last',type=int)
args=parser.parse_args()
base=Path(__file__).resolve().parents[1]
pdf=base/'sources'/(args.stem+'.pdf')
prefix=base/'notes'/'B_scan_images'/(args.stem+'_ocr')
started=time.monotonic()
subprocess.run(['pdftoppm','-f',str(args.first),'-l',str(args.last),'-r','120','-png',str(pdf),str(prefix)],check=True)

def one(page):
    candidates=list(prefix.parent.glob(prefix.name+f'-*{page}.png'))
    candidates=[p for p in candidates if int(p.stem.rsplit('-',1)[1])==page]
    assert len(candidates)==1,(page,candidates)
    result=subprocess.run(['tesseract',str(candidates[0]),'stdout','--psm','3'],check=True,capture_output=True,text=True)
    return f'\n===== PDF PAGE {page} =====\n'+result.stdout

with ThreadPoolExecutor(max_workers=4) as executor:
    output=''.join(executor.map(one,range(args.first,args.last+1)))
dest=base/'sources'/f'{args.stem}_ocr_{args.first}_{args.last}.txt'
dest.write_text(output)
receipt=dict(pdf=str(pdf),first=args.first,last=args.last,output=str(dest),seconds=time.monotonic()-started)
(base/'logs'/f'{args.stem}_ocr_{args.first}_{args.last}.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt))
