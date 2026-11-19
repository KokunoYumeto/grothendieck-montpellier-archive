from pathlib import Path
p=Path('/workspace/scratch/7feb9690b71f/SA08_work/programs/late_build_items.py')
lines=[]
for line in p.read_text().splitlines():
 s=line.strip()
 if s.startswith("'") and (s.endswith("',") or s.endswith("')")):
  suffix=s[-1]
  value=s[1:-2].replace("\\'", "'")
  line=line[:len(line)-len(line.lstrip())]+repr(value)+suffix
 lines.append(line)
p.write_text('\n'.join(lines)+'\n')
print('Normalized authored prose string literals; no content adjudication changed.')
