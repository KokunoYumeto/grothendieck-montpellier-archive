# K17: current Steinberg-homology source check for the two K12 ranks

Date: 2026-11-21 UTC. Researcher: /root/vandiver_k, GPT-6 Astra Pro.
Reasoning effort: not exposed. This is a source-scope check and a conditional
reduction; it does not assert either missing integral vanishing.

## 1. Miller--Patzt--Putman, September 2025

Primary source: J. Miller, P. Patzt, A. Putman, *Homological vanishing for the
Steinberg representation II: reductive groups and integral conjectures*,
arXiv:2509.01559v1, 1 September 2025, 74 pages.
https://arxiv.org/pdf/2509.01559

Saved files:

- `work/steinberg_integral_mpp_2025.pdf`
- `work/steinberg_integral_mpp_2025.txt`
- `work/k12_mpp_bibitems.tex`

PDF SHA256: `b27dce174deffc0b68b0f760929fa0f218859ee1fa72f56c6b1c7d3538bd2396`.

Theorem C, p.6, assumes for every n>=4 that the double Tits building
T²(Z^n) is (n-2+min(b,floor((n-1)/2)))-connected. Under that hypothesis,
Steinberg homology of GL_n(Z) and SL_n(Z), with coefficients in any
commutative ring F, vanishes for

- i <= min(b,floor((n-2)/2)) when 2 and 3 are units in F;
- i <= min(b,floor((n-3)/3)) for arbitrary F.

Theorem D, p.6 (equivalent algebraic statement Theorem D', p.64), proves
only n-connectivity for n>=4, supplying b=2. Corollary E, p.7, therefore
proves degree-two vanishing for n>=6 if 2,3 are units and n>=8 for arbitrary
F. In particular,

    H_2(GL_11(Z); St_11) = H_2(SL_11(Z); St_11) = 0

is already a consequence of this source with integral coefficients. The
rank-eleven removal should cite this current result. In addition, Remark
1.18, p.7, explicitly says that the earlier degree-one and degree-two
proofs work over a commutative ring in which every prime <=n is a unit.
It therefore already covers the all-n>=3 localized statement with
R_n=Z[1/(n+1)!]. The independently reconstructed localization argument
is a source recheck, not a new theorem. Lemma 25.3, Claim 2, pp.56--57,
spells out the degree-one localization proof; the degree-two attribution
is the separate assertion of Remark 1.18, rather than Claim 2 itself.

Theorem C'.1, p.54, also gives surjectivity from either end Levi subgroup
to SL_(n+1) in degrees i<=min(b,floor(n/2)), over Z[1/6]. This does not
remove the b restriction. The established b=2 case supplies no degree-three
or degree-four surjection. If the b=4 conjecture were supplied, the
rank-nine degree-four Levi source is GL_8 and its degree-four homology
already vanishes, so the surjection would close that rank as well. This
is a conditional implication, not an established extra stable range.

Theorem 23.3, p.49, and the complete proof of Lemma 23.5, pp.50--51,
give a sharper finite-rank alternative, written out and checked in
`work/k12_double_building_gate.md`: it suffices to establish just

    H~_10(T²(Z^9);R) = H~_11(T²(Z^9);R)
      = H~_11(T²(Z^10);R) = 0,  R=Z[1/13!].

None of these three additional vanishings is established in this run.

The proof itself has a definite higher-degree obstruction. Sections
31--33, pp.64--72, construct a double complex from augmented-frame
chain complexes X_•(V). Theorem 31.5 supplies their homology only in
degrees zero and one. Lemma 32.2 accordingly identifies total-complex
homology with the decomposition-complex homology only through degree
zero and supplies a surjection in degree one. The q=2 vertical row is
explicitly left unspecified. Additional horizontal vanishing at ranks
nine or ten does not eliminate possible transgressions to that row.
Thus the actual proof has no hidden degree-three/four consequence
that follows simply by substituting the target ranks.

Reading scope: the statements and hypotheses above were read in full;
the construction and proof of Lemma 23.5 and Theorem 23.3's comparison
were read completely. Sections 23--25 and the Theorem D'/D comparison
were examined to check the range and the surjectivity cap. The full
construction/proof in sections 31--33 was then read to locate the
uncontrolled vertical homology row just described. This record
does not claim an independent whole-proof audit of all 74 pages or of
the external bar-construction results cited by Theorem 23.3.

## 2. Updated DEKM source and exact public-data inventory

Current author PDF:
https://jamartin.perso.math.cnrs.fr/Publications/DEKM.pdf

Saved as `work/k12_source_data/dekm_author_current.pdf` and `.txt`.
SHA256: `eb49d991c6509ccb7432a5e85955a735534885d0a4250c92044c2d1cab35cda4`.
This version includes the 2025 count 2,237,251,040 of rank-nine perfect
forms. Nevertheless Table 4, printed p.15, still has question marks for
the two target counts, and Remark 6.6, p.19, still lists the rank-nine,
rank-ten, and rank-eleven degree-twelve Voronoi homology computations as
missing. Theorem 4.5, p.16, and Table 5, p.17, retain their stated
vanishing ranges; Table 5 was visually inspected as well as text-read.

The correct repository is
https://github.com/elbazvip/Voronoi-complexes-database . Its complete
recursive GitHub tree was retrieved on 2026-11-21 and saved, without
truncation, in `work/k12_source_data/voronoi_repository_tree.json`.
Its README is saved beside it. The GAP and PARI data both stop at
`n9_rnk11` / `n9_rank11` and `n10_rnk11` / `n10_rank11`; rank-eight
data go through rank twelve. There are no target boundary matrices or
new rank-nine/rank-ten rank-twelve files in that snapshot. This is an
inventory of the retrieved repository, not a claim that no private or
other public calculation exists.

Index caution: raw filenames use the rank of the span of rank-one
quadratic forms. The text also uses projective cell dimensions. Table 4
starts its rank-eight row with thirteen eight-vector configurations under
column eight. Do not infer a new projective chain degree solely from a
raw filename or that table; the conditional K12 reduction uses the
explicit homology statements of Theorem 4.5, Table 5, Proposition 1.5,
and Remark 6.6.

## 3. Very recent rational claim, kept separate

Taiwang Deng, *Vanishing near the virtual cohomological dimension of
SL_n(Z)*, arXiv:2610.39960v1, 29 October 2026:
https://arxiv.org/abs/2610.39960 . The primary PDF and arXiv metadata were
downloaded directly and saved as `work/k12_source_data/deng_vcd_2026.*`.
Theorem 1.1, p.2, claims the full Church--Farb--Putman rational vanishing.
Section 1.6, p.4, explicitly excludes torsion control and an integral
Steinberg-homology conclusion. The introduction and scope were read;
the 69-page proof has not been independently audited here. Consequently
this note records a recent source claim, not a newly certified theorem.
Even the claimed rational conclusion would leave the two localized
torsion groups in the K12 gate undecided.

Avner Ash and Paul E. Gunnells, arXiv:2611.03303v1, 2 November 2026,
was likewise downloaded as `work/k12_source_data/ash_gunnells_parabolic_2026.*`.
Its introduction constructs a parabolic sharbly resolution and a chain
map computing restriction in finite characteristic. It states no
rank-nine degree-four or rank-ten degree-three vanishing. No complete
audit of that paper is claimed.

## 4. Numerical consequence still absent

The exact K12 reduction to the two localized Steinberg groups remains
as stated in `work/k12_rank_reduction.tex`. The finite double-building
gate below is another sufficient set of hypotheses, not a proof of them.
No complete trace polynomial for the automorphic alternative has been
located or computed; the field/level/multiplicity coverage condition in
`work/k_numeric_followup.md` remains necessary. No K12 or K16 vanishing
is asserted from this source update.
