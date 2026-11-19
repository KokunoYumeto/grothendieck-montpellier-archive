#!/usr/bin/env python3
"""Codex-only continuations: no synthetic NOTES_INDEX verdict rows."""
import build_root_early
b=build_root_early.b
def add(n,kind,scans,ranges,words,statement,reconstruction,reason):
 sid=f'SA06-{n}'
 b.items.append(dict(id=sid,sources=[],kind=kind,cote='15',scans=scans,lines={'file':'SA06_texts/codex/K15-08_transcription.tex','ranges':ranges},his_words=words,statement=statement,reconstruction=reconstruction,check='agrees',check_reason=reason))
 b.events.append(dict(statement_id=sid,date=b.DATE,who=b.RUN,type='used and rechecked in this run',outcome='Read complete Codex-only passage and short notes; '+reason+' No NOTES_INDEX row is invented.'))
add(900,'self-flagged step',[195],[[3,20]],'provenant sans doute; deux filtrations',
 'For a characteristic-zero base dominating SpecZ, the page proposes ℓ-adic fibres with henselian origins and crystalline fibres at characteristic-p specializations. The Hodge filtration on the realization functor is distinguished from a motivic filtration.',
 'This continues the Pro191/193 comparison agenda. Existence of particular realization functors, smoothness and the coefficient group must precede any Lang argument.',
 'The tentative wording and the distinction between functor filtration and submotives are explicit; the continuation does not remove the earlier qualifications.')
add(901,'self-flagged step',[197],[[50,61]],'non nécessairement isomorphes; H²(Q_ℓ,G)',
 'Two characteristic-zero de Rham fibres or two rational trivializations are not declared canonically isomorphic. The comparison with ℓ-adic fibres is left doubtful even in degree-zero Artin-type examples; an obstruction is written in H²(Q_ℓ,G).',
 'Once both fibre functors are fixed, their isomorphism object is a G-torsor and its obstruction to a rational point lies in nonabelian H¹. H² concerns neutrality/existence of a banded gerbe. The written exponent is a scan alarm, not an emendation.',
 'The manuscript distinguishes noncanonical comparison from nonexistence, but the H² label needs a categorical-level check.')
add(902,'unproved claim',[199],[[85,111]],'ξ_Z⊗Z_ℓ; ξ_Z⊗C; conjugaison',
 'The Betti integral fibre at a complex point is compared after scalar extension with ℓ-adic and complex de Rham fibres. Complex conjugation relates the conjugate complex points involutively.',
 'For a concrete smooth projective variety, ordinary comparison theorems give these maps with their naturality; extending them to a conjectural motivic category requires specifying the equivalence relation and realization. An archimedean place and a chosen embedding remain different data.',
 'Both comparison arrows and the complex-conjugation operation are written. Their assumed geometric realization context is retained.')
add(903,'unproved claim',[201],[[139,158]],'τ; semi-linéaire; ne ... a priori',
 'At a real place, distinguish the integral Betti involution induced by geometric complex conjugation from semilinear conjugation of coefficients and the real de Rham structure. The page does not grant the entire fundamental group an action on the integral Betti lattice.',
 'The real involution may preserve the lattice even when a full profinite action is available only after ℓ-adic completion. No general integral action is reconstructed from the family of completions.',
 'The restrictions on the claimed action are explicit and agree with the continuation’s comparison diagrams.')
add(904,'self-flagged step',[203],[[182,214]],'τ=τ′τ″=τ″τ′; à vérifier',
 'The two semilinear conjugations transported through the Betti–de Rham comparison are proposed to commute, with product the geometric real involution. Compatibility with real Frobenius on ℓ-adic cohomology is also marked for verification.',
 'For a variety defined over R this follows from conjugation-equivariance of the comparison isomorphism. It does not identify either semilinear map alone with the linear real involution. The one-Tate-object period2πi gives a sign check.',
 'The equality and both verification requests were read; a conditional proof is recorded separately and the manuscript’s precise labels are preserved.')
add(905,'conjecture',[205],[[240,253]],'conjecture de Hodge; F^(p)∩f_∞F^(p)',
 'The page proposes to recover a motivic level/effectivity filtration from rational classes in an intersection of Hodge-type filtrations related by the real involution.',
 'An arbitrary rational intersection need not be a sub-Hodge structure. The later amended generalized Hodge conjecture instead compares geometric coniveau with the largest rational sub-Hodge structure of the required Hodge coniveau. The written indexing and role of f∞ are not silently normalized.',
 'This is a genuine open conjectural step on the page; it must not be equated with an unconditional Hodge decomposition or with the ordinary cycle-class conjecture in every degree.')
add(906,'other',[196],[[24,46]],'racines; rang; Cartan',
 'Reused Lie-algebra editorial notes discuss the dimension of root spaces, rank and reductions in a semisimple characteristic-zero proof.',
 'These are classical Lie statements and editing instructions, not new motivic constructions; missing numbered lemmas are not recreated from presumed later editions.',
 'The whole interleaved sheet was read independently of the surrounding motivic continuation.')
add(907,'other',[198],[[65,81]],'sl₂; dimension finie; caractéristique0',
 'The reused sheet requests finite-dimensionality and characteristic-zero hypotheses in an sl₂ argument and its use in Lie theory.',
 'Finite-dimensional characteristic-zero sl₂-module theory supplies the expected result. The exact missing theorem’s full statement is not recoverable from a bare editorial reference.',
 'The requested hypotheses are kept as authorial editing points rather than inferred universal theorems.')
add(908,'other',[200],[[115,135]],'sous-algèbres de Cartan; conjuguées',
 'The reused editorial list concerns Cartan subalgebras and their conjugacy in the characteristic-zero algebraic Lie-theory setting.',
 'Conjugacy over an algebraically closed field is distinguished from rational conjugacy over an arbitrary base. The notes do not establish the latter.',
 'The sheet is a separate review of Lie-text statements; no motivic-group conjugacy result is inferred.')
add(909,'other',[202],[[162,178]],'normalisateur; réguliers; caractéristique2',
 'The reused Lie sheet discusses Cartan normalizers, regular elements and zero-weight/nilpotent subalgebras, with an explicit characteristic-two sl₂ warning.',
 'The matrix algebra sl₂ in characteristic2 has central h=I and lower central dimensions3,1,0; it is nilpotent, so a characteristic-zero proof cannot be used unchanged.',
 'The warning has an exact elementary certificate. Other referenced propositions remain conditional on their unreproduced definitions.')
add(910,'other',[204],[[218,236]],'poids; somme; produit',
 'The reused page records weight-space behaviour under addition, tensor products and multiplication in Lie representations.',
 'For commuting semisimple operators, a product or tensor of weightα and weightβ has weightα+β by the derivation/diagonal action identity; a sum remains a weight vector only within a common weight space.',
 'The elementary identity is checked directly and is not interpreted as an identity of motivic weights without an actual grading.')
add(911,'self-flagged step',[206],[[257,283]],'Cartier; structures sur Z; trialité',
 'The final reused leaf is an editorial programme concerning integral forms, Cartier’s constructions and triality, with references whose full statements are absent.',
 'Chevalley integral forms and the D4 triality automorphism are established subjects, but no exact new integral theorem can be reconstructed from these headings alone.',
 'The live requests are retained in the problem index with classF where quantifiers or a referenced formula are missing.')

if __name__=='__main__':b.save()
