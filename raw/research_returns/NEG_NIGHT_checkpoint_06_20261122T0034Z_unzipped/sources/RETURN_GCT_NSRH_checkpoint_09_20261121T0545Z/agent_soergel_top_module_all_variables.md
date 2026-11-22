# F59 continuation: the tensor-dimension theorem in every polynomial dimension

Author: `/root/rectangular_and_theta`, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This note extends the module input of `agent_soergel_top_module_gate.md` to any finite number of polynomial variables. It **uses a known theorem of Lichtenbaum** instead of attempting to extend the elementary two-variable projective-dimension argument. The earlier report remains frozen as an independent elementary proof in two variables. The complete descending-cohomology argument is a separate report by `/root/grothendieck_dictionary`.

## 1. The known theorem used, and primary-source status

Stephen Lichtenbaum, *On the vanishing of Tor in regular local rings*, Illinois Journal of Mathematics 10(2) (1966), 220--226, DOI `10.1215/ijm/1256055103`, Theorem 2, printed pp. 222--223, applies to a **complete unramified regular local ring B** and finite B-modules. The exact parts needed are:

- Part (2): when the relevant Tor modules have finite length, the higher Euler characteristic chi_i is nonnegative.
- Part (4): if chi_1 is zero and either module is torsion-free, Tor_1 is zero.
- Part (1): vanishing of a positive Tor forces all subsequent Tor modules to vanish.

We apply these statements only after completing a polynomial local ring and only with one module torsion-free. No unverified ramified case or general i=1 theorem is needed.

I read the original article's theorem and surrounding proof through the author's publicly uploaded full text:

https://www.researchgate.net/publication/247050802_On_the_vanishing_of_Tor_in_regular_local_rings

The primary extraction is saved as `primary_sources/Lichtenbaum_1966_primary_web_excerpt.txt`. It includes the theorem, its hypotheses and the proof context, with the original printed page break at p. 223. It is an actual web extraction, **not a downloaded or visually inspected PDF**.

For an independent primary-author cross-check, I read Mel Hochster's *Math 615 Lecture Notes, Winter 2012*, Supplementary Lecture of April 18, printed p. 169, Corollary (S. Lichtenbaum), case (1): when the completion is a power series ring over a field, chi_i is nonnegative and vanishes exactly when all Tor_j for j>=i vanish. The surrounding proof reduces to Koszul homology. The exact primary URL is

https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/10/615W12.pdf

The relevant primary extraction is `primary_sources/Hochster_2012_primary_web_excerpt.txt`. The web tool opened the PDF and its complete text; direct local download returned HTTP403, so no local PDF is claimed. The simpler proof below uses only the weaker original Theorem 2 and the torsion quotient argument.

Completion flatness and faithful flatness were separately read in Stacks Lemmas 10.97.2 and 10.97.3, tags `00MB` and `00MC`:

https://stacks.math.columbia.edu/tag/00MB

https://stacks.math.columbia.edu/tag/00MC

These standard theorems are cited, not reproved or claimed as new deductions.

## 2. All-variable tensor-dimension proposition

Let A=k[x_1,...,x_N] with each variable of positive degree, m=(x_1,...,x_N), and let V be a nonzero finite-dimensional graded right A-module. Let M be a finite graded left A-module of rank r over the fraction field of A. Then

`dim_k(V tensor_A M) >= r dim_k V`,                                      (AV1)

with equality if and only if M is graded free. For N=0 this is immediate over the field. Assume N>=1.

### Proof for a torsion-free module Q

Choose a minimal graded free resolution F of Q. It is finite: the N-variable Koszul complex resolves k and computes Tor_i(k,Q)=0 for i>N, while minimality identifies Tor_i(k,Q) with k tensor F_i. Thus F_i=0 for i>N. Let f_i be its finite free ranks. Exactness after passage to the fraction field gives

`sum_i (-1)^i f_i = rank_A Q = r`.

Since V has finite length at m, all modules V tensor F_i and their homology have finite k-dimension. Their Euler characteristic is

`chi_0^A(V,Q) = r dim_k V`.

It follows that

`dim_k(V tensor_A Q)-r dim_k V = chi_1^A(V,Q)`.                         (AV2)

Localize at m and complete. The completed ring is B=k[[x_1,...,x_N]], a complete equicharacteristic regular local ring. Write Q_hat=B tensor_A Q. A finite torsion-free module Q embeds in a finite free A-module: choose a basis over the fraction field and clear finitely many denominators of a finite generating set. Flatness of A_m->B preserves that injection, so Q_hat is torsion-free over the domain B.

The right module V is killed by some m^s, so its scalar extension to B is canonically the same finite-dimensional module. The completed finite free resolution B tensor F computes the same finite-dimensional tensor complex V tensor F. All its Tor lengths and Euler characteristics are therefore unchanged. Lichtenbaum Theorem 2(2) gives chi_1(V,Q)>=0.

Suppose equality holds in AV2. By Theorem 2(4), Tor_1^B(V,Q_hat)=0; by part (1), all positive Tor groups vanish. If Q were not graded free, its minimal resolution would have a last nonzero term F_t with t>=1. The completed resolution remains minimal. Its final differential has entries in the maximal ideal, and V has a nonzero socle. Consequently a copy of soc(V) in each generator of F_t lies in the kernel of the last differential of V tensor F. There is no incoming term beyond F_t. Hence Tor_t^B(V,Q_hat) is nonzero, a contradiction.

Thus Q is graded free if equality holds. A free Q plainly gives equality, and a nonfree torsion-free Q gives strict inequality.

### Arbitrary M, including torsion

Let T be the graded torsion submodule and Q=M/T. The quotient is finite graded torsion-free and has rank r. If Q is nonfree, the surjection V tensor M->V tensor Q and the strict torsion-free inequality prove strictness for M. If Q is free, M->Q splits as a graded left-module map. Thus

`V tensor M is isomorphic to (V tensor Q) direct sum (V tensor T)`.

When T is nonzero, V tensor T surjects onto `(V/Vm) tensor_k(T/mT)`, which is nonzero by graded Nakayama. Thus strictness also holds in this case. Equality holds precisely when T=0 and Q is graded free. This proves AV1. QED.

The only extra ingredient beyond the complete two-variable proof is the cited known Euler-characteristic rigidity theorem. In particular the argument does not misstate that a torsion-free module over a polynomial ring of arbitrary dimension has projective dimension at most one.

## 3. Exact application to top cohomology

All statements and arguments in Sections 3--4 of `agent_soergel_top_module_gate.md` now hold with A=k[x_1,...,x_N] and AV1 in place of TM-A:

1. If a nonzero finite graded bimodule M satisfies an actual module isomorphism `M tensor_A M ~= U tensor_k M`, with `dim U=rank_A M`, then taking V=k tensor_A M and applying AV1 forces M graded free on the left.
2. For a bounded bifree complex X with nonzero generic graph cohomology and an actual relation `X tensor_A^L X ~= C tensor_k X`, where C has nonzero cohomology, the highest global cohomology survives generic localization and is graded free on the left.

For the second assertion, the proof of nonzero M tensor M is unchanged: after the left-origin quotient it surjects onto the tensor product of the two nonzero origin generator spaces. Thus the global highest degree equals the highest degree of C. The generic graph relation gives the same highest degree and forces `dim H^top(C)=rank H^top(X)`. The module result then applies. This reasoning is valid in the actual ambient polynomial ring and needs no specialization of spectator variables or reduction to a smaller reflection subgroup.

If the generic support is e together with the simultaneous involution tau that changes the signs of two independent coordinates x,y and fixes the remaining coordinates, the already checked coprimality/graph-splitting lemma applies over k[x,y,z_1,...,z_{N-2}] exactly as written. Its coordinate coprimality is unaffected by the spectator polynomial variables. It makes the top cohomology graph-free on both sides when characteristic is not two.

The separate descending-cohomology proof must still be checked in full before concluding that every cohomology module is free. This note supplies the all-variable module input; it does not replace that proof with a generic K0 assertion.

## 4. Separate dictionary and check record

This application concerns actual finite modules, the exact tensor functor, finite free resolutions, and actual Tor groups. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 give the affine sheaf dictionary. SGA6 I Definition4.7 pp121--122 and Example4.8 p122 provide the perfect-complex language. AV2 is an Euler characteristic of an actual finite tensor complex; the equality case retains the positive Tor information through the cited rigidity theorem, rather than declaring an Euler-zero complex acyclic.

The effective grading and actual versus virtual coefficient conventions remain SGA3 I4.7.2--3/cote90 scan17 and SGA6 V Sections2--3/cote133 scan18. No archival statement is claimed to give the nonstandard canonical comparison.

I checked all theorem hypotheses against the primary contexts: the completed polynomial ring is complete and equicharacteristic, the completed quotient Q is torsion-free, V has finite length and unchanged residue field, every Tor has finite length, and the finite resolution has a final term whenever Q is nonfree. I checked the completion and Tor-identification steps separately, and retained the one-sided nature of the splitting M=Q direct sum T. The exact primary URLs and local retrieval status are recorded above. Independent full review is requested; no master file or shared log was edited.
