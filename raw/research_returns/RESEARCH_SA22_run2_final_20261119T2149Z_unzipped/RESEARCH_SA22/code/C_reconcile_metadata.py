#!/usr/bin/env python3
"""Idempotent additions for the completed C/A2 contributions.

This preserves existing result rows, unlike the superseded initial generator.
"""
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WHO = "GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode"
DATE = "2026-11-19"


def main():
    path = ROOT / "C_results.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        rows = list(reader)
    updates = {
        "C.24": {"notes": "Injectivity part of A.2(b); exact image and all large-length limits proved in the following C_A2b_image.tex fragment."},
        "C.12": {"notes": "Scan044 asks a question rather than asserting bijectivity; both universal bijectivity answers are false. Four distinct obstructions are now illustrated, with further examples in C.35."},
        "C.17": {"notes": "Every printed axiom including kernel covariance retained. Literal existence allows empty fibers; full-cardinality exact-kernel existence is separately impossible on C3 (C.36)."},
    }
    for row in rows:
        row.update(updates.get(row["id"], {}))
    extra = [
        ["C.33", "Arbitrarily thin analytic boundary collars make canonical hyperbolic metrics incomparable pointwise on every compact stable bordered type", "Proved", "sections/C_A2e_collar.tex, label C:A2e-nonmonotonicity", "A:collar; Rupflin2021 Lemma2.9(ii); coercive Neumann estimates; Gauss-Bonnet", "67/021", "Exact unrestricted collar question settled; independent root audit passed. Explicit positive oscillatory width and frequency bound; no pseudodifferential or unproved shape-derivative assumption."],
        ["C.34", "Truncated polynomial base extension implies formal exponential bijectivity, including arbitrary internal Hom and infinite product functors", "Proved", "sections/part_C.tex, label C:functor-basechange", "Coefficient comparison over universal truncated polynomial rings", "68/043-044", "Ordinary polynomial base extension yields classification by natural pointwise locally nilpotent endomorphisms; global nilpotence restriction is stated exactly. Sufficient base-extension conditions are not claimed necessary."],
        ["C.35", "Formal actions can fail unipotence or, independently, parameter division even after scalar-linear square-zero logarithms", "Proved", "sections/part_C.tex, label C:functor-separate-obstructions", "C:functor-criterion", "68/044", "Regular translation on the free module on Nil(R) supplies nonunipotence; R direct_sum Nil(R) supplies a nonzero delta-cokernel class. Exact dual-number matrix certificate attached."],
        ["C.36", "On C3 the exact two-torsion kernel condition forbids every two-element generating set, hence full cardinality coverage", "Proved", "sections/part_C.tex, label C:C3-coverage-obstruction", "Chain and convolution axioms; exact kernel; three elementary convolution identities", "68/017-022", "Exhaustive 1728-system certificate:64 convolution-closed systems, none with a two-element generator. Does not contradict the printed degenerate finite existence classification."],
    ]
    by_id = {row["id"]: row for row in rows}
    for values in extra:
        row = dict(zip(fields, values))
        if row["id"] in by_id:
            by_id[row["id"]].update(row)
        else:
            rows.append(row)
            by_id[row["id"]] = row
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    events_path = ROOT / "C_CHECK_EVENTS.tsv"
    with events_path.open(newline="", encoding="utf-8") as stream:
        reader = csv.reader(stream, delimiter="\t")
        events = list(reader)
    checks = [
        ("C.33 / C:A2e-nonmonotonicity", "targeted proof check", "Official scan67/021 visually inspected; no equidistant hypothesis. Full nonlinear comparison, barriers, H1 response, explicit oscillatory energy estimate and opposite sign by area proved."),
        ("C.33 / C:A2e-nonmonotonicity", "independent targeted proof check by root", "Parent /root independently checked curvature sign with f=1, both barriers, pulled weak equation, H1 convergence, C_R estimate, reciprocity and Fourier bound, explicit frequency inequality, Gauss-Bonnet. Audit passed."),
        ("C_Rupflin2021 Lemma2.9(ii)", "source opened and exact scope checked", "Publisher original HTML and PDF opened. Eq2.22 pp3126-3127 allows arbitrary L2 boundary data; c=0 gives the exact geodesic-boundary operator. Web refs turn693361254view0/1 and turn686255032view0/1."),
        ("C.34 / C:functor-basechange", "targeted proof check", "Universal coefficient argument performed over every base R; iterated truncated polynomial rings justify two-variable group law. Internal Hom comparison uses only finite direct sums, not finite presentation."),
        ("C.35 / C:functor-separate-obstructions", "targeted proof check", "All module structures and semilinear transitions specified. Nil-shear has square-zero log linear in scalar but no parameter division; regular translation is not locally unipotent at a dual-number scalar."),
        ("C.35 / C:functor-separate-obstructions", "computation or formal certificate", "code/C_functor_obstructions.py; exact3x3 matrices and9 matrix units; separating functional vanishes on every epsilon-times matrix but equals1 on the logarithm; logs/C_functor_obstructions.json."),
        ("C.36 / C:C3-coverage-obstruction", "targeted proof check", "Root proposed C3 obstruction; child completed proof using the positive level-set property of a chain cone and h^3=e from exact kernel. Contradictory sets are {0} and its two-point complement in the identity chain."),
        ("C.36 / C:C3-coverage-obstruction", "computation or formal certificate", "code/C_C3_impossibility.py exhausts1728 systems;1216 contain two-point generators;64 are convolution closed;none of those64 contains a two-point generator. All three missing-point convolution identities checked. logs/C_C3_impossibility.json."),
        ("A:graph-radius-domain / A:graph-pi-one", "independent targeted proof check by child", "Audited B-copying for loops and external flags, fixed cusp faces, injective graph matrix, finite support gap, both parameter escapes, intrinsic radial homotopy and phase torsors. Fixed-normalization block diagonal; varying-moduli full differential block triangular."),
        ("C.25 / C:A2b-support", "definition precision audit", "Characteristic domains explicitly restricted to active punctured discs; no extra characteristic annuli; inactive marks have at most simple poles. This matches Liu Theorem3.4 exactly."),
        ("A:hinich-explicit", "independent computation or formal certificate", "code/C_plumbing_crossratio.py verifies11 exact rational assertions independently of the Kodaira-Spencer residue argument: full-domain global coordinate, distinct marks, simple critical point99/101, and nonzero derivative at0. Output logs/C_plumbing_crossratio.json; detailed domain audit notes/C_A1_comparison_audit.md."),
        ("A:EarleMarden-local / A:cap-plumbing-equation", "independent primary-source comparison audit", "Full Hubbard-Koch Appendix and Theorems9.11/10.1 opened and checked. Explicit opposite exponential end coordinates give zw=t with smoothing exponent1; normalization and normal-direction blocks give the germ isomorphism. Exact prompt does not name the2012 chapter; its lack of access remains a bibliographic limitation, not an undecided local comparison. notes/C_A1_comparison_audit.md."),
        ("EarleMarden2012 source retrieval", "archive and library retrieval audit", "Original chapter not obtained. OpenAlex has only closed DOI location; Crossref has no content link; both ISBNs and chapter-title Internet Archive searches empty; both HathiTrust ISBN lookups empty; tested Wayback author/Bonn paths give no snapshot. Two JSON logs and notes/C_EarleMarden_sourceaudit.md retain all routes without claiming an opened chapter."),
        ("B.3 / Gabber1994 and Fujiwara1995 original-source gate", "independent archive and repository retrieval audit", "Neither original opened. Exact ISTEX articles located, but both advertised PDF links redirect to RENATER authentication; exact Duke IA issue has access-restricted-item=true and private fulltext files. HAL exact-title queries empty; OpenAlex has no repository copy; official author/journal/preprint routes supply metadata only. Six actual-response JSON logs and notes/C_GabberFujiwara_sourceaudit.md retain the distinct attempts. The explicitly requested original-reading requirement remains unmet; modern proofs are unchanged."),
        ("A:polycurve-coarse-compactification", "independent targeted proof and primary-source audit", "PASS. Opened full Mochizuki author PDF and exact Thm3.3, Cor6.2, Cor7.4 and Section7 Remark1. Checked saturated-cover existence, automatic residue-characteristic-zero tameness, moved auxiliary constants, deck group law, normal projective invariant quotient, both common-cover comparisons, and return of an existing polystable compactification. notes/C_coarse_compactification_audit.md."),
        ("A:intrinsic-anabelian-compactification", "independent targeted proof check including nondominant maps", "PASS. Finite lifts extend by evaluating finite algebra sections on dense interiors and using integral closedness, without any function-field map from a nondominant target. Checked excellent noetherian test pairs, disconnected torsor normalization, quotient descent without flatness, intrinsic uniqueness and arbitrary-map functoriality. Suggested explicit integral-cover/normalization-action clarifications were implemented and re-read. notes/C_coarse_compactification_audit.md."),
        ("A:polycurve-coarse-compactification / SchmidtStix2016 Cor1.6", "independent exact-scope source check", "Opened local original PDF at Cor1.6 and preceding definition of outer augmentation-compatible maps. Arithmetic reconstruction is restricted to strongly hyperbolic Artin neighbourhoods over finitely generated extensions of Q, with geometric inner conjugation. No anabelian reconstruction theorem for all polycurves or coarse-boundary log regularity inferred."),
        ("B:nontorsion-rigidity / inverse-image structure sheaf", "independent targeted category and sheaf audit", "PASS. Proved E_g is canonically the henselization of B[1/g], hence B to E_g is ind-etale; checked strict-local stalk identification f^{-1}O_B=O_E, functorial closed-fibre square, and affine henselian H0 comparison. The identifications respect all restriction maps. No tensor-product pullback and no henselianity of an ordinary localization assumed. notes/C_subject21_sheaf_audit.md."),
        ("C:torsion-degree-two-reduction", "independent derivation and primary-source audit", "Opened full French SGA4III retypesetting XII6.5(iii),6.6,6.7,6.13 and Stacks09Z7,03SA,03Q5,09ZE. Derived equivalence of supported H2 vanishing, all-torsion H1 surjectivity, and extension of constant cyclic prime-power torsors on finite covers; finite-fp covers suffice. Explicit acyclic torsion embedding avoids preservation-of-injectives assumptions. notes/C_subject21_q2_reduction.tex; local source and fetch JSON retained."),
        ("C:torsion-degree-two-reduction", "independent targeted proof check by root", "PASS. Parent read complete draft and opened Stacks09Z7/03SA/03Q5,59.55.2-3 and SGA4XII6.5(iii)/6.6 with the original transfer proof. Verified divisibility of injective sections, acyclicity of the torsion part using qcqs colimits, the dimension shift and full H0/H1 chase. Integrated by B owner; B owns the result row. This is a certified reduction, not a proof of the general torsion assertion."),
        ("C:henselian-flat-trait-proper / C:henselian-trait-comparison / C:henselian-proper-closed-fibre", "targeted derivation and independent source audit", "Proposal by B agent completed and independently checked by C agent. Opened Stacks053U,00QK,02LS,0F41,0CT9. Proved flat separated finite-type universal-H0 pairs over henselian DVRs are proper; reduced generic-fibre closure plus a stalkwise closed-cover sequence removes flatness for torsion comparison. Proper closed fibre criterion proved separately. No excellence or completeness needed. notes/C_subject21_DVR.tex."),
        ("C:henselian-flat-trait-proper / C:henselian-trait-comparison / C:henselian-proper-closed-fibre", "independent targeted proof check by root", "PASS. Parent opened all six required Stacks sources and checked every proof step; B agent independently passed the written draft. B owner integrated all three labelled statements and owns their result rows. The arbitrary qcqs nonproper torsion problem remains unresolved."),
        ("C:henselian-affine-closed-fibre", "targeted derivation and independent primary-source audit", "PASS. Opened published AHHR2024 Theorem1.2 and its full Section3 proof (turn790072925view0, turn715755014view0). Applied to identity of affine closed Z; universal H0 produces a section into affine etale W, and the section is closed because W to X is separated. No PC/N/FC or original qc hypotheses. Affine Gabber then proves all torsion degrees. notes/C_subject21_affine_closed.tex; B owns the integrated result row."),
        ("C:henselian-affine-closed-fibre", "independent targeted proof check by root", "PASS. Parent opened the full published Cambridge Theorem1.2 and Section3 proof (turn679179655view0, turn413018108view0), and independently checked trivial stabilizers, the non-qc reduction, represented-sheaf restriction, separatedness from the absolute affine diagonal, the closed section and affine Gabber consequence."),
        ("C:Goldman-double-conditional", "conditional construction and obstruction audit", "PROVED CONDITIONAL ONLY. For a strictly henselian local domain with open generic point and a disconnected nonempty principal boundary open, proved universal H0 for the double using every finite cover and computed nonzero constant finite H1 on its boundary. No input ring constructed. Reciprocal-complement normalization locality is an explicit question in the opened 2025 primary source, so the example remains conditional. notes/C_subject21_Goldman_double.tex and C_subject21_Goldman_gate.md."),
        ("C:Goldman-double-conditional", "independent targeted proof check by root", "PASS FOR THE CONDITIONAL STATEMENT ONLY. Parent independently checked the full finite-clopen argument and both Mayer-Vietoris sequences, recording the audit in notes/ROOT_source_audits_checkpoint04.md. No ring meeting the construction hypothesis is asserted to exist; no torsion counterexample claimed."),
        ("C:Jacobson-localization-double-conditional", "independent targeted proof check by geometry agent", "PASS FOR THE CONDITIONAL STATEMENT ONLY. A567 independently verified integral contraction of maximal ideals for finite overlap algebras, the nonzero direct-factor contradiction, universal H0 by Hall-Rydh, and both Mayer-Vietoris calculations. It independently opened Stacks0GED and checked that no noetherian input can satisfy the displayed hypotheses. Actual ring existence remains unresolved."),
        ("C:Goldman-double-conditional / failed Jacobson-forcing attempts", "targeted algebraic obstruction check", "Proved that adjoining xy/(x+y)^n forces x/(x+y) integral and splits the 0/1 Hensel branches. Independently factored the completed unit-adjunction equation (b^N-xy)v-xy into (1+v)(x-br)(x-b(1-r)), with r(1-r)=b^(N-2)v/(1+v). Opened0GED and extended its obstruction to local integral extensions of noetherian rings. A567 supplied the separate zero-Jacobson-radical Laurent-series obstruction. notes/C_subject21_failed_Jacobson_constructions.md."),
        ("B:henselian-local-flat-proper", "independent targeted final-draft proof check", "PASS. C agent supplied the Krull-Akizuki removal of Nagata and checked the entire final B draft. Reopened09IG,04GH,0CT9,02L1 (turn428637183view0-3). Verified local henselian normalization without module finiteness, closed-point preservation under integral base change, trait properness, residue-field descent and proper-clopen elimination. No higher-dimensional horizontal-flatness assertion. notes/C_subject21_local_properness_audit.md; B owns insertion and result row."),
        ("C:Goldman-double-conditional / integral-extension obstruction", "independent targeted proof check by geometry agent", "PASS. A567 independently checked that a local integral extension A of a noetherian local ring has nil Jacobson radical after any principal localization by b in its maximal ideal, using finite local subalgebras, lying-over of maximal ideals and0GED. No domain hypothesis needed; no automatic extension to later localizations or henselizations. notes/C_subject21_failed_Jacobson_constructions.md."),
        ("C:local-curve-avoidance / C:henselian-horizontal-proper / C:henselian-noetherian-pair-comparison", "joint derivation and independent primary-source check", "PROVED restricted class. B proposed curve selection; C supplied the local noetherian Goldman lemma and an initial catenary proof; root removed catenarity and locality using0CT9. C independently checked the full strongest argument, reopening0F41,0CT9,01TI,0397,02LS and writing notes/C_subject21_noetherian_pair.tex. All separated finite-type schemes over noetherian henselian ring pairs with all closed points in the distinguished fibre satisfy torsion comparison. Arbitrary scheme pairs remain unresolved. B owns eventual result rows."),
        ("C:local-curve-avoidance / C:henselian-horizontal-proper / C:henselian-noetherian-pair-comparison", "independent targeted final-draft proof check by B agent", "PASS. B read the exact strongest draft and reopened0F41,0CT9,01TI,0397,02LS at17:51UTC. Checked local curve, clopen singleton, proper-component lift, non-quasi-finite locus, finite algebra Jacobson radical, local dimension1, finite proper union and all-degree closed-cover sequence. Source references turn351608357view0-2 and turn991970103view0-1."),
        ("C:local-curve-avoidance / C:henselian-horizontal-proper / C:henselian-noetherian-pair-comparison", "independent targeted final-draft proof check by root", "PASS. Parent read the exact arbitrary-pair version, checked finite irreducible components and the proper-complement argument over an arbitrary henselian pair, and authorized B integration. C's final Leray derivation explicitly avoids an unproved degree-zero premise for the proper horizontal union."),
        ("C:local-curve-avoidance / C:henselian-horizontal-proper / C:henselian-noetherian-pair-comparison", "independent targeted final-draft proof check by geometry agent", "PASS. A567 read the exact final version and opened0CT9,02LS,0F41,01TI,0397,09ZI,095T. Checked the entire strongest proof including proper base change plus affine Gabber and Leray without an H0(Y,YI) premise. Independent note notes/A567_noetherian_henselian_audit.md."),
        ("C:henselian-noetherian-closedpoint-criterion", "derivation and independent targeted proof check by B agent", "PASS. Universal H0 is equivalent to every closed point lying in XI for separated finite-type X over a noetherian henselian ring pair. Proved finite-cover clopen extension by proper horizontal decomposition,0CT9 and gluing across the closed cover; uniqueness by closed points. B independently passed the argument. Hall-Rydh5.4 gives all etale sets, without a separate arbitrary-sets proper base-change claim."),
    ]
    existing = {tuple(row) for row in events}
    for statement, event_type, outcome in checks:
        event = [statement, DATE, WHO, event_type, outcome]
        if tuple(event) not in existing:
            events.append(event)
            existing.add(tuple(event))
    with events_path.open("w", newline="", encoding="utf-8") as stream:
        csv.writer(stream, delimiter="\t").writerows(events)
    print(json.dumps({"result_rows": len(rows), "event_rows": len(events)-1,
                      "added_result_ids": [row[0] for row in extra]}, indent=2))


if __name__ == "__main__":
    main()
