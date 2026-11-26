"""Version-2 metadata of hexagon:2611.00939 (WB-0006) from version 1's (main session 329fb1e6, Claude Opus 5.5 at effort max,
24 Nov 2026). The two provenance paragraphs come from the editor's METADATA_PROVENANCE_v2.txt (a49aabbf)."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
m = json.load(open("HEXAGON_METADATA_WB0006.json", encoding="utf-8"))
V2 = "<local>/Documents/reports_20261124/INTAKE_PILE_20261124/v2/2611.00939/"
src = open(V2 + "METADATA_PROVENANCE_v2.txt", encoding="utf-8").read()
paras = [x.strip() for x in src.split("\n\n") if x.strip()]
prod = next(x for x in paras if x.startswith("How it was produced."))
chk = next(x for x in paras if x.startswith("How it was checked."))
old_tail = "the two new remarks have had no second reader."
assert old_tail in chk
chk = chk.replace(old_tail, "Claude Opus 5.5, at effort max, read the version-2 changes before deposit and checked the "
                            "deduction in Remark 7.2 from the statements cited, not the cited proofs.")
p = m["provenance"]
blocks = p.split("\n\n")
i_prod = next(i for i, x in enumerate(blocks) if x.startswith("How it was produced."))
i_chk = next(i for i, x in enumerate(blocks) if x.startswith("How it was checked."))
blocks[i_prod], blocks[i_chk] = prod, chk
m["provenance"] = "\n\n".join(blocks)
assert "earlier versions" not in m["provenance"]
head = ("Version 2 (24 November 2026): no statement or proof is changed. Locators corrected: Sharifi 2002 is cited in the "
        "numbering of arXiv:math/0104116v2 (Theorem 1, Lemma 4), and his 2019 sentence is on p. 221 of RIMS Kokyuroku 2120, "
        "pp. 220-227. New Remark 7.2: Kurihara's equivalence of Vandiver's conjecture with the absence of p-torsion in "
        "K_{4k}(Z); the unrefereed statement of Mok and Zheng (Hexagon 2611.00998) that K_{4m}(Z) = 0 for m <= 30 adds no "
        "prime to the theorem. New Remark 8.1: Ishii's analogue for CM elliptic curves (arXiv:2312.04196v3).\n\n")
m["comments"] = head + m["comments"]
json.dump(m, open("HEXAGON_METADATA_WB0006_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("comments", len(m["comments"]), "| provenance", len(m["provenance"]), "| abstract", len(m["abstract"]))
