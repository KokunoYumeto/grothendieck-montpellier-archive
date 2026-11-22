from pathlib import Path
import ast,hashlib,json
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source=root/'code/geometry_final_package.py';data=source.read_bytes();text=data.decode()
tree=ast.parse(text)
wanted={'omission_record','omitted_cache_inventory','current_inventory','verify_source_snapshot','create_final'}
functions=[]
for node in tree.body:
 if isinstance(node,ast.FunctionDef) and node.name in wanted:
  body=ast.get_source_segment(text,node)
  functions.append({'name':node.name,'first_line':node.lineno,'last_line':node.end_lineno,'sha256':hashlib.sha256(body.encode()).hexdigest()})
print(json.dumps({'source':str(source),'sha256':hashlib.sha256(data).hexdigest(),'review_kind':'read-only targeted code review; no package-plan or archive-creation execution','functions':functions},indent=2))
