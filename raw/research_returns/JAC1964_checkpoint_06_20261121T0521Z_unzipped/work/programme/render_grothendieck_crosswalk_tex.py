"""Render the authored TSV as a self-contained, pdflatex-safe appendix.

Grouping is exact on archive locator, archive role, SGA locator, and SGA
role.  Large identical groups are split for page layout, never merged
with a merely similar group.  Modern source paragraphs remain in proofs.
"""
from pathlib import Path
import ast
import collections
import csv
import json
import re

HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader((HERE / "GROTHENDIECK_CROSSWALK.tsv").open(), delimiter="\t"))
tree = ast.parse((HERE / "build_grothendieck_crosswalk.py").read_text())
catalogs = {}
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ("ARCHIVE", "SGA"):
                catalogs[target.id] = ast.literal_eval(node.value)
archive, sga = catalogs["ARCHIVE"], catalogs["SGA"]

ascii_tex = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
    "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}
unicode_tex = {
    "–": "--", "—": "---", "−": r"\(-\)", "×": r"\(\times\)",
    "·": r"\(\cdot\)", "≤": r"\(\leq\)", "≥": r"\(\geq\)",
    "≠": r"\(\ne\)", "≅": r"\(\simeq\)", "→": r"\(\to\)",
    "⊗": r"\(\otimes\)", "⊕": r"\(\oplus\)", "∞": r"\(\infty\)",
    "§": r"\S{}", "α": r"\(\alpha\)", "β": r"\(\beta\)",
    "γ": r"\(\gamma\)", "δ": r"\(\delta\)", "η": r"\(\eta\)",
    "θ": r"\(\theta\)", "κ": r"\(\kappa\)", "τ": r"\(\tau\)",
    "φ": r"\(\varphi\)", "ψ": r"\(\psi\)", "χ": r"\(\chi\)",
    "Λ": r"\(\Lambda\)", "Δ": r"\(\Delta\)", "Ω": r"\(\Omega\)",
    "ℓ": r"\(\ell\)", "é": r"\'{e}", "ü": r"\"{u}",
    "à": r"\`{a}", "è": r"\`{e}", "ö": r"\"{o}",
    "’": "'", "‘": "`", "“": "``", "”": "''", "…": r"\ldots{}",
}
superscripts = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-"))
subscripts = dict(zip("₀₁₂₃₄₅₆₇₈₉₋", "0123456789-"))

math_phrases = {
    "D=r_*(p*z·q*z)": r"\(D=r_*(p^*z\cdot q^*z)\)",
    "T_l(J^i)": r"\(T_\ell(J^i)\)",
    "dim J^i≤b_(2i−1)/2": r"\(\dim J^i\leq b_{2i-1}/2\)",
    "Λ_Y=φ*Λ_X²φ_*": r"\(\Lambda_Y=\varphi^*\Lambda_X^2\varphi_*\)",
    "2i≤n−1": r"\(2i\leq n-1\)",
    "2i=n": r"\(2i=n\)",
    "2i≥n+1": r"\(2i\geq n+1\)",
    "EGA IV_4": r"EGA~IV\textsubscript{4}",
    "EGA III_2": r"EGA~III\textsubscript{2}",
    "(−1)^(r+1)": r"\((-1)^{r+1}\)",
    "δ(L)=m*L−pr_1*L−pr_2*L": r"\(\delta(L)=m^*L-\operatorname{pr}_1^*L-\operatorname{pr}_2^*L\)",
    "Fbar_p": r"\(\overline{\mathbf F}_p\)",
    "N=h³(J)^G": r"\(N=h^3(J)^G\)",
    "a_l²=q₀/(ec)": r"\(a_\ell^2=q_0/(ec)\)",
    "q₀=u/s=(us)/s²": r"\(q_0=u/s=(us)/s^2\)",
    "c>0": r"\(c>0\)",
    "t≥0": r"\(t\geq0\)",
    "d≥2": r"\(d\geq2\)",
    "(g+c−1)!/c!": r"\((g+c-1)!/c!\)",
    "(g−1)!": r"\((g-1)!\)",
}
math_pattern = re.compile("|".join(re.escape(s) for s in sorted(math_phrases, key=len, reverse=True)))

def tex_plain(value):
    out = []
    for c in value:
        if c in superscripts:
            out.append(r"\({}^{" + superscripts[c] + r"}\)")
        elif c in subscripts:
            out.append(r"\({}_{" + subscripts[c] + r"}\)")
        elif c in ascii_tex:
            out.append(ascii_tex[c])
        elif c in unicode_tex:
            out.append(unicode_tex[c])
        elif ord(c) < 128:
            out.append(c)
        else:
            raise ValueError(f"Unmapped Unicode {c!r} in {value!r}")
    return "".join(out)

def tex(value):
    out, start = [], 0
    for match in math_pattern.finditer(value):
        out.append(tex_plain(value[start:match.start()]))
        out.append(math_phrases[match.group()])
        start = match.end()
    out.append(tex_plain(value[start:]))
    return "".join(out)

def key(value):
    return r"\textsf{" + tex(value) + "}"

def archive_keys(row):
    parts = row["archive_locator"].split(" | ")
    inverse = {v:k for k,v in archive.items()}
    return [inverse[p] for p in parts]

def archive_role(row):
    value = row["archive_relationship"]
    if value.startswith("Repaired/proved"):
        return r"\textbf{Programme claim.} Repaired or proved form; the new proof is not attributed to Grothendieck."
    if value.startswith("Not a separate"):
        return r"\textbf{Supporting lemma.} Technical support for the indicated claim."
    if value.startswith("Counterexample"):
        return r"\textbf{Scope obstruction.} Counterexample or boundary of an unqualified reading."
    if value.startswith("Not a statement"):
        return r"\textbf{Modern application.} Not a statement in Grothendieck."
    raise ValueError(value)

# Authored classification: a definition/convention or thematic framework is
# deliberately distinguished from a substantive direct theorem input.
direct_ids = set("""
JAC-P04 JAC-P07 H9-C1 H9-T2 H9-T3 H9-T5 H9-L2 H9-T6 H9-T6a
H9-T7 H9-T8 H9-T8a H9-T10 H9-T12 H9-T13 H9-T17 H9-T18 H9-T19
H9-T19a H9-T20 H9-T21 H9-T22 H9-T23 H9-T23a H9-T24 H9-T25 H9-T26 AR-22
""".split())

def sga_role(row):
    keys = row["SGA_source_keys"].split(";") if row["SGA_source_keys"] else []
    value = row["role_of_SGA_EGA_FGA"]
    if not keys:
        result = r"\textbf{No direct SGA/EGA/FGA input.}"
        if value != "No direct SGA/EGA/FGA input. The archive connection is as stated, not an invented source attribution.":
            result += " " + tex(value)
        return result
    category = "Direct input" if row["finding_id"] in direct_ids else "Related framework or convention"
    return (", ".join(key(k) for k in keys) + r".\par "
            + r"\textbf{" + category + ".} " + tex(value))

parts = [r"""% Generated from the authored live TSV. Do not edit this file manually.
% Requires longtable, booktabs, array, amsmath; compatible with pdflatex.
\section*{Appendix: finding-to-Grothendieck locator crosswalk}
\addcontentsline{toc}{section}{Finding-to-Grothendieck locator crosswalk}
\begingroup
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTpre}{5pt}
\setlength{\LTpost}{7pt}

This appendix maps every stable finding ID to the supplied archive locus
and, separately, to any actual SGA/EGA/FGA input. The archive keys and
source keys are expanded in full below; they are exact cross-references,
not generic citations. Modern primary references and the precise scope
of each conclusion remain in its proof, so their long bibliographies
are not repeated here.

\textbf{Reading the roles.} A \emph{programme claim} is a repaired or
proved form of the indicated 1964 question. A \emph{supporting lemma}
or \emph{scope obstruction} serves that question. A \emph{modern
application} is explicitly \emph{not a statement in Grothendieck}.
Independently, the final column distinguishes a \emph{direct input}
from a \emph{related framework or convention}; the latter does not
prove the new conclusion. An inherited direct input is identified as
such in the role text. Where none is used, the table says
\emph{no direct SGA/EGA/FGA input}.

Only the supplied cote transcriptions were available. Their scan
numbers are supplied-file locators, not reconstructed manuscript
pagination; no palaeographic verification is claimed. Cote~44 scans
3, 5 and 7 contain unrelated interleaved material. The incidence
quotient is Saito's higher Picard variety up to isogeny; a universal
regular algebraic representative is identified only in the expressly
proved codimension-two cases. No general higher-Picard theorem is
invented or attributed to FGA.

\subsection*{Archive register}
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.115\linewidth}>{\raggedright\arraybackslash}p{\dimexpr.885\linewidth-2\tabcolsep\relax}@{}}
\toprule
Key & Exact supplied locus and subject \\
\midrule\endfirsthead
\toprule Key & Exact supplied locus and subject (continued) \\
\midrule\endhead
\bottomrule\endfoot
"""]
for k, v in archive.items():
    parts.append(key(k) + " & " + tex(v) + r" \\" + "\n")
parts.append(r"""\end{longtable}

\subsection*{Exact SGA/EGA source register}
Page numbers are the original printed pagination. No page number has
been guessed where only a section was checked. The three original
volumes are SGA~6, SGA~7~I and SGA~7~II; the volume, exposition and
number in each entry determine the cited statement uniquely.

\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.115\linewidth}>{\raggedright\arraybackslash}p{\dimexpr.885\linewidth-2\tabcolsep\relax}@{}}
\toprule
Key & Exact locus and role \\
\midrule\endfirsthead
\toprule Key & Exact locus and role (continued) \\
\midrule\endhead
\bottomrule\endfoot
""")
for k, (locator, role, url, check) in sga.items():
    parts.append(key(k) + " & " + tex(locator) + ". " + tex(role) + r". \\" + "\n")
parts.append(r"""\end{longtable}

\textbf{Source-check boundary.} The original printed SGA pages recorded
in the source register and live TSV were visually inspected where that
record says so. The section-only entries \textsf{S7inv},
\textsf{S7biext} and \textsf{S7ret}, and the section-only portions of
other entries, were read in a primary-content transcription. The EGA
locator \textsf{EGAaxis} was verified as SGA's explicit reference;
the original EGA theorem was not independently inspected. It is listed
as transverse-axis background, not as a substitute for a proved step.
The accepted 032/Milne inputs are used on the terms stated in the paper.

\subsection*{Complete finding crosswalk}
""")
parts.append(f"The inventory contains {len(rows)} finding IDs. Rows are combined only when\n"
             "their archive locators, archive roles, SGA/EGA/FGA locators and\n"
             "SGA/EGA/FGA roles are identical. A large identical group may be\n"
             "split across several rows for readability. Each ID is listed\n"
             "once in this table; the TSV separately records its proof file\n"
             "and hash. Enumeration and hashes are mechanical coverage checks,\n"
             "not formal proof verification.\n\n")
parts.append(r"""\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.355\linewidth}>{\raggedright\arraybackslash}p{\dimexpr.235\linewidth-2\tabcolsep\relax}>{\raggedright\arraybackslash}p{\dimexpr.410\linewidth-2\tabcolsep\relax}@{}}
\toprule
Finding ID and conclusion & Archive connection & Actual SGA/EGA/FGA input and role \\
\midrule\endfirsthead
\toprule
Finding ID and conclusion & Archive connection & Actual SGA/EGA/FGA input and role (continued) \\
\midrule\endhead
\bottomrule\endfoot
""")
groups = collections.OrderedDict()
for row in rows:
    grouping = tuple(row[f] for f in ("archive_locator", "archive_relationship",
                                     "SGA_EGA_FGA_locator", "role_of_SGA_EGA_FGA"))
    groups.setdefault(grouping, []).append(row)
seen = []
for grouping, group in groups.items():
    # Cap the height of rows which share broad modern-application metadata.
    for start in range(0, len(group), 3):
        chunk = group[start:start+3]
        first = chunk[0]
        assert all(sga_role(r) == sga_role(first) for r in chunk)
        findings = []
        for row in chunk:
            seen.append(row["finding_id"])
            findings.append(r"\textbf{" + tex(row["finding_id"]) + "}. " + tex(row["finding"]))
        col1 = r"\par\smallskip ".join(findings)
        col2 = ", ".join(key(k) for k in archive_keys(first)) + r".\par " + archive_role(first)
        col3 = sga_role(first)
        parts.append(" & ".join((col1, col2, col3)) + r" \\" + "\n")
        parts.append(r"\addlinespace[4pt]" + "\n")
parts.append(r"\end{longtable}" + "\n" + r"\endgroup" + "\n")
assert len(seen) == len(rows) and set(seen) == {r["finding_id"] for r in rows}
content = "".join(parts)
assert all(content.count(r"\textbf{" + r["finding_id"] + "}") == 1 for r in rows)
assert content.isascii()
(HERE / "GROTHENDIECK_CROSSWALK.tex").write_text(content)
report = {"finding_count": len(rows), "exact_groups": len(groups), "table_ids": seen,
          "source": "GROTHENDIECK_CROSSWALK.tsv", "output": "GROTHENDIECK_CROSSWALK.tex",
          "scope": "Exact grouping and ID coverage; not mathematical or palaeographic verification"}
(HERE / "GROTHENDIECK_CROSSWALK_TEX_COVERAGE.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"finding_count": len(rows), "exact_groups": len(groups), "ascii_safe": True}))
