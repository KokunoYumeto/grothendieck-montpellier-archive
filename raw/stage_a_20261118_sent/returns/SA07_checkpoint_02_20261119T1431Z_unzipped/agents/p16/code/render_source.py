"""Render selected primary-source PDF pages for formula inspection."""
import subprocess,pathlib,sys
key,first,last=sys.argv[1:];D=pathlib.Path(__file__).parents[1]/'evidence'
cmd=['pdftoppm','-f',first,'-l',last,'-r','115','-png',str(D/(key+'.pdf')),str(D/(key+'-page'))]
print('Command:',cmd)
p=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
print(p.stdout,p.stderr,'exit',p.returncode)
for f in sorted(D.glob(key+'-page-*.png')):print(f.name,f.stat().st_size)
