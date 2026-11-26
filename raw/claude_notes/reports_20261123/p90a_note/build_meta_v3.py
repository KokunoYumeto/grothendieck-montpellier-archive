"""Build HEXAGON_METADATA_WB0003_v3.json from v2's metadata and the v3 source (main session 329fb1e6, Claude Opus 5.5 at
effort max, 24 Nov 2026)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
m = json.load(open("HEXAGON_METADATA_WB0003_v2.json", encoding="utf-8"))
tex = open(r"<local>/Documents/reports_20261124/INTAKE_PILE_20261124/v2/2611.00936_v3/p90a_note_v3.tex",
           encoding="utf-8").read()
a = tex.split("\\begin{abstract}")[1].split("\\end{abstract}")[0]
a = re.sub(r"(?m)(?<!\\)%.*$", "", a)
a = a.replace("~", " ")
a = re.sub(r"\s+", " ", a).strip()
a = a.replace("\\noindent ", "").replace("\\OO", "\\mathcal O")
line =next(l for l in tex.splitlines() if l.startswith("\\title{"))
t = line[len("\\title{"):-1].replace("\\\\", " ")
t = re.sub(r"\s+", " ", t).strip()
m["title"] = t
m["abstract"] = a
head = ("Version 3 adds Theorem 4, proved in a new Section 7: in every positive characteristic p there is a smooth "
        "projective surface with a very ample L such that H^1(L^{-1}) is nonzero, from a cyclic cover of degree p+1 of "
        "Tango's ruled surface over an Artin-Schreier curve. The characteristic-2 theorem (562, 1, 565), Theorem 3 and "
        "Corollary 2 are unchanged. Version 2 added Corollary 2 (the second part of Kweon's Question 7.7) and corrected "
        "Theorem 3. ")
c = m["comments"]
c = c[c.index("This note answers"):]
c = c.replace("The surface, the bundle and the question are Raynaud's.",
              "The characteristic-2 surface and the question are Raynaud's.")
old1 = "what is new is the globally generated twist on Raynaud's surface and the very ampleness of the root cover."
old2 = "No human has checked the proof. Records,"
assert old1 in c and old2 in c
c = c.replace(old1, "what is new is the globally generated twist on Raynaud's surface, its analogue on a cyclic cover of "
              "Tango's ruled surface in every characteristic, and the very ampleness of the root cover.")
c = c.replace(old2, "Version 3's construction in every characteristic comes from a separate GPT-6 Astra (ChatGPT Pro mode) "
              "run: Claude Opus 5.5 at effort max made a targeted check of its vanishing ranges, Claude Opus 5.5 at effort high "
              "checked every step and every invariant for every p and wrote Section 7, and Claude Opus 5.5 at effort max read "
              "Section 7 step by step before posting. No human has checked the proof. Records,")
c = c.replace("Records, checks and programs: ", "Records: ")
m["comments"] = head + c
p = m["provenance"]
assert "Where the records are." in p
v3 = ("Version 3. The construction in every characteristic (Theorem 4) was produced by GPT-6 Astra (ChatGPT Pro mode) in "
      "a separate research run on crystalline questions in positive characteristic. Claude Opus 5.5, at effort max, made a "
      "targeted check of its vanishing ranges. Claude Opus 5.5, at effort high, checked every step and every invariant "
      "against that run's text for every prime p, and wrote Section 7. Claude Opus 5.5, at effort max, read Section 7 step "
      "by step and every page of version 3 before posting. No human has checked it.\n\n")
m["provenance"] = p.replace("Where the records are.", v3 + "Where the records are.")
m["tags"] = m["tags"] + [x for x in ["Artin-Schreier curves"] if x not in m["tags"]]
json.dump(m, open("HEXAGON_METADATA_WB0003_v3.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("title:", t)
print("abstract", len(a), "chars:")
print(a)
print("comments", len(m["comments"]), "| provenance", len(m["provenance"]))
