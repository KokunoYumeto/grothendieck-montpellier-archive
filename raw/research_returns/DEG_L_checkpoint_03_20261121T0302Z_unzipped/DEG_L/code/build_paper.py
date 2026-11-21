"""Assemble the live DEG_L paper without discarding its component proof records."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def from_md(path):
    text = path.read_text()
    # The report title is supplied by the enclosing section.
    lines = text.splitlines()
    if lines and lines[0].startswith('# '):
        lines = lines[1:]
    result = subprocess.run(
        ['pandoc', '--from=markdown+tex_math_dollars+tex_math_single_backslash', '--to=latex'],
        input='\n'.join(lines), text=True, capture_output=True, check=True)
    return result.stdout

preamble = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\DeclareUnicodeCharacter{0393}{\ensuremath{\Gamma}}
\pdfmapfile{+lm.map}
\pdfmapfile{+cm.map}
\pdfmapfile{+symbols.map}
\pdfmapfile{+euler.map}
\pdfmapfile{+rsfs.map}
\usepackage[margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs}
\usepackage{booktabs,longtable,array}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xurl}
\usepackage{microtype}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlength{\emergencystretch}{3em}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\pandocbounded}[1]{#1}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\title{DEG\_L: Degrees, theta norms, and semiregularity\\
in the 032 construction}
\author{DEG\_L research run\\GPT-6 Astra Pro}
\date{21 November 2026}
\begin{document}
\maketitle
\begin{abstract}
This working paper separates the effective input surface, its nonzero mixed
period, and the signed codimension-two output of the 032 construction.
It proves exact Chow cancellations, integral norm-and-trace division,
fixed-field Weil projectors, and quantitative extraction of any fixed Weil
class from an effective witness. The theta spanning theorem supplies an
exact finite character-theta formula for the energy, and an explicit
surface-degree inequality. The exact quartic spectral formula is a finite rank-two standard-$L(1)$
norm sum, with source representations, multiplicity copies and measures
retained. Sharp local estimates distinguish Schwartz support from level.
The actual CM Hom covolume is computed in a fixed simple CM isogeny
class, giving a conductor-dependent bound and a sharp limitation for
fixed-reference witness transport even after passing to reduced images.
The original construction does not specify a smooth embedding; universal
semiregularity of its deeper-level morphism presentations is false. The
remaining deformation problem is reduced to a gluable weakly equivariant
replacement object with its full Hodge-compatible character. An Adams
operation on its finite twisting gerbe then constructs a signed-cycle
bound even in virtual rank zero. A proper Hilbert parameter-space
argument carries a uniform effective witness bound on dense fibres to
bounded division on the entire family. The general uniform witness bound
in the open Weil families is not asserted. This is a live checkpoint
manuscript; the session has not ended.
\end{abstract}
\tableofcontents
\clearpage
\section{Scope, assumptions, and check protocol}
The prompt and the attached bridge sketch determine the questions. The
sketch is treated as a map of questions, not as a source of proved facts.
As requested, the attached 032 CM Hodge theorem and the stated Alp\"oge
Dirichlet GRH theorem are admitted inputs. The full Lean dependency archive
was not supplied or compiled. General Hecke GRH is a conditional input
attributed by the prompt to Masullo, \S1.2; the attached index does not
contain a complete numbered Hecke-GRH statement. No trace-formula number
is silently substituted for it.

Every finding has a stable run identifier: T6.x, Bx, S-xx, DIVx, or DERx within
DEG\_L\_20261121. Findings are formulations proved in this run, without a
claim that all elementary ingredients are new to the literature. A
conditional implication is proved only with its displayed hypotheses.
The detailed event ledger distinguishes whole-proof reading, targeted
checks, background use, and computations. Exact reasoning effort is not
exposed by the execution environment and is not invented.

The cycle equality $Nt=[Z^+]-[Z^-]$ means equality in cohomology under the
cycle-class map, unless a Chow-group equality is explicitly written. The
word degree always includes the chosen polarization and distinguishes a
pushforward cycle with multiplicity from its reduced image.

\part{Checked findings and explicitly conditional reductions}
'''

parts = [preamble]
sections = [
    ('The surface degree and the Rallis comparison', 'rallis_t6.md', 'rallis_t6_proofs.tex'),
    ('Bounds, Weil projectors, and the integral map lattice', 'lvalue_bounds.md', 'bounds_proofs.tex'),
    ('The limit of transporting a fixed witness', 'fixed_witness_transport.md', 'fixed_witness_transport_proofs.tex'),
    ('Transporting a bounded family of source witnesses', 'bounded_source_transport.md', 'bounded_source_transport_proofs.tex'),
    ('A local Fourier normalization control', 'local_fourier_period.md', 'local_fourier_period_proofs.tex'),
    ('Semiregularity and the replacement-object problem', 'semireg_t7.md', 'semireg_t7_proofs.tex'),
    ('Bounded division in families', 'bounded_division.md', 'bounded_division_proofs.tex'),
    ('Polarization constraints and syzygy candidates', 'derived_candidates.md', 'derived_candidates_proofs.tex'),
    ('Faithful operations and the remaining replacement gate', 'derived_functors.md', 'derived_functors_proofs.tex'),
]
for title, md, tex in sections:
    parts.append('\\section{' + title + '}\n')
    candidate = ROOT/'research'/tex
    parts.append(candidate.read_text() if candidate.exists() else from_md(ROOT/'research'/md))

parts.append(r'''\clearpage
\part{Open questions and unproved implications}
\section{The remaining main questions}
No statement in this part is asserted as a theorem without an explicit
conditional antecedent. The exact raw degree is not a function of source
level alone. A complete normalization specifies the primitive integral
maps, their polarization, theta inputs, adelic measures and local factors.
The finite spectral formula does not automatically reduce every rank-two
standard $L$-function to Hecke characters.

The uniform geometric question is the existence, on dense fibres of each
open Weil family, of effective middle-dimensional cycles of bounded degree
whose Weil component is nonzero. B6--B8 and DIV1--DIV2 remove the generic
projector and bounded-division extraction from that question. They do not
prove the bounded witness assertion. The integral Hom covolume, its rank,
and the generic mapping degree must be retained when converting theta
norms into a bound for the reduced image.

For a specified smooth reduced 032 image the Bloch question remains the
surjectivity in S-02. The universal assertion for all allowed deeper-level
map presentations is refuted by S-05--S-06. A deformation of a projected
class requires a different semiregular object, or another argument; the
full unprojected rigid surface class need not stay Hodge. A projected
$K_0$ class is not a proof that a representative object is semiregular.
S-14 and DER4 reduce the sufficient deformation route to one gluable
weakly target-equivariant object with complete character
$e^{B_0}\operatorname{ch}(E_0)=P(\theta_0)+\lambda t_0$.
DER4 constructs fixed signed-cycle bounds from its local deformation
without a virtual-rank assumption; DER7 makes the multiplier independent
of the gerbe order when the virtual rank is nonzero. DER1--DER6 and
S-18 exclude several specified canonical attempts to construct that object.

Every approach tried, its outcome, and the next precise gate are recorded
in the component reports, QUESTIONS.tsv, and LEDGER.md. The scheduled
three-hour progress review has not yet occurred in this checkpoint.
\section{Consequences and exact framework locators}
''')
parts.append(from_md(ROOT/'IMPLICATIONS.md'))
parts.append('\n\\end{document}\n')
(ROOT/'DEG_L.tex').write_text('\n'.join(parts))
print(ROOT/'DEG_L.tex')
