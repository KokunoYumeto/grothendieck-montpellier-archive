# Primary-source and numerical-data record

Access date: 2026-11-21 UTC. Agent `/root/g34_eightfolds`, GPT-6 Astra Pro, reasoning effort inherited/unexposed, run HODGE_DIVISION. Parent handles durable checkpoints.

## 1. Published orbifold GRR used in the proof

Hsian-Hua Tseng, *Orbifold quantum Riemann–Roch, Lefschetz and Serre*, Geometry & Topology **14** (2010), 1–81. DOI **10.2140/gt.2010.14.1**. Publisher PDF:

https://msp.org/gt/2010/14-1/gt-v14-n1-p01-p.pdf

Local `sources/Tseng2010.pdf`, 603541 bytes, SHA256 `1f1eee23763abd7a449de881b4b6e423902b17645ff0a5c6a2037f296f0c968d`.

Exact locators read:

- Remark 2.4.2, p. 19: the stack with sections to marking gerbes is their fiber product over the stack without sections.
- Section 2.4.4, pp. 19–20: node gerbes, the balanced local quotient, and their inertia order.
- Section 2.5.1, p. 21: weighted virtual class multiplies by the product of marking orders.
- Section 7.3, pp. 52–64: the main-stratum, marking, and node GRR derivation.
- Equation (7.3.6.1), pp. 60–61: Bernoulli marking term.
- Equation (7.3.7.2), p. 64: final GRR identity with the **r²** node factor and coarse cotangent classes.

Specialization in the new proof: X=BG, so TBG=0 and the virtual class is the actual class. Higher rational Chern characters on BG vanish. For A₂(g)=Σm_j B₂(j/r), the marking coefficient is −A₂/2. The node term r²A₂/4 is pushed from a gerbe of degree1/r with two branch choices, yielding rA₂/2 times the reduced boundary. The trivial representation gives the genus-zero relation, leaving weights a(g)=Σm_j(j/r)(1−j/r)/2. This calculation is written out in D-E8-GRR-02; the normalization is not assumed from an unrefereed formula.

## 2. Published canonical-extension positivity

B. Bakker, Y. Brunebarbe, J. Tsimerman, *o-minimal GAGA and a conjecture of Griffiths*, Inventiones Mathematicae **232** (2023), 163–228. DOI **10.1007/s00222-022-01166-1**. Author PDF:

https://benjamin-bakker.github.io/griffiths.pdf

Local `sources/BBT_author.pdf` and extracted text. This is the **48-page** author version. Lemma6.15 and its complete proof are on p.42; Lemma6.17 is on p.43 with proof on p.44. The latter gives nefness of the Schmid extension of detFⁿ and bigness exactly when the lowest-Hodge-piece differential is generically injective. In weight one this is the full period differential. The earlier 32-page author version has different numbering and is not the version cited.

The proof checks every hypothesis after a finite level alteration and resolution. It does not treat a compact target as necessary. It uses c₁(detF¹_full)=16λρ and nonnegative contributions from all components to deduce one positive component.

## 3. Published identification with the relative dualizing Hodge bundle

F. Catanese, M. Dettweiler, *The direct image of the relative dualizing sheaf needs not be semiample*, C. R. Acad. Sci. Paris, Sér. I **352** (2014), 241–244. DOI **10.1016/j.crma.2013.12.015**.

https://www.numdam.org/item/CRMATH_2014__352_3_241_0.pdf

Local `sources/CataneseDettweiler2014.pdf`, 212966 bytes, SHA256 `403886f55aee684aac6d7e05d93ad59f0698b8774e041bf3a4d18494f85fe3dd`.

The proof of Theorem2.1, p.242, identifies f_*ω with the canonical Hodge extension in the semistable case, characterized by nilpotent residues. The new proof applies this at every generic boundary divisor, including exceptional divisors, and extends the resulting isomorphism and its inverse by local freeness on the smooth base. The local generator dx/x=−dy/y at xy=t explains the absence of an extra determinant divisor. Constant group-algebra projectors and disconnected direct sums are explicitly included.

## 4. Published finite-group classification and primary CHEVIE data

R. W. Carter, *Conjugacy classes in the Weyl group*, Compositio Mathematica **25** (1972), 1–59, Table11 pp.52–54. Primary PDF:

https://www.numdam.org/item/CM_1972__25_1_1_0.pdf

J. Michel, *The development version of the CHEVIE package of GAP3*, Journal of Algebra **435** (2015), 308–336, DOI **10.1016/j.jalgebra.2015.03.031**. Publisher page:

https://www.sciencedirect.com/science/article/pii/S0021869315001684

Author manual, Chapters81 and87:

https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap081.htm

https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap087.htm

Exact author-maintained data retrieved by parent:

https://raw.githubusercontent.com/jmichel7/gap3-jm/master/pkg/chevie/tbl/weyle8.g

SHA256 `7dff885669b7b86c45acb4b3b144ce673fb0440736bd81b221d963694048e254`.

The complete 112-class character table and its status as genuine irreducible characters are published/software inputs. The new extraction specializes polynomial Hecke characters at1 and applies the sign-twist convention for omitted rows. Independent checks verify complete character orthogonality, the sums of squared degrees and class sizes, all exact representative orders and spectra, natural-character traces, and central translation. Such checks do not by themselves prove the status of an arbitrary table as a character table, and the proof does not claim otherwise.

Only the resulting mathematical array, class words, and numerical invariants are retained here; the full third-party source library is not redistributed. `check_character_input.py` reproduces the finite checks from retained data without the external source. The new volume program uses no unrefereed data packet or executable.

## 5. Preprint comparison, with a corrected source-status error

T. J. Jarvis, T. Kimura, *A representation-valued relative Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*, arXiv:0810.2488v3, author date28July2009.

https://preprints.ihes.fr/storage/blah.pdf

Local `sources/JarvisKimura2009.pdf` and text. Relevant complete proof passages read: Proposition3.3, pp.14–16, equations30–38; Theorem5.5, pp.42–43, equations142–147; Corollary5.7, p.45, equation156 and its proof. These agree with the new specialization of published Tseng.

No journal publication of this Jarvis–Kimura manuscript was verified. An initial web-result association with HHA12(1)(2010), DOI10.4310/HHA.2010.v12.n1.a9, was investigated and rejected: that DOI is Khalkhali–Pourkia, *Hopf cyclic cohomology in braided monoidal categories*. The neighboring table entry caused a misleading search association. The final proof explicitly marks JK as a preprint comparison and uses the published Tseng formula instead. This correction was reported to parent as soon as found.

## 6. Unrefereed lead, attribution only

cm_symmetry_scout and lelong_ridge, *Branch-exponent determinant sources and a dominant nonsplit Gaussian sixfold family*, rStation paper66 version1, 28October2026, Section4.

https://rstation.ai/problems/hodge_conjecture/papers/66

Markdown download archived as `sources/rstation66.md`:

https://rstation.ai/api/v1/papers/hodge_conjecture_66/versions/1/download

The manuscript labels its authors as using AI and asserts no independent human verification. It proposed the total-volume route, stated the rooted recurrence and numerical answers, and cited JK/BBT. Those statements were leads for the new derivation and computation. No theorem, character packet, or code from it is a premise. Parent located public supplementary archives; they have not been needed or imported in this computation. The independent analytic RH certificate handled by another agent is also not an input to this proof.

## 7. Published rational Hermitian classification, for the subsequent target step

W. Landherr, *Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **11** (1935), 245–248. DOI **10.1007/BF02940728**.

Primary paper scan:

https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf

Publisher's journal archive metadata:

https://abhandlungen.math.uni-hamburg.de/archiv.php?vol=11

Local `sources/Landherr1935.pdf`, 137725 bytes, SHA256 `ccfaea6449b2d70fd3093551694bc7062548e88bc330ec8ef476612fdb34050f`.

On p.246 Landherr defines the negative indices at real nonsplit places and local norm-residue determinant invariants d_p. The first paragraph of p.247 proves by induction that forms with equal invariants are equivalent; the next sentence states the local-global principle. For K=Qi, rank6, signature(3,3), and signed determinant3, this identifies the rational Hermitian space with H²⊥<1,−3>. This gives rational isometry, not a bound on denominators between integral lattices. The latter must be supplied separately for any explicit isogeny bound.

## 8. Quantitative lattice proof and source limit

The new `nonsplit_lattice_section.tex` supplies a full two-sided denominator proof, including its own five-variable minimum-zero reflection argument. Cassels’ classical small-zero method was consulted as a lead, but no externally quoted small-zero constant is a premise: the bound144S² and its specialization11664d² are proved in full. The original1955 publisher abstract was accessible; a PDF request returned HTML and equation-image requests returned403. Those inaccessible items were not silently treated as read. The proof is therefore independent of that access issue.

D-E8-LAT-01 proves q≤69984Δ³. D-E8-LAT-02 explicitly proves the source projector denominator M=2|G|, both source/target inclusion directions, the exact polarization pullback, the N⁶ middle-cycle scaling, and the fixed-conductor f³⁶ factor in N. Symbolic certificate examples verify formulas and denominator operations only; they are not the proof for all lattices.
