"""Check the complete included LaTeX source graph, without claiming a compile."""
from pathlib import Path
import argparse, collections, hashlib, json, re

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--output", default="research/tex_source_integrity.json")
args = parser.parse_args()
seen, missing, input_order = set(), [], []

def read(path):
    if path in seen:
        return
    seen.add(path)
    if not path.is_file():
        missing.append(str(path.relative_to(root)))
        return
    input_order.append(path)
    source = path.read_text()
    for name in re.findall(r"\\input\{([^}]+)\}", source):
        target = root / name
        if not target.suffix:
            target = target.with_suffix(".tex")
        read(target)

read(root / "HODGE_DIVISION.tex")
bibs, labels, cited, refs, environments, hashes = [], [], [], [], [], {}
for path in input_order:
    text = path.read_text()
    # Strip ordinary comments, preserving escaped percent signs.
    text = re.sub(r"(?<!\\)%[^\n]*", "", text)
    bibs.extend(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", text))
    labels.extend(re.findall(r"\\label\{([^}]+)\}", text))
    for group in re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", text):
        cited.extend(x.strip() for x in group.split(","))
    refs.extend(re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text))
    stack = []
    errors = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", text):
        if kind == "begin":
            stack.append(name)
        elif not stack or stack[-1] != name:
            errors.append({"end": name, "stack": list(stack)})
        else:
            stack.pop()
    if stack or errors:
        environments.append({"file": str(path.relative_to(root)),
                             "unclosed": stack, "mismatches": errors})
    hashes[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()

def duplicates(values):
    return sorted(k for k, count in collections.Counter(values).items() if count > 1)

result = {
    "scope": "Included source graph, bibliography, labels and per-file environments only; not TeX compilation",
    "input_files": len(input_order), "missing_inputs": missing,
    "undefined_citations": sorted(set(cited)-set(bibs)),
    "undefined_references": sorted(set(refs)-set(labels)),
    "duplicate_bibitems": duplicates(bibs), "duplicate_labels": duplicates(labels),
    "environment_findings": environments, "file_sha256": hashes,
}
# Bibliography/document environments intentionally cross the root input boundary
# only through complete inputs; each input otherwise uses balanced environments.
result["status"] = "PASS" if all(not result[k] for k in (
    "missing_inputs", "undefined_citations", "undefined_references",
    "duplicate_bibitems", "duplicate_labels", "environment_findings")) else "FINDINGS"
out = root / args.output
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k!="file_sha256"}))
