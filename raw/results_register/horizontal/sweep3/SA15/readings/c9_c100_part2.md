# SA15, cote 100 scans 3-45 (part 2 of c9_c100): extending abelian schemes across a closed set of characteristic p by their p-divisible group, and descent of abelian schemes along proper epimorphisms

Claude Opus 5.5 at effort max (SA15-c9_c100-part2, sweep 3 reader), 19 Nov 2026. Launched by the SA15 c9_c100 reader
(Claude Opus 5.5 at effort max) under agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max). Brief: `sweep3/READER_BRIEF.md`.
Companion files: `c9_c100_part2_CHECK_EVENTS.tsv` (24 events), `c9_c100_part2_CORRECTIONS.tsv` (14 rows). Scans 48-53 are
in `sweep3/SA15/STUDY.md` §3 and are not repeated here; this file says where 3-45 lead into them.

**Read:** all 43 scans 3-45 of package `MPL_8_079-081+9+4+100`, in page order, from the raw Pro `.tex` (the reader tool
drops the figure nodes, and on this cote they hold margin text such as "Douteux, sans doute faux" on 17 and the NB on 31,
so I read the raw files); the Pro notes #150-#224 (scans 3-22) in full and #225-#316 (scans 22-45) searched for
flagged problems; the Codex web witnesses K100-01..04 at the readings
that carry the mathematics. Ink checked on the images: 2 (folder cover), 11, 13, 23, 29, 30, 31 (sheet pairing), and 6,
10, 18, 34 for the hands. Michel Hua's project was not needed for any reading here and is not used.

## 0. What the stretch is

**Sheets.** Scans 3-46 are 22 sheets, each scanned recto then verso: (3,4), (5,6), ..., (45,46). His manuscript is on
the rectos (odd scans) and, on the first sheet only, also on the verso (4 = his page "1 bis"). The versos 6-46 are reused
paper. Two pieces of evidence for the pairing: on 3 his margin "Pour 1) TSVP" sends the reader overleaf to 4, which holds
the lemma used for 1); and the large faint mark "...304 MARAIS" on the left edge of 30 shows through, mirrored, on the
right edge of 29 (checked at 150 dpi, flopped crop). His page numbers: 1 (3), 1 bis (4), 2) (5), 3 (7); later pages are
unnumbered. The numbers at the foot of every scan (2, 3, 4, ...) are the archive's, scan - 1.

**Dating (correction of sweep 2).** The folder cover (scan 2) reads "Bonne réduction et groupes p-divisibles" and
carries **no date** (image checked). The date 14 March 1967 that sweep 2 put on "the cover" is stamped on a reused
printer's cover, "PUBLICATIONS MATHÉMATIQUES No 32 ... Bon à tirer", scan 20, the verso of his page 19 (Publ. Math.
IHÉS 32 is EGA IV, 4e partie). Scan 29, his "d) Construction d'un schéma abélien formel", is written on the back of
L. Illusie's typed letter "Paris, le 24 Février 1968" (scan 30). So 29 was written after 24 February 1968, and with it
the descent text of 23-45 that 29 continues. Pages 3-19 point forward to that text ("un th. de descente qui nous assure
cela, cf plus bas", 15; "lemme à dégager", 13), so the whole manuscript is most likely from 1968, not March 1967; from the
sheets alone 3-19 are only known to be after 14 March 1967. Correction row 1.

**Contents.** Three pieces, one argument:
- 3-19: a theorem on extending abelian schemes from an open U to S when T = S - U has residue characteristic p and the
  p-divisible group is given on all of S (full faithfulness, then essential surjectivity in five cases a-e).
- 21: when a homomorphism of p-divisible groups is algebraic (the locus is a closed subscheme, open at points of
  characteristic p).
- 23-45: descent of abelian schemes along proper epimorphisms (the "lemme à dégager" of 13 and the "th. de descente ...
  cf plus bas" of 15): full faithfulness (Lemma 1, Corollaries 1-3), then effectivity through formal moduli and an
  algebraization criterion for formal abelian schemes over complete local rings, tested on complete traits; then
  remarks for proper flat schemes.

## 1. 100:3-4 — the Theorem, and the Lemma, Complément and Corollary that give 1) (SA15-19)

**What he states (3).** S locally noetherian, U open, T = S - U, p prime with char k(t) = p for all t in T. C = abelian
schemes over S; C' = triples (A_U, M, phi) with A_U abelian over U, M p-divisible over S, phi: M|U -> T_p(A_U).
F(A) = (A_U, T_p(A), id).
1) If U meets every connected component of S ("p.ex. U dense dans S, i.e. prof et_T(S) >= 1"), F is fully faithful.
2) If a) there is a finite surjective S' -> S with S' geometrically unibranch (e.g. the normalization finite over S) and
b) prof et_T(S) >= 2, then F is an equivalence. (A cancelled earlier b): for t in T, any two irreducible components of
the strict localization meet outside the closed point; equivalently U'' is dense in S'' = S' x_S S'.)
Margin footnote: with L_n = pi_0 of S', S'', S''' and K_n the components whose image meets U, the condition b'): "la plus
petite partie de L_1 contenant K_1 et stable par 'troisième face' soit L_1 (c'est ce qui est assuré par la condition b))".

**What 4 proves.** Lemma (for any prime l): A, B abelian over S locally noetherian, u_l: T_l(A) -> T_l(B); there is a
closed subscheme T of S such that u_l becomes algebraic over S'/S iff S' -> S factors through T. "Cf Inventiones 1.2 (ou
démonstration cristalline)": presumably his own "Un théorème sur les homomorphismes de schémas abéliens", Invent. Math. 2
(1966) 59-78 (locator unverified). Complément: at t in T with char k(t) = l, T contains an open neighbourhood of t.
Corollary: if every connected component of S meets U, every point of S - U has characteristic l and u_l|U is
algebraic, then u_l is algebraic.

**Checked.**
- Corollary (check event 100:4a): T contains U as an open subscheme (hypothesis c), and a neighbourhood of each point of
  T in S - U (Complément and b); so T is open and closed, contains U, and meets every component: T = S. Correct.
- Complément (100:4b): over the infinitesimal neighbourhoods of t (l nilpotent there), Serre-Tate lifts the homomorphism
  given at t along u_l; Grothendieck's existence theorem algebraizes it over Spec of the completion of O_(S,t); since
  O_(S,t) -> its completion is faithfully flat, the ideal of T vanishes at t, so T contains Spec O_(S,t) and hence a
  neighbourhood. Correct; this is the "démonstration cristalline" in today's form.
- The role of b) (100:4c): at points of characteristic 0 the locus is closed but need not be open as a subscheme. Example:
  E with CM over Spec Q̄[eps], deformed so that j = j_0 + eps; the CM endomorphism of T_l(E) exists over Q̄[eps]
  (étale sheaves do not see eps) and is algebraic at the point, but not over Q̄[eps]. So the Corollary needs exactly his
  b), and the Theorem's 1) is his Corollary with l = p (100:3a).
- Faithfulness, "bien connu" on 5 (100:5): if u kills every A[p^n] then u = v[p^n] for every n, and Hom(A, B) is
  finitely generated and free over a connected base, so u = 0. Correct.

**Footnote b'), checked with a precision (100:3b).** Strict-locally at t in T, write the strict henselization as a union
of irreducible components Z_i; prof et_T >= 2 makes the punctured scheme connected, i.e. the graph with an edge (i, j)
when Z_i meets Z_j outside T is connected. Components S'_i x S'_j of S'' over the same Z, or over adjacent Z, meet U'';
a path i = i_0, ..., i_k = j and the triangles (i_0, i_m, i_m+1) in L_2 then put (i, j) in the closure under third
faces. So b) gives b') **provided every irreducible component of S' meets U'** (true for S' the normalization of S_red,
since U is dense); for an arbitrary finite surjective geometrically unibranch S' it is false (S' = normalization plus a
copy of a point of T has components of S'' that no triangle reaches). Correction row 9.

## 2. 100:5 — "1) Foncteur pleinement fidèle", second version (SA15-19)

He restates the triples (here M "sur T", phi: T_p(A_U) = M) and reproves 1): fullness reduces to "si u_p est algébrique
sur U, il l'est sur S"; for U schematically dense "cela résulte de [ ] 1.2"; in general through the schematic closure of U
"dans X" (a slip for S, correction row 6) and "[ ] 1.1". A cancelled paragraph does it with Serre-Tate on the infinitesimal
neighbourhoods of T and the faithfully flat completion. Margin: "Pour pleine fidélité au lieu de U dense, il me suffit
que ...", with the example of two complete discrete valuation rings glued at their closed points, U = one generic point,
and "Y a-t-il des contre-exemples avec S de t. f. sur un corps ?". The Corollary of 4 settles that example: the
algebraicity locus contains the closure of U, hence the closed point, hence (Complément, characteristic p there) the
whole of S. Nothing wrong; the margin question is answered by his own 4.

## 3. 100:7-19 — 2) essential surjectivity (SA15-19)

Boxed hypothesis on 7: "Si S géom. unibranche en les points de S - U, et si le normalisé de S_red est fini sur S"; a
bracket generalizes to "U^(n) rencontre toutes composantes connexes de S^(n)".

**a) Reduction to S reduced (7). Wrong as written: correction row 2, check event 100:7.** He takes A_0 on S_0 = S_red,
uses Serre-Tate on the infinitesimal neighbourhoods T_n of T to get a formal abelian scheme over the completion
Spec of Lambda^ along T, algebraizes it ("(réf ... !!!)"), and glues with A_U by descent along U ⊔ Spec Lambda^ -> S,
"d'après le critère de Raynaud. On gagne !". He put "?" twice in the margin. The gluing needs an isomorphism of A' and
A_U over U x_S Spec Lambda^, which nothing provides when p is not nilpotent there, and in fact **part 2) of the Theorem
is false for non-reduced S.** Counterexample: S = Spec Z_p[eps]/(eps^2), T = V(p), U = Spec Q_p[eps]/(eps^2); a) holds
with S' = Spec Z_p; b) holds since the étale site of S is that of Spec Z_p, whose punctured strict henselization is a
point. Let E_0/Q_p have good reduction with Néron model E over Z_p, let A_U be a non-trivial first-order deformation of
E_0 over Q_p[eps] (class c != 0 in H^1(E_0, T) = Q_p), M = E[p^infinity] x Z_p[eps], and phi the canonical isomorphism
(finite étale group schemes over Q_p[eps] are those over Q_p). If A over S had A_U as generic fibre and T_p(A) = M, then
A would be a deformation of E (A_red has generic fibre E_0, so A_red = E); by Serre-Tate over Z/p^n[eps] its class in
H^1(E, T) = Z_p vanishes mod p^n for all n, so A is the constant deformation, whose generic fibre is the trivial
deformation, not A_U (automorphisms of E_0 act trivially on H^1(E_0, T)). So the triple is not in the essential image.
Refined statement: 2) for S reduced, which is what cases b)-e) treat. The missing step in a) is exactly the gluing
isomorphism over U x_S Spec Lambda^ that he queried.

**b) S geometrically unibranch (first "normal"), A_U with a level ("rigidification de Jacobi") and a polarization (9).**
The graph of U -> R (fine moduli scheme) has closure S' in S x R; S' -> S is proper by the valuative criterion and "le
résultat de Raynaud dans le cas d'un trait" — that is the theorem of the typescript 100:48-51 (STUDY.md §3: over a trait,
A_K extends iff its p-divisible group does, through Tate's theorem). Then: "tout revient, grâce à Tate, à prouver que A_U
se prolonge ... cet M étant unique à iso unique près" (Tate's full faithfulness on normal bases with generic
characteristic 0: Tate, "p-divisible groups", Driebergen 1966, §4 (locator unverified); in generic characteristic p, de
Jong, Invent. Math. 134 (1998) (locator unverified)). Main Theorem: reduce to discrete fibres; on the normalization
S'' (first assumed finite) Tate gives T_p(A_S'') = M_S''; over a fibre S''_s (geometrically connected, characteristic
p) the p-divisible group is constant, so (Corollary of 4: the identity of p-divisible groups is algebraic at one point,
hence on the connected fibre) A is constant there, the polarized rigidified object too, and the fibre maps to one point
of R. Checked (100:9). Precision (correction row 8): with "normal" replaced by "géom. unib.", the Main Theorem gives
S' -> S finite, birational and radicial, not an isomorphism (the normalization of a cusp); that case then needs the
descent of 23-45, which is what d) does. The case without finite normalization is "O.K." (11, replacing "Il faudrait
tirer au clair cette question") with a reference "[ ] p 75-76" not identified; not proved on the page.

**c) S geometrically unibranch (11-13).** "Choisissons un nb premier l != p, 3" — the ink shows a 3 written heavily over
another digit (check event 100:11); the level-l structures rigidify for l >= 3, so the exclusion needed is l = 2 (and l
must be invertible on U): an edition keeps "3" and notes this. Normalize S in the function field of a finite étale U'
trivializing the level; S' -> S finite surjective, S' normal; b) on S'; full faithfulness on S'' = S' x_S S', with U''
dense in S'' because S' -> S is universally open (Chevalley's criterion, EGA IV 14.4.4, locator unverified); so a
descent datum on A'; on _l A' it descends ("S' -> S est un morphisme de descente effective pour les schémas relatifs
finis étales (SGA 1 VIII)"), so a finite étale S_1 -> S splits _l(A_U), and the descent along finite étale S_1 -> S is
effective since A' is projective. Checked (100:11-13). The reference: the ink reads "(SGA 1 VIII)" (checked), but S' -> S
is finite surjective, not flat; the statement used is SGA 1 IX 4.7 (locator unverified). Correction row 5.

**d) S reduced, S' finite over S geometrically unibranch (13-15).** By c) on S', full faithfulness on (S'', U'') gives
a descent datum; "le morphisme S' -> S, étant un épimorphisme fini, est un morphisme de descente pour les schémas
abéliens, et aussi pour les groupes p-divisibles" (margin "lemme à dégager": this is Lemma 1 and Corollaries 2-3 on
23-25); effectivity: "un th. de descente qui nous assure cela, cf plus bas" (27-45).

**e) General case (15-19). The doubtful lemma is not needed: check event 100:15-17 (independent re-proof).** S reduced;
by d) a solution A(s) over each Spec O_(S,s); "par unicité" they form a local system; he then needs the lemma "Un 'syst
local' de schémas abéliens sur un schéma [loc. noeth] provient d'un schéma abélien", circled in the margin "Douteux, sans
doute faux" (17). His margin lemma on 15 says what is really needed: (A_U, M, phi) is in the essential image iff there
is a solution over Spec O_(S,t) for every t in T; and 17 reduces it correctly: given A_U and t maximal in T, extend over
a neighbourhood of t. That reduction is provable without the local-system lemma: take a solution A(t) over Spec O_(S,t)
with A(t)|U(t) = A_U|U(t), U(t) = Spec O_(S,t) - {t}; spread A(t) to B over an affine V containing t; U(t) is the limit
of the U ∩ V' over affine V' containing t, with affine transition maps, so the isomorphism B|U(t) = A_U|U(t) and the one
on p-divisible groups spread to some V' (EGA IV 8.8.2); glue B|V' with A_U over U ∩ V'; T shrinks by a neighbourhood of
t in T; noetherian induction finishes. At each later step the local problem at a new maximal t is the old one, because
full faithfulness 1) over the punctured scheme U_k(t), with dense open U(t), identifies the extended A_(U_k) with the old
solution there (U is dense, since prof et_T(S) >= 1). So e) holds given d), and the "Douteux" lemma can be dropped; his
margin "inutile ?" beside it on 17 points the same way. The uniform-neighbourhood lemma begun on 19 ("Supposons d'abord S
excellent ... Alors", unfinished) is likewise not needed. Whether the local-system lemma itself is true is left open
(hunch H4).

## 4. 100:21 — when a homomorphism of p-divisible groups is algebraic (SA15-19)

"Question: quand [u_p: T_p(A) -> T_p(B)] provient-il d'un hom u: A -> B." a) (S noetherian) there is a largest subscheme
T on which u_p is algebraic; T is closed and its formation commutes with any base change. b) If t in T has
characteristic p, T contains an open neighbourhood of t. Cor.: "Soit Z l'ens des pts de S qui sont maximaux, ou qui sont
associés à O_S et de car. != p. Supposons que z in Z => closure(z) ∩ S_p ∩ T non vide. Alors u_p est algébrique." These
are the Lemma and Complément of 4 for l = p, and the Corollary in the form used on 9-11. The figure draws a family over S
with A_(S') -> B_(S').

**Checked (100:21).** The corollary holds when Z = Max(S) ∪ (Ass(O_S) ∩ S[1/p]): an associated point x of the ideal of T
is either in Z (then it generizes a point of T of characteristic p, so x has a neighbourhood in T) or an associated point
of characteristic p lying in the closure of a maximal point already in T (then b) applies at x); so the ideal is 0. The
other parse ("(maximaux ou associés) et de car != p") makes it false: S = Spec k, k an algebraic closure of F_p(t), E
ordinary with j = t, u_p the idempotent (1, 0) of End(E[p^infinity]) = Z_p x Z_p, not algebraic since End(E) = Z; Z is
empty and the hypothesis holds vacuously. His first wording, cancelled ("des éléments de Max S ... et de l'ens des"),
confirms the first parse. Correction row 12 (punctuation of the edition).

## 5. 100:23-27 — descent of morphisms along proper epimorphisms (SA15-19)

**Lemma 1 (23).** f: S' -> S a proper epimorphism of locally noetherian schemes (epimorphism: O_S -> f_* O_S' injective),
X formally unramified over S: Hom_S(S, X) -> Hom_S(S', X) => Hom_S(S'', X) is exact. Proof: g' with g' pr_1 = g' pr_2
factors topologically through S (f is submersive); the sheaf map lands in A = Ker(f_* O_S' => h_* O_S''), so g' factors
through S' -> Spec(A) = S'_1 -> X; "EGA III 3 indique aisément que S'_1 -> S' est fini, radiciel" — the ink reads S'
(checked); it must be S'_1 -> S (correction row 3); S'_1 -> S is an epimorphism since O_S ⊂ A ⊂ f_* O_S'.
**Checked (100:23a), independent re-proof:** S'_1 -> S is finite by coherence of f_* O_S' (EGA III 3.2.1, locator
unverified); radicial: for two points (or two Omega-points) of S' over the same point of S there is a point of S'' over
the pair, and the two composites S'' => S' -> S'_1 agree, so all of S' over s goes to one point of S'_1, and two
embeddings of its residue field over k(s) into an algebraically closed Omega agree; since S' -> S'_1 is surjective (A ⊂
f_* O_S'), S'_1 -> S is radicial.
**Corollary 1** (f entier radiciel epimorphism, X formally unramified; f finite and S locally noetherian, or X locally of
finite type): Hom_S(S, X) -> Hom_S(S', X) bijective. Checked (100:25): S' -> S is a homeomorphism; locally, replacing X
by the schematic image, O_(S,s) ⊂ O_(X,x) ⊂ O_(S',s') with O_(X,x) finite over O_(S,s), unramified, residue extension
radicial hence trivial; Nakayama gives equality. **Corollary 2:** a proper epimorphism of noetherian schemes is a descent
morphism (full faithfulness) for abelian schemes, since Hom_S(A, B) is representable and unramified. Correct.
**Corollary 3** (p-divisible groups): reduced to "Il faut prouver que X [= Hom_S(A, B)] est formellement net"; open on the
page. Check event 100:25b: formal unramifiedness of the Hom functor of p-divisible groups holds by rigidity
(Katz, LNM 868 (1981), Lemma 1.1.3, locator unverified), but Lemma 1's route through Corollary 1 needs it for the limit,
not for the finite levels Hom(A[p^n], B[p^n]), which are not unramified (Hom(alpha_p, alpha_p) = G_a); the page does not
say how to pass to the limit.

**Effectivity (27).** f as in Cor. 2 and an effective epimorphism. a) reduction to S local, "triviale, par passage à la
limite"; b) to S complete, by "le critère de descente plate des schémas abéliens de Raynaud", noting that Cor. 2 cannot
be applied to S_2 = Spec of the completed tensor square (not noetherian) and that flat base change carries the
radicial algebra A along. Margin: "donner remarque après lemme 1; donne aussi le cas de 0-descente". A cancelled c)
(dimension 0) is replaced by d) on 29.

## 6. 100:29-39 — a formal abelian scheme, and when it is algebraic (SA15-19)

**d) Construction of the formal abelian scheme (29-31).** "si S_0 = Spec k (k corps résiduel) alors S'_0/S_0 a une
section, donc S'_0 -> S_0 est un morphisme de descente effective universelle" — ink checked: "a une section" (Codex web
reads so; Pro has "une galér(?)", correction row 4); it needs k algebraically closed, as in the cancelled c) of 27. With
M the formal moduli of A_0 over Spf W(k), a formal deformation of A'_0 over S^' is a map S^' -> M; the descent datum is
"phi' p_1 = phi' p_2"; the sequence S^ <- S^' <= S^'' of formal schemes is exact (comparison theorem), so A^' descends to
a formal abelian scheme A^ over Spf R. Checked (100:29): maps S^' -> M are continuous maps of the universal deformation
ring into Gamma(S^', O), which is the completion of Gamma(S', O) by EGA III 4.1.5 (locator unverified); completion is
exact on finite modules, and the effective-epimorphism hypothesis gives O_S = Ker(f_* O_S' => h_* O_S''), so equalized
maps from S^' come from S^.

**Th. (31-35).** R complete local noetherian, S = Spec R, A^ a formal abelian scheme over Spf R ("Spf B" in the
transcription; R is meant). Equivalent: (i) A^ algebraic; (ii) A^ becomes algebraic after some proper surjective
S' -> S; (iii) for every integral quotient B "de A" (read: of R, correction row 7) of dimension 1, with normalization B',
A^ over Spf B' is algebraic. Margin NB: the proof only needs the one-dimensional points outside any given countable union
of closed sets T_i. Proof: (ii) => (iii) by a trait T_1 finite over the complete trait and descent along the finite
flat T_1 -> T (projective); (iii) => (ii'): a finite surjective unramified S' -> S over which A^ is algebraic — the
polarizations of the A_n form a formal scheme P^ = ⊔ P^alpha, a countable family of finite unramified S-schemes; (iii)
puts every one-dimensional point in some Z_alpha = Im(P^alpha); the Proposition gives finitely many; (ii') => (i'):
algebraic over S_red (closed immersions S'_i -> S after a finite étale base change, one of them an isomorphism on each
irreducible component; then a gluing lemma for components: O_S = O_S' x_(O_T) O_S'' for S = S' ∪ S'' reduced); (i') => (i):
Lemma: X^ proper smooth over Spf R, algebraic over S_red => algebraic, by deformation theory with the obstruction in
H^2 and the indeterminacy in H^1 of T ⊗ J on X_0 and on X^_0, identified by the comparison theorem ("sans doute cas
particulier d'un [lemme] vieillot à démontrer avec complexe cot. relatif"). Checked (100:31, 100:33-35, 100:35-37): each
implication holds as written; in (i') => (i) the two torsors of liftings correspond under the comparison isomorphism, so
the formal lifting is algebraic, and the group law algebraizes (EGA III 5.4.1, locator unverified). The second H in 2°
on 37 is H^1 (Codex web reads H^1; Pro leaves H^(1|2)); correction row 11.

**Proposition and Corollary (37-39). Independent re-proof, check event 100:37-39.** S local noetherian complete, (Z_i)
a countable family of closed sets whose union contains every x with dim closure(x) <= 1: finitely many Z_i cover S.
Reduce to S integral (components); if no Z_i is all of S they are all nowhere dense, and the Corollary gives a point of
dimension 1 outside their union. The Corollary: R finite over V[[T_1, ..., T_r]], V a complete discrete valuation ring
(Cohen); images of nowhere dense closed sets stay nowhere dense (R a domain); the V-homomorphisms
V[[T]] -> V form m^r, a complete metric space; for f != 0 the zero set of f in m^r is closed with empty interior (after
translating and scaling, a non-zero power series vanishing on all of m^r contradicts Weierstrass preparation in one
variable by induction on r, m being infinite); Baire gives phi outside all of them, and Ker(phi) is a point of dimension 1
avoiding every Z_i. Correct.

## 7. 100:41-45 — remarks: proper flat formal schemes, and descent of flat proper schemes (SA15-19)

**Remarque (41).** 𝔛 proper flat over S = Spec R complete, H^0(X_0, O) = k, Pic^0_(X_n/S_n) flat (e.g. Pic^0_(X_0/k)
smooth); NS and its ample part P_n; P^ = ⊔ P_alpha, finite unramified. Equivalent: (i) after a proper surjective S',
algebraic and projective; (ii) the same on the normalizations of all closed T of dimension <= 1; (iii) after a finite
surjective unramified S'; (iv) after a finite étale S', on each reduced irreducible component, "rationnellement projectif";
"De plus, si S' -> S est comme dans (iv), X^_S' est algébrique". Margin NB: only if Pic^0_(X_0/S_0) is smooth; otherwise
take S' -> S finite and flat in (iii), (iv), "car une polarisation ne définit pas tjrs un faisceau inversible". NB (43):
for X_0 abelian or para-abelian these are equivalent to (0) 𝔛 algebraic, and projectivity can be dropped. Precision
(correction row 14): the "De plus" goes through the gluing lemma of 35, which gives algebraicity over S'_red; to reach S'
itself when S' is not reduced the smooth lemma of 35-37 is needed, so for non-smooth X it holds for S reduced only.

**Remarque (43-45).** S' -> S proper, an effective epimorphism, locally noetherian: "un morphisme de descente effective
pour les schémas relatifs plats" (both witnesses read "effective"; what the next sentence asks — whether a descent datum
on a proper flat X' is effective — shows the claim is full faithfulness, which holds since the condition
O = Ker(f_* O => h_* O) is stable under flat base change); a) reduce to the local rings; b) to the completions and a
finite étale extension; c) without infinitesimal automorphisms and with "assez de sections plates ... le long desquelles
X'/S' soit lisse", formal moduli give X^ descending X^'; d) (45) with a projective S'' -> S' making X projective, a finite
étale T over Spec of the completed local ring on which the descent is effective. Last Remarque: (X', L') proper flat with
an invertible L' and a descent datum, (X'_s', L'_s') without infinitesimal automorphisms: effective, "Argument par
modules formels ...". Precision (correction row 13): for Grothendieck's existence theorem to make the descended formal
scheme algebraic, L' must be relatively ample; with L' only invertible (e.g. trivial) the statement is about proper
non-projective X', where effective descent of schemes can fail even along finite étale maps (Néron Models, §6.7,
locator unverified). The margin "Conditions sans doute inutiles" (43) sits beside c).

## 8. The reused versos, one line each (SA15-12)

| Scan | What it is | His hand? |
|---|---|---|
| 6, 8, 10, 14, 16, 22, 24, 28, 32 | D. Mumford's typescript of the book on invariant theory and moduli (Geometric Invariant Theory), chapter 0, pages 0.13, 0.14, 0.15, 0.19, 0.18, 0.9, 0.16 bis, 0.4, 0.2 | French margins on 6 ("Il paraît suffisant que phi soit quasi-cpt ..."), 8 ("phi quasi-compact quasi-séparé"), 10 ("conflits avec des terminologies reçues; dire: proper and free"; "a closed immersion" circled, "monomorphism" boxed), 22 ("type" circled in "loc. of finite type", margin "présentation"; image checked, nothing else in hand); an English diagonal note on 6 (definition of a quotient X/R); presumably his, as a reader of the draft. None of 6-46 is a page of his manuscript; WHAT_IS_WHERE's "his pages" 10 and 22 are these margins |
| 26, 34, 36, 38 | the same typescript's preface, pages iv, iii, ii, i ("Harvard University, Oct. 27, 1963"; thanks to Zariski, Tate and Grothendieck) | 34: English insertions ("That it is", "developed"), hand not identified |
| 12 | an English errata list (pages 2-75; "[AVB 2.2 and 3.3]") | no |
| 18 | typed corrections "EGA IV 4o (2èmes épreuves)", pages 164-271, struck through, in his voice ("c'est bien triste ...", "encore canulée") | typed; two words inserted by hand |
| 20 | printer's cover "Publications Mathématiques No 32 ... Bon à tirer", stamped 14 MARS 1967, circled numbers 17.1.6, 19.1.8, 19.4.11 | the circled numbers are handwritten |
| 30 | L. Illusie to Grothendieck, typed, "Paris, le 24 Février 1968" (Exp. IV, the appendix on R-R in analytic geometry, CNRS renewal, prenotes on Künneth), struck through | no (signature Illusie) |
| 40 | typed copy of his letter "Cher Dieudonné", 7.4.1967, on EGA IV 12.1.1 (vi bis), 15.5.6.1, 15.6.3-15.6.4, struck through | his text, typed, unsigned |
| 42, 44 | typed EGA IV errata and "points d'autocritique" (14-15 to be redone by henselization "suivant une idée de Raynaud"; "non ramifié" for "net"), with (vi bis) for 12.1.1 | his text, typed |
| 46 | not in this stretch | — |

These are SA15-12 (documents). The two items in his voice (40; 18, 42, 44) are EGA material of March-April 1967 and belong
with the EGA dossiers if an edition of his letters is made; they are not studied here.

## Dependencies

- **Uses SA15-19, 100:48-51** (STUDY.md §3): "le résultat de Raynaud dans le cas d'un trait" (9) is the theorem of the
  typescript "Modèles de Néron et groupes p-divisibles" (good reduction over a trait iff the p-divisible group extends).
  The higher-dimensional theorem of 3 is built on it.
- **Uses SA15-16** (6:22-32): Serre-Tate (deformations of abelian schemes = deformations of p-divisible groups where p is
  nilpotent) on 4 (Complément), 5 (cancelled), 7.
- **Uses SA15-14 and SA15-1 only through SA15-16**; no crystalline cohomology appears on these pages beyond "ou
  démonstration cristalline" (4).
- **Uses SA15-17** (6:33-37): no. The elliptic-curve reduction pages do not appear in 3-45; no Serre-Tate canonical
  lifts, no ordinary reduction.
- **Uses cote 9, 9:11-14** (inertia characters, potentially good reduction; part 1): not cited on these pages.
- **Literature:** his Inventiones paper of 1966 (4, 5); Tate's p-divisible groups (9); SGA 1 VIII/IX (13); EGA III 3,
  4, 5 (23, 29-37); Raynaud's flat descent criterion for abelian schemes (7, 27, 33).
- **Across topics:** SA18-11 (integral models and local duality), as recorded in WHAT_IS_WHERE; SGA 7 IX (the
  good-reduction criterion over a trait, the case S of dimension 1 of the Theorem).

## Hunches

- **H1 (status of the Theorem for reduced S).** With S reduced, the proof on 3-45 closes up to two points it leaves open:
  the gluing in a) is not needed (S reduced), Cor. 3's passage to the limit, and the non-finite normalization case of b).
  For S normal of generic characteristic 0 the statement follows from Tate's full faithfulness plus extension over
  points of codimension 1 and descent; I expect the reduced, geometrically unibranch case to be true as stated. Grounds:
  every step checked above; the counterexample needs nilpotents. Related later work on extending abelian schemes over
  bases of dimension >= 2: Faltings-Chai, Degeneration of Abelian Varieties (1990), chapter V §6, and Vasiu-Zink,
  "Purity results for p-divisible groups and abelian schemes over regular bases of mixed characteristic", Doc. Math. 15
  (2010) (both locators unverified).
- **H2 (dating).** The manuscript is from 1968, the year SGA 7 (1967-1969) was being written; 3-45 look like the
  generalization to bases of dimension > 1 of the trait case typed on 48-51 for SGA 7 IX. Grounds: the Illusie letter
  under 29, the forward references 13 and 15, the typescript 48-51 cited as "Raynaud" on 9.
- **H3 (the algebraization criterion of 31).** "A formal abelian scheme over a complete local noetherian ring is algebraic
  iff it is algebraic over the normalization of every one-dimensional integral quotient, even avoiding a countable union of
  closed sets" may not be in print in this form. Grounds: I know of no such statement; it would follow today from Artin's
  algebraization for formal abelian schemes with an ample class, through the same NS-and-Baire argument.
- **H4 (the local-system lemma of 17).** For S normal it is true (homomorphisms of abelian schemes extend over normal
  bases); for reduced non-normal S I could not decide it; his "Douteux, sans doute faux" may target non-reduced bases,
  where the counterexample to 2) suggests local data need not glue. It is not needed for the Theorem (section 3 e).
- **H5 (the uniform neighbourhood of 19).** True for S normal; for non-normal S the neighbourhood V must avoid the points
  where the punctured strict localization is disconnected (a nodal curve with a twist by -1 at the node: an isomorphism
  given at a smooth point does not extend across the node). The lemma is unfinished and not needed.
- **H6 (l != p, 3 on 11).** The overwritten digit was probably 2 ("l != p, 2"); 3 over it may be a slip.

## Deliverable state of 100:3-45

- **Passes:** Pro transcription and notes (GPT-6 Astra, ChatGPT Pro mode; package `MPL_8_079-081+9+4+100`); Codex web
  K100-01 (2-14), K100-02 (15-27), K100-03 (28-40), K100-04 (41-53), at reasoning effort max, with notes and math notes;
  this sweep-3 reading (all 43 scans, raw `.tex`, ink checks above). Michel Hua's project not consulted for these readings.
- **Readings decided here:** 29 "a une section" (Pro wrong), 23 "S'_1 -> S'" in the ink (his slip) and "indique
  aisément" (Pro wrong), 13 "(SGA 1 VIII)" in the ink, 11 the overwritten "3".
- **Open readings:** 3 the cancelled b) and the margin §; 5 the cancelled margin; 15 the foot of the margin lemma; 17-19
  the uniqueness phrase ("toute composante ponctuelle | point associé"); 31 "Spf B|R"; 37 the 2° exponent (H^1 by the
  mathematics); 41-45 several single words ("rationnellement projectif", "intrinsèques | intéressantes", "V^t | pts").
- **Ready for an edition:** yes as a transcription edition of his pages, with these notes: the sheet order and pairing,
  the dating (not March 1967), the counterexample to 2) for non-reduced S, the slips of rows 3, 6, 7, the reference of
  row 5, and the parse of Z on 21. The even scans are reused paper; only the EGA letter and errata (18, 40, 42, 44) are
  his text and belong to the EGA material.
