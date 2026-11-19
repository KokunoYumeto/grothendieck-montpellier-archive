p = "core.py"
s = open(p, encoding="utf-8").read()
a = 'ID_RE = (r"[A-Z]{1,4}\d*[A-Z]{0,3}(?:\.(?:\d+|[A-Z]{1,3}\d*))+[a-z]?(?:\([ivxa-h]+\))?"'
assert a in s, "ID_RE"
s = s.replace(a, 'ID_RE = (r"[A-Z]{1,4}\d*[A-Z]{0,3}(?:\.(?:\d+|[A-Z]{1,3}\d*|[a-z]{1,2}\d+))+[a-z]?(?:\([ivxa-h]+\))?"')
b = '''    if parent and t.count(".") >= 2:                            # E.97.1 -> E.97 (a part of the row)'''
assert b in s, "parent"
s = s.replace(b, '''    m = re.fullmatch(r"(.*\.\d+)[a-z](?:\d+|-[a-z])?", t)              # D.37f, D.2.22t19, D.2.45e-k -> the row
    if parent and m and m.group(1) in IDS[run]:
        HOW[(run, tok)] = "parent"
        return m.group(1)
''' + b)
c = '''            if alias not in ("AN", "GT", "DF", "DL") or "." not in m.group(3):'''
assert c in s, "weak"
s = s.replace(c, '''            if not (alias in ("AN", "GT", "DF", "DL") and "." in m.group(3)) and alias != "CK":''')
d = '''ID_LIST = re.compile(r"((?:" + ID_RE + r")(?:\s*(?:,|and|–|--|-|—|to|&|/)\s*(?:" + ID_RE + r"|\d+(?:\.\d+)*))*)")'''
assert d in s, "idlist"
s = s.replace(d, '''ID_LIST = re.compile(r"((?:" + ID_RE + r")(?:(?:\s*(?:,|and|–|--|-|—|to|&|/)\s*|\s+)(?:" + ID_RE + r"|\d+(?:\.\d+)*(?![\w])))*)")''')
open(p, "w", encoding="utf-8").write(s)

p = "resolve.py"
s = open(p, encoding="utf-8").read()
e = '''        if NOTATION.fullmatch(tok):
            continue                 # F3, S3, H1, Z3, PSL2(F7): notation, not an item'''
assert e in s, "notation"
s = s.replace(e, '''        if NOTATION.fullmatch(tok) or ("." not in tok and ":" not in tok and frag.strip(" .;,()") != tok):
            continue                 # F3, SL2, GT0, PD2, Q576: notation, not an item
        if re.fullmatch(r"[A-Z]{3,}\d+(?:\.\d+)*", tok) or head[max(0, m.start() - 2):m.start()] in ("\\S", "§", "\\S "):
            continue                 # GPS6.1, CCS7.2: a source key and section; \S4.2: a section of the paper''')
f = '''        cand = sorted({tg for (_, tgs) in tab.values() for tg in tgs if tg.split(":", 1)[1] == tok})
        if len(cand) == 1:
            out.append(("uses" if field in ("depends_on", "where_proved") else "names", cand[0], "bare id found in the prompt rows"))
            continue
        if run in PRED and find_id(PRED[run], tok):
            out.append(("uses" if field in ("depends_on", "where_proved") else "names", f"{PRED[run]}:{find_id(PRED[run], tok)}",
                        "bare id found in the predecessor run"))
            continue'''
assert f in s, "bare"
s = s.replace(f, '''        cand = sorted({tg for (_, tgs) in tab.values() for tg in tgs if tg.split(":", 1)[1] == tok})
        if len(cand) == 1:
            out.append((rel_kind, cand[0], "bare id found in the prompt rows"))
            continue
        ctx = [r2 for r2 in ROW_CTX.get(CUR[0], []) if find_id(r2, tok)]
        if len(ctx) == 1:
            out.append((rel_kind, f"{ctx[0]}:{find_id(ctx[0], tok)}", "bare id; its run is named elsewhere in the row"))
            continue
        if run in PRED and find_id(PRED[run], tok):
            out.append((rel_kind, f"{PRED[run]}:{find_id(PRED[run], tok)}", "bare id found in the predecessor run"))
            continue
        pr = [r2 for r2 in PROMPT_RUNS.get(run, []) if find_id(r2, tok)]
        if len(pr) == 1:
            out.append((rel_kind, f"{pr[0]}:{find_id(pr[0], tok)}", "bare id; the only run named in the prompt that has it"))
            continue''')
g = '''edges = []
unres = []'''
assert g in s, "edges"
s = s.replace(g, '''PROMPT_RUNS = {run: list(dict.fromkeys(tg.split(":", 1)[0] for (_, tgs) in tab.values() for tg in tgs))
               for run, (_, tab) in PROMPT_ROWS.items()}
ROW_CTX = {}
CUR = [None]
for _r in ROWS:
    _t = norm_text(" ".join(_r.get(k, "") or "" for k in ("statement", "notes", "depends_on", "where_proved", "his_places")))
    ROW_CTX[_r["tag"]] = list(dict.fromkeys(x[0] for x in cross_refs(_t, _r["run"]) if x[1]))
edges = []
unres = []''')
h = '''for r in ROWS:
    tag, run = r["tag"], r["run"]'''
assert h in s, "loop"
s = s.replace(h, h + '''
    CUR[0] = tag''')
open(p, "w", encoding="utf-8").write(s)
print("patched")
