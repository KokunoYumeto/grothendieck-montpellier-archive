#!/usr/bin/env python3
"""Rebuild the documentary input audit from explicit, reviewed assignments.

No keyword rule chooses a class.  The sets below are the audit's decisions.
Text matching is used only to find evidence and to check cited-ID coverage.
Run from any directory.  Sources are read-only; output belongs to this module.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
ROOT = WORK.parent
SOURCES = ROOT / "sources"
GRH = next(SOURCES.glob("RETURN_GRH_NIGHT_checkpoint_07_*"))
ALP = next(SOURCES.glob("RETURN_ALPOGE_BRIDGES_checkpoint_09_*"))
DATE = "2026-11-21"
WHO = "GPT-6 Astra Pro; inherited effort setting; MAS_ARTIN/input_audit"
CLASSES = {"A", "M", "outside preprint", "none"}
PRECEDENCE = {"none": 0, "A": 1, "outside preprint": 2, "M": 3}


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path, rows, columns):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def seq(prefix, start, end, width=2):
    return {f"{prefix}{i:0{width}d}" for i in range(start, end + 1)}


def words(text):
    return set(text.split())


ASSIGNMENTS = {}


def assign(ids, classification):
    assert classification in CLASSES
    for identifier in ids:
        assert identifier not in ASSIGNMENTS, ("duplicate explicit assignment", identifier)
        ASSIGNMENTS[identifier] = classification


# GRH_NIGHT: 129 number-theory rows.  The actual asserted conclusion is
# classified, including a conditional arithmetic branch when the row asserts it.
assign(seq("NT-P", 1, 16), "A")
assign(seq("NT-C", 1, 13), "M")
assign(seq("NT-H", 1, 4), "A")
assign(seq("NT-H", 5, 13), "M")
assign(seq("NT-A", 1, 18) | seq("NT-A", 20, 21), "M")
assign({"NT-A19"}, "A")
assign(seq("NT-F", 1, 4), "M")
assign(words("NT-L01 NT-L02 NT-L04 NT-L05 NT-L06 NT-L07 NT-L09 NT-L11 NT-L12"), "A")
assign(words("NT-L03 NT-L08 NT-L10 NT-L13 NT-L14 NT-L17"), "M")
assign(words("NT-L15 NT-L16"), "none")
assign(words("NT-Z01 NT-Z02 NT-Z05 NT-Z07 NT-Z08 NT-Z09 NT-Z11 NT-Z12 NT-Z18"), "A")
assign(words("NT-Z13 NT-Z14 NT-Z15 NT-Z16 NT-Z17"), "M")
assign(words("NT-Z03 NT-Z04 NT-Z06 NT-Z10 NT-Z19"), "none")
assign(seq("NT-R", 1, 4), "A")
assign(seq("NT-R", 5, 8), "M")
assign(seq("NT-E", 1, 9) | {"NT-E11"} | seq("NT-E", 14, 16), "M")
assign(words("NT-E10 NT-E12 NT-E13"), "none")
assign(words("NT-E17 NT-E18"), "A")

# GRH_NIGHT: 110 geometry/programme rows.
assign(words("AG-AT AG-NONCM AG-NODE AG-CM-MODEL-DEGREE AG-FROB-Z"), "A")
assign(words("AG-ARTIN AG-DED AG-CM AG-NONCM-W0 AG-FROB AG-LAMBDA AG-DET AG-MOMENT AG-HANKEL AG-SIGNED AG-C1 AG-C44 AG-GT"), "M")
assign(words("AG-CYCLIC-DIV AG-DP-EGS AG-FOURIER-ISOGENY"), "outside preprint")
assign(words("""
AG-LOCAL AG-MODEL AG-WEIGHT AG-SCHEMES AG-SIGN AG-HEIGHT AG-SIGN-NORM
AG-CRITICAL AG-EXT AG-EXT-K AG-C16 AG-C34-74 AG-C34-64 AG-C149 AG-INERTIA
AG-PURITY AG-WM AG-STANDARD AG-COVER AG-KUMMER AG-KUMMER-2 AG-CM-REC
AG-CM-PERIOD AG-C34-TYPE AG-C34-REPAIR AG-C34-INDEX AG-C34-SECTION
AG-C34-NONSOLV AG-C149-COMP AG-C149-LIFT AG-C149-ELLIPTIC AG-LM6-REG
AG-LM6-IRREG AG-LM6-NORM AG-FG-EXP AG-FG-DER AG-FG-PPOWER AG-FG-PRODUCT
AG-FG-THETA AG-ARTHUR-ARCH AG-ARTHUR-PARAM AG-ARTHUR-MIN AG-LEFSCH-LATTICE
AG-LEFSCH-SPLIT AG-C149-NORMAL AG-C149-FULLLIFT AG-C149-CUSP AG-LEFSCH-INDEX
AG-LEFSCH-DEFECT AG-THETA-REG AG-THETA-TORS AG-THETA-HECKE AG-THETA-CLASS
AG-THETA-RAY AG-FG-POLE AG-THETA-PCOND AG-THETA-NONINT AG-CM-INTEGRAL-MODEL
AG-FG-FOURIER AG-THETA-FOURIER AG-SHIMURA-PERIOD AG-SHIMURA-SLOPE
AG-SHIMURA-RAM AG-DENINGER AG-CENTRAL-STRUCT AG-CENTRAL-FUNCTOR
AG-CENTRAL-REAL AG-EXP-VANISH AG-EXP-SEPARATE AG-CENTRAL-Q8 AG-LOCAL-EXP
AG-LOCAL-EXCEPTION AG-LOCAL-DET AG-LOCAL-PURITY AG-FROB-PROJECTOR
AG-FROB-ORDER AG-FROB-COLLISION AG-LOCAL-WD AG-LOCAL-SPLICE AG-FROB-NIL
AG-FROB-CHOW AG-FROB-CYCLES AG-LEFSCH-SMITH AG-LEFSCH-CYCLES AG-FOURIER-MIN
AG-DP-ALG AG-FOURIER-CM2 AG-K8 AG-K8-TWIST
"""), "none")

# GRH_NIGHT: 54 complexity rows.
assign(words("CX-ALG-001 CX-ALG-003 CX-ALG-004 CX-ALG-005 CX-ALG-006 CX-ALG-007 CX-ALG-008 CX-ALG-010 CX-ALG-015 CX-ALG-021 CX-HN-003"), "A")
assign(words("""
CX-ALG-009 CX-ALG-011 CX-ALG-012 CX-ALG-013 CX-ALG-019 CX-ALG-020
CX-ALG-022 CX-ALG-024 CX-ALG-025 CX-ALG-026 CX-ALG-027 CX-ALG-028
CX-HN-001 CX-HN-002 CX-GEO-001 CX-GEO-002 CX-GEO-003 CX-GEO-004
CX-GEO-006 CX-GEO-008 CX-GEO-009 CX-GEO-010 CX-GEO-011 CX-GEO-012
CX-NN-001 CX-NN-002 CX-NN-004
"""), "M")
assign(words("""
CX-ALG-002 CX-ALG-014 CX-ALG-016 CX-ALG-017 CX-ALG-018 CX-ALG-023
CX-HN-004 CX-GEO-005 CX-GEO-007 CX-GEO-013 CX-GEO-014 CX-GEO-015
CX-NN-003 CX-LIM-001 CX-LIM-002 CX-LIM-003
"""), "none")

# GRH_NIGHT: 69 root rows.
assign(words("MT-A01 MT-Q02 MT-NB01 MT-NB04 MT-S506"), "A")
assign(words("MT-ART01 MT-ART06 MT-ART07 MT-ART09 MT-H02 MT-H03 MT-L01 MT-S501 MT-S502 MT-S503 MT-S504 MT-S505 MT-S508 MT-NB02 MT-NB03 MT-M23 MT-M26 MT-M28 MT-M29") | seq("MT-M", 11, 17), "M")
assign(words("MT-ART02 MT-ART03 MT-ART04 MT-ART05 MT-ART08 MT-ART10 MT-ART11 MT-ART12 MT-Q01 MT-H01 MT-L02 MT-S507") | seq("MT-M", 1, 10) | words("MT-M18 MT-M19 MT-M20 MT-M21 MT-M22 MT-M24 MT-M25 MT-M27 MT-M30 MT-M31 MT-M32 MT-M33 MT-M34 MT-M35 MT-M36 MT-M37"), "none")


PREPRINTS = {
    "PF26": {
        "name": "OpenAI (2026), Deterministic Polynomial Factorization over Prime Fields (PF26)",
        "designated": True,
        "url": "https://github.com/openai/math/tree/main/preprints",
        "status": "Preprint dated 4 October 2026; supplied PDF; separate MAS_ARTIN PF26 proof audit",
    },
    "VHS26": {
        "name": "van Hoften–Sempliner, The Hodge Conjecture for CM abelian varieties, Hexagon 2610.00259v2",
        "designated": True,
        "url": "https://hexagonmath.org/pdf/2610.00259v2",
        "status": "Prompt-designated outside preprint; source theorem statements imported, not re-proved in the input audit",
    },
    "MAD26": {
        "name": "Madapusi (contributor), ChatGPT and Claude (PDF byline), Milne's rationality conjecture, Hexagon 2610.00226v1",
        "designated": True,
        "url": "https://hexagonmath.org/pdf/2610.00226v1",
        "status": "Prompt-designated outside preprint; mixed-characteristic lifting and specialization retained as separate premises",
    },
    "MIL26": {
        "name": "Milne, On the Hodge, Tate, and standard conjectures for abelian varieties, Hexagon 2611.00244v1",
        "designated": True,
        "url": "https://hexagonmath.org/pdf/2611.00244v1",
        "status": "Prompt-designated outside preprint; some citations are exposition/corroboration, not an indispensable extra theorem",
    },
    "EGS25": {
        "name": "Engel–de Gaay Fortman–Schreieder, Matroids and the integral Hodge conjecture for abelian varieties, arXiv:2507.15704v3",
        "designated": False,
        "url": "https://arxiv.org/abs/2507.15704",
        "status": "Author institution explicitly lists working paper/preprint; version 3 dated 27 March 2026",
    },
    "FHL26": {
        "name": "Fu–Huang–Li, Supersingular Tate conjecture for irreducible symplectic varieties of known types: I, arXiv:2609.38801v2",
        "designated": False,
        "url": "https://arxiv.org/abs/2609.38801",
        "status": "2026 preprint; version 2 dated 20 October 2026; no journal publication established",
    },
    "RSW25": {
        "name": "Ramzi–Sosnilo–Winges, Every motive is the motive of a stable infinity-category, arXiv:2503.11338v1",
        "designated": False,
        "url": "https://arxiv.org/abs/2503.11338",
        "status": "Author lists accepted in JEMS; no issued publication established in this audit; treated as accepted preprint",
    },
    "IZ26": {
        "name": "Ito–Zou, Semisimplicity, purity and the Mumford–Tate conjecture for hyper-Kähler varieties, arXiv:2610.07890v1",
        "designated": False,
        "url": "https://arxiv.org/abs/2610.07890",
        "status": "2026 preprint; no journal publication established",
    },
    "PZ26": {
        "name": "Petrov–Zavyalov, Formality for rigid-analytic spaces satisfying the weight-monodromy conjecture, arXiv:2607.14517v2",
        "designated": False,
        "url": "https://arxiv.org/abs/2607.14517",
        "status": "2026 preprint; no journal publication established",
    },
    "BROE26": {
        "name": "Broe, The Tate conjecture for abelian fourfolds over finite fields, arXiv:2608.28651v1",
        "designated": False,
        "url": "https://arxiv.org/abs/2608.28651",
        "status": "2026 preprint; no journal publication established",
    },
    "E26": {
        "name": "OpenAI, The Exponential Time Hypothesis is False, 25 October 2026 (E)",
        "designated": False,
        "url": "https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026",
        "status": "Official preprints repository; E is outside the A/M analytic assertions",
    },
    "WEAR23": {
        "name": "Wear, Perfectoid covers of abelian varieties and the weight-monodromy conjecture, arXiv:2303.05610v1",
        "designated": False,
        "url": "https://arxiv.org/abs/2303.05610",
        "status": "Author research page lists submitted; article based on 2020 thesis. No journal publication established.",
    },
}


GRH_OUTSIDE = {
    "AG-CYCLIC-DIV": ["PF26"],
    "AG-DP-EGS": ["EGS25"],
    "AG-FOURIER-ISOGENY": ["EGS25"],
    "CX-ALG-027": ["PF26"],
    "CX-ALG-028": ["PF26"],
}

NOTES = {
    "NT-Z13": "Full asserted scope includes finite-order Hecke characters over arbitrary number fields. A supplies only the zeta/Dirichlet specialization. The complete original input field already mentions M; its leading A label is weaker than the full proof scope.",
    "NT-Z15": "The central multiplicity estimate includes finite-order Hecke L-functions. M supplies their GRH. The leading A label is misleading even though the remainder of the original field records the conditional Hecke branch.",
    "NT-Z16": "The first nonnegative-zero bound includes finite-order Hecke L-functions and inherits NT-Z13's analytic hypotheses. Full scope is M; A is the Dirichlet specialization. No first strictly positive-zero assertion is inferred.",
    "NT-Z14": "Inherits the Hecke branch of NT-Z13; therefore full scope M, with A sufficient over Q.",
    "NT-Z03": "The analytic identity is unconditional on the admissible complex-ordinate test class. A is needed only for the separately described real-ordinate interpretation.",
    "NT-Z04": "The restricted moment identities are unconditional analytic identities. A gives the optional real-ordinate reading. No full-support Gaussian limit is asserted.",
    "NT-Z06": "This row records a limitation of zero-location input; it does not assert the missing GUE, simplicity or nonvanishing conclusion.",
    "NT-Z07": "A is only part of the conjunction: GRH for the specified non-CM GL2 forms is an independent residual premise, not supplied by M.",
    "NT-L15": "The stronger explicit weak mean-square premise B_eta<infinity supplies the zero-location and simplicity consequences; neither A nor M is used once that premise is imposed.",
    "NT-L16": "A specified zero and its real part/order are explicit premises of the implication. M only supplies the optional critical-line specialization.",
    "NT-L17": "The Kummer multiple-zero, weak-mean and full-jet positivity obstructions are unconditional. The same row additionally asserts a critical-line constant and trace positivity under RH(zeta_E), for which M is the sufficient full-scope input.",
    "NT-Z19": "The B_eta finite premise is strictly stronger in the stated argument than A/M alone; classify the implication as none while retaining that premise.",
    "AG-CYCLIC-DIV": "The proof imports PF26 section 4, Lemmas 4.1–4.4, Corollary 4.5 and Proposition 4.6 for the odd splitter. The full original input already names the recent manuscript. Only the leading 'neither' needs four-way relabelling: it excludes A/M but does not mean no outside preprint.",
    "AG-DP-EGS": "Theorem 1.1 and Corollary 1.2 of EGS are substantive imported premises, not a comparison target. 'Neither A nor M' remains correct but is incomplete as a four-way label.",
    "AG-FOURIER-ISOGENY": "Finite-flat push-pull and the isogeny annihilator are classical. The asserted very-general even-degree specialization additionally imports EGS; the class retains this full-scope branch.",
    "AG-LOCAL-EXCEPTION": "BKNO arXiv:2508.17776 is the refutation target, not a theorem premise. The filtered phi-module counterexample uses classical weak admissibility/Colmez–Fontaine and Bloch–Kato calculations.",
    "AG-DENINGER": "The cited arXiv:2504.15767 source is now published: Journal of Number Theory 286 (2026), 47–66, DOI 10.1016/j.jnt.2026.02.004. Retain its exact analytic assumptions; it is not an outside-preprint dependency in this dated audit.",
    "AG-K8": "The K8 theorem is published in JIMJ 25(1), 565–590 (online 24 November 2025), DOI 10.1017/S1474748025101394; the source also cites independent Kupers 2019 input. An arXiv/author PDF locator does not make a published theorem a preprint input.",
    "AG-K8-TWIST": "Uses AG-K8's published K-theory result and published comparison theorems; no A/M or unpublished theorem is needed.",
    "AG-SIGN": "A real analytic zero-free interval and sign normalization are explicit premises of the sign lemma. A/M applications supplying that interval are separate.",
    "AG-HEIGHT": "The supplied height identity, its normalization and analytic sign premises remain explicit. This implication does not construct the pairing or establish these premises from A/M.",
    "AG-SIGNED": "Full arithmetic application to an identified Hecke quotient uses M for real positive squared-zero support, and A suffices for covered Dirichlet quotients. The abstract signed-moment equivalence with a positive support supplied independently has class none. This distinction preserves the source input's actual quotient-divisor application.",
    "AG-DET": "The abstract entire-function determinant lemma is elementary once the critical-line zero hypothesis is supplied. The source explicitly applies it to covered Hecke/CM functions under M, and to real Dirichlet functions under A; the full arithmetic row is classified M.",
    "AG-MOMENT": "The positive-spectral moment lemma alone has class none. The row's actual Hecke/CM determinant application inherits M from AG-DET, with A sufficient in its Dirichlet specialization.",
    "AG-HANKEL": "The abstract Gram-matrix lemma alone has class none. The row's actual Hecke/CM determinant application inherits M from AG-DET, with A sufficient in its Dirichlet specialization. Infinite distinct positive support remains a hypothesis.",
    "AG-WEIGHT": "Formal unitary normalization and the expected shifted line are classified as none; establishing that line for a given L-function is a separate A/M application.",
    "AG-SCHEMES": "The statement is an exact factor/reduction and exceptional-fibre scope statement; it does not assert GRH for the remaining geometric factors.",
    "AG-ARTHUR-PARAM": "The local parameter and monodromy-block calculation is formal. Global zero-location applications require the separately specified rank-one A/M input.",
    "AG-MODEL": "The model-factor counterexample is unconditional; zero location for the related primitive cohomological factors is not needed to produce its extra vertical-line zeros.",
    "AG-COVER": "The concrete covering obstruction is unconditional; optional zero-location information on other factors is separate.",
    "AG-CENTRAL-FUNCTOR": "Central Artin holomorphy and the stated equivariant BSD/functorial conditions are residual premises; none does not assert that M proves them.",
    "CX-ALG-010": "The A-only scope reduction is asserted; a full general factoring theorem is not. Mention of newer algorithmic bounds does not make PF26 a premise of the displayed reduction.",
    "CX-ALG-017": "The finite-field implication takes the root of unity as supplied input. A constructs it in a separate inherited application.",
    "CX-ALG-024": "The exact smaller input is A plus RH for the displayed pure field, equivalently its order-r Kummer Hecke factor over Q(zeta_r). M is a sufficient source, not a necessary premise in its full universal strength.",
    "CX-ALG-025": "Exact premise A plus the finite bad-prime pure-field family; M supplies the latter conditionally. If the family is empty, specialize the class to A.",
    "CX-ALG-026": "Exact premise A plus the listed finite pure-field family; M supplies it conditionally. Preserve the unary/dense-output convention.",
    "CX-ALG-027": "Conjunction M (or the stated smaller Dedekind family) and PF26. Administrative precedence chooses M; it does not subsume the algebraic preprint.",
    "CX-ALG-028": "Conjunction PF26, A and the finite bad-prime pure-field RH family; M supplies that family. Empty bad set gives PF26+A, and the stronger supplied-field promise has no analytic input. See the separate MAS_ARTIN PF26 audit for proof corrections/acceptance.",
    "CX-GEO-014": "Both reductions and HN-completeness are unconditional. The separate AM membership corollary uses M via CX-GEO-012.",
    "CX-LIM-001": "A scope limitation, not a claimed algorithm under A/M; the extra hardness/algorithmic hypotheses remain unproved.",
    "CX-LIM-003": "An input-scope statement only. E is discussed as the separate premise of inherited ETH consequences; this row does not use E to establish a new bound.",
    "MT-ART02": "The criterion itself is unconditional; M confines subsequent tests to the critical line. That optional application is not the assertion being classified.",
    "MT-L02": "The zero-free/approximation equivalence is unconditional. M supplies one side for general Artin factors; A supplies the Dirichlet specialization.",
    "MT-M19": "Unconditional nuclear trace construction and equivalence. A/M imply the separately described positivity side, not the equivalence itself.",
    "MT-M20": "Unconditional equivalence: faithful positive full-jet completion iff GRH and simplicity. A/M alone do not supply simplicity or the claimed completion.",
    "MT-M23": "Multiple zeros and the obstruction to faithful full-jet positivity are unconditional. The same row's additional assertion of trace positivity under M retains M as full-scope class.",
    "MT-M25": "The arithmetic witness is constructed at any specified real part a. M is only used if one elects to specialize a to one half.",
    "MT-M26": "Wide containing-strip theorem and equivalence are unconditional. The row also asserts trace class on every positive-width centered strip under M, so its full advertised scope is M.",
    "MT-M27": "Wide-strip trace class and its positivity equivalence are unconditional. M only supplies the positivity specialization.",
    "MT-M30": "Compact test-class and full-jet trace identity use unconditional analytic estimates; A/M apply only to later positivity on convolution squares.",
    "MT-M36": "Measure obstruction and corrected normalization/lifts are unconditional; the proof's wide-strip trace-class instance is MT-M27. Invoking a positive-width narrow-strip instance requires the separate conditional MT-M28.",
    "MT-S507": "The cone and sharp order bounds are unconditional once pointwise rank-four holomorphy is supplied (Calegari in the indicated family). A/M are separately described restrictions on possible arithmetic realizations, not inputs to the cone calculation.",
    "MT-S508": "The exact central-comparison input is the single real-zero assertion R_B, weaker than universal M. Full GRH for B is an extra premise for the stated GRH conclusions. M is a sufficient source for full scope; the central equality is not established by assigning this class.",
}

FLAGS = {
    **{identifier: ("leading_A_weaker_than_full_scope", "MA-IN-001") for identifier in ("NT-Z13", "NT-Z15", "NT-Z16")},
    "AG-CYCLIC-DIV": ("leading_neither_means_no_A_M__PF26_already_named", "MA-IN-002"),
    "AG-DP-EGS": ("neither_means_no_A_or_M_only", "MA-IN-006"),
    "AG-FOURIER-ISOGENY": ("leading_neither_requires_EGS_specialization_label", "MA-IN-006"),
}

TARGETED_IDS = words("""
NT-Z03 NT-Z04 NT-Z06 NT-Z07 NT-Z10 NT-Z13 NT-Z14 NT-Z15 NT-Z16 NT-Z19
NT-L15 NT-L16 NT-L17 AG-CYCLIC-DIV AG-DP-EGS AG-FOURIER-ISOGENY
AG-LOCAL-EXCEPTION AG-SIGN AG-HEIGHT AG-SIGNED AG-WEIGHT AG-SCHEMES
AG-ARTHUR-PARAM AG-MODEL AG-COVER AG-CENTRAL-FUNCTOR AG-DENINGER
AG-K8 AG-K8-TWIST CX-ALG-010 CX-ALG-017 CX-ALG-023 CX-ALG-024 CX-ALG-025
CX-ALG-026 CX-ALG-027 CX-ALG-028 CX-GEO-014 CX-LIM-001 CX-LIM-003
MT-ART02 MT-L02 MT-M19 MT-M20 MT-M23 MT-M25 MT-M26 MT-M27 MT-M30
MT-M36 MT-S507 MT-S508
""")


def module_for(identifier):
    if identifier.startswith("NT-"):
        return GRH / "work/number_theory/section.tex"
    if identifier.startswith("AG-"):
        return GRH / "work/geometry_programme/section.tex"
    if identifier.startswith("CX-"):
        return GRH / "work/complexity/section.tex"
    return GRH / "work/root/section.tex"


def first_locator(path, identifier, aliases=()):
    identifiers = (identifier, *aliases)
    text = path.read_text(encoding="utf-8", errors="replace")
    matches = []
    for name in identifiers:
        for match in re.finditer(r"(?<![A-Za-z0-9-])" + re.escape(name) + r"(?![A-Za-z0-9]|-[A-Za-z0-9])", text):
            start = text.rfind("\n", 0, match.start()) + 1
            line = text[start:text.find("\n", match.end()) if "\n" in text[match.end():] else len(text)]
            heading = bool(re.search(r"\\(?:sub)*section|\\paragraph|^#{1,6} |\\begin\{(?:theorem|proposition|lemma|corollary)\}", line))
            matches.append((not heading, match.start(), name))
    if not matches:
        return ""
    _, position, name = min(matches)
    line_number = text.count("\n", 0, position) + 1
    return f"{path.relative_to(SOURCES)}:{line_number} [{name}]"


def grh_rows():
    originals = read_tsv(GRH / "CONSEQUENCES.tsv")
    assert len(originals) == 362
    ids = {row["id"] for row in originals}
    assert len(ids) == 362
    assert ids == set(ASSIGNMENTS), {"missing": sorted(ids-set(ASSIGNMENTS)), "extra": sorted(set(ASSIGNMENTS)-ids)}
    result = []
    for catalogue_line, row in enumerate(originals, 2):
        identifier = row["id"]
        outside = GRH_OUTSIDE.get(identifier, [])
        classification = ASSIGNMENTS[identifier]
        flag, finding = FLAGS.get(identifier, ("", ""))
        targeted = identifier in TARGETED_IDS
        other_classes = []
        if outside and classification != "outside preprint":
            other_classes.append("outside preprint")
        if identifier in {"CX-ALG-024", "CX-ALG-025", "CX-ALG-026", "CX-ALG-027", "CX-ALG-028", "NT-Z13", "NT-Z14", "NT-Z15", "NT-Z16", "AG-DET", "AG-MOMENT", "AG-HANKEL", "AG-SIGNED"}:
            other_classes.append("A (Dirichlet part; subsumed analytically by M)")
        result.append({
            "run": "GRH_NIGHT", "row_id": identifier, "input_class": classification,
            "other_four_way_inputs": "; ".join(other_classes),
            "outside_preprints": "; ".join(PREPRINTS[key]["name"] for key in outside),
            "outside_keys": ";".join(outside),
            "task_designated_outside": ";".join(key for key in outside if PREPRINTS[key]["designated"]),
            "statement": row["statement"], "stated_input": row["input"],
            "source_status": row["status"],
            "audit_status": "targeted dependency reading; no full-proof certification" if targeted else "source dependency statement carried; no full-proof recheck",
            "input_flag": flag, "audit_finding_id": finding,
            "evidence_locator": first_locator(module_for(identifier), identifier) or f"{GRH.name}/CONSEQUENCES.tsv:{catalogue_line} [{identifier}]; grouped classical proof reference in original_proof_locator",
            "original_proof_locator": row["where_the_proof_is"],
            "grothendieck_locator": row["where_it_lives"],
            "scope_basis": "every row of GRH_NIGHT CONSEQUENCES.tsv",
            "residual_notes": NOTES.get(identifier, "All additional hypotheses, classical literature and case restrictions in stated_input and original_proof_locator remain part of the proof. The four-way class does not replace those premises."),
        })
    return result


COLUMNS = ["run", "row_id", "input_class", "other_four_way_inputs", "outside_preprints", "outside_keys", "task_designated_outside", "statement", "stated_input", "source_status", "audit_status", "input_flag", "audit_finding_id", "evidence_locator", "original_proof_locator", "grothendieck_locator", "scope_basis", "residual_notes"]


def main():
    rows = grh_rows() + alp_rows() + cx_rows()
    keys = [(row["run"], row["row_id"]) for row in rows]
    assert len(keys) == len(set(keys)), "duplicate run/id"
    assert all(row["input_class"] in CLASSES for row in rows)
    assert all(row["evidence_locator"] for row in rows), "missing evidence locator"
    write_tsv(WORK / "INPUT_CLASSIFICATION.tsv", rows, COLUMNS)
    write_scope_register(rows)
    write_events(rows)
    report = {
        "date": DATE,
        "source_catalogue_sha256": hashlib.sha256((GRH / "CONSEQUENCES.tsv").read_bytes()).hexdigest(),
        "counts_by_run": dict(Counter(row["run"] for row in rows)),
        "counts_by_class": dict(Counter(row["input_class"] for row in rows)),
        "GRH_NIGHT_counts_by_class": dict(Counter(row["input_class"] for row in rows if row["run"] == "GRH_NIGHT")),
        "flagged": [{key: row[key] for key in ("run", "row_id", "input_class", "input_flag")} for row in rows if row["input_flag"]],
        "unique_run_id_pairs": len(set(keys)),
        "precedence": "M > outside preprint > A > none; administrative only, not logical implication or mathematical necessity",
        "proof_scope": "Coverage and integrity certificate; no claim of a new full proof check of every inherited theorem",
    }
    (WORK / "checks/input_coverage.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (WORK / "checks/input_preprint_register.json").write_text(json.dumps(PREPRINTS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("counts_by_run", "counts_by_class", "GRH_NIGHT_counts_by_class", "unique_run_id_pairs")}, ensure_ascii=False, indent=2))


# ALPOGE_BRIDGES and CX_GRH explicit manifests are defined below.
ALP_MANIFEST = {}


def alp_add(ids, classification, scope, outside=(), note=""):
    for identifier in ids:
        assert identifier not in ALP_MANIFEST, ("duplicate ALPOGE assignment", identifier)
        ALP_MANIFEST[identifier] = {
            "class": classification, "scope": scope,
            "outside": list(outside), "note": note,
        }


BASE_SCOPE = "INTAKE_ALPOGE_BRIDGES_cp03_20261121.md section 0: BR-AT-01 to BR-ANA-01 and CC-C01 to CC-F03b; conservatively includes the whole unchanged root_core/consequences_criteria finding block"
alp_add(words("BR-AT-01 BR-TR-01 BR-TR-02"), "A", BASE_SCOPE,
        note="The RH/Dirichlet-GRH application is actually asserted; the underlying determinant or factorization calculation alone is unconditional.")
alp_add(words("BR-MIX-01 BR-WM-01 BR-WM-02 BR-NODE-01 BR-DER-01 BR-DER-02 BR-ANA-01"), "none", BASE_SCOPE)
alp_add(seq("CC-C", 1, 8) | words("CC-F01 CC-F01b CC-F02 CC-F03b CC-F04 CC-F05") | seq("CC-P", 1, 6) | words("CC-P08 CC-P09"), "A", BASE_SCOPE,
        note="A supplies the exact rational Dirichlet factors or RH criterion asserted in the source. Preserve the source's support, model-factor, encoding and bad-prime restrictions.")
alp_add(words("CC-F01a CC-F03 CC-F06 CC-P07"), "none", BASE_SCOPE,
        note="A counterexample or exact scope obstruction is asserted; A/M are not needed to construct it.")

CP03 = "INTAKE_ALPOGE_BRIDGES_cp03_20261121.md sections 0–1 (explicit IDs or displayed range)"
PART4 = "INTAKE_ALPOGE_BRIDGES_20261121_part4.md sections 0–2 (explicit IDs or contextual shorthand range)"
alp_add(seq("BR-123", 1, 4) | seq("BR-66-", 1, 3) | seq("BR-134", 1, 6), "none", CP03)
alp_add({"F-SM-13"}, "A", "Prompt and INTAKE_GRH_NIGHT_20261121_part3.md: F-SM-13 numerical trace identity over Q",
        note="Numerical Q identity uses the adopted Dirichlet-GRH theorem. It is not a geometric construction of the narrow-strip intertwiner.")
alp_add(seq("F-SM-", 14, 31) | seq("F-SM-", 34, 44), "none", CP03 + "; " + PART4 + "; complete F-SM-13–44 source block retained to cover abbreviated ranges and cited final question rows",
        note="Classical/categorical arguments or explicit counterexamples; source hypotheses remain. The assignment does not certify the original Masullo infrastructure.")
alp_add(words("F-SM-32 F-SM-33"), "outside preprint", PART4 + "; F-SM-33 retained as the adjacent supporting refinement", outside=["RSW25"],
        note="Ramzi–Sosnilo–Winges Definition 2.5 and Theorem 2.6(1),(4), pp. 5–6, supplies preservation of coproducts through Dwyer–Kan localization. Author lists accepted JEMS; no issued publication was established.")

alp_add(seq("CC-AG", 1, 17), "outside preprint", CP03 + "; " + PART4 + "; contextual CC-AG abelian-sector group", outside=["VHS26"],
        note="Full abelian numerical-motive classification uses CC-TATE01/02: van Hoften–Sempliner Theorem I, p. 1, plus Milne 1999 Theorem 7.1 (p. 72) and Propositions 7.3–7.4 (pp. 73–75), and Milne 2002 Theorem 3.3. The latter are published conditional implications; the new CM Hodge input is retained.")
alp_add(seq("CC-XC", 1, 19), "outside preprint", CP03 + "; " + PART4 + "; explicit CC-XC01–04 and CC-XC05–23 ranges", outside=["VHS26"],
        note="The asserted arbitrary-abelian target/forward-cycle conclusion uses the all-abelian Tate input through CC-TATE01/02. Some necessity, descent or Schur-index subarguments are classical; the full asserted target-realization scope retains the preprint.")
alp_add(seq("CC-XC", 20, 22), "none", PART4,
        note="The source deliberately uses published Fu–Li supersingular Chow results and an explicit descent/correspondence argument. No all-abelian Tate preprint is needed for these limited classes.")
alp_add({"CC-XC23"}, "outside preprint", PART4, outside=["FHL26"],
        note="Fu–Huang–Li Theorem 1.9, p. 5, supplies the known-type Chow-motive input; retain excellent lifting, p>dim(X), and the stated Artin-invariant exclusions. Final source dependencies include Theorems 7.13 and 8.9, pp. 44 and 49, and Lemma 6.12, pp. 39–40.")
alp_add(words("CC-TATE01 CC-TATE02 CC-TATE04"), "outside preprint", PART4 + "; CC-TATE01–03 explicitly cited and adjacent CC-TATE04 scope retained", outside=["VHS26"],
        note="Milne Hexagon 2611.00244v1, Theorems 2.1 (p. 4), 3.1 (p. 6), 3.5 (p. 8), is cited as corroboration. The indispensable new theorem is van Hoften–Sempliner Theorem I; the implications are checked against Milne's published 1999/2002 papers.")
alp_add({"CC-TATE03"}, "outside preprint", PART4, outside=["MAD26", "VHS26"],
        note="Madapusi-contributed ChatGPT/Claude manuscript Theorem 1.1 (p. 1), Theorem 5.1 (pp. 11–12), Proposition A.1 (pp. 13–14), Corollary 6.2 (p. 13). Rationality uses MAD26; the simultaneous algebraic special-fibre cycle additionally uses VHS26. No general characteristic-zero Hodge algebraicity is inferred.")
alp_add({"CC-TATE05"}, "outside preprint", "Supporting named primary-source comparison in the same CC-TATE block", outside=["BROE26"],
        note="Broe Theorem 1.1 (p. 1), Corollary 1.2 (p. 2), final Sections 7–8 (pp. 17–20) is a narrower separate fourfold input, not the arbitrary-dimensional CM theorem.")

alp_add(words("BR-EFF01 AQ-RATIONAL-FIBRE"), "none", CP03 + "; contextual cote-15 effectivity and rational-fibre clauses",
        note="An equivalence or explicit rational neutralization obstruction; full Tate is an explicit condition, not silently supplied by A/M.")
alp_add(words("BR-EFF02 BR-EFF03 AQ-ABELIAN-RECOGNITION"), "outside preprint", CP03 + "; contextual cote-15 abelian effectivity/recognition clauses", outside=["VHS26"],
        note="The asserted abelian numerical-motive sector uses CC-TATE01/02. General-motive statements retain the full-Tate gate separately.")
alp_add(words("AQ-14-QUASIPROJECTIVE AQ-14-NONPROPER AQ-14-ALTERATION AQ-67-EXACT AQ-67-NONHOLO"), "none", CP03)
alp_add(words("AQ-136-STRICT AQ-136-SEMILOCAL AQ-136-COSPAN AQ-136-CONNECTED-SOURCES AQ-136-SEMILOCAL-SOURCES AQ-136-FIRST-SKELETON AQ-136-FREE-ZERO-FORMS AQ-136-HIGHER-COMPLETION AQ-136-MULTIPLICATIVE AQ-136-PD-OPERATIONS AQ-136-PD-RIGIDITY"), "none", PART4,
        note="The ring hypotheses and the distinction between strict common sources, connectedness and localization loops remain explicit. No connectedness theorem over Z is inferred.")
alp_add(words("BR-14-SEP BR-15-CLASSBOUND BR-15-SLOPEBOUND BR-15-ORBIT-RETRACT BR-15-QUADRIC-DISCRIMINANT BR-15-QUADRIC-TATE CC-RK03 CC-RK04 CC-APG04 CC-ST04 CC-RES01 CC-RES02"), "none", CP03 + "; " + PART4,
        note="Published geometric/category-theoretic input and explicit arguments. The 2026 Haine–Porta–Teyssier exodromy source is published in Journal of Topology 19(3), DOI 10.1112/topo.70091; it is not classified as an outside preprint merely because an arXiv version is cited.")
alp_add({"CC-WM01"}, "outside preprint", CP03, outside=["IZ26", "WEAR23"],
        note="The toric cases use published Scholze and Binda–Kato–Vezzani results. The hyper-Kähler branch uses Ito–Zou Theorem B (p. 2), Lemma 3.8 (p. 8), Theorem 4.4 (pp. 12–13). The abelian complete-intersection branch uses Wear Theorem 1.1.2 (p. 3), still listed as submitted on the author's page. Full scope retains both preprints.")
alp_add(words("CC-WM02 CC-WM03"), "outside preprint", CP03, outside=["PZ26"],
        note="Petrov–Zavyalov Theorem 1.2 (p. 2), Proposition 3.2 (p. 5), Theorem 5.1/Lemma 5.2 (p. 18), final proof pp. 25–26; preserve the weight-monodromy hypotheses in the formality transfer.")

ALP_SPECIAL = {
    "F-SM-14": "Weibel VI Corollary 8.3 and the classical Kummer/Brauer comparison are published inputs. The subsequent K8 example uses the published JIMJ theorem; no A/M input.",
    "F-SM-15": "The cited arXiv:2602.05090 theorem is now published as Chen, Lau, Lee, Ono and Zhang, Archiv der Mathematik 127 (2026), 165–178, DOI 10.1007/s00013-026-02261-y (2 July 2026). The density theorem and reflection remain substantive published inputs, so class none rather than outside preprint.",
    "F-SM-18": "Conditional on a supplied trace-class operator, the L1 trace-density/shell argument is functional analysis. This is not an assertion that the draft's claimed arithmetic trace-class premise has been proved; narrow-strip applicability remains separate.",
    "F-SM-19": "The printed section-indicator indentation is the refutation target; the singleton/atomless-measure obstruction uses no zero location.",
    "F-SM-20": "The corrected clopen fundamental domain and compact compression are measure-theoretic. No zero-location premise is used.",
    "F-SM-21": "The local/global trace mismatch is conditional on the exact trace identifications stated in the source. Its prime contribution follows from the explicit formula without locating zeros. This input audit does not certify the draft's global-to-local identification.",
    "F-SM-22": "The multiplicative Dirac replacement is noncompact by an explicit operator argument. No A/M input.",
    "F-SM-44": "The full proof is categorical scalar-duality/Yoneda-extension analysis; it does not invoke the RSW preprint used by F-SM-32. Monicity in every degree and degree-0/1 surjectivity retain their exact hypotheses.",
    "BR-15-CLASSBOUND": "The class-number obstruction is derived from classical Honda–Tate and ideal theory. Thakur arXiv:2001.00210 Proposition 2.9 is a refutation target, not a premise; no 2026 all-abelian Tate input is used.",
    "BR-15-SLOPEBOUND": "Honda–Tate local invariants and the degree/class-number bound are classical; no all-abelian Tate input is needed.",
    "BR-15-QUADRIC-TATE": "Uses the explicit quadric-discriminant geometry and published supersingular K3 Tate input for the specified class, not the arbitrary-abelian preprints.",
}

ALP_PROOF_READ = words("""
BR-AT-01 BR-MIX-01 BR-TR-01 BR-TR-02 BR-WM-01 BR-NODE-01
CC-F01 CC-F01b CC-F01a CC-F03 CC-F03b CC-F06 CC-P07
F-SM-13 F-SM-14 F-SM-15 F-SM-16 F-SM-18 F-SM-19 F-SM-20 F-SM-21 F-SM-22
F-SM-32 F-SM-33 F-SM-44 CC-TATE01 CC-TATE02 CC-TATE03 CC-TATE04 CC-TATE05
CC-AG14 CC-XC11 CC-XC13 CC-XC20 CC-XC21 CC-XC22 CC-XC23
BR-EFF01 BR-EFF02 BR-EFF03 BR-15-CLASSBOUND BR-15-SLOPEBOUND
BR-15-QUADRIC-DISCRIMINANT BR-15-QUADRIC-TATE CC-WM01 CC-WM02 CC-WM03
CC-RES01 CC-RES02
""")


def alias_ids(identifier):
    aliases = []
    if identifier.startswith("F-SM-"):
        aliases.append(identifier.replace("F-SM-", "F-SM"))
    return aliases


def alp_locator(identifier):
    candidates = []
    for path in sorted((ALP / "research").glob("*.tex")):
        locator = first_locator(path, identifier, alias_ids(identifier))
        if locator:
            # Prefer the actual heading in its modular source over a citation.
            line_no = int(locator.rsplit(":", 1)[1].split()[0])
            text = path.read_text(encoding="utf-8", errors="replace").splitlines()
            line = text[line_no-1]
            heading = bool(re.search(r"\\(?:sub)*section|\\paragraph|\\begin\{(?:theorem|proposition|lemma|corollary)\}", line))
            candidates.append((not heading, "unresolved" in path.name, str(path), locator, line.strip()))
    if not candidates:
        for path in sorted((ALP / "research").glob("*.md")):
            locator = first_locator(path, identifier, alias_ids(identifier))
            if locator:
                line_no = int(locator.rsplit(":", 1)[1].split()[0])
                line = path.read_text(encoding="utf-8", errors="replace").splitlines()[line_no-1]
                candidates.append((not line.startswith("#"), False, str(path), locator, line.strip()))
    assert candidates, ("no supplied source for manifest entry", identifier)
    *_, locator, title = min(candidates)
    return locator, title


def alp_rows():
    result = []
    for identifier, entry in sorted(ALP_MANIFEST.items()):
        locator, title = alp_locator(identifier)
        outside = entry["outside"]
        # 'none' in cp03's uses column excluded A/M, but its unconditional
        # prose also concealed the later named all-abelian Tate preprint.
        flag = ""
        finding = ""
        if identifier in seq("CC-AG", 1, 3) | seq("CC-XC", 1, 4):
            flag = "cp03_none_unconditional_overstates_external_input_status"
            finding = "MA-IN-003"
        elif identifier in {"CC-WM01", "CC-WM02", "CC-WM03", "F-SM-32"}:
            flag = "no_A_M_label_does_not_disclose_outside_preprint"
            finding = "MA-IN-006"
        result.append({
            "run": "ALPOGE_BRIDGES", "row_id": identifier, "input_class": entry["class"],
            "other_four_way_inputs": "",
            "outside_preprints": "; ".join(PREPRINTS[key]["name"] for key in outside),
            "outside_keys": ";".join(outside),
            "task_designated_outside": ";".join(key for key in outside if PREPRINTS[key]["designated"]),
            "statement": title,
            "stated_input": "See supplied modular statement and proof at evidence_locator; intake summaries are not a substitute for the full hypotheses.",
            "source_status": "inherited finding; publication and dependency status retained below",
            "audit_status": "targeted dependency reading; no full-proof certification" if identifier in ALP_PROOF_READ else "source assertion and dependency route carried; no full-proof recheck",
            "input_flag": flag, "audit_finding_id": finding,
            "evidence_locator": locator,
            "original_proof_locator": locator,
            "grothendieck_locator": "Exact archive/SGA locator remains in the source module; no invented scan attribution added.",
            "scope_basis": entry["scope"],
            "residual_notes": ALP_SPECIAL.get(identifier, entry["note"] or "No A/M or current unpublished theorem is required by the stated route; classical results and every ring/geometric/encoding hypothesis remain in the cited statement. This is an input audit, not a new full proof check."),
        })
    return result


CX_MANIFEST = {}


def cx_add(ids, classification, note="", outside=()):
    for identifier in ids:
        assert identifier not in CX_MANIFEST
        CX_MANIFEST[identifier] = {"class": classification, "note": note, "outside": list(outside)}


cx_add(words("CX-R01 CX-K01 CX-K02 CX-K05 CX-K06") | seq("CX-N", 5, 12) | {"CX-N15"}, "M",
       "The supplied intake identifies the exact Hecke/Dedekind family. M is sufficient; A applies only under the stated abelian-over-Q or Dirichlet specializations. Original CX_GRH proofs are not attached/resolved in this audit.")
cx_add({"CX-K03"} | seq("CX-N", 1, 4) | words("CX-N13 CX-N14"), "A",
       "A supplies the specific Dirichlet character input. Preserve supplied factorization/field data and stated prime divisibility restrictions. CX-N14 uses A only in branch (ii); branches (i),(iii) and its counterexample are unconditional.")
cx_add(words("CX-R02 CX-K04 CX-K07 CX-K08 CX-E06 CX-E07 CX-E08") | seq("CX-G", 1, 6), "none",
       "Counterexample, published result, geometric dictionary or scope statement. No new A/M/E-dependent algorithm is asserted by this row.")
cx_add(seq("CX-E", 1, 5), "outside preprint", outside=["E26"],
       note="The actual consequence invokes OpenAI's fixed-width SAT counting result E (Theorem 1.1 or Corollary 1.4). E is separate from A/M. The intake's later shorthand 'none' means no A/M, and is incomplete for the requested four-way classification.")


def cx_rows():
    path = SOURCES / "INTAKE_CX_GRH_20261121.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    result = []
    assert len(CX_MANIFEST) == 39
    for identifier, entry in sorted(CX_MANIFEST.items()):
        # Exact table row where present; compact dictionary range otherwise.
        matches = [(i+1, line) for i, line in enumerate(lines) if re.match(r"\|\s*" + re.escape(identifier) + r"\s*\|", line)]
        if matches:
            number, line = matches[0]
            fields = [field.strip() for field in line.strip().strip("|").split("|")]
            statement = fields[1]
            stated = fields[2] if len(fields) >= 4 else "dictionary; no analytic hypothesis"
            prior = fields[-1]
        else:
            # This is an explicit manual expansion of the intake's compound
            # CX-K08, CX-E07, CX-E08, CX-G01-G05 row.
            number, line = next((i+1, line) for i, line in enumerate(lines) if line.startswith("| CX-K08, CX-E07"))
            statement = "Geometric dictionary entry in the intake's compound row"
            stated = "none (dictionary)"
            prior = "statement level only in supplied intake; original statement not present"
        outside = entry["outside"]
        result.append({
            "run": "CX_GRH", "row_id": identifier, "input_class": entry["class"],
            "other_four_way_inputs": "A (abelian/Dirichlet specialization)" if identifier == "CX-R01" else "",
            "outside_preprints": "; ".join(PREPRINTS[key]["name"] for key in outside),
            "outside_keys": ";".join(outside),
            "task_designated_outside": ";".join(key for key in outside if PREPRINTS[key]["designated"]),
            "statement": statement, "stated_input": stated,
            "source_status": "Intake report: " + prior,
            "audit_status": "intake-only dependency classification; original CX_GRH proof not available/resolved; no proof recheck claimed",
            "input_flag": "intake_none_means_no_A_M_only_E_is_outside" if outside else "",
            "audit_finding_id": "MA-IN-006" if outside else "",
            "evidence_locator": f"{path.name}:{number} [{identifier}]",
            "original_proof_locator": "Original CX_GRH.tex not attached/resolved; predecessor proof-check report only",
            "grothendieck_locator": "Intake section 4.2: cited language-only archive locations carry no mathematical weight; no new archive attribution.",
            "scope_basis": "INTAKE_CX_GRH_20261121.md: all 39 findings; explicit range/dictionary expansion",
            "residual_notes": entry["note"],
        })
    return result


ALP_QUESTION_IDS = words("AQ-Q-134-SCOPE AQ-Q-14-F AQ-Q-SA08-CS AQ-Q-SA08-TL G-123-RANK-STRICT G-123-DISTINGUISHED R-MAS-KERNEL R-GTHAT R-KGROUP")
CX_GATES = seq("CX-U", 1, 6)


def canonical(identifier):
    return re.sub(r"^F-SM(\d+)$", r"F-SM-\1", identifier)


def explicit_tokens(text):
    # Numeric ranges are expanded separately in the explicit manifests above.
    return [(canonical(m.group()), m.start()) for m in re.finditer(r"(?<![A-Za-z0-9-])(?:F-SM-?\d{2}|(?:BR|CC|AQ|CX|G|R)-[A-Z0-9]+(?:-[A-Z0-9]+)*[a-z]?)(?![A-Za-z0-9-])", text)]


GROUP_TOKENS = {
    "BR-13401-06": seq("BR-134", 1, 6),
    "CC-AG": seq("CC-AG", 1, 17),
    "CC-AG01-03": seq("CC-AG", 1, 3),
    "CC-AG12-17": seq("CC-AG", 12, 17),
    "CC-RES01-02": seq("CC-RES", 1, 2),
    "CC-TATE": seq("CC-TATE", 1, 5),
    "CC-TATE01-03": seq("CC-TATE", 1, 3),
    "CC-WM01-03": seq("CC-WM", 1, 3),
    "CC-XC": seq("CC-XC", 1, 23),
    "CC-XC01-04": seq("CC-XC", 1, 4),
    "CC-XC05-23": seq("CC-XC", 5, 23),
    "CC-XC16-23": seq("CC-XC", 16, 23),
    "CX-ALG-016-018": seq("CX-ALG-", 16, 18, 3),
    "CX-ALG-023-026": seq("CX-ALG-", 23, 26, 3),
    "CX-ALG-024-026": seq("CX-ALG-", 24, 26, 3),
    "CX-G01-G05": seq("CX-G", 1, 5),
    "CX-N13-N15": seq("CX-N", 13, 15),
}


def write_scope_register(rows):
    by_id = {}
    for row in rows:
        by_id.setdefault(row["row_id"], []).append(row)
    register = []
    excluded = []
    for path in sorted(SOURCES.glob("INTAKE*.md")) + [SOURCES / "MASULLO_DEFECTS_20261121.md"]:
        content = path.read_text(encoding="utf-8")
        for identifier, position in explicit_tokens(content):
            line = content.count("\n", 0, position) + 1
            start = content.rfind("\n", 0, position) + 1
            end = content.find("\n", position)
            context = content[start:end if end >= 0 else len(content)].strip()
            if identifier in by_id:
                status = "classified finding"
                run = ";".join(row["run"] for row in by_id[identifier])
                reason = "See INPUT_CLASSIFICATION.tsv; range expansion is explicit in build_input_classification.py"
            elif identifier in GROUP_TOKENS:
                expanded = GROUP_TOKENS[identifier]
                assert expanded <= set(by_id), (identifier, sorted(expanded-set(by_id)))
                status = "range or family token expanded and covered"
                run = ";".join(sorted({row["run"] for name in expanded for row in by_id[name]}))
                reason = "Covered members: " + ";".join(sorted(expanded))
            elif identifier in CX_GATES:
                status = "question/gate, not a classified proved assertion"
                run = "CX_GRH"
                reason = "Exact gate evidence recorded in INPUT_UNCLASSIFIED_GATES.tsv; no four-way class invented for an unprovided statement"
            elif identifier in ALP_QUESTION_IDS:
                status = "question/current-gate row"
                run = "ALPOGE_BRIDGES"
                reason = "Question/current state copied to INPUT_UNCLASSIFIED_GATES.tsv; associated finding IDs classified separately"
            else:
                status = "contextual question, other-run ID, or non-finding citation"
                run = "outside requested finding scope"
                reason = "Context reviewed: CX-Q22/CX-Q39 here are GRH_NIGHT QUESTIONS.tsv rows, whereas task 4 requests its 362 CONSEQUENCES.tsv rows. No extra theorem assertion is silently classified from a question identifier."
                excluded.append(identifier)
            register.append({"cited_token": identifier, "intake_locator": f"{path.name}:{line}", "run": run, "scope_status": status, "context": context, "resolution": reason})
    # Add every range-expanded classified finding, even if it never appears as
    # a standalone token in prose (for example CC-XC06 within CC-XC05–23).
    literal_ids = {entry["cited_token"] for entry in register}
    for row in rows:
        if row["run"] != "GRH_NIGHT" and row["row_id"] not in literal_ids:
            register.append({"cited_token": row["row_id"], "intake_locator": row["scope_basis"], "run": row["run"], "scope_status": "range/context expansion or explicitly marked supporting block", "context": row["scope_basis"], "resolution": "Explicitly included and classified; see manifest"})
    write_tsv(WORK / "INPUT_CITED_SCOPE.tsv", register, ["cited_token", "intake_locator", "run", "scope_status", "context", "resolution"])
    questions = {row["id"]: row for row in read_tsv(ALP / "QUESTIONS.tsv")}
    gates = []
    for identifier in sorted(ALP_QUESTION_IDS):
        row = questions[identifier]
        gates.append({"run": "ALPOGE_BRIDGES", "row_id": identifier, "source_locator": f"{ALP.name}/QUESTIONS.tsv [{identifier}]", "status": row["state"], "current_gate_or_summary": row["finding_ids_or_gate"], "missing_information": "Not a theorem/finding row; exact reported current state retained. Its substantive associated findings are classified separately.", "input_class": "not assigned: question/gate"})
    for identifier in sorted(CX_GATES):
        summary = {
            "CX-U02": "A-only deterministic factoring gate: construct the maximal coefficient Teichmuller unit in the remaining non-split higher-valuation case; intake section 5.2 narrows it via CX-ALG-023–025 to the pure-field/Kummer family.",
            "CX-U03": "Mentioned as an unproved extension in the intake; later GRH_NIGHT intake discusses PF26 factoring transfer. Exact original gate wording not attached.",
            "CX-U05": "Mentioned as an unproved extension; later GRH_NIGHT intake discusses orbit/HN reductions. Exact original gate wording not attached.",
        }.get(identifier, "Only the collective CX-U01 to U06 gate citation is supplied; no individual statement is present.")
        gates.append({"run": "CX_GRH", "row_id": identifier, "source_locator": "INTAKE_CX_GRH_20261121.md sections 0, 1 (Unproved extensions), 5.2 for U02", "status": "unproved gate reported by intake; original return not available/resolved in this audit", "current_gate_or_summary": summary, "missing_information": "Original CX_GRH QUESTIONS.tsv/CX_GRH.tex row and its exact hypotheses are needed before assigning a theorem input class. No original proof was checked.", "input_class": "not assigned: question/gate"})
    write_tsv(WORK / "INPUT_UNCLASSIFIED_GATES.tsv", gates, ["run", "row_id", "source_locator", "status", "current_gate_or_summary", "missing_information", "input_class"])
    (WORK / "checks/input_context_tokens.json").write_text(json.dumps(sorted(set(excluded)), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


def write_events(rows):
    events = []
    for row in rows:
        targeted = row["audit_status"].startswith("targeted")
        events.append({
            "statement_id": f"{row['run']}:{row['row_id']}", "date": DATE, "who": WHO,
            "type": "targeted proof check" if targeted else "carried as background without fault found",
            "outcome": f"Input classification {row['input_class']}. {row['audit_status']}. Evidence: {row['evidence_locator']}. " + ("Flag: " + row["input_flag"] + ". " if row["input_flag"] else "") + "This event checks dependency attribution only and does not assert a whole-proof recheck.",
            "method": "Read the indicated dependency-bearing source passage and compared assertion scope" if targeted else "Carried the supplied theorem/dependency description; original proof not independently reread",
            "source_locator": row["evidence_locator"],
        })
    finding_checks = {
        "MA-IN-001": ("targeted proof check", "Whole documentary argument checked: NT-Z13/15/16 full Hecke scope requires the M branch; the full original input text already contains that branch, so only the leading A label is flagged.", "GRH_NIGHT NT-Z13/15/16; source input fields and number_theory/section.tex"),
        "MA-IN-002": ("targeted proof check", "Whole dependency argument checked: AG-CYCLIC-DIV imports PF26 odd-splitter results. PF26 agent separately confirmed full source reading in MA-PF-001; the input audit does not claim its own whole PF26 proof check.", "GRH_NIGHT AG-CYCLIC-DIV; PF26 section 4 pp. 13–19; MAS_ARTIN MA-PF-001"),
        "MA-IN-003": ("targeted proof check", "Whole provenance argument checked against CC-TATE01/02/03 and the cp03/part4 intakes; all-CM Hodge and rational-specialization manuscripts retained by name; old Milne implications distinguished from his 2026 corroborating note.", "ALPOGE_BRIDGES CC-TATE01–03; CC-AG01–03; CC-XC01–04"),
        "MA-IN-004": ("targeted proof check", "Whole classification-convention argument checked: administrative projection retains all conjuncts; formal equivalences and actual arithmetic applications are separated, including AG-DET/MOMENT/HANKEL/SIGNED versus MT-M19/20/27.", "modules/inputs.tex; original statements at per-row evidence locators"),
        "MA-IN-005": ("computation or formal certificate", "Coverage/integrity script passed: 362 exact GRH IDs and original fields; 162 ALPOGE findings; 39 CX findings; no duplicate run/ID; 126 numeric/range intake IDs and 22 contextual IDs covered; six CX gates separately recorded. This is a data certificate, not mathematical formal verification.", "checks/audit_input_classification.py; checks/input_independent_audit.json"),
        "MA-IN-006": ("targeted proof check", "Whole source-status/dependency argument checked; primary publisher/author/arXiv records distinguish actual preprints, published sources, refutation targets and optional corroboration. No cited outside theorem is claimed newly proved here.", "modules/inputs_source_status.tsv; modules/inputs_notes.md"),
        "MA-IN-007": ("targeted proof check", "Whole locator audit checked: public Remark p. 4 step 20 and predecessor's two Lean interface-file declarations. No Lean file/tree is present in this attachment, no new Lean build or scan is claimed.", "ALPOGE_BRIDGES research/source_and_masullo.md sections 1.1–1.2; https://alpo.ge/remark.pdf"),
    }
    for identifier, (kind, outcome, locator) in finding_checks.items():
        events.append({"statement_id": identifier, "date": DATE, "who": WHO, "type": kind, "outcome": outcome, "method": "Complete reading of the documentary proof and comparison with its cited evidence; independent data check where stated", "source_locator": locator})
    write_tsv(WORK / "modules/inputs_events.tsv", events, ["statement_id", "date", "who", "type", "outcome", "method", "source_locator"])


if __name__ == "__main__":
    main()
