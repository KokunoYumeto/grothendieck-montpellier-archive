from pathlib import Path
import hashlib
import ast
root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
for relative in ['code/geometry_final_package.py', 'code/checkpoint.py']:
    path = root / relative
    data = path.read_bytes()
    tree = ast.parse(data, filename=relative)
    print('REVIEWED', relative, 'BYTES', len(data), 'SHA256', hashlib.sha256(data).hexdigest())
    print('FUNCTIONS', [n.name for n in tree.body if isinstance(n, ast.FunctionDef)])
print('Only source parsing/fingerprinting was performed by this program. No module import, plan execution, ZIP creation, or final output action.')
