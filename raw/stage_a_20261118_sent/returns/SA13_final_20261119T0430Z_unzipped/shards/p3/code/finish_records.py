"""Human-authored completion paragraphs and search records; no classification."""
from pathlib import Path
S=Path(__file__).resolve().parents[1]
p=S/'review.md'
s=p.read_text()
needle='### Coherent trace, stable ranks, and the dimension check'
insert='''### A counterexample to the arbitrary-point specialization lemma

The additional hypothesis in Lemma 7.8 matters independently of the trace gap. The assertion on A36-02, scan 36:026, global line 111 allows **any point t of a normal scheme S**, with s a specialization of t. Its proof at line 118 reduces to t generic in a normal integral henselian S. That reduction is invalid: the closure of an arbitrary point in a normal scheme need not be normal. This yields an explicit counterexample to the assertion as transcribed (C-SA13-355), and a precise repaired statement (C-SA13-363).

Work over k = F3 and take the smooth, integral, normal affine scheme S = Spec k[x,x⁻¹,y]. On the free rank-one module put the p-linear endomorphism F(v) = x v³. Since x is a unit, the semilinear map is invertible on every geometric fibre. Let C be the closed curve y² = x(x−2)², let t be its generic point, and let s = (2,0). The polynomial defining C is irreducible: x is not a square in k(x), and multiplying by the square (x−2)² does not change its square class. Thus C is integral, and s belongs to its closure, so t specializes to s exactly as required. At s its quadratic tangent cone is y²−2(x−2)², with two distinct conjugate branches over F9. It is an ordinary nonsplit node.

The parametrization x = u², y = u(u²−2) identifies k(C) with k(u), since u = y/(x−2) in the function field. The generic fixed vectors satisfy v = x v³, hence are 0 and ±1/u. They are already rational over k(t). The generic fixed representation is therefore the trivial one-dimensional F3 representation; restriction to any open subgroup remains trivial. At s the equation becomes v = 2v³. Its nonzero solutions satisfy v² = 2 and lie in F9. Arithmetic Frobenius sends v to v³ = 2v = −v, so the special representation has image C2. No subrepresentation of the trivial generic line can have that image, after any finite extension of k(t). The exact F9 and rational-function checks are executed in `code/specialization_counterexample.py`, with output retained in `outputs/specialization_counterexample.txt`.

Normalizing C makes the two geometric branches above the node into a closed point with residue field F9. Its residue extension kills precisely the special C2 action. Thus normalization does not repair the original quantifier while preserving the given special representation. Normality of the **ambient** S is fully satisfied in this counterexample and is not the missing assumption.

There is a valid generic-point repair, proved here as a reviewer refinement. Suppose S is normal, integral and noetherian, t is its generic point, s is any point, and V is a finite-rank locally free module with a p-linear endomorphism. The fixed scheme F(v)−v=0 is affine and étale: its Jacobian in the vector coordinates is −I. Over the henselization of the local ring at s, the open-and-closed part meeting the closed fibre is finite étale. It is a subgroup: addition and scalar multiplication preserve it because their domains are finite over the local base and every nonempty finite component meets the closed fibre. Its special fibre is the full special fixed representation. Finite étale schemes over a henselian local ring are equivalent to those over its residue field. Choose the finite connected splitting torsor for this representation, and descend both the finite subgroup and that torsor to an elementary étale neighbourhood of s. This is possible because the data are finitely presented. The neighbourhood is normal; connected finite étale covers of a normal integral scheme remain connected over its generic point. Its generic point gives a finite separable extension of k(t), and the descended splitting torsor proves that the image is exactly the special image, rather than an unspecified larger group. The finite subgroup supplies the required subrepresentation. The same repair applies within a normal integral closure of t only if its special residue data remain the data originally requested.

The opened primary sources are Stacks Lemma 41.20.5 (tag 0BTN), Lemma 10.153.7 (tag 04GK), and Lemma 37.41.6 (tag 02LP); their precise conclusions supply the finite-part decomposition, residue-field equivalence, and elementary étale neighbourhood. This proof verifies the generic-point case used at the end of the manuscript proof. It does not validate the preceding arbitrary-point statement, and no ink correction is made. [SGA7XXII; Stacks0BTN; Stacks04GK; Stacks02LP.]

'''
assert needle in s
if '### A counterexample to the arbitrary-point specialization lemma' not in s:
 s=s.replace(needle,insert+needle)
p.write_text(s)
p=S/'code/search_records.py';s=p.read_text()
extra='''a(10,'Frobenius fixed locus henselian finite etale part specialization normal generic point | site:stacks.math.columbia.edu henselian etale finite part closed fibre | specialization subrepresentation normal scheme arbitrary point',
  'Opened Stacks0BTN,04GK,02LP and read their hypotheses. An explicit smooth normal ambient scheme and an integral nodal specialization refute arbitrary-point Lemma7.8. Independently proved the normal integral generic-point repair using the finite fixed subgroup and its splitting torsor.',
  'SGA7XXII;Stacks0BTN;Stacks04GK;Stacks02LP','The counterexample is a reviewer construction, not a found historical publication. Normalizing the closure changes the special residue field; the original image condition is therefore not preserved.')
records.append(dict(search_id='P3-R01',date='2026-11-19',queries='Zarhin Tate conjecture endomorphisms characteristic2 Mori Moret Bailly XII2.5 | homomorphism abelian schemes normal base extends | Gajda Petersen Tate homomorphisms finitely generated fields',platform='Web engines; arXiv; MathNet; Numdam original; Algebraic Geometry original journal',result='Opened Zarhin2011 history and references, the Zarhin1975 and1976 primary bibliographic records, Moret-Bailly1985 original XII0.1 and2.4–2.5 pp239,244–245, Gajda–Petersen Theorem2.3 and Lemma3.4, and ACV2023 Proposition4.5(ii). Moret-Bailly explicitly calls the characteristic2 Mori result unpublished there. Saved root_lie_audit.md with the exact Tate and normal-base scope.',opened_references='Zarhin2011Geometric;Zarhin1975Endomorphisms;Zarhin1976Abelian;MoretBailly1985;GajdaPetersen2023;AchterCasalainaVial2023',limits='Root claims C-SA13-652 and associated K34:198–199 records own the final Tate classification. No invented Mori publication year; no integral p-adic Tate theorem inferred.'))

'''
if "a(10,'Frobenius" not in s: s=s.replace('\ndef save():','\n'+extra+'def save():')
p.write_text(s)
p=S/'code/a36_records.py';s=p.read_text();s=s.replace("['Koblitz1975'],['P3-A08'],computation='computations.py degree2,3,4", "['SGA7XXI','Koblitz1975'],['P3-A08'],computation='computations.py degree2,3,4")
p.write_text(s)
print('Specialization audit and search evidence saved.')
