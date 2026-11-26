# -*- coding: utf-8 -*-
"""Node verdicts of VPVNP_INTEGRATION_20261124.md: what the two VP != VNP claims (Anthropic 23 Nov, OpenAI 24 Nov 2026,
both unchecked by any human) do to the nodes of JOINT_GCT_LEMMA_SPACE.tsv. Writes VPVNP_NODE_VERDICTS_20261124.tsv."""
import os
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'VPVNP_NODE_VERDICTS_20261124.tsv')
A = 'Anthropic thm 1.1 / thm 1.4 (approx) / Remark N.6 (dc, not formalized)'
O = 'OpenAI thm 1.1 (border, f_n) / cor 1.2 (perm, HC, border dc, orbit closure)'
B = 'both'
J = '<local>/pequalnp_work\\fleet_map\\JOINT_GCT_LEMMA_SPACE.tsv row '
V = [
    # fleet (swarm) GCT nodes
    ('L-gct-011', 'swarm', 'for every c >= 1 and m >= m0(c): paddedPerm C m (m^c) not in orbitClosure(detPoly C (m^c+1))', J + 'L-gct-011',
     'implied (claimed)', O + '; ' + A,
     'OpenAI cor 1.2 states the exclusion for m <= N <= exp(c (log m)^{5/4}) in characteristic 0, for padding by a new or an existing variable; Anthropic gives it through thm 1.4 and det circuits (Remark N.6, the one unformalized statement). Both need the converse of L-gct-006 (orbit closure gives a border determinantal expression), our PNP-SURVEY:converse-006.'),
    ('L-gct-026', 'swarm', 'exists c, m0: every border determinantal expression of perm_m (m >= m0) has size n with m^3 <= c n', J + 'L-gct-026',
     'implied (claimed), for large m', B, 'any superpolynomial border dc bound gives it: N >= exp(c (log m)^{5/4}) >= m^3 for m >= m0. The plan target is reached by a route the fleet does not use.'),
    ('L-gct-027', 'swarm', 'assembly: 023 + 024 + 025 imply 026 (checked, conditional)', J + 'L-gct-027', 'unchanged', B, 'its conclusion would hold independently of 025.'),
    ('L-gct-025', 'swarm', 'perm_{11k} restricts to a smooth form of degree >= k/3 in >= k^2/100 - 1 variables (k >= 128)', J + 'L-gct-025',
     'made moot (as a route)', B, 'the statement stays open; it is no longer needed for 026.'),
    ('L-gct-028', 'swarm', 'border dc(perm_m) >= m^2/2 + 1 for every m >= 3', J + 'L-gct-028', 'implied (claimed) for m >= m0 only', B,
     'the claims are asymptotic with an ineffective m0 (Anthropic) or unspecified constants (OpenAI); small m stay open.'),
    ('L-gct-009/010/015', 'swarm', 'dc and border dc of perm_m >= m^2/2 (MR, LMR); dc >= m^2/2 + 1 (m >= 3)', J + 'L-gct-009', 'unchanged; superseded asymptotically', B, 'checked statements; the claimed bounds are quasipolynomial.'),
    ('L-gct-064/070/072', 'swarm', '3n >= 2m^2 - 10m + 11 for exact and border expressions (m >= 3)', J + 'L-gct-070', 'unchanged; superseded asymptotically', B, 'explicit for every m >= 3, which the claims are not.'),
    ('L-gct-056/057/074', 'swarm', 'border dc(perm_m)/m^2 -> infinity', J + 'L-gct-074', 'unchanged; superseded (claimed)', B, 'the claims give exp(Omega((log m)^{4/3})) (Anthropic, through det circuits) and exp(Omega((log m)^{5/4})) (OpenAI).'),
    ('L-gct-024/029/045', 'swarm', 'smooth forms and power sums: (r-1)(d-1) <= 11 n', J + 'L-gct-024', 'unchanged', B, 'statements about polynomials in VP; VP != VNP says nothing about them.'),
    ('L-gct-035/069/077', 'swarm', 'subspace reductions; level spaces to border dc', J + 'L-gct-077', 'unchanged', B, 'their use for lower bounds is made moot asymptotically.'),
    ('L-gct-036/037', 'swarm', 'zeros of perm_m with no large linear space through them (m = 4: 6; all m: 2m - 2)', J + 'L-gct-037', 'made moot (as a route)', B, 'statements about the permanent hypersurface, unchanged and open; the bound they serve ((m-1)^2 + 1) is below the claimed ones for large m.'),
    ('L-gct-086', 'swarm', 'level spaces of perm at J have dim <= C n', J + 'L-gct-086', 'made moot (as a route)', B, 'via 077 it gives m^2 - O(m) only; as a statement about level spaces it is unchanged and open.'),
    ('level-space small cases (091, 179-217, 211, 116, 122)', 'swarm', 'exact small cases and symmetric classes of level spaces', J + 'L-gct-091', 'unchanged', B, 'combinatorial and algebraic statements; no payoff change beyond 086.'),
    ('L-gct-103/104', 'swarm', 'DIV hypotheses: signed sums of K powers of T-sparse integer polynomials divisible by (X+1)...(X+N) force N^25 <= T^27 (M = 3), N^5 <= T^6 (M = 4)', J + 'L-gct-103',
     'made moot (as a route)', B, 'the algebraic route to permanent lower bounds is no longer needed; the number-theoretic statements stay open.'),
    ('L-gct-006', 'swarm', 'a determinantal expression puts the padded permanent in the orbit closure of det', J + 'L-gct-006', 'unchanged; its converse is used', O,
     'OpenAI cor 1.2 proof: "the orbit consists of determinants of linear matrices and padding by a power of a new variable can be undone by specialization" (Paper.tex lines 101-105), the converse that the fleet lacks as a node.'),
    ('riffle rank (095-097, 124, 125, 139, 140, 218)', 'swarm', 'riffle rank of [a=b][c=d]', J + 'L-gct-139', 'unchanged', B, 'VP != VNP does not touch VBP versus VNC^1; Rossman C.2 was already negated by 097/218.'),
    ('L-gct-012/013/016-021', 'swarm', 'Hessian rank facts (MR)', J + 'L-gct-013', 'unchanged', B, ''),
    # ours
    ('WB-0002.001/.002/.003; GCT_FLIP:I.thm:main-collapse', 'ours', "GCT VI's RH, PH1 (det side) and OH fail for the padded permanent and det", J + 'WB-0002.001',
     'unchanged', B, 'the claims reach the separation the flip aimed at without the flip; our results remain statements about that route. No tension.'),
    ('GCT_FLIP:I.thm:new-variable-no-occurrence', 'ours', 'every representation occurring for the new-variable padded permanent occurs for det_m when m >= (n+1)^25, or n >= 5 and m >= n^25', J + 'GCT_FLIP:I.thm:new-variable-no-occurrence',
     'unchanged; sharpened in meaning', B, 'with the claims: in this range the separation holds while no occurrence obstruction witnesses it. Both papers cite BIP19 for this.'),
    ('GCT_FLIP:I.prop:general-padding-nonnormal', 'ours', 'fresh-variable padded orbit closures of forms without linear factors are not normal', J + 'GCT_FLIP:I.prop:general-padding-nonnormal', 'unchanged', B, ''),
    ('GCT_KRON:M-008; GCT_KRON:O-018; GCT_OBS:S-004', 'ours', 'at n >= m^c (c >= 6) no multiplicity obstruction with <= 2c + 1 rows; BIP-range row gates; their transfer to independent padding', J + 'GCT_KRON:M-008',
     'unchanged; sharpened in meaning', B, 'with the claims: the separation holds at n = m^c, but any multiplicity obstruction witnessing it has more than 2c + 1 rows.'),
    ('CUE_GCT:R-14; HEX:H14', 'ours', 'four-row multiplicity obstructions for the padded permanent exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17)', J + 'CUE_GCT:R-14',
     'unchanged; sharpened in meaning', B, 'with the claims: for n^2 > 2m^2 - m + 1 the separation holds without a four-row witness.'),
    ('GCT_KRON:A-030/A-034/O-030; GCT_SEPARATIONS:I.thm:full-family; CUE_GCT:R-12/R-13; HEX:H13', 'ours', 'explicit occurrence and multiplicity obstructions per_n against det_n, no padding', J + 'GCT_KRON:A-030',
     'unchanged', B, 'already implied separations (LMR); our certificates remain the only explicit representation-theoretic ones.'),
    ('GCT_SEPARATIONS:II.thm:finite-nonic; GCT_OBS:Q1a/Q1b/S-025/QC-019', 'ours', 'finite multiplicity obstruction at (8, 9); explicit obstructions asked at (8, 9) and (17, 23)', J + 'GCT_SEPARATIONS:II.thm:finite-nonic',
     'unchanged', B, 'fixed sizes; the claims are asymptotic and say nothing at m = 8 or 17.'),
    ('GCT_KRON:M-007; CUE_GCT:G-08; GCT_KRON:F-009; GCT_OBS:QC-014', 'ours', 'explicit determinantal containments of padded forms (sizes S(m,r), B(m,k), 2^m - 1; quaternary quartics at n >= 7)', J + 'GCT_KRON:M-007',
     'unchanged', B, 'upper bounds, consistent with the claims (all far above exp(c (log m)^{5/4}) for the permanent).'),
    ('CUE_GCT:ctx-G13', 'ours', '"the established quadratic lower bound border dc(per_m) >= m^2/2 of LMR"', J + 'CUE_GCT:ctx-G13', 'strengthened (claimed)', B, 'quasipolynomial if either claim holds.'),
    ('PNP-SURVEY:L011-c<=2; PNP-SURVEY:converse-006', 'ours', 'L-gct-011 for c <= 2 from the checked L-gct-074; the converse of L-gct-006', J + 'PNP-SURVEY:L011-c<=2',
     'strengthened (claimed: all c); converse used by both claims', B, 'c <= 2 remains the only case derived from Lean-checked inputs plus a short converse.'),
    ('PNP-CODEX:LS-sharp; PNP-MBR:A3; PNP-MAR:1.2', 'ours', 'LS(n) <= floor(n^2/3) + 2n - 2 and 3N + 10m >= 2m^2 + 14; quadratic and cubic layers', J + 'PNP-CODEX:LS-sharp', 'made moot (as lower bounds)', B, 'level-space statements unchanged.'),
    ('ALPOGE_GCT:B7.1/B7.2/B7.3 (prompt 23 bridges)', 'ours', 'a characteristic-zero orbit-closure separation survives outside an explicit finite set of primes; a fixed-degree rank criterion; bad-prime noncontainment need not lift', J + 'ALPOGE_GCT:B7.1',
     'unchanged; applies', O, "B7.1 transfers OpenAI's characteristic-zero orbit-closure exclusion to all but finitely many p for each fixed (m, N); in a fixed characteristic the circuit bounds give it directly (det has division-free polynomial circuits in every characteristic)."),
    ('ALPOGE_GCT:B4.1/B4.2/B5.1-B5.3 (prompt 23 bridges)', 'ours', 'limits of norm obstructions: scalar invariance, bounded-operator monotonicity, no uniform normalized rank gap', J + 'ALPOGE_GCT:B5.1',
     'unchanged; relates', A, "spectral points are the functionals that are monotone under all restrictions and multiplicative; they avoid B5.1's scalar problem (aT and T restrict to each other) and are the unbounded analogue of B5.2."),
    ('BR_PENCIL; BORDER_RANK thm:43/44/52; GCT_GINEQ F-01..F-24', 'ours', 'CP border rank of the det_4/per_4 coefficient tensors >= 43, 44, 52; image substitution; norm certificates', J + 'BORDER_RANK:thm:52',
     'unchanged; tools for the open hinge', B, 'lower-bound tools for asymptotic restrictions among wire networks (the hinge of both proofs); see section (b) of the integration.'),
    ('GCT_POS K-series; HEX:H02/H02b/H23/GPK08/GPK18; GCT_PLETH; GCT_NSRH; ALPOGE_GCT P-F*', 'ours', 'positivity hypotheses, Kronecker and plethysm coefficients, invariant theory of 3-tensors', J + 'GCT_POS:K-023',
     'unchanged', B, "moment polytopes give the quantum functionals, the only explicit spectral points over C besides flattening ranks; their prices are star metrics (integration, finding 3)."),
    ('meta, pcx, clb, lib, alg programmes', 'swarm', 'P vs NP side of the board', 'PROOF_GRAPH.tsv', 'unchanged', B, 'neither claim settles P vs NP or a Boolean separation.'),
]
with open(OUT, 'w', encoding='utf-8', newline='') as f:
    f.write('\t'.join(['node_id', 'side', 'statement', 'locator', 'verdict', 'via_claim', 'note']) + '\n')
    for r in V:
        f.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')
print(len(V), 'rows ->', OUT)
