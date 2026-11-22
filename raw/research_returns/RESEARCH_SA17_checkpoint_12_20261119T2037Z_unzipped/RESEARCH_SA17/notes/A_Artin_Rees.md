# Conditional L1: Artin–Rees route, proof checked, full paper write-up next

Hypothesis: actual separated locally quasi-finite representations F over every S_s.

For R Noetherian, fixed finite C with presentation R^d/K, choose N with K intersect I^N R^d contained in IK. Any finite B to C inducing an isomorphism modulo I^N, after flat local base change with I in the maximal ideal, is an isomorphism: Nakayama gives surjectivity; choose fixed generator lifts, B=R^d/K', K' subset K; the mod-I^N isomorphism gives K subset K'+I^N R^d, hence K=K'+IK and K=K'. Flat base change preserves the kernel and intersection. For a direct summand C_j of C, add the complementary summand to B and use identity there.

Finite T/R: strictly henselian branches of T and local F-model are finite local; an etale branch map modulo I^N is an isomorphism because both residue fields are purely inseparable over the separably closed base field. The uniform module lemma reflects this isomorphism, hence etaleness before quotient.

For a closed irreducible stratum C in T with generic c etale over its local F-model, etale-localize S and shrink T so T is finite and the branch at c becomes an actual local isomorphism. Let I define closure of its base image. Apply8 to the irreducible open component Z of T modulo I^N after deleting the other components. Its generic point is c. Any nonempty8-open is dense in this component, so uniform reflection makes the original morphism etale along that open. Etale projection gives a dense open in C. Thus noetherian induction makes the E-locus constructible; its generization stability makes it open.

Spread local affine charts; E open lets them be made formally etale everywhere. For P=V times_F T, axioms1–4 and valuation uniqueness hold, and relative Artin-etale representability gives a separated etale scheme P over T. Limit preservation handles arbitrary non-Noetherian T by descent to finite presentation. Charts give an algebraic space locally quasi-finite over S. For affine chart pairs, the relation is separated etale with finite fibers. Stacks086R bounds degrees by finitely many generic degrees; Stacks07RY gives a finite stratification with finite locally free restrictions, so relation is quasi-compact. Stacks03KV plus6 gives separation. Stacks0417 gives a scheme, hence original M is open.

All module, branch, isolation, relation/quasi-compactness steps were targeted-checked by bt_crystals. Primary sources086R,07RY,03KV,0BB6 opened by root and checking agent. This is conditional only; it does not derive actual local representability from literal7.
