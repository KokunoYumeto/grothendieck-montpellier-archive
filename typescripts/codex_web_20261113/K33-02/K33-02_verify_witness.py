"""Recover the independent freeze from the witness table and verify both sets of SHA-256 digests."""
import csv
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def digests(stage, log):
    return {name: value for value, name in re.findall(
        rf"^{stage} SHA-256 ([0-9a-f]{{64}})  (.+)$", log, re.MULTILINE)}

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    log = (ROOT / "progress.log").read_text(encoding="utf-8")
    frozen = digests("frozen", log)
    post = digests("witness", log)
    assert len(frozen) == len(post) == 17 and frozen.keys() == post.keys()
    with (ROOT / "K33-02_witness.tsv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    reconstructed, distributed = [], []
    for scan in range(18, 34):
        name = f"pages/K33-02_33_scan{scan:03}.tex"
        page = (ROOT / name).read_text(encoding="utf-8")
        assert sha(page) == post[name], name
        distributed.append(page)
        indexes = [r for r in rows if int(r["scan"]) == scan]
        for row in reversed(indexes):
            offset = int(row["final_offset"])
            before, after = row["frozen"], row["final"]
            assert before.startswith(("\\unsure{", "\\illegible{")), row["locus"]
            assert page[offset:offset+len(after)] == after, row["locus"]
            page = page[:offset] + before + page[offset+len(after):]
        assert sha(page) == frozen[name], name
        for row in indexes:
            offset = int(row["frozen_offset"])
            assert page.startswith(row["frozen"], offset), row["locus"]
        reconstructed.append(page)
    whole = "K33-02_transcription.tex"
    assert sha("".join(reconstructed)) == frozen[whole]
    assert sha("".join(distributed)) == post[whole]
    assert (ROOT / whole).read_bytes() == "".join(distributed).encode("utf-8")
    print("PASS: the table reverses the witness edits exactly; all 17 frozen and all 17 final SHA-256 digests agree.")

if __name__ == "__main__":
    main()
