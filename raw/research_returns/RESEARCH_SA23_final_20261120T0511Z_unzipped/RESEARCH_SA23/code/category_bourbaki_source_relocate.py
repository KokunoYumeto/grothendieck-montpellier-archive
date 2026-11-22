from pathlib import Path
import hashlib,json
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
rows=[]
for source_name,target_name in [('notes/category_bourbaki_nbr082.pdf','sources/category_bourbaki_nbr082.pdf'),('notes/category_bourbaki_nbr082_payload.download','sources/category_bourbaki_nbr082_payload.download')]:
 source=root/source_name;target=root/target_name
 if target.exists(): raise FileExistsError(target)
 fingerprint=hashlib.sha256(source.read_bytes()).hexdigest();size=source.stat().st_size
 source.rename(target)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==fingerprint
 rows.append({'old_path':source_name,'new_path':target_name,'sha256':fingerprint,'bytes':size,'reason':'Parent requested retrievable primary PDF in sources cache; exact bytes preserved'})
(root/'notes/category_bourbaki_source_relocations.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
