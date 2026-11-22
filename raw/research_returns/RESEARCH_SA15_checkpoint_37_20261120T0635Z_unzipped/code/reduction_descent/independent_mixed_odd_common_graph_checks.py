from pathlib import Path
import hashlib,contextlib,io,json
p=Path("RESEARCH_SA15_work/agents/monodromy")
source=p/"code/mixed_odd_common_graph_checks.py"
author=p/"outputs/mixed_odd_common_graph_checks.json"
before=hashlib.sha256(author.read_bytes()).hexdigest()
code=source.read_text().replace("dest.write_text(json.dumps(result,indent=2)+'\\n')", "# Independent read-only audit: author output write suppressed.")
assert "dest.write_text" not in code
out=io.StringIO()
with contextlib.redirect_stdout(out):exec(compile(code,str(source),"exec"),{"__file__":str(source.resolve()),"__name__":"__main__"})
assert hashlib.sha256(author.read_bytes()).hexdigest()==before
print(json.dumps({"author_sha256_preserved":before,"result":json.loads(out.getvalue())},indent=2))
