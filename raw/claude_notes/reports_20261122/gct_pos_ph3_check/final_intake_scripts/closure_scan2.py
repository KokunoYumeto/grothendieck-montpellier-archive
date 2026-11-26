"""Static scan, second pass: also the copied entry module, write modes given by keyword or on Path.open, and imports outside work/."""
import ast, collections, hashlib, pathlib, re, sys
R = pathlib.Path("<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped")
C = pathlib.Path("<local>/AppData/Local/Temp/claude/f2c80a22394db22f/e0d20ada-e036-40ad-83b1-31e9a63b69bc/scratchpad/chk")
h = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
copy, orig = C / "runcode/shp.py", R / "work/root/stable_hook_positive.py"
print("copy equals the return's file:", h(copy) == h(orig))
by = collections.defaultdict(list)
for p in R.rglob("*.py"): by[p.stem].append(p)
todo = [copy, orig] + by["outer_five_positive"]
seen, hits, outside = set(), set(), set()
BAD_NAME = {"exec","eval","compile","__import__","globals","getattr","setattr","input","breakpoint"}
BAD_ATTR = {"system","popen","Popen","unlink","rmtree","rename","urlopen","write_text","write_bytes","exec_module","spec_from_file_location","import_module","run_path","run_module","check_output","check_call","putenv","startfile","mkdir","makedirs","touch","chmod","symlink_to","dump","save","savetxt","to_csv"}
while todo:
    p = todo.pop()
    if p in seen: continue
    seen.add(p)
    tree = ast.parse(p.read_text(encoding="utf-8"))
    where = p.name
    for n in ast.walk(tree):
        names = []
        if isinstance(n, ast.Import): names = [a.name.split(".")[0] for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module: names = [n.module.split(".")[0]]
        for x in names:
            if x in by: todo += by[x]
            else: outside.add(x)
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and re.fullmatch(r"[A-Za-z0-9_./-]+[.]py", n.value):
            todo += by.get(n.value[:-3].split("/")[-1], [])
        if not isinstance(n, ast.Call): continue
        f = n.func
        if isinstance(f, ast.Name):
            if f.id in BAD_NAME: hits.add((where, n.lineno, f.id))
            name, pos = f.id, 1
        elif isinstance(f, ast.Attribute):
            if f.attr in BAD_ATTR: hits.add((where, n.lineno, f.attr))
            name, pos = f.attr, 0
        else:
            hits.add((where, n.lineno, "computed callee " + type(f).__name__)); continue
        if name == "open":
            modes = [a for a in n.args[pos:pos+1]] + [k.value for k in n.keywords if k.arg == "mode"]
            for m in modes:
                if not isinstance(m, ast.Constant) or re.search("[wax+]", str(m.value)):
                    hits.add((where, n.lineno, "open, not plainly for reading"))
print("files in closure:", len(seen))
print("imports from outside the return:", sorted(outside), "| non-stdlib:", sorted(x for x in outside if x not in sys.stdlib_module_names))
for x in sorted(hits): print("  ", *x)
