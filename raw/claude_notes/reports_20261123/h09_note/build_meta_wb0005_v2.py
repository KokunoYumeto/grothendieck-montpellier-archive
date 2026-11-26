"""Version-2 metadata of hexagon:2611.00938 (WB-0005) from version 1's (main session 329fb1e6, Claude Opus 5.5 at effort max,
24 Nov 2026)."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
m = json.load(open("HEXAGON_METADATA_WB0005.json", encoding="utf-8"))
head = ("Version 2 adds one paragraph to Section 1.5 (Context), with three references, on two papers of Y. Katagiri "
        "(arXiv:2609.20002 and arXiv:2611.25978): they determine the valuations of the Schneider-Teitelbaum polynomials at "
        "a period, that is, the coefficients of one eigenfunction of the invariant derivation D, on which D^n acts with "
        "valuation exactly c_h n. Theorems A and B bound D^n f for every integral f, a different quantity. The theorems and "
        "their proofs are unchanged.\n\n")
m["comments"] = head + m["comments"]
p = m["provenance"]
key = "Where the records are."
assert key in p
v2 = ("Version 2 (24 November 2026) adds the last paragraph of Section 1.5 and three references, and changes nothing else. "
      "Claude Fable 5.2, at effort max, wrote that paragraph after reading the abstracts, introductions and main "
      "statements of Katagiri's two papers in their arXiv sources; Claude Opus 5.5, at effort max, read it against those "
      "statements before deposit.\n\n")
m["provenance"] = p.replace(key, v2 + key)
json.dump(m, open("HEXAGON_METADATA_WB0005_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("comments", len(m["comments"]), "| provenance", len(m["provenance"]), "| tags", len(m["tags"]))
