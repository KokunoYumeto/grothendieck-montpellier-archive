"""Final manual alignment of check events to the stable claim IDs."""
from pathlib import Path
import re
S=Path(__file__).resolve().parents[1]
p=S/'code/event_records.py';t=p.read_text()
fix={
335:("U",'Original SGA7 XX4.1, printed355, proves vanishing of the rational cycle class under its four hypotheses; high degree does not remove the algebraic-inverse requirement.'),
336:("P",'Original XX5.1 gives a dimension inequality and a quotient of a subgroup of the Griffiths group. The reverse abstract embedding is noncanonical.'),
337:("P",'Compared the general positive-characteristic condition b with XX4.3 and Koblitz rank growth; the finite-field nonconiveau route is separately labelled and does not prove whole-space trace variation.'),
339:("U",'Original XX4.3 gives the characteristic-zero Hodge argument: high-degree sections have extreme vanishing Hodge types outside the curve-level pair.'),
342:("P",'The integrality theorem proves the necessary eigenvalue divisibility implication. Its converse would construct correspondences and is not proved by the cited numeric condition.'),
343:("P",'The whole-space trace assertion is explicitly unproved and then weakened by an invariant-subspace insertion; Katz and Koblitz establish different quantified results.'),
344:("I",'The trivial group on Fp^(p−1) realizes every invariant-subspace trace but only one whole-space trace; this also invalidates the deleted non-p-group consequence.'),
345:("P",'Chebotarev realizes conjugacy classes on a fixed representation. It cannot promote a trace on a chosen subrepresentation to the trace on the whole space required by corollary7.2.'),
346:("U",'Original XXII3.1–3.2 gives the proper finite-field coherent trace congruence using the q-power linear Frobenius.'),
347:("I",'Serre duality and Serre vanishing prove the negative-twist CM vanishing; the effective Cartier sequence gives the stated low-degree isomorphisms and injection.'),
348:("U",'Koblitz I§2 supplies cohomological flatness and base change on the proper-section open. A Frobenius-stable subbundle is only asserted after shrinking.'),
349:("I",'For finitely many finite-field linear Frobenius operators, a common power makes all nonzero eigenvalues one. Trace then equals stable rank, without assuming semisimplicity.')}
for n,(typ,out) in fix.items():
 t,count=re.subn(r'^'+str(n)+r':\(.*?\),$',f'{n}:({typ},{out!r}),',t,flags=re.M)
 assert count==1,(n,count)
t=t.replace("342:'Exact subspace trace sets", "344:'Exact subspace trace sets")
t=t.replace("for n,outcome in {\n266:","for n,outcome in {\n262:'Finite cone representatives for M=Z,G=Q/Z verify the written pair relation and n-torsion in three exact examples.',\n263:'The same finite examples have kernel cardinality n and quotient M/nM; the general exact proof remains separate.',\n268:'An upper-triangular filtered matrix has determinant one, illustrating the general filtration proof.',\n270:'The Artin–Schreier H0 term over Fp was computed for p=2,3,5,7; no alpha_p and Z/p conflation is made.',\n286:'Exact finite-field values of F−1 over Fp confirm the nonzero base-field cokernel.',\n290:'Finite symplectic pairings over Z/n are perfect for n=2,3,4; the transition powers are checked separately.',\n349:'Exact finite-field eigenvalue powers for p=3,5,7 are0 or1; the general common-power proof is in review.md.',\n266:")
p.write_text(t)
p=S/'code/a36_records.py';t=p.read_text()
t=t.replace('For a locally free module with p-linear endomorphism on a normal base, the Frobenius-fixed representation of a specialization appears as a subspace in the generic representation after a suitable open subgroup, with the same finite image action. Lemma7.5 applies this to a special-fibre characteristic polynomial.','The manuscript asserts that, for a locally free module with p-linear endomorphism on a normal base, the special Frobenius-fixed representation appears inside that at any generization t after an open subgroup, with the same finite image. Lemma7.5 applies the proposed mechanism to a characteristic polynomial.')
t=t.replace('The insertion is a subspace statement, not constancy of the whole generic representation. The purported proof is only a reduction to the integral henselian case.','The arbitrary-point assertion is false: C-SA13-355 gives the smooth-ambient nodal counterexample. C-SA13-363 proves the repaired statement when t is the generic point of a normal integral base. The final generic-point reduction does not preserve normality of an arbitrary specialization closure. The subspace insertion also differs from constancy of the whole representation.')
p.write_text(t)
print('Event IDs corrected against every actual A36 claim; Lemma7.8 item wording aligned.')
