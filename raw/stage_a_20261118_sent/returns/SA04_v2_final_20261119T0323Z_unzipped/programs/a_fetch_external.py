"""Retrieve already located primary documents for reading; do not package their text.

Usage: python a_fetch_external.py URL NAME [FIRST_PAGE LAST_PAGE]
Output is a /tmp path and factual retrieval/extraction metadata, not a theorem check.
External originals and extracted text stay outside the deliverable tree.
"""
import pathlib, subprocess, sys, urllib.request, hashlib
url,name=sys.argv[1:3]
target=pathlib.Path('/tmp/SA04_a_external');target.mkdir(exist_ok=True)
pdf=target/(name+'.pdf'); txt=target/(name+'.txt')
with urllib.request.urlopen(url,timeout=45) as r:
    data=r.read()
pdf.write_bytes(data)
cmd=['pdftotext','-layout']
if len(sys.argv)>3:cmd+=['-f',sys.argv[3],'-l',sys.argv[4]]
subprocess.run(cmd+[str(pdf),str(txt)],check=True)
print('URL',url)
print('PDF',pdf,'sha256',hashlib.sha256(data).hexdigest())
print('TEXT',txt,'bytes',txt.stat().st_size)
