"""Source-only checks for K33-10. This program does not invoke TeX."""
import csv
import re
from hashlib import sha256
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parent
ALLOWED = set("""
Downarrow Gamma Leftarrow alpha arraycolsep arrow bar baselineskip begin begingroup beta
bigcap bigcup bigl bigr boxed bullet cap cdot cdots cotefile csname deleted diagram dim
draw ell end endcsname endgroup figure fill frac gamma geq handwritten height hfill hookrightarrow in
infty inserted int ldots left leq limits log longleftarrow longleftrightarrow longrightarrow
makebox margin mathbb mathrm mathscr mspage ne node not operatorname otimes overset pi prod
qquad quad raisebox rho right rule scanpage scriptsize setlength simeq subset sum tag text
times to uline underline underset unsure vert illegible uuline
""".split())
ENVIRONMENTS = {"aligned", "array", "tikzcd", "tikzpicture", "scope"}
TOKEN = re.compile(r"\\([A-Za-z@]+|.)|([{}$%])", re.S)

def check(path):
    text = path.read_text()
    envs, modes = [], []
    depth, groups, offset, counts = 0, 0, 0, Counter()
    while (match := TOKEN.search(text, offset)):
        command, symbol = match.groups()
        offset = match.end()
        if symbol == "%":
            end = text.find("\n", offset)
            offset = len(text) if end < 0 else end + 1
        elif symbol in ("{", "}"):
            depth += 1 if symbol == "{" else -1
            assert depth >= 0, (path, match.start(), "extra closing brace")
        elif symbol == "$":
            if modes and modes[-1] == "$":
                modes.pop()
            else:
                modes.append("$")
        elif command in ("[", "]"):
            if command == "[":
                assert not modes, (path, match.start(), "nested display")
                modes.append("[")
            else:
                assert modes.pop() == "[", (path, "display mismatch")
        elif command and command[0].isalpha():
            assert command in ALLOWED, (path, match.start(), "unknown command", command)
            counts[command] += 1
            if command in ("begin", "end"):
                name = re.match(r"\{([^}]+)\}", text[offset:]).group(1)
                assert name in ENVIRONMENTS, (path, name)
                if command == "begin":
                    envs.append(name)
                else:
                    assert envs.pop() == name, (path, match.start(), name)
            if command in ("begingroup", "endgroup"):
                groups += 1 if command == "begingroup" else -1
                assert groups >= 0
            if command == "csname":
                assert text.startswith(r" tagsleft@true\endcsname", offset)
    assert (depth, groups, modes, envs) == (0, 0, [], []), (path, depth, groups, modes, envs)
    return counts
def verify_witness_history(paths, fragment):
    changes = ROOT / "K33-10_witness_changes.tsv"
    if not changes.exists():
        return
    with changes.open(newline="") as stream:
        records = list(csv.DictReader(stream, delimiter="\t"))
    assert len(records) == len({r["id"] for r in records})
    assert Counter(r["decision"] for r in records) == {"changed": 9, "alternative added": 18}

    log = (ROOT / "progress.log").read_text()
    def logged_hashes(phase):
        block = log.split(phase + " SHA-256 set\n", 1)[1]
        entries = re.findall(r"^([a-f0-9]{64})  (.+)$", block, re.M)[:12]
        assert len(entries) == 12
        return {filename: digest for digest, filename in entries}

    independently_hashed = logged_hashes("Independent")
    expected_final = logged_hashes("Post-witness") if "Post-witness SHA-256 set\n" in log else {}
    restored_pages = []
    for path in paths:
        n = path.stem[-3:]
        current = path.read_bytes()
        restored = current.decode("utf-8")
        rows = [r for r in records if r["scan"] == n]
        previous_end = 0
        cumulative_delta = 0
        for row in rows:
            a, b = int(row["independent_offset"]), int(row["final_offset"])
            assert a >= previous_end and a + cumulative_delta == b
            assert row["independent_text"].startswith(("\\unsure{", "\\illegible{"))
            previous_end = a + len(row["independent_text"])
            cumulative_delta += len(row["final_text"]) - len(row["independent_text"])
        for row in reversed(rows):
            pos = int(row["final_offset"])
            end = pos + len(row["final_text"])
            assert restored[pos:end] == row["final_text"]
            restored = restored[:pos] + row["independent_text"] + restored[end:]
        restored = restored.encode("utf-8")
        rel = path.relative_to(ROOT).as_posix()
        assert sha256(restored).hexdigest() == independently_hashed[rel]
        if expected_final:
            assert sha256(current).hexdigest() == expected_final[rel]
        restored_pages.append(restored)
    assert sha256(b"".join(restored_pages)).hexdigest() == independently_hashed[fragment.name]
    if expected_final:
        assert sha256(fragment.read_bytes()).hexdigest() == expected_final[fragment.name]
    print(f"Reversing {len(records)} marked edits reproduces all 12 independent hashes.")
    if expected_final:
        print("All 12 post-witness hashes also match.")

def main():
    paths = [ROOT / "pages" / f"K33-10_33_scan{n}.tex" for n in range(171, 182)]
    fragment = ROOT / "K33-10_transcription.tex"
    assert fragment.read_bytes() == b"".join(p.read_bytes() for p in paths)
    combined = Counter()
    for n, p in enumerate(paths, 171):
        c = check(p)
        assert c["scanpage"] == 1 and c["cotefile"] == (n == 171)
        assert rf"\scanpage{{{n}}}" in p.read_text()
        combined.update(c)
        print(f"{n}: balanced braces, displays, dollars and environments; command inventory passes")
    verify_witness_history(paths, fragment)
    assert combined == check(fragment)
    print("Assembled fragment matches the pages and passes the same checks.")
    print("Marks:", ", ".join(f"{k} {combined[k]}" for k in ("unsure","illegible","deleted")))
if __name__ == "__main__":
    main()
