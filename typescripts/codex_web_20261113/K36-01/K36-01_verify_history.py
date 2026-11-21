"""Verify both sets of SHA-256 hashes and the scope of the witness changes. Read only."""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    hashes = {}
    for line in (ROOT / "progress.log").read_text().splitlines():
        fields = line.split()
        if len(fields) == 4 and fields[1] == "sha256":
            stage, _, hexdigest, filename = fields
            hashes[stage, filename] = hexdigest
    with (ROOT / "K36-01_witness_spans.tsv").open() as source:
        entries = list(csv.DictReader(source, delimiter="\t"))
    pages = sorted((ROOT / "pages").glob("*.tex"))
    assert len(pages) == 16
    assert len(entries) == len({r['place_id'] for r in entries}) == 134
    original_pages = []
    for page in pages:
        filekey = page.relative_to(ROOT).as_posix()
        src = page.read_bytes()
        assert digest(src) == hashes["witness", filekey], filekey
        last = 0
        result = bytearray()
        for r in entries:
            if r["place_id"].split(".")[0] != page.stem[-3:]:
                continue
            old, new = r["frozen_fragment"].encode(), r["final_fragment"].encode()
            offset = int(r["final_byte"])
            assert offset >= last and src[offset:offset + len(new)] == new, r["place_id"]
            result.extend(src[last:offset])
            assert len(result) == int(r["frozen_byte"]), r["place_id"]
            assert old.startswith((b"\\unsure{", b"\\illegible{")) and old.endswith(b"}")
            action = r["outcome"]
            assert action in {"changed", "alternative added", "unchanged"}
            assert (action == "unchanged") == (old == new), r["place_id"]
            if action == "alternative added":
                assert new.startswith(old[:-1] + b"|") and new.endswith(b"}")
            result.extend(old)
            last = offset + len(new)
        result.extend(src[last:])
        assert digest(result) == hashes["frozen", filekey], filekey
        original_pages.append(bytes(result))
    key = "K36-01_transcription.tex"
    assemble = lambda parts: b"\n".join(p.rstrip() + b"\n" for p in parts)
    assert digest(assemble(original_pages)) == hashes["frozen", key]
    final = (ROOT / key).read_bytes()
    assert assemble([page.read_bytes() for page in pages]) == final
    assert digest(final) == hashes["witness", key]
    for action in ("changed", "alternative added", "unchanged"):
        print(f"{action}: {sum(r['outcome'] == action for r in entries)}")
    print("All 17 frozen and all 17 final digests match. All bytes outside the listed marks agree.")

if __name__ == "__main__":
    main()
