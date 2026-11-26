"""Version-2 metadata of hexagon:2611.00940 (WB-0007) from version 1's and the editor's METADATA_FIELDS_v2.txt
(a49aabbf, Claude Fable 5.2 at effort max); main session 329fb1e6 (Claude Opus 5.5 at effort max), 24 Nov 2026."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
V2 = "<local>/Documents/reports_20261124/INTAKE_PILE_20261124/v2/2611.00940/"
m = json.load(open("HEXAGON_METADATA_WB0007.json", encoding="utf-8"))
m["title"] = ("Relations (III') and (IV) of Nakamura and Schneps hold on the profinite Grothendieck-Teichmüller group, "
              "with an application to the two elliptic points of the modular curve")
m["abstract"] = re.sub(r"\s+", " ", open(V2 + "ABSTRACT_v2.txt", encoding="utf-8").read()).strip()
head = ("Version 2 (24 November 2026): version 1 is unchanged. New: relation (III') "
        "holds for every element of GT-hat (Theorem 20), so the subgroup I-Gamma of Nakamura and Schneps is all of GT-hat "
        "(Corollary 21); Lochak's questions on compatible pairs (Algebra i Analiz 37:2, 2025) are answered, and with his "
        "Theorem 5.10 the inertia-preserving outer automorphisms of the procongruence mapping class group of every "
        "surface of generic type form GT-hat (Corollary 22). Corrected: version 1 called the strictness of GT-hat in the "
        "gentle group known; no published proof was found.\n\n")
c = m["comments"]
i = c.index("New here:")
j = c.index("\n\nChecks:")
c = c[:i] + ("New here: (IV) on all of GT-hat, the decomposition GT-hat = Lambda_0 . G_Q, and the vanishing of the "
             "level-twelve character delta on normalized elements (version 1); (III') on all of GT-hat, hence I-Gamma = "
             "GT-hat, and the positive answer to the questions of Lochak on compatible pairs (version 2).") + c[j:]
k = c.index("Checks:")
c = c[:k] + ("Checks: Claude Fable 5.2 at effort max checked the proofs of version 1 and wrote the text; Claude Opus 5.5 at "
             "effort max refereed version 1 as second reader. Theorem 20 and Corollaries 21-22 (by Claude Fable 5.2 at "
             "effort max) were checked by a second reader, Claude Opus 5.5 at effort max, and read again before deposit. "
             "No human has checked it. Records: https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/works/WB-0007.md")
m["comments"] = head + c
p = m["provenance"].split("\n\n")
ip = next(n for n, x in enumerate(p) if x.startswith("How it was produced."))
ic = next(n for n, x in enumerate(p) if x.startswith("How it was checked."))
p[ip] += (" On 24 November 2026 Claude Fable 5.2 (Anthropic), at effort max, made version 2: it found and proved Theorem 20 "
          "(relation (III')) and Corollary 21, re-derived Corollary 22, which Claude Opus 5.5 (Anthropic), at effort max, had "
          "proved in substance in a survey of connections, and added Remarks 19 and 23. An earlier run of GPT-6 Astra "
          "(ChatGPT Pro mode) of 16 November 2026 had proved Theorem 1 in Lochak's formulation.")
p[ic] += (" Theorem 20 and Corollaries 21-22 were checked by a second reader, Claude Opus 5.5 at effort max, in a separate run "
          "(24 November 2026): every step was followed and the braid and abelianization identities recomputed; "
          "Nakamura-Schneps 2000 (Theorem 1.1, Definition 1.1, Theorems 1.3-1.4), Boggi-Zalesskii Theorem A(iii), Furusho "
          "2002 (p. 191) and Lochak 2025 (Definitions 5.4 and 5.8, Proposition-Definition 5.6, Theorem 5.10, pp. 61-62) "
          "were opened at the statements used. The statement of Lochak's Theorem 5.10 ii) and the labels of his relations "
          "were then read on the printed page by Claude Fable 5.2 at effort max. Claude Opus 5.5 at effort max read the "
          "proof of Theorem 20 step by step and the changed pages again before deposit. Remark 19 has been checked by its "
          "author only. Lochak's Theorem 5.10 and Nakamura and Schneps's Theorems 1.3 and 1.4 are used as published, and "
          "their proofs were not checked. The statement of version 1 that the strictness of the inclusion of GT-hat in the "
          "gentle group is known was wrong as a statement about the literature and is corrected.")
m["provenance"] = "\n\n".join(p)
m["tags"] = m["tags"] + [t for t in ["compatible pairs (Lochak)"] if t not in m["tags"]]
json.dump(m, open("HEXAGON_METADATA_WB0007_v2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in m.items() if isinstance(v, str)}, "tags", len(m["tags"]))
