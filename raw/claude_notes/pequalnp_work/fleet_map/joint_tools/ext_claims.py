# -*- coding: utf-8 -*-
"""External claims added 24 Nov 2026: the two claimed proofs of VP != VNP (Anthropic, 23 Nov; OpenAI, 24 Nov 2026).
No human mathematician has checked either. Rows go to hand_rows.R with side 'external'; edges to edges.E.
See ..\\VPVNP_INTEGRATION_20261124.md."""
import hand_rows
import edges

AN = '<local>/AppData\\Local\\Temp\\claude\\f2c80a22394db22f\\329fb1e6-0570-47be-9060-a2a454bf3e15\\scratchpad\\anthropic_vpvnp\\'
OA = '<local>/AppData\\Local\\Temp\\claude\\f2c80a22394db22f\\329fb1e6-0570-47be-9060-a2a454bf3e15\\scratchpad\\oai_vpvnp\\'
ANU = 'https://github.com/anthropics/formal-math/tree/main/vp-vnp'
OAU = 'https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026'
ANS = ('claimed (Anthropic, by Claude, found by an internal research Claude model; posted 23 Nov 2026 about 21:00 UTC); '
       'no human check')
OAS = 'claimed (OpenAI, openai/math preprint; commit 24 Nov 2026 01:20 UTC); no human check'


def ext(id, statement, status, link, topics, title, notes='', attribution=''):
    hand_rows.R.append(dict(id=id, side='external', statement=statement, status=status, proof_link=link, topics=topics,
                            title=title, depends_on='', used_by='', notes=notes, source='statement: ' + link,
                            formal_statement='', attribution=attribution))


ext('EXT-ANTH:thm1.1', 'There is an absolute c > 0 and, for every characteristic p, an m0 such that over every field of '
    'characteristic p and for every m >= m0 every circuit for HC_m, and for PERM_m if p != 2, has more than '
    'm^(c (log m)^(1/3)) gates (variables and constants count as gates).',
    ANS + '; Lean (Statement.lean MainTheorem; axioms propext, Quot.sound, Classical.choice; CI with Comparator and nanoda)',
    ANU + ' ; local ' + AN + 'paper.pdf (Theorem 1.1, thm_allfields) and Statement.lean', 'border dc; obstructions',
    'VP != VNP over every field: main theorem', attribution='Anthropic (Claude)')
ext('EXT-ANTH:thm1.4', 'Theorem 1.1 holds for circuits over k((eps)) that approximate HC_m, respectively PERM_m (they compute '
    'f + eps g with g having coefficients in k[[eps]]); in particular VNP is not contained in the closure of VP over every field.',
    ANS + '; Lean (MainTheoremApprox, SeparationClosure)',
    ANU + ' ; local ' + AN + 'paper.pdf (Theorem 1.4, Definition 1.3, Appendix N)', 'border dc; obstructions; padding',
    'VNP not in the closure of VP', attribution='Anthropic (Claude)')
ext('EXT-ANTH:rmkN.6', 'Consequence of Theorem 1.4 for determinantal complexity: the permanent is not approximated by '
    'determinants of polynomial size (over C, the Mulmuley-Sohoni conjecture in the language of orbit closures).',
    ANS + '; the one numbered statement of the paper that is not formalized in Lean',
    ANU + ' ; local ' + AN + 'paper.pdf (Section 1.2, Remark N.6)', 'border dc; padding; obstructions',
    'Determinantal complexity consequence', attribution='Anthropic (Claude)')
ext('EXT-ANTH:thm2.2', 'Over every field at least one of two hypotheses (Definition 2.1) holds: contracting (for some n >= 2 every '
    'price on Mat_n(F_2) falls short of a Euclidean rectangle by a fixed factor in the mean squared distances of rank-n against '
    'rank-1 steps) or flat (for every finite subset of a Euclidean space and every eps > 0 some spectral point realizes its '
    'distances up to eps and scale). Which one holds is not known, even over R; mutual exclusivity is not shown.',
    ANS + '; Lean (thm_alt); which case holds is open',
    ANU + ' ; local ' + AN + 'paper.pdf (Definition 2.1, Theorem 2.2, Section 2.2)', 'border rank; border dc',
    'The flat/contracting dichotomy (open hinge)', attribution='Anthropic (Claude)',
    notes='Flat case: 2^(Omega((log m)^(4/3))) (thm_flat_rate); contracting case: 2^(Omega((log m)^2/log log m)) (thm_contracting).')
ext('EXT-OAI:thm1.1', 'Over every field, border circuits for f_n(Z) = sum_x c_x Z_{1,x_1}...Z_{n,x_n} (c_x counts accepting paths of '
    'a universal machine, at most n^1000 steps) require exp(Omega((log n)^(5/4))) gates, even measuring approximation in degree n only.',
    OAS + '; the Comparator challenge states only IsVP != IsVNP (exact classes, families in Fin n x Bool)',
    OAU + ' ; local ' + OA + 'Paper.tex (Theorem 1.1, lines 70-73)', 'border dc; obstructions',
    'VP and VNP are different: main theorem', attribution='OpenAI')
ext('EXT-OAI:cor1.2', 'The same bound in matrix order for directed HC and, in characteristic other than two, the permanent, and for '
    '(border) determinantal complexity; for all large m and m <= N <= exp(c (log m)^(5/4)), c small, the degree-N padded m x m '
    'permanent in characteristic zero is outside the determinant orbit closure.', OAS + '; not in the Lean challenge',
    OAU + ' ; local ' + OA + 'Paper.tex (Corollary 1.2, lines 83-106)', 'border dc; padding; obstructions',
    'Permanent, HC, border dc, orbit closure', attribution='OpenAI')
ext('EXT-OAI:thm1.3', 'If a strict shortening exists in the characteristic considered (possibly zero), then the border cost of f_n '
    'exceeds 2^(n^sigma) for some sigma > 0 and all large n.', OAS + '; not in the Lean challenge',
    OAU + ' ; local ' + OA + 'Paper.tex (Theorem stretch, lines 282-287)', 'border rank; border dc', 'Stretch theorem',
    attribution='OpenAI')
ext('EXT-OAI:def2.1', 'Strict shortening: in dimension D >= 2, C_{D,m} is the tensor of width-m cables on the D coordinate diameters '
    'of the Euclidean unit ball; a strict shortening is a finite sum identity for it over a field using A networks in the ball, each '
    'of cost at most w (width times length), with w + 2D log2 A < 2Dm. Whether one exists is not decided.',
    OAS + '; existence open', OAU + ' ; local ' + OA + 'Paper.tex (Definition, lines 203-211)', 'border rank; border dc',
    'Strict shortening (open hinge)', attribution='OpenAI',
    notes='Without a shortening: the direct proof of Section 2.1 (expander, hub displaced by b/sqrt d).')

edges.E += [
    ('EXT-OAI:cor1.2', 'improves', 'L-gct-011', '', 'claimed: the exclusion for m <= N <= exp(c (log m)^{5/4}) contains every c of L-gct-011, with either padding convention'),
    ('EXT-ANTH:rmkN.6', 'improves', 'L-gct-011', 'Remark N.6 is not formalized: write it with the converse of L-gct-006 and division-free det circuits', 'claimed, from Theorem 1.4'),
    ('EXT-OAI:cor1.2', 'improves', 'L-gct-026', '', 'claimed: a superpolynomial border bound gives m^3 <= c n for large m'),
    ('EXT-ANTH:rmkN.6', 'improves', 'L-gct-026', '', 'claimed quasipolynomial border dc'),
    ('EXT-OAI:cor1.2', 'improves', 'L-gct-028', '', 'claimed, for m >= m0 only'),
    ('EXT-OAI:cor1.2', 'improves', 'L-gct-074', '', 'claimed: exp(Omega((log m)^{5/4})) in place of R m^2'),
    ('EXT-ANTH:rmkN.6', 'improves', 'CUE_GCT:ctx-G13', '', 'claimed quasipolynomial border bound'),
    ('EXT-OAI:cor1.2', 'uses', 'PNP-SURVEY:converse-006', '', 'Paper.tex lines 101-105: the orbit consists of determinants of linear matrices; padding undone by specialization'),
    ('EXT-ANTH:thm1.4', 'parallel', 'GCT_FLIP:I.thm:new-variable-no-occurrence', '', 'separation without occurrence obstructions; both papers cite BIP19'),
    ('EXT-ANTH:thm1.4', 'parallel', 'GCT_KRON:M-008', '', 'if the claims hold, any multiplicity obstruction for n = m^c has more than 2c + 1 rows'),
    ('EXT-ANTH:thm1.4', 'parallel', 'CUE_GCT:R-14', '', 'if the claims hold, the separation holds beyond n^2 = 2m^2 - m + 1 without four-row witnesses'),
    ('EXT-OAI:cor1.2', 'parallel', 'ALPOGE_GCT:B7.1', '', 'B7.1 transfers a characteristic-zero orbit-closure exclusion to all but finitely many primes for each fixed (m, N)'),
    ('EXT-ANTH:thm1.4', 'parallel', 'WB-0002.003', '', 'the separation the flip aimed at, reached without the flip; WB-0002 stays a statement about the route'),
    ('EXT-ANTH:thm2.2', 'open_target_of', 'L-gct-011', 'decide which hypothesis holds; contracting or a strict shortening gives far stronger bounds (vpvnp_integration/PROMPT.md)', 'the shared open hinge of both proofs'),
    ('EXT-OAI:def2.1', 'open_target_of', 'L-gct-011', 'construct a strict shortening or prove that none exists (vpvnp_integration/PROMPT.md)', 'with Theorem 1.3 a shortening gives 2^{n^sigma}'),
    ('EXT-OAI:def2.1', 'parallel', 'BORDER_RANK:thm:52', 'border apolarity and Koszul certificates as lower-bound tools for identities among wire networks', 'tools for the hinge'),
    ('EXT-ANTH:thm2.2', 'parallel', 'GCT_POS:K-023', 'moment polytopes give the quantum functionals, whose prices are star metrics (integration, finding 3)', 'tools for the hinge'),
]
