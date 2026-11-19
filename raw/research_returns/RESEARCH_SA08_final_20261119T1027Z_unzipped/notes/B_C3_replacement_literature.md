# Primary-source audit of the C32 local repair hypothesis

2026-11-19. Owner: /root/automorphisms. This is a source-scope audit,
not a proof or refutation of the remaining local construction.

## Exact requested theorem

For the specified map P_(p) -> T_(p), one needs a factorization
P_(p) -> E_p -> T_(p), with E_p an admissible strict simplicial
weight-graded positive-cochain PD algebra. The first arrow must be
an actual isomorphism in every weight and simplex in all form degrees
q < d_p, with d_p tending to infinity. The prescribed map and all
simplicial and PD identities must be retained. The target may have
eventual constant H0 and H1, as in C32; ordinary p-local uniqueness
does not supply this stronger factorization.

## Opened primary results and their exact scope

### Menichi, On the cohomology algebra of a fiber (2001)

Source: sources/B_menichi2001_fiber.pdf/.txt; arXiv math/0201134,
published Algebraic & Geometric Topology 1, 719--742.

* Lemma 7.2, pp736--737, text937--989: an explicit factorization
  between minimal Sullivan models over the field used in the paper,
  with generator spaces in degrees at least two. Its source is an
  ordinary free commutative algebra, not an arbitrary existing DGPD
  algebra. Its proof chooses representatives and primitives.
* Proposition 8.3, p739, text1059--1078: under a prescribed A -> B
  with admissible B, it produces A -> A tensor Gamma(V') and a
  comparison zigzag
  A tensor Gamma(V') <-~ A tensor Lambda(V) ->~ B.
  In particular the displayed diagram supplies **no arrow from the
  Gamma extension to B**. It cannot be read as the required factorization.
* Definition on p738, text1046--1048: admissible here means a quotient
  of an acyclic algebra; this is different from SA08 eventuality.
  Lemma8.5 p739, text1085--1096 imposes connectedness and an upper
  cohomology bound. Section7 p735, text881--882 explicitly warns
  against a general positive-characteristic lifting lemma.

The paper cites Halperin's unpublished Notes on divided powers
algebras, II.2.7; those notes were not located or opened. No stronger
theorem is attributed to them.

### Scott, Hopf algebras up to homotopy and the Bockstein spectral sequence (2005)

Source: sources/B_scott2005_hopf.pdf/.txt, AGT5,119--128.
The paper supplies a new proof, so it is a primary source for the
stated Anick theorem, not merely a bibliographic report.

* Anick's theorem [Anick5.6], p119, text20--41: over a subring R of Q
  containing 1/2, with least noninvertible prime rho>2, a free chain
  Hopf algebra up to homotopy generated in degrees q through q*rho-1
  can be made primitively generated.
* Theorem1.1, p120, text51--79: a free one-generator extension in the
  specified range can have its diagonal made trivial relative to the
  old algebra. It is a statement about chain Hopf structures, with
  finite-type and primitive-boundary hypotheses.

Neither statement gives a positive-cochain DGPD replacement under an
arbitrary P -> T. Linear dualization would require additional finiteness
and exactness hypotheses and reverse arrows; it does not preserve the
specific strict simplicial factorization without a separate proof.
Anick's original1989 full text remains not opened: both AMS PDF URL
forms returned403. The Scott proof is what was actually read.

### Scheerer--Tanre, Exploring W.G. Dwyer's tame homotopy theory (1991)

Source: sources/B_scheerer_tanre1991_tame.pdf/.txt,
Publicacions Matematiques35,375--402.

The model structures on pp376--377 (text59--124) use a sequence of
rings R_k in which successively more integers are invertible. Weak
equivalences test H_(s+k)(f) tensor R_k, not ordinary integral or fixed
Z_(p) homology in all degrees. The algebraic category is reduced
homological differential graded Lie algebras. Construction2.2 and
Proposition2.4, pp383--385 (text390--485), give explicit and functorial
free Lie resolutions. They do not assert that the same construction
works for positive-cochain PD algebras or retains a given simplicial
PD map with fixed weights. A model structure with weaker, degree-varying
tests cannot be silently substituted for the required vertical
resolution axiom.

Dwyer1979 itself is not opened; the preceding description cites the
opened Scheerer--Tanre primary treatment. Dwyer's DOI was identified
as10.1016/0040-9383(79)90023-5, without a retrieved full text.

### Hanke, The stable free rank of symmetry of products of spheres (2009 preprint)

Source: sources/B_hanke2009_stable_rank.pdf/.txt, arXiv0803.3572v3.
The downloaded PDF has a later TeX date in its header; the version
identifier and actual file hash are recorded rather than inferring
a revision date from that header.

Section3 pp6--7, text275--300, uses filtered algebras over Q with
filtration-q coefficient ring Q_q=Z[1/l: l prime, l<=q].
Definition4.1 p12, text536--546, tests bounded-degree equivalences
modulo primes l>q. Theorem4.6 pp13--14, text645--650, is a genuine
relative tame Hirsch lemma under the particular Cenkl--Porter
cochain algebra T(X), with an elementary two-term parameter complex
(Definition4.3 pp12--13, text553--567). It does not give an arbitrary
under-P repair. In particular, taking every weight while keeping
one prime noninvertible is outside its coefficient convention.
The proof appears in Section6, and its finite range is essential.

The cited general filtered-model references include unpublished
FU Berlin theses and Scheerer's1988 report. The report's publisher
page was opened, but its full text is subscription-only and was not
opened. No replacement theorem is inferred from that metadata.

### Richter, Divided power structures and chain complexes (2009)

Already available primary file: sources/D_Richter2009.pdf/.txt.
Theorem7.5 and Remarks7.6--7.7, printed pp250--252,
text919--1049, distinguish the transferred category of commutative
monoids for the **large tensor product** from ordinary DGPD algebras.
Remark7.6 transfers the simplicial model structure to the former;
Remark7.7 explicitly says that a characterization of those objects
by divided powers and higher versions is unavailable there.
Thus the transferred structure is not a replacement theorem for
all of the strict DGPD objects occurring in C32. Its grading is
nonnegative homological, another distinction requiring proof.

## Outcome and retrieval record

No opened theorem establishes the required local repair. This is an
absence of a verified application, not a claim that no such theorem
exists. The smallest gate remains the actual coherent construction
under P with low-form preservation. The useful exact relative theorems
above all have a different algebraic category, arrow direction,
coefficient convention, or connectedness/range hypothesis.

Code/receipt: code/B_fetch_relative_literature.py and
logs/B_relative_literature_fetch.json. Successful full downloads:
Menichi, Scott, Scheerer--Tanre, Hanke. Richter was read from the
already archived D source and independently opened on arXiv.
Halperin1992's publisher page returned403; Halperin's unpublished
Notes were not found; Scheerer1988 full text was subscription-only;
Anick1989 AMS full text returned403. These remain not-opened sources.

Searches used both engines, including exact-title queries for Anick,
Dwyer, Halperin's Notes, Halperin1992, tame relative divided powers,
positive-cochain divided power model structures, the tame Hirsch
lemma, and Richter's transferred model structure. General web summaries
claiming an unrestricted PD lifting theorem were not treated as evidence;
the previously audited Caradot--Lin lifting defect remains relevant.

Primary web locators: Menichi turn581688274view0 and
turn381324965view0; Scott turn508525517view1; Scheerer--Tanre
turn508525517view0; Hanke turn249544771view0 and
turn246946249view0; Richter turn401290060view0 (published version)
and turn519851303view0 (arXiv model-structure passage).
