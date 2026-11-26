import ast, collections, json, pathlib, re, sys
W = pathlib.Path("<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped/work")
T = pathlib.Path("F:/user/.claude/projects/C--Users-user-Documents/e0d20ada-e036-40ad-83b1-31e9a63b69bc/subagents/agent-a0805369bae2ebddc.jsonl")
runs = []
for line in T.read_text(encoding="utf-8", errors="replace").splitlines():
    try: r = json.loads(line)
    except ValueError: continue
    c = (r.get("message") or {}).get("content")
    if not isinstance(c, list): continue
    for b in c:
        if isinstance(b, dict) and b.get("type") == "tool_use":
            s = (b.get("input") or {}).get("command") or ""
            if "python" in s and "GCT_PLETH" in s:
                runs.append((r["timestamp"], s))
print("python commands naming that return:", len(runs))
started = set()
for t, s in runs:
    for m in re.finditer(r"(?m)^.*python[^\n]*$", s):
        print(t[5:16], m.group(0)[:210])
    started |= set(re.findall(r"([A-Za-z0-9_]+)[.]py", s))
    started |= set(re.findall(r"(?:from|import) +([A-Za-z0-9_]+)", s))
by = collections.defaultdict(list)
for p in W.rglob("*.py"): by[p.stem].append(p)
started |= {"outer_five_positive", "stable_hook_positive", "generic_twist_lower_positive", "shp"}
todo = [x for x in started if x in by]
print("entry modules:", sorted(todo))
seen, hits = set(), []
BAD = set("system popen Popen unlink remove rmtree rename replace urlopen write_text write_bytes exec eval compile __import__ exec_module spec_from_file_location import_module run check_output call putenv".split())
while todo:
    stem = todo.pop()
    for p in by[stem]:
        if p in seen: continue
        seen.add(p)
        src = p.read_text(encoding="utf-8", errors="replace")
        try: tree = ast.parse(src)
        except SyntaxError: hits.append((p.name, 0, "UNPARSED")); continue
        for n in ast.walk(tree):
            names = []
            if isinstance(n, ast.Import): names = [a.name.split(".")[0] for a in n.names]
            elif isinstance(n, ast.ImportFrom) and n.module: names = [n.module.split(".")[0]]
            for x in names:
                if x in by: todo.append(x)
                if x in ("subprocess","socket","urllib","requests","shutil","ctypes","http","ftplib","pickle","marshal"): hits.append((str(p.relative_to(W)), n.lineno, "import " + x))
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and re.fullmatch(r"[A-Za-z0-9_/]+[.]py", n.value.strip()):
                s = n.value.strip()[:-3].split("/")[-1]
                if s in by: todo.append(s)
            if isinstance(n, ast.Call):
                f = n.func
                name = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
                base = f.value.id if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) else ""
                if name in BAD and not (name in ("compile",) and base == "re") and name != "replace":
                    hits.append((str(p.relative_to(W)), n.lineno, (base + "." if base else "") + name))
                if name == "open" and len(n.args) > 1 and isinstance(n.args[1], ast.Constant) and re.search("[wa+x]", str(n.args[1].value)):
                    hits.append((str(p.relative_to(W)), n.lineno, "open for writing"))
print("modules in the closure (same-named copies included):", len(seen))
for h in sorted(set(hits)): print("  ", *h)
