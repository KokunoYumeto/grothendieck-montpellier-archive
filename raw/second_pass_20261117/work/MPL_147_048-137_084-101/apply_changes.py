"""Apply the second-pass corrections for MPL_147_048-137 scans 084-101 and write the corrected files.

Every replacement must match exactly once in its first-pass file; nothing is written otherwise.
"""
import difflib
import sys
from pathlib import Path

ROOT = Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SRC = ROOT / "returns/MPL_147_048-137_unzipped/pages"
OUT = ROOT / "second_pass/out/MPL_147_048-137"

AP = r"""\unsure{aplaties|orphelines}"""

CHANGES = {
    "085": [
        (r"""\margin{ici $A$ désigne l'ens. de toutes les arêtes de $G$.}""",
         r"""\margin{ici $A$ désigne l'ens. de \unsure{ttes|toutes} les arêtes de $G$.}"""),
    ],
    "086": [
        (r"""\tag{120}""", r"""\tag{1\unsure{20|19}}"""),
        (r"""S_C\Pi M_G\deleted{\Gamma'} \arrow[r]""",
         r"""S_C\Pi M_G\deleted{\unsure{\Gamma^!|\Gamma'}} \arrow[r]"""),
    ],
    "087": [
        (r"""(S_{\unsure{S|C}}\Pi M_G,\Gamma') \arrow[r] \arrow[d,equal]""",
         r'''(S_S\Pi M_G,\Gamma') \arrow[r] \arrow[d,phantom,sloped,"\simeq"]'''),
        (r"""$S_A\Pi M_G$ dépendent fonctoriellement""",
         r"""$S_A\Pi M_G$ dépend fonctoriellement"""),
    ],
    "088": [
        (r"""isomorphe} \unsure{à} un ens. des parties d'un ens. fini.""",
         r"""isomorphe} \unsure{à l'|à un} ens. des parties d'un ens. fini."""),
        (r"""par $\mathbf Z^{A(G)}$ (en fait,""", r"""par $\mathbf Z^{A(G)}$. (en fait,"""),
    ],
    "090": [
        (r"""sur un corps alg. clos $\unsure{k|h}$""", r"""sur un corps alg. clos $\unsure{h|k}$"""),
    ],
    "091": [
        (r"""\deleted{\unsure{et|en}} et en normalisant""", r"""\deleted{\unsure{lin|en}} et en normalisant"""),
        (r"""Le \deleted{MD}-\unsure{marquage|marqué}""", r"""Le \deleted{MD}-m.graphe"""),
    ],
    "093": [
        (r"""alors pour la courbe spéciale $G$-épinglée""",
         r"""alors pour \unsure{$\forall$|la} courbe spéciale $G$-épinglée"""),
        (r"""(120)\qquad I'\longrightarrow S""", r"""(126)\qquad I'\longrightarrow S"""),
    ],
    "094": [
        (r"""\text{induite par }""", r"""\text{induit par }"""),
    ],
    "095": [
        (r"""dont l'image est contenue \unsure{dans} $I\amalg\widetilde J$""",
         r"""dont l'image est contenue $I\amalg\widetilde J$"""),
    ],
    "096": [
        (r"""branches \unsure{orphelines|aplaties}""", r"""branches """ + AP),
        (r"""au voisinage de tt pt de $S$""", r"""au voisinage de $\forall$ pt de $S$"""),
        (r"""est une involution de $\widehat A$, et""",
         r"""est une involution de $\unsure{\widetilde A|\widehat A}$, et"""),
    ],
    "097": [
        (r"""aux ``branches orphelines'' du""", r"""aux ``branches """ + AP + r"""'' du"""),
        (r"""La donnée d'un graphe à branches orphelines revient""",
         r"""La donnée d'un graphe à branches """ + AP + r""" revient"""),
        (r"""On décrit un tel graphe à branches orphelines par""",
         r"""On décrit un tel graphe à branches """ + AP + r""" par"""),
        (r"""et les branches orphelines \deleted{sont}""", r"""et les branches """ + AP + r""" \deleted{sont}"""),
        (r"""\inserted{à \unsure{b.o.|b.a.}}""", r"""\inserted{à b.a.}"""),
    ],
    "098": [
        (r"""\deleted{\unsure{pieds}}""", r"""\deleted{\unsure{flèches|pieds}}"""),
        (r"""On trouve un nouveau graphe à branches orphelines (qui""",
         r"""On trouve un nouveau graphe à branches """ + AP + r""" (qui"""),
        (r"""pas de branches flottantes, il a""", r"""pas de branches """ + AP + r""", il a"""),
        (r"""branches ``flottantes'', ce qui""", r"""branches ``""" + AP + r"""'', ce qui"""),
        (r"""certaines branches orphelines, et""", r"""certaines branches """ + AP + r""", et"""),
    ],
    "099": [
        (r"""retranchant des branches orphelines)""", r"""retranchant des branches """ + AP + r""")"""),
    ],
    "101": [
        (r"""\deleted{\unsure{graphes connexes}}""", r"""\deleted{\unsure{composantes connexes|graphes connexes}}"""),
    ],
}

SCANS = [f"{n:03d}" for n in range(84, 102)]


def main():
    write = "--write" in sys.argv
    results = {}
    ok = True
    for n in SCANS:
        name = f"MPL_147_048-137_scan{n}.tex"
        raw = (SRC / name).read_bytes()
        assert b"\r\n" not in raw, name
        text = raw.decode("utf-8")
        new = text
        for old, rep in CHANGES.get(n, []):
            c = new.count(old)
            if c != 1:
                ok = False
                print(f"!! scan {n}: count {c} for {old!r}")
                continue
            new = new.replace(old, rep)
        results[n] = (name, text, new)
    bad = [ch for ch in "".join(r[2] for r in results.values()) if ord(ch) < 32 and ch not in "\n"]
    if bad:
        ok = False
        print("!! control characters:", sorted(set(map(ord, bad))))
    total = sum(len(v) for v in CHANGES.values())
    print("replacements listed:", total, "ok:", ok)
    for n, (name, text, new) in results.items():
        if text != new:
            for line in difflib.unified_diff(text.splitlines(), new.splitlines(), lineterm="", n=0):
                if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
                    print(n, line[:220])
    if ok and write:
        OUT.mkdir(parents=True, exist_ok=True)
        existing = [r[0] for r in results.values() if (OUT / r[0]).exists()]
        if existing:
            print("!! already present, not overwritten:", existing)
            return
        for name, text, new in results.values():
            (OUT / name).write_bytes(new.encode("utf-8"))
        print("written:", len(results), "files to", OUT)


main()
