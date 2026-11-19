"""An explicit source question recovered in the final individual origin audit."""
from register_common import add, I, C

add(108,'Veronese embeddings and a fixed positive-dimensional linear space',[81],3283,3292,'false as stated','B',
'The author asks whether, after a degree-n Veronese with n≥2, the dual discriminant can no longer contain the family of all hyperplanes through a fixed positive-dimensional linear subspace C. No transversality or first-jet hypothesis on C is written. The unrestricted hope is false even for the degree2 embedding of a smooth projective plane in characteristic0.',
'The unrestricted question has a negative answer by the explicit pencil a x²+b y² constructed here. Stacks33.47.1 and33.47.3 distinguish smoothness away from a fixed base subscheme from the first-jet obstruction at its points. Wutz2016 Theorem1.2 gives a finite-field analogue with embedding-dimension restrictions, not an unrestricted fixed-linear-space theorem. No historical priority is claimed for this counterexample.',
'Stacks0FD4,Wutz2016',
'computations.py veronese_fixed_linear_space verifies q(p)=0 and all three partial derivatives vanish at p=[0:0:1] for q=a x²+b y². Proof: take k algebraically closed of characteristic0, f=id on P², and its degree2 Veronese v₂:P²→P⁵. The independent coordinate equations U_x²=U_y²=0 define C≅P³. Every hyperplane containing C pulls back to a nonzero member of that pencil, which is singular at p. The intersection C∩v₂(P²) has local ideal(x²,y²), so it is even finite, although nonreduced. For every degree n≥2 the analogous pencil a x^n+b y^n lies in the square of the maximal ideal at p and gives the same obstruction. All smoothness, irreducibility, projectivity and unramifiedness assumptions on X and f hold.',
refine='Veronese degree alone does not remove prescribed-base singularities. In a smooth ambient variety, a member containing p is smooth at p only when its local defining section has a nonzero first-order class. Smooth Bertini on the complement of a fixed base subscheme needs the generating/immersion hypotheses there; smoothness at the base requires additional local conditions.',
group='veronese_fixed_space')
I[-1]['kind']='conjecture'
for c in C[-2:]:
 c['source_status_detail']='A tentative authorial hope/question, not a proved source assertion; the negative answer is this run’s explicit counterexample.'
 c['fate_date']='Negative unrestricted answer checked19November2026 in this run. Wutz arXiv posted28November2016 and cites an earlier thesis result; earliest circulation and a journal edition were not independently verified.'

add(109,'The cancelled promise of the general divisor scheme',[112],4484,4494,'stated without proof','A',
'For a flat, locally finitely presented projective morphism X→S, the source promises a later proof that the functor of relative effective Cartier divisors on X is representable. This general functor is distinct from fixing the associated line bundle L and from the special projective-bundle formula.',
'Grothendieck’s Bourbaki232 Proposition4.1 (1962), printed152, is the exact projective-flat representability statement over a locally noetherian base: Div is an open subfunctor of Hilb. The arbitrary-base finite-presentation version uses noetherian approximation in addition. The deleted manuscript promise has no independently established date relative to this publication; classA records its own-publication counterpart without a claim of historical priority.',
'GrothPicard1962,GrothPicardErr1962,GrothHilbert1961,EGAIV3,Stacks056P',
'Targeted proof check: the opened original section4, printed150–152, explains the relative Cartier condition, arbitrary base change and the open immersion into Hilb, then invokes Hilbert-scheme existence. For a Hilbert family D⊂X_T, the non-Cartier locus is closed in the proper X_T; removing its image from T gives the required open parameter locus. The finite-presentation extension descends a projective flat model and the finite presentation of D to noetherian approximations; it is a modern extension, not a hypothesis silently attributed to the printed1962 proposition.',
group='general_divisor_scheme')
I[-1]['kind']='self-flagged step'
I[-1]['check_reason']+=' The entire promise is inside deletion wrappers. It remains an explicit historical deferred step, not a live conjecture or the fixed-L theorem.'
C[-1]['source_status_detail']='Explicit future-chapter promise inside a wholly cancelled passage; no proof of the general functor is supplied there.'
C[-1]['fate_date']='Bourbaki exposé232 delivered February1962; volume publication1962. Exact first circulation apart from that talk and the cancelled leaf’s relative date are unknown.'
