# Finishes the intake of RESEARCH_SA08_C3_D031 (cp08) under the 50,000-token cap: scope, Part B citations and the
# corrected criteria B-003/B-004, Part A main results at statement level, closing sections, row table, check events.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 20 Nov 2026 (~21:15 UTC).
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents/results_register/horizontal/sweep3/SA08/'
F = D + 'INTAKE_RESEARCH_SA08_C3_D031_20261120.md'
T = D + 'INTAKE_RESEARCH_SA08_C3_D031_20261120_CHECK_EVENTS.tsv'
NEW = D + 'INTAKE_RESEARCH_SA08_C3_D031_20261120.new.md'
t = open(F, encoding='utf-8', newline='').read()


def repl(t, start, end, new):
    a = t.index(start); b = t.index(end, a)
    return t[:a] + new + t[b:]


SCOPE = '''- **Scope.** This is final, written on 20 Nov 2026 at about 21:15 UTC. The intake stopped under a 50,000-token cap set by
  the main session.
  - **Read in full and checked:**
    - B-001 (D-031), with its proof and its source: arXiv:2511.22614v4, §2.1, §3.5 Prop. 3.10 and its proof, and
      Theorem 3.15;
    - a search of the whole HTML text of v4 for citations of Prop. 3.10;
    - B-003 and B-004 (the corrected lifting criteria), with their proofs.
  - **Checked in part:**
    - B-006 and B-008 (the reach of D-031), against the source;
    - A-WF02 and A-L10, at the level of their printed statements, for the bridges (section 4).
  - **Statement level only**, from the register statement, the run status, the run's own check events and the report's
    outcome table: the other 107 rows. That is all of Part A, and B-002, B-005 and B-007.
  - **Not reached:**
    - the proofs of Part A, about 15,000 lines;
    - B-002, the free PD algebra with the extension bijection (B.4), on which the PD clauses of B-003 and B-004 rest;
    - the proofs of B-005 to B-008.
  - **Earlier intakes:** the sort (`SORTED/RESEARCH_SA08_C3_D031.tsv`, column earlier_intake) records none for any row
    of this run, so none is cited.

'''
t = repl(t, '- **Scope.**', '## 1. Verdicts', SCOPE)

COUNTS = '''**Counts:**
- 3 rows confirmed with their proofs read in full: B-001, B-003 and B-004;
- 2 rows confirmed in part (the reach of D-031): B-006 and B-008;
- 107 rows not read in full, at the level of the statement;
- no gap found and no row refuted, within that scope.

'''
t = repl(t, '**Counts:**', '**Part B: D-031 is confirmed.**', COUNTS)

PARTB = '''- **Citations of Prop. 3.10.** These were checked on 20 Nov 2026, about 20:4x UTC.
  - A search of the whole HTML text of v4 (characters 0-157,000, in two fetches) finds Prop. 3.10 only in its own
    statement and proof (§3.5). Its proof cites Theorem 3.9.
  - Nothing in §3.6 cites it, before Theorem 3.11 or after, and neither do the later sections or the introduction. The
    abstract speaks of "many lifting properties" of the resolution in general.
  - So within v4 no other result rests on Prop. 3.10. D-031 reaches that proposition alone, and Theorem 3.15 has its own
    proof.
- **The corrected criteria B-003 and B-004 are confirmed:** targeted proof checks of both proofs in full,
  `sections/B_lifting_audit.tex` l.265-382.
  - **Setting.** π is surjective on the ideals, X has projective terms, ρ: X → J is a chain map, and
    K = ker(J' → J).
  - **B-003.**
    - For any graded lift g, the defect dg − gd lands in K. It is a cocycle of Hom_k(X, K), and its class
      o(ρ, π) ∈ H^1 Hom_k(X, K) does not depend on g: changing g by h ∈ Hom^0(X, K) changes the defect by ∂h.
    - Chain lifts exist exactly when o(ρ, π) = 0. They then form a torsor under the degree-0 cocycles of Hom(X, K).
  - **B-004 (1).** X lifts every chain map through every degreewise surjection if and only if X is contractible.
    - Necessity: the cone C(X) → X, (a, b) ↦ a, is degreewise surjective. A chain section s of it gives the contraction
      p·h_C·s, since d(p h_C s) + (p h_C s)d = p(d_C h_C + h_C d_C)s = 1.
    - Sufficiency: for a contraction h and a graded lift g, ℓ = dgh + ghd = ∂(gh) is a cocycle, and qℓ = ρ(dh + hd) = ρ.
  - **B-004 (2).** X lifts through every surjective quasi-isomorphism if and only if X is K-projective.
    - Sufficiency: the kernel of such a map is acyclic, so the class (B.7) vanishes.
    - Necessity: for acyclic Y the cone map C(Y) → Y is a surjective quasi-isomorphism, so every map from X to every
      shift of Y is null-homotopic.
  - **The PD forms.** Necessity comes from the square-zero functor S(Y) = (k ⊕ Y, Y, γ_{>1} = 0), sufficiency from the
    extension bijection (B.4).
  - **Not checked:** (B.4), which is B-002, and the cited Stacks Project Lemma 13.19.4, the standard fact that a
    bounded-above complex of projectives is K-projective.
  - **What they are.** These are the standard lifting properties of complexes: contractible complexes of projectives
    against all surjections, and K-projective ones against surjective quasi-isomorphisms. Here they are proved for the
    PD dg algebras of the source, so they give the corrected Prop. 3.10.
  - **In the example of B-001,** K = kv in degree −1, and (B.7) is the class of ε ↦ v, which no degree-0 element of
    Hom(X, K) can kill.

'''
t = repl(t, '**Part A: C.3 is undecided at checkpoint 08.**', '**Part A: C.3 is undecided at checkpoint 08.**', PARTB)

MAINA = '''**Part A, the main results at the level of the statement** (with "used by n", the number of rows that rest on each):
- **A-SAT01 (used by 7).** Countable PD closure and based saturation inside the fixed rational algebra kill all H^1
  above one fixed cutoff. They extend every specified torsion-free target map, and fix simplex 1 when it is integrally
  exact.
- **AT16 (used by 6).** An actual K(2)-parameter coefficient-tail quadratic repair, with simultaneous target maps by
  Ext^2(L/mL, S) = 0, a rational contraction, and a torsion-free quotient that leaves simplices 0 and 1 unchanged.
- **A-S09-24 (used by 5).** For each fixed d, both integral questions reduce to the proper full subcategory C^[d], with
  the free first skeleton and the coefficient comparison through d, by weight-tail functors and finite-word localization
  equivalences.
- **AT01 (used by 5).** The pure completed arithmetic sequence and its exact graded coefficient extension.
- **A-S09-27 (used by 4).** For each fixed d, the common-source assertion is equivalent to internal common sources in
  the proper full subcategory E^[d], with one common P(N).
- **A-004 to A-006 (A-004 used by 3).** Every admissible theory has an actual admissible replacement with a prescribed
  common free first skeleton, functorially (the functor R and natural transformations).
- **A-S09-09 and A-S09-12.** The cellular free simplicial PD resolution of S/I_2 has special cotangent π_2 elements of
  exact order p in weight 2p for every odd p; its weight-6 π_2 is Z/3. For every N ≥ 2, every p > 3(N−1) and every
  k ≥ 1, there are nonzero p-local classes in degree 2k−1 and weight p^k.
- **A-P01, A-L20, A-L21.** Exact order-p classes surviving every based saturation, at every prime, each with an actual
  next repair.
- **A-WF01 and A-WF02.** The de Rham-Witt completion kills the positive-weight coefficients (section 4).
- **The two gates.**
  - **A-S09-29:** common sources over Z are equivalent to common sources for countable sources and targets internal to
    E_ω^[d]. These keep the single-disk first skeleton, global comparison through d, and rows through d+2 exact from the
    cutoff; the target pair can share N.
  - **A-S09-30:** terminal localization over Z is equivalent to terminality in the all-arrow localization of
    F_3,ω^[d], whose countable objects have one, two or three first-skeleton disks per weight, global comparison through
    d, and one common row cutoff.
  - **What is open:** both gate assertions themselves (A-CS, A-TL), and the application of SA09's structures (A-SA09).

'''
t = repl(t, '**Row by row:**', '**Row by row:**', MAINA)

t = repl(t, '  - The corrected criteria B-003 and B-004 have the form', '- **Against our own results.**',
         '''  - The corrected criteria B-003 and B-004 are checked (section 1). As statements about complexes they are the
    standard lifting properties: contractible complexes of projectives against all surjections, and K-projective ones
    against surjective quasi-isomorphisms. What is new is their PD form for the algebras of the source, which is the
    corrected Prop. 3.10. Prop. 3.10 itself is used nowhere else in v4.
''')
t = t.replace('  - The corrected criteria B-003 and B-004 should be checked before a note states them.',
              '  - B-003 and B-004 are checked, except for the extension bijection (B.4) of B-002. A note can therefore also\n'
              '    state the corrected criterion: a chain lift exists exactly when the class (B.7) in H^1 Hom(X, ker) vanishes.\n'
              '    The lift exists universally for contractible X (all maps surjective on the ideals), and for K-projective X\n'
              '    (surjective quasi-isomorphisms).')
t = t.replace('- **Part B is finished.** Drop it. B-003 and B-004 need one check by a reader or an intake before any note to the\n'
              '  authors cites them.',
              '- **Part B is finished.** This intake checked B-001, B-003 and B-004, and found that no other result of v4 cites\n'
              '  Prop. 3.10. Drop Part B. Before a note to the authors cites B-003 and B-004, read B-002 once.')
V = 'confirmed: targeted proof check of the proof in full (section 1); (B.4) of B-002 and the Stacks locator not opened'
lines = t.split('\n')
for k, L in enumerate(lines):
    if L.startswith('| B-003 |') or L.startswith('| B-004 |'):
        cells = L.split(' | ')
        cells[-1] = V + ' |'
        lines[k] = ' | '.join(cells)
t = '\n'.join(lines)
open(F, 'w', encoding='utf-8', newline='').write(t)

W = 'Claude Opus 5.5 at effort max, agent a34c04448e8299803, intake of RESEARCH_SA08_C3_D031 checkpoint 08 (GPT-6 Astra, ChatGPT Pro mode)'
rows = [
    ('B-001, B-006, B-008 (citations of Prop. 3.10)', 'targeted proof check',
     'confirmed against the source: the whole HTML text of arXiv:2511.22614v4 (two fetches, characters 0-157,000) cites Prop. 3.10 only in its own statement and proof (Section 3.5, whose proof cites Thm 3.9); no citation in Section 3.6 before or after Thm 3.11, in later sections or in the introduction. D-031 reaches Prop. 3.10 alone.'),
    ('B-003', 'targeted proof check',
     'confirmed. Proof read in full (sections/B_lifting_audit.tex l.276-306): the defect dg - gd of a graded lift lands in K = ker(J -> J) and is a cocycle; its class in H^1 Hom(X,K) is independent of g; chain lifts exist iff it vanishes and form a torsor under Z^0 Hom(X,K). The PD clause rests on the extension bijection (B.4) of B-002, not checked.'),
    ('B-004', 'targeted proof check',
     'confirmed. Proof read in full (l.308-382): (1) contractible iff lifting through all degreewise surjections (cone C(X) -> X and the contraction p h_C s; conversely l = d g h + g h d); (2) K-projective iff lifting through surjective quasi-isomorphisms (acyclic kernel; cone of an acyclic Y). PD forms by the square-zero functor and (B.4). Not checked: (B.4) and the Stacks Project Lemma 13.19.4 (standard).'),
]
with open(T, 'a', encoding='utf-8', newline='') as f:
    for sid, typ, out in rows:
        f.write('\t'.join([sid, '2026-11-20', W, typ, out]) + '\n')
if os.path.exists(NEW):
    os.remove(NEW); print('removed', NEW)
print('sections:', re.findall(r'^## .*$', t, re.M))
print('B-003/B-004 rows updated:', sum(1 for L in lines if L.startswith('| B-00') and V in L))
print('tsv columns:', sorted({len(L.split('\t')) for L in open(T, encoding='utf-8').read().splitlines()}))
