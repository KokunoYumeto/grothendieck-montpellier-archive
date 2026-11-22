# Proof compendium for both uploaded files

This document compiles the theorem-like statements (theorems, propositions, corollaries, lemmas) from both uploaded files and preserves the source numbering. Where the markdown source stated a corollary without an explicit proof, I supplied a short proof from the immediately preceding results. Definitions are omitted except where they are needed inside a proof.

## Source 1: `globalization_note.pdf`

Proposition 1.2. The structure (S, ⊕, ·, τ, 1) is a commutative unital semiring.
Proof. Let
D := {(0, 0)} ∪ (Z × {1}) ⊂ Z × B,
where B = {0, 1} is the Boolean semiring, written additively and multiplicatively in the usual
way. The subset D is closed under the componentwise operations of Z × B:
(n, 1) + (m, 1) = (n + m, 1),

(n, 1) + (0, 0) = (n, 1),

(n, 1)(m, 1) = (nm, 1),

(n, 1)(0, 0) = (0, 0),

(0, 0) + (0, 0) = (0, 0),
(0, 0)(0, 0) = (0, 0).

Define
ι : S −→ D,

ι(τ ) = (0, 0),

ι(n) = (n, 1) (n ∈ Z).

This is bijective, and the transported operations are exactly ⊕ and ·. Since D is a subsemiring
of the commutative unital semiring Z × B, the same is true of S.

---

Proposition 1.3. The map
p : S −→ Z,

p(τ ) = 0,

p(n) = n (n ∈ Z),

is a surjective semiring homomorphism. Its kernel ideal is
A := {0, τ }.
Moreover, A is a subsemiring of S and

A∼
=B

as semirings.
Proof. Surjectivity is immediate. For m, n ∈ Z one has
p(m ⊕ n) = m + n = p(m) + p(n),

p(mn) = mn = p(m)p(n).

Also,
p(m ⊕ τ ) = p(m) = m = p(m) + 0 = p(m) + p(τ ),
p(mτ ) = p(τ ) = 0 = p(m) · 0 = p(m)p(τ ),
and similarly for the remaining cases. Hence p is a semiring homomorphism.
Its kernel is
ker p = {x ∈ S : p(x) = 0} = {0, τ } = A.
The set A is closed under both operations because
0 ⊕ 0 = 0,

0 ⊕ τ = 0,

τ ⊕ τ = τ,

0 · 0 = 0,

0 · τ = τ,

τ · τ = τ.

Thus A is a subsemiring. Define
ψ : A −→ B,

ψ(τ ) = 0,

ψ(0) = 1.

By inspection of the operation tables, ψ preserves addition and multiplication and is bijective;
therefore A ∼
= B.

---

Proposition 1.4. There is no unital semiring homomorphism B → S.
Proof. Assume that f : B → S is a unital semiring homomorphism. Then
f (1) = 1.
Since 1 + 1 = 1 in B, additivity gives
1 = f (1) = f (1 + 1) = f (1) ⊕ f (1) = 1 ⊕ 1 = 2,
a contradiction.

---

Proposition 1.5. Let {±1} act on S by multiplication. Then
S {±1} = {0, τ } = A ∼
= B.
Proof. An element x ∈ S is fixed if and only if (−1)x = x. If x = n ∈ Z, then (−1)x = −n, and
−n = n ⇐⇒ 2n = 0 ⇐⇒ n = 0.
If x = τ , then (−1)τ = τ by definition. Hence the fixed set is {0, τ } = A, which is Boolean by

---

Theorem 2.2. Every ideal I ⊆ S is either {τ } or In for a unique integer n ≥ 0. Equivalently,
{
} {
}
Id(S) = {τ } ∪ J ∪ {τ } : J ◁ Z .
In particular, every ideal of S is principal.
Proof. Let I be an ideal of S. Since τ = 0S , one has τ ∈ I. Set
J := I ∩ Z.
If J = ∅, then I = {τ }. Assume now that J 6= ∅. We claim that J ◁ Z. Indeed, if a, b ∈ J,
then a, b ∈ I, and therefore
a + b = a ⊕ b ∈ I.
Since a + b ∈ Z, it follows that a + b ∈ J. Next, if r ∈ Z and a ∈ J, then
ra = r · a ∈ I,
and again ra ∈ Z, so ra ∈ J. Hence J is an ideal of Z.
Conversely,
I = (I ∩ Z) ∪ {τ } = J ∪ {τ }.
Since every ideal of Z has the form nZ for a unique n ≥ 0, every ideal of S has the form In or
{τ }.

It remains to verify that J ∪ {τ } is indeed an ideal whenever J ◁ Z. Let x, y ∈ J ∪ {τ }. If
both are in J, then x ⊕ y = x + y ∈ J ⊆ J ∪ {τ }. If one of them is τ , then x ⊕ y equals the
other one, hence again lies in J ∪ {τ }. Finally, for any s ∈ S and x ∈ J ∪ {τ }, the product sx
lies in J ∪ {τ }: if x = τ , then sx = τ ; if x ∈ J and s ∈ Z, then sx ∈ J; if x ∈ J and s = τ , then
sx = τ .

---

Corollary 2.3. The prime ideals of S are exactly
Pτ := {τ },

P0 := {0, τ },

Pp := pZ ∪ {τ } (p prime in Z).

Proof. By Theorem 2.2, every proper ideal of S has the form J ∪ {τ }, where J is a proper ideal
of Z, or else {τ }.
First, {τ } is prime. Indeed, if ab = τ , then by definition of multiplication in S, one of a, b
equals τ .
Next, let J ⊊ Z be an ideal, and consider I = J ∪ {τ }. We show that I is prime if and only
if J is prime in Z. Suppose first that I is prime. If ab ∈ J with a, b ∈ Z, then ab ∈ I, so a ∈ I
or b ∈ I. Since a, b ∈ Z, this means a ∈ J or b ∈ J. Thus J is prime.
Conversely, assume that J is prime in Z. Let a, b ∈ S with ab ∈ I. If one of a, b equals τ ,
then that element already belongs to I. Otherwise a, b ∈ Z, so ab ∈ J, and primality of J gives
a ∈ J or b ∈ J, hence a ∈ I or b ∈ I.
The prime ideals of Z are (0) and (p) for prime numbers p. This yields precisely the listed
primes.

---

Corollary 2.4. The Krull dimension of S is
dim S = 2.
More precisely,
Pτ ⊊ P0 ⊊ Pp
for every prime number p, and there is no strictly longer chain of prime ideals.
Proof. The displayed chain is immediate from the descriptions in Corollary 2.3. Hence dim S ≥
2.
On the other hand, Corollary 2.3 lists all prime ideals of S. The ideal Pτ is contained in
every prime ideal. Among the remaining primes, P0 is contained in each Pp , while distinct ideals
Pp and Pq with p 6= q are incomparable. Therefore no chain can have length exceeding 2.

3. Divisibility, congruences, and zeta

---

Proposition 3.1. The group of units of S is
S × = {±1}.
The irreducible elements of S are exactly ±p, where p ranges over the prime numbers.
Proof. If u ∈ S is a unit, there exists v ∈ S with uv = 1. Since τ · x = τ for all x, necessarily
u, v ∈ Z. Then uv = 1 in Z, so u = ±1.
Now let x ∈ S be irreducible. Then x 6= τ and x is not a unit, so x ∈ Z \ {0, ±1}. Write
x = ab in Z. This is also a factorization in S. Irreducibility of x in S implies that one of a, b is
a unit of S, hence ±1. Therefore x is irreducible in Z, so x = ±p.

Conversely, let x = ±p with p prime. If x = ab in S, then a, b 6= τ , because otherwise ab = τ .
Hence a, b ∈ Z, and the factorization occurs already in Z. Since ±p is irreducible in Z, one of
a, b equals ±1, hence is a unit of S.

---

Theorem 3.2. The element 0 ∈ Z ⊂ S is prime in the divisibility sense but not irreducible.
Consequently S is not a unique factorization semiring.
Proof. First we show that 0 is not irreducible. One has
0 = 2 · 0,
and neither factor is a unit of S. Thus 0 is reducible.
Now we show that 0 is prime. Suppose
0 | ab.
By definition, this means that there exists c ∈ S such that
ab = 0 · c.
If c = τ , then 0 · c = τ ; if c ∈ Z, then 0 · c = 0. Hence
ab ∈ {0, τ }.
If both a and b lie in Z \ {0}, then ab ∈ Z \ {0}, contradiction. Therefore at least one of a, b
belongs to {0, τ }. If a = 0, then 0 | a via a = 0 · 1. If a = τ , then 0 | a via a = 0 · τ . The same
argument applies to b. Thus
0 | ab =⇒ 0 | a or 0 | b,
so 0 is prime.
Finally, in any factorization of a product of irreducibles in S, each factor is of the form ±p
by Proposition 3.1; their product is then a nonzero integer, never equal to 0. Hence the nonunit
element 0 admits no factorization into irreducibles. Therefore unique factorization fails.
Definition 3.3. For n ≥ 0, define a relation ρn on S by
x ρn y ⇐⇒

(

)
(
x = y = τ or x, y ∈ Z and x ≡ y

)
(mod n) .

For n ≥ 0, define
πn : S −→ Z/nZ
by
πn (τ ) = 0̄,

πn (m) = m̄ (m ∈ Z),

where for n = 0 we interpret Z/0Z as Z itself. Let ρ′n be the congruence induced by πn :
x ρ′n y ⇐⇒ πn (x) = πn (y).

---

Theorem 3.4. Every congruence on S is either ρn or ρ′n for a unique n ≥ 0. Moreover:
S/ρn ∼
= G(Z/nZ)
S/ρ′n ∼
= Z/nZ

(n ≥ 0),
(n ≥ 0).

In particular,

S/ρ′0 ∼
= Z.

Proof. Let ∼ be a congruence on S. Its restriction to Z ⊂ S is a ring congruence on Z, hence
there exists a unique n ≥ 0 such that for a, b ∈ Z,
a ∼ b ⇐⇒ a ≡ b

(mod n).

We now distinguish two cases.
Case 1: τ 6∼ 0. We claim that τ is equivalent to no integer. Indeed, if m ∈ Z and m ∼ τ ,
then adding −m to both sides yields
0 = m ⊕ (−m) ∼ τ ⊕ (−m) = −m.
Since −m ∈ Z, this implies −m ≡ 0 (mod n), hence −m ∼ 0. By transitivity, τ ∼ 0, contradiction. Therefore the ∼-class of τ is {τ }, and all other classes are the residue classes modulo n
inside Z. Hence ∼= ρn .
The quotient S/ρn has one distinguished zero class [τ ] and residue classes [0], [1], . . . , [n − 1]
coming from Z. The operations are exactly those of the globalization G(Z/nZ), so
S/ρn ∼
= G(Z/nZ).
Case 2: τ ∼ 0. Then for m ∈ Z,
m ∼ τ ⇐⇒ m ∼ 0 ⇐⇒ n | m.
Hence the class of τ is
In = nZ ∪ {τ }.
Since the restriction of ∼ to Z is still congruence modulo n, the classes are exactly In together
with the nonzero residue classes modulo n. Therefore ∼= ρ′n .
By construction, ρ′n is the kernel congruence of πn , so the first isomorphism theorem for
semirings gives
S/ρ′n ∼
= im(πn ) = Z/nZ.
When n = 0, this reads S/ρ′0 ∼
= Z.

---

Corollary 3.5. Let
ζS (s) :=

∑

N (I)−s ,

I

where the sum runs over ideals of finite norm and
N (I) := |S/ρI |
for the quotient by the congruence naturally associated to I. Then
∑
n−s = ζ(s).
ζS (s) =
n≥1

Proof. By Theorem 2.2, the ideals are {τ } and In for n ≥ 0. The ideal {τ } has quotient S
itself, hence infinite norm. The ideal I0 = {0, τ } has quotient Z by Theorem 3.4, hence infinite
norm. For n ≥ 1, the quotient by the congruence associated to In is Z/nZ, again by Theorem

3.4. Therefore
N (In ) = |Z/nZ| = n
and so
ζS (s) =

∑

(n ≥ 1),

n−s = ζ(s).

n≥1

4. Localization and local stalks
Localization of semirings is standard; cf. Golan [2, Ch. 17]. In the present situation, the proofs
are completely explicit.

---

Theorem 4.1. Let M ⊆ Z be a multiplicative subset with 0 ∈
/ M . Then the localization SM is
canonically isomorphic to
G(ZM ).
Proof. Recall that SM is the quotient of S × M by the relation
(r1 , m1 ) ∼ (r2 , m2 ) ⇐⇒ ∃k ∈ M : k(r1 m2 ) = k(r2 m1 ).
Because 0 ∈
/ M , every k ∈ M is a nonzero integer.
Define
Φ : SM −→ G(ZM )
by
Φ([τ, m]) = τ,

Φ([r, m]) = r/m

(r ∈ Z).

We first show that Φ is well defined. Suppose (r1 , m1 ) ∼ (r2 , m2 ). If r1 = τ , then
k(r1 m2 ) = kτ = τ.
Hence k(r2 m1 ) = τ , which is impossible when r2 ∈ Z, because then r2 m1 ∈ Z and multiplication
by the nonzero integer k stays in Z. Therefore r2 = τ as well. Thus all classes represented by
(τ, m) map to τ .
Now assume r1 , r2 ∈ Z. Then the equality
k(r1 m2 ) = k(r2 m1 )
holds in Z, and since k 6= 0, cancellation in the integral domain Z gives
r1 m2 = r2 m1 .
Hence r1 /m1 = r2 /m2 in ZM .
The map Φ is a semiring homomorphism by direct calculation on representatives. It is
surjective because every element of G(ZM ) is either τ or a fraction r/m with r ∈ Z, m ∈ M . It
is injective by the same argument used for well-definedness: if two non-τ classes have the same
image, then they satisfy cross-multiplication in Z, hence are equivalent in the localization; and
the class of τ cannot coincide with a class represented by an integer.

---

Theorem 4.2. If one localizes at the full multiplicative subset Z ⊂ S, then
Frac(S) = SZ ∼
= B.

Proof. We write classes in SZ as [r, m] with r ∈ S, m ∈ Z. First,
C0 := [τ, 1]
is a class represented only by pairs (τ, m). Indeed, if [r, m] = [τ, 1], then there exists k ∈ Z such
that
k(r · 1) = k(τ · m) = kτ = τ.
If r ∈ Z, the left-hand side is either an integer or 0, never τ . Hence r = τ .
Now let
C1 := [1, 1].
We claim that every class represented by an integer numerator equals C1 . Let [r1 , m1 ] and
[r2 , m2 ] have r1 , r2 , m1 , m2 ∈ Z. Taking k = 0 ∈ Z in the localization relation gives
0(r1 m2 ) = 0 = 0(r2 m1 ),
so [r1 , m1 ] = [r2 , m2 ]. Thus all such pairs lie in a single class, namely C1 .
The classes C0 and C1 are distinct. If [τ, 1] = [1, 1], there would exist k ∈ Z with
kτ = k,
which is impossible because the left-hand side is always τ and the right-hand side lies in Z.
Therefore SZ has exactly two elements. Their operations are forced:
C0 + C0 = C0 ,

C 0 + C1 = C1 ,

C0 C0 = C0 ,

C 0 C1 = C0 ,

C1 + C1 = [2, 1] = C1 ,
C 1 C1 = C1 .

This is exactly the Boolean semiring B.

---

Corollary 4.3. Let O be the structure sheaf of Spec(S). Then
OP τ ∼
= B,

OP 0 ∼
= G(Q),

OP p ∼
= G(Z(p) ).

Proof. By definition, the stalk at a prime ideal P is the localization at the complement S \ P .
For Pτ = {τ }, one has S \ Pτ = Z, so
OP τ ∼
= SZ ∼
=B
by Theorem 4.2.
For P0 = {0, τ }, the complement is Z \ {0}, which is multiplicative and avoids 0. Hence by

---

Theorem 5.2. The prime ideals of the commutative monoid M = (Z, ×) are exactly the sets
PΣ with Σ ⊆ P. The inclusion relation is
PΣ1 ⊆ PΣ2 ⇐⇒ Σ1 ⊆ Σ2 .
Consequently,
dim Spec(M ) = ∞.
Proof. We first verify that each PΣ is a prime ideal. If n ∈ PΣ and m ∈ Z, then some p ∈ Σ
divides n, hence divides mn, so mn ∈ PΣ . Thus PΣ is an ideal of the monoid. It is proper
because 1 ∈
/ PΣ . Now assume ab ∈ PΣ . Then some p ∈ Σ divides ab, and primality of p in Z
gives p | a or p | b. Hence a ∈ PΣ or b ∈ PΣ . Therefore PΣ is prime.
Conversely, let P be a prime ideal of M . If P = {0}, then P = P∅ . Assume P 6= {0}. Define
Σ(P ) := {p ∈ P : p ∈ P }.
We claim that P = PΣ(P ) . First, if p ∈ Σ(P ), then p ∈ P , and ideality gives pZ ⊆ P . Therefore
PΣ(P ) ⊆ P .
For the reverse inclusion, let x ∈ P \ {0}. Write
x = ±p1 · · · pr
as a prime factorization in Z. Since P is prime and x ∈ P , repeated use of primality shows that
one of the factors ±pi belongs to P . If −pi ∈ P , then multiplying by −1 ∈ M yields
(−1)(−pi ) = pi ∈ P.
Hence some prime number pi belongs to P , i.e. pi ∈ Σ(P ). Since pi | x, one has x ∈ pi Z ⊆ PΣ(P ) .
Therefore P ⊆ PΣ(P ) , and the classification follows.
The inclusion criterion is immediate from the classification: if Σ1 ⊆ Σ2 , then PΣ1 ⊆ PΣ2 .
Conversely, if PΣ1 ⊆ PΣ2 and p ∈ Σ1 , then p ∈ PΣ1 ⊆ PΣ2 , so some q ∈ Σ2 divides p; necessarily
q = p, hence p ∈ Σ2 .
Choose distinct primes p1 , p2 , . . ., and set Σn = {p1 , . . . , pn }. Then
P∅ ⊊ PΣ1 ⊊ PΣ2 ⊊ · · ·
is an infinite strictly increasing chain of prime ideals. Thus dim Spec(M ) = ∞.


---

Corollary 5.3. The prime ideals of MS are exactly
{τ }

and PΣ ∪ {τ }

(Σ ⊆ P).

Hence
dim Spec(MS ) = ∞.
The unique maximal prime ideal of MS is
(Z \ {±1}) ∪ {τ }.
Proof. Every prime ideal of MS contains τ , because τ is the absorbing element. If P ′ is prime
in MS , then P := P ′ ∩ Z is prime in M , and
P ′ = P ∪ {τ }.
Conversely, if P is prime in M , then P ∪ {τ } is prime in MS by a direct case distinction on
whether one of the factors is τ . The classification follows from Theorem 5.2. The dimension
statement follows immediately.
For maximality, take Σ = P. Then
PP = {n ∈ Z : some prime divides n} = Z \ {±1},
and every other PΣ is contained in it.

---

Corollary 5.4. The topological spaces Spec(S) and Spec(MS ) are not homeomorphic.
Proof. Krull dimension is a homeomorphism invariant. By Corollary 2.4,
dim Spec(S) = 2,
whereas by Corollary 5.3,
dim Spec(MS ) = ∞.
Hence the spaces cannot be homeomorphic.

---

Theorem 5.5. Let Z0 [MS ] be the contracted monoid algebra of MS , i.e.
Z0 [MS ] := Z[MS ]/([τ ]).
Then

Z0 [MS ] ∼
= Z[M ] ∼
= Z × Z[M × ],

where M × = Z \ {0} is the multiplicative monoid of nonzero integers. Consequently,
(
)
Spec(Z0 [MS ]) ∼
= Spec(Z) t Spec Z[M × ] .
Proof. The first isomorphism is immediate from the definition of the contracted monoid algebra:
quotienting Z[MS ] by [τ ] kills the absorbing basis element and leaves the monoid ring on the
remaining monoid M = (Z, ×).
For the second isomorphism, define
Φ : Z[M ] −→ Z × Z[M × ]

on basis elements by
Φ([0]) = (1, 0),

Φ([n]) = (1, [n])

(n ∈ Z \ {0}),

and extend Z-linearly. Thus, for a general element
∑
α = a0 [0] +
an [n],
n̸=0

one has

(
)
∑
∑
Φ(α) = a0 +
an ,
an [n] .
n̸=0

n̸=0

We verify multiplicativity on basis elements. If one factor is [0], then
[0][m] = [0]
in Z[M ], while
Φ([0])Φ([m]) = (1, 0) · Φ([m]) = (1, 0) = Φ([0]).
If m, n 6= 0, then
Φ([m])Φ([n]) = (1, [m])(1, [n]) = (1, [mn]) = Φ([mn]).
Thus Φ is a ring homomorphism.
It is bijective with inverse
Ψ : Z × Z[M × ] −→ Z[M ],
( ∑
) (
∑ )
∑
Ψ c,
bn [n] = c −
bn [0] +
bn [n].
n̸=0

n̸=0

n̸=0

A direct calculation shows Ψ ◦ Φ = id and Φ ◦ Ψ = id.
Finally, the spectrum of a product of rings is the disjoint union of the spectra of the factors.
Therefore
(
)
Spec(Z0 [MS ]) ∼
= Spec(Z) t Spec Z[M × ] .

Remark 5.6. By the semiring embedding into the category of blueprints, a semiring determines
a blueprint whose underlying monoid is its multiplicative monoid and whose pre-addition records
exactly the additive relations; see Lorscheid [3, §4.1.1] and [4, §4]. In the present case, the
associated blueprint BS has underlying monoid MS and pre-addition generated by the relations
[a] + [b] ≡ [a + b]

(a, b ∈ Z)

and
[x] + [τ ] ≡ [x]

(x ∈ MS ).

This isolates formally the distinction between the semiring geometry of S and the monoid
geometry of MS .

6. Extension to rings of integers
Let K be a number field, and let OK be its ring of integers. Standard facts on OK may be
found in Neukirch [5, Chs. I–VII].

Definition 6.1. Define
S(OK ) := OK t {τ },
with the same rules as before:
x⊕y =x+y
xy = xy

(x, y ∈ OK ),

(x, y ∈ OK ),

x ⊕ τ = x,

τ ⊕ τ = τ,

xτ = τ x = τ,

τ 2 = τ.

---

Theorem 6.2. The ideals of S(OK ) are exactly
{τ }

and IJ := J ∪ {τ },

where J ranges over the ideals of OK . The prime ideals are exactly
{τ },

{0} ∪ {τ },

p ∪ {τ } (p 6= 0 prime in OK ).

In particular,
dim S(OK ) = 2.
If OK is a PID, then S(OK ) is a principal ideal semiring.
Proof. The proof of the ideal classification is verbatim the same as for Z: every ideal contains
τ , its intersection with OK is an ideal of OK , and conversely every J ∪ {τ } is an ideal.
The prime ideal classification is also the same as before. The ideal {τ } is prime because a
product equals τ if and only if one factor equals τ . For a proper ideal J ⊊ OK , the ideal J ∪ {τ }
is prime in S(OK ) if and only if J is prime in OK , by the same argument as in the proof of

---

Theorem 6.4. There is a canonical isomorphism of commutative monoids
Cl(S(OK )) ∼
= Cl(K).
Proof. For a nonzero ideal J ⊆ OK , let
IJ := J ∪ {τ }.
Define
Φ : Cl(K) −→ Cl(S(OK )),

[J] 7−→ [IJ ].

We first show that Φ is well defined. If [J1 ] = [J2 ] in Cl(K), then there exist a, b ∈ OK \ {0}
such that
aJ1 = bJ2 .
Therefore
aIJ1 = a(J1 ∪ {τ }) = (aJ1 ) ∪ {τ } = (bJ2 ) ∪ {τ } = bIJ2 ,
so [IJ1 ] = [IJ2 ] in Cl(S(OK )).
Next, Φ is multiplicative because
IJ1 IJ2 = (J1 ∪ {τ })(J2 ∪ {τ }) = J1 J2 ∪ {τ } = IJ1 J2 .
To prove injectivity, suppose [IJ1 ] = [IJ2 ]. Then there exist a, b ∈ OK \ {0} such that
aIJ1 = bIJ2 .
Intersecting both sides with OK gives
aJ1 = bJ2 ,
so [J1 ] = [J2 ] in Cl(K).
For surjectivity, let [I] ∈ Cl(S(OK )). Since I is a nonzero ideal, the ideal classification from

---

Theorem 6.5. The ideal zeta function of S(OK ) is the Dedekind zeta function of K:
ζS(OK ) (s) = ζK (s).
Proof. For each nonzero ideal J ⊆ OK , define the semiring morphism
πJ : S(OK ) −→ OK /J
by
πJ (τ ) = 0,

πJ (x) = x mod J

(x ∈ OK ).

The verification that πJ is a surjective semiring homomorphism is immediate. Its kernel is
exactly
IJ = J ∪ {τ }.
Hence the quotient by the corresponding congruence is isomorphic to OK /J, and the norm of
IJ is
N (IJ ) = |OK /J| = N (J).
The ideals of finite norm are exactly the IJ with J 6= 0; the ideal {τ } has infinite quotient.
Therefore
∑
∑
ζS(OK ) (s) =
N (IJ )−s =
N (J)−s = ζK (s).
0̸=J◁OK

0̸=J◁OK

×

---

Corollary 6.6. Under the action of OK
on S(OK ) by multiplication, the fixed-point subsemiring
is
×
S(OK )OK = {0, τ } ∼
= B.

Proof. Certainly 0 and τ are fixed. If x ∈ OK is fixed by every unit, then in particular it is

×
fixed by −1 ∈ OK
, so

−x = x.

Since OK has characteristic 0, this implies x = 0. Thus the fixed set is {0, τ }, which is Boolean
by the same two-element table as before.

Acknowledgment on provenance
The proofs above are self-contained. The original note was based on a conceptual structure generated by Gemini DeepThink 2.5, the article cites only published literature: semiring background
from Golan [2], monoidal F1 -geometry from Deitmar [1], blueprint formalism from Lorscheid
[3, 4], and algebraic number theory from Neukirch [5].

References
[1] A. Deitmar, Schemes over F1 , in Number Fields and Function Fields—Two Parallel Worlds,
Progr. Math. 239, Birkhäuser Boston, Boston, MA, 2005, pp. 87–100.
[2] J. S. Golan, Semirings and Their Applications, Kluwer Academic Publishers, Dordrecht,
1999.
[3] O. Lorscheid, A blueprinted view on F1 -geometry, in K. Thas (ed.), Absolute Arithmetic
and F1 -Geometry, EMS Congress Reports, European Mathematical Society, Zürich, 2016,
pp. 161–220.
[4] O. Lorscheid, The geometry of blueprints. Part I: Algebraic background and scheme theory,
Adv. Math. 229 (2012), no. 3, 1804–1846.
[5] J. Neukirch, Algebraic Number Theory, Grundlehren der Mathematischen Wissenschaften
322, Springer-Verlag, Berlin, 1999.


---

## Source 2: `ChatGPT-Error correction and review (12).md`

Proposition A.1. The claim that “ $\tau$  is not a multiplicative absorber globally” is false.

Proof. The note defines

$$
m\cdot \tau=\tau\cdot m=\tau,\qquad \tau\cdot\tau=\tau
$$

for all  $m\in \mathbf Z$ . Thus  $\tau$  is a multiplicative absorber by definition.

globalization\_note

The contrary statement appears in the markdown thread.

ChatGPT-Implications Beyond the…

---

Proposition A.2. The claim that  $\operatorname{Spec}(S)$  has “two distinct generic points” is false if interpreted as generic points of the whole space.

Proof. The note proves that the prime ideals are exactly

$$
P_\tau=\{\tau\},\qquad P_0=\{0,\tau\},\qquad P_p=p\mathbf Z\cup\{\tau\}\quad(p\text{ prime}),
$$

with chains

$$
P_\tau\subsetneq P_0\subsetneq P_p.
$$

Hence  $P_\tau$  is contained in every prime ideal, so  $P_\tau$  is the unique generic point of the whole spectrum.

globalization\_note

What is true is that  $P_0$  is the generic point of the closed subspace

$$
V(P_0)=\{P_0\}\cup\{P_p\},
$$

which is the arithmetic stratum identified with  $\operatorname{Spec}(\mathbf Z)$ . This corrected statement was reached only later in the markdown thread.

ChatGPT-Implications Beyond the…

The earlier “dual generic points” formulation was therefore incorrect.

ChatGPT-Implications Beyond the…

---

Proposition A.3. The residue objects

$$
\kappa(P_\tau)=\mathbf B,\qquad \kappa(P_0)=\mathbf Q,\qquad \kappa(P_p)=\mathbf F_p
$$

are correct, but the prior thread’s implied chain

$$
\mathbf B\to \mathbf Q\to \mathbf F_p
$$

as a chain of natural unital local morphisms is false.

Proof. The note proves the stalk identifications

$$
\mathcal O_{P_\tau}\cong \mathbf B,\qquad \mathcal O_{P_0}\cong G(\mathbf Q),\qquad \mathcal O_{P_p}\cong G(\mathbf Z_{(p)}),
$$

hence the residue objects above.

However, the natural specialization/localization maps go in the opposite semiring direction:

$$
G(\mathbf Z_{(p)})\longrightarrow G(\mathbf Q)\longrightarrow \mathbf B.
$$

There is no unital semiring map  $\mathbf B\to G(R)$  for any nonzero ring  $R$ , and the note proves this for  $R=\mathbf Z$ .

globalization\_note

So the objects  $\mathbf B,\mathbf Q,\mathbf F_p$  are the correct residue objects, but the earlier displayed chain treated them too loosely. The relevant semiring chain is through the stalks, not through unital maps  $\mathbf B\to G(\mathbf Q)\to G(\mathbf Z_{(p)})$ . The incorrect formulation appears in the markdown thread.

---

Proposition A.4. The claim that the classical spectrum embeds as an “open and dense” subspace is false.

Proof. The corrected theorem is

$$
Y_R:=V(\{0,\tau\})=\{P_{\mathfrak p}:\mathfrak p\in \operatorname{Spec}(R)\},
$$

and  $Y_R$  is a closed subspace canonically homeomorphic to  $\operatorname{Spec}(R)$ . In the case  $R=\mathbf Z$ , this gives the closed arithmetic stratum

$$
V(P_0)=\{P_0\}\cup\{P_p\}\cong \operatorname{Spec}(\mathbf Z).
$$

By contrast, the singleton

$$
\{P_\tau\}=D(0)
$$

is open and dense. This is exactly the opposite of the earlier mistaken audit phrase. The corrected argument appears later in the markdown thread, and the note supports the  $D(0)$  computation through its prime classification.

---

Proposition A.5. The statements about a “place at  $\mathbf F_1$ ”, a “boundary extension”

$$
(0,\infty)\sqcup\{\infty_{\mathrm{ar}},\infty_{\mathrm{abs}}\},
$$

a “second Archimedean axis”, or cohomological/thin-group analogies are not theorems of the note and have no demonstrated mathematical status in the thread.

Proof. The note proves concrete statements about ideals, prime ideals, congruences, localizations, monoid prime spectra, contracted monoid algebras, and extensions to rings of integers. It does not define any such boundary extension or prove any such interpretation. Its only formal  $\mathbf F_1$ \-geometric remark is the blueprint remark, namely that semiring geometry differs from bare monoid geometry and that the associated blueprint remembers the pre-addition.

The speculative formulations occur only in the markdown thread and are unsupported.

---

Proposition A.6. The prior thread’s generalization of the factorization failure from  $\mathbf Z$  to arbitrary rings was overstated; the clean theorem requires an integral domain hypothesis.

Proof. The note proves for  $S=G(\mathbf Z)$  that  $0\in \mathbf Z\subset S$  is prime in the divisibility sense but not irreducible, so  $S$  is not a unique factorization semiring.

globalization\_note

The same proof extends to any integral domain, but not verbatim to rings with zero divisors, because the step “if  $ab\in\{0,\tau\}$  then one factor lies in  $\{0,\tau\}$ ” uses domain cancellation/absence of zero divisors. So the domain hypothesis is essential for the clean general theorem below.

---

Proposition A.7. The only canonical zeta function proved in the note is the ideal zeta

$$
\zeta_S(s)=\zeta(s)
$$

and, for  $S(\mathcal O_K)$ , the Dedekind zeta

$$
\zeta_{S(\mathcal O_K)}(s)=\zeta_K(s).
$$

Proof. This is exactly Corollary 3.5 for  $\mathbf Z$  and Theorem 6.5 for  $\mathcal O_K$ .

The later thread’s “refined congruence zeta” such as  $2\zeta(s)-1$  is not in the note and was introduced without a canonical definition. It must therefore be withdrawn as part of the formal correction.

ChatGPT-Implications Beyond the…

II. The corrected structure for the globalization construction over an arbitrary ring

From now on, let  $R$  be a nonzero commutative ring with identity. Define

$$
G(R):=R\sqcup\{\tau\},
$$

with operations

$$
r\oplus s=r+s,\qquad r\oplus\tau=r,\qquad \tau\oplus\tau=\tau,
$$

and

$$
rs=rs,\qquad r\tau=\tau r=\tau,\qquad \tau^2=\tau.
$$

This is the obvious generalization of the note’s construction. For  $R=\mathbf Z$  and  $R=\mathcal O_K$ , all of the specialized statements below recover what the note proves.

1.  Canonical maps

Definition B.1. Define

$$
p_R:G(R)\to R,\qquad p_R(\tau)=0,\quad p_R(r)=r,
$$

and

$$
\chi_R:G(R)\to \mathbf B,\qquad \chi_R(\tau)=0,\quad \chi_R(r)=1\ \ (r\in R),
$$

where  $\mathbf B=\{0,1\}$  is the Boolean semiring.

---

Proposition B.2. Both  $p_R$  and  $\chi_R$  are unital semiring homomorphisms.

Proof. For  $p_R$ , additivity and multiplicativity are immediate from the definitions:

$$
p_R(r\oplus s)=r+s=p_R(r)+p_R(s),\qquad p_R(r\tau)=0=p_R(r)p_R(\tau),
$$

and similarly in all other cases. Also  $p_R(\tau)=0_R$ ,  $p_R(1_R)=1_R$ .

For  $\chi_R$ , note that every supported element maps to  $1$ , while  $\tau$  maps to  $0$ . Then:

$$
\chi_R(r\oplus s)=1=1+1,\qquad \chi_R(r\oplus \tau)=1=1+0,
$$

and

$$
\chi_R(rs)=1=1\cdot 1,\qquad \chi_R(r\tau)=0=1\cdot 0,
$$

with the remaining cases immediate. Also  $\chi_R(\tau)=0$  and  $\chi_R(1_R)=1$ . ∎

---

Proposition B.3. The map

$$
(p_R,\chi_R):G(R)\to R\times \mathbf B
$$

is injective, and its image is

$$
D_R:=\{(0,0)\}\cup (R\times\{1\}).
$$

Proof. If  $x=\tau$ , then  $(p_R,\chi_R)(x)=(0,0)$ . If  $x=r\in R$ , then  $(p_R,\chi_R)(x)=(r,1)$ . Hence the image is exactly  $D_R$ .

Injectivity is immediate:  $(0,0)$  has only preimage  $\tau$ , while  $(r,1)$  has only preimage  $r\in R$ . ∎

Thus  $G(R)$  is not mysterious: it is precisely the subsemiring

$$
D_R=\{(0,0)\}\cup (R\times\{1\})\subset R\times\mathbf B.
$$

What the construction does is split the zero fiber of  $R$  into the two points  $(0,1)$  and  $(0,0)$ .

2.  Universal ring quotient

---

Proposition B.4. For every commutative ring  $A$ , composition with  $p_R$  induces a bijection

$$
\operatorname{Hom}_{\mathrm{Ring}}(R,A)\xrightarrow{\sim}\operatorname{Hom}_{\mathrm{SemiRing}}(G(R),A).
$$

Proof. Let  $f:G(R)\to A$  be a semiring homomorphism. Since  $f$  preserves semiring zero,

$$
f(\tau)=0_A.
$$

Also,

$$
f(0_R)=f(0_R\oplus 0_R)=f(0_R)+f(0_R),
$$

so subtraction in the ring  $A$  gives  $f(0_R)=0_A$ .

Define  $\bar f:R\to A$  by  $\bar f(r)=f(r)$ . Then for  $r,s\in R$ ,

$$
\bar f(r+s)=f(r\oplus s)=f(r)+f(s)=\bar f(r)+\bar f(s),
$$
 
$$
\bar f(rs)=f(rs)=f(r)f(s)=\bar f(r)\bar f(s),
$$

and  $\bar f(1)=f(1)=1$ . Thus  $\bar f$  is a ring homomorphism. Finally,

$$
(\bar f\circ p_R)(\tau)=\bar f(0)=0_A=f(\tau),\qquad (\bar f\circ p_R)(r)=\bar f(r)=f(r),
$$

so  $f=\bar f\circ p_R$ . Uniqueness follows from surjectivity of  $p_R$ . ∎

Therefore  $R$  is the maximal ring quotient of  $G(R)$ . Every ring-valued invariant of  $G(R)$  factors through the collapse  $\tau\sim 0$ .

3.  Full faithfulness on the category of rings

---

Proposition B.5. For nonzero commutative rings  $R,R'$ , restriction induces a bijection

$$
\operatorname{Hom}_{\mathrm{SemiRing}}(G(R),G(R'))\xrightarrow{\sim}\operatorname{Hom}_{\mathrm{Ring}}(R,R').
$$

Proof. Let  $f:G(R)\to G(R')$  be a semiring homomorphism.

First,

$$
f(\tau)=\tau,
$$

because semiring homomorphisms preserve semiring zero.

Next,  $f(0_R)$  is additively idempotent:

$$
f(0_R)=f(0_R\oplus 0_R)=f(0_R)\oplus f(0_R).
$$

Using  $0_R=1_R\oplus (-1_R)$  inside the supported copy of  $R$ , one sees  $f(0_R)\neq \tau$ , for otherwise

$$
\tau=f(0_R)=f(1_R)\oplus f(-1_R)=1_{R'}\oplus f(-1_R),
$$

but the right side is supported, contradiction. Hence  $f(0_R)\in R'$ . Since the induced addition on supported elements is ring addition, the idempotence forces  $f(0_R)=0_{R'}$ .

Now suppose  $f(r)=\tau$  for some  $r\in R$ . Then

$$
\tau=f(r)=f(r\oplus 0_R)=f(r)\oplus f(0_R)=\tau\oplus 0_{R'}=0_{R'},
$$

contradiction. Hence  $f(R)\subset R'$ .

So the restriction  $f|_R:R\to R'$  preserves addition, multiplication, and unit, hence is a ring homomorphism.

Conversely, any ring homomorphism  $g:R\to R'$  extends uniquely to

$$
G(g):G(R)\to G(R'),\qquad G(g)(\tau)=\tau,\quad G(g)(r)=g(r),
$$

which is visibly a semiring homomorphism.

These two constructions are inverse. ∎

---

Corollary B.6.  $G(R)\cong G(R')$  as semirings if and only if  $R\cong R'$  as rings.

So the globalization construction is fully faithful on rings. It does not forget ring data; it adds one extra zero.

4.  Absence of Boolean base structure

**Proof.** If $G(R)\cong G(R')$ as semirings, Proposition B.5 identifies any semiring isomorphism with a ring isomorphism $R\to R'$. Conversely, any ring isomorphism $R\to R'$ extends uniquely to a semiring isomorphism $G(R)\to G(R')$ by sending $\tau$ to $\tau$. ∎


---

Proposition B.7. There is no unital semiring homomorphism

$$
\mathbf B\to G(R).
$$

Proof. Suppose  $v:\mathbf B\to G(R)$  is unital. Then  $v(1)=1_R$ . Since  $1+1=1$  in  $\mathbf B$ ,

$$
1_R=v(1)=v(1+1)=v(1)\oplus v(1)=1_R\oplus 1_R=1_R+1_R.
$$

Both summands lie in the supported copy of  $R$ , so the last equality is computed in the ring  $R$ . Subtracting  $1_R$  yields  $1_R=0_R$ , contradiction. ∎

---

Proposition B.8. There is no unital semiring homomorphism

$$
R\to \mathbf B.
$$

Proof. If  $u:R\to\mathbf B$  were such a homomorphism, then

$$
0=u(0)=u(1+(-1))=u(1)+u(-1)=1+u(-1)=1
$$

in  $\mathbf B$ , contradiction. ∎

Thus the Boolean semiring appears canonically inside the structure only as a quotient observable  $ \chi_R$ , not as a unital base object.

5.  Ideals and prime ideals

---

Theorem B.9. The ideals of  $G(R)$  are exactly

$$
\{\tau\}\quad\text{and}\quad I_J:=J\cup\{\tau\}\qquad (J\triangleleft R).
$$

Proof. Let  $I\subseteq G(R)$  be an ideal. Since  $\tau=0_{G(R)}$ , we have  $\tau\in I$ . Set  $J=I\cap R$ .

If  $J=\varnothing$ , then  $I=\{\tau\}$ . Otherwise, if  $a,b\in J$ , then  $a,b\in I$ , so

$$
a+b=a\oplus b\in I,
$$

hence  $a+b\in J$ . If  $r\in R$  and  $a\in J$ , then  $ra=r\cdot a\in I$ , hence  $ra\in J$ . So  $J\triangleleft R$ .

Conversely, for any ideal  $J\triangleleft R$ , the set  $J\cup\{\tau\}$  is clearly closed under  $\oplus$  and under multiplication by arbitrary elements of  $G(R)$ . ∎

---

Theorem B.10. The prime ideals of  $G(R)$  are exactly

$$
P_\tau:=\{\tau\} \quad\text{and}\quad P_{\mathfrak p}:=\mathfrak p\cup\{\tau\}\qquad (\mathfrak p\in\operatorname{Spec}(R)).
$$

Proof.  $P_\tau$  is prime because  $xy=\tau$  holds if and only if  $x=\tau$  or  $y=\tau$ .

Now let  $J\triangleleft R$  be proper. Then  $J\cup\{\tau\}$  is prime in  $G(R)$  iff  $J$  is prime in  $R$ . Indeed, if  $J\cup\{\tau\}$  is prime and  $ab\in J$  with  $a,b\in R$ , then  $ab\in J\cup\{\tau\}$ , so  $a\in J\cup\{\tau\}$  or  $b\in J\cup\{\tau\}$ , hence  $a\in J$  or  $b\in J$ . Conversely, if  $J$  is prime and  $xy\in J\cup\{\tau\}$ , then either one factor is  $\tau$ , or both factors lie in  $R$  and their product lies in  $J$ , which implies one factor lies in  $J$ . ∎

---

Corollary B.11. The map

$$
\iota:\operatorname{Spec}(R)\to \operatorname{Spec}(G(R)),\qquad \mathfrak p\mapsto P_{\mathfrak p},
$$

is an order embedding, and

$$
\operatorname{Spec}(G(R))=\{P_\tau\}\sqcup \iota(\operatorname{Spec}(R)).
$$

Proof. Immediate from the description above and

$$
P_{\mathfrak p}\subseteq P_{\mathfrak q}\iff \mathfrak p\subseteq \mathfrak q.
$$

Also  $P_\tau\subseteq P_{\mathfrak p}$  for every  $\mathfrak p$ , since  $\tau\in P_{\mathfrak p}$ . ∎

6.  Topology and dimension

---

Proposition B.12.  $P_\tau$  is the generic point of  $\operatorname{Spec}(G(R))$ , and

$$
D_{G(R)}(0_R)=\{P_\tau\}.
$$

Proof. Since  $P_\tau\subseteq Q$  for every prime  $Q$ , the closure of  $\{P_\tau\}$  is the whole space.

Now  $D(0_R)$  is the set of primes not containing the supported zero  $0_R\in R\subset G(R)$ . Every prime  $P_{\mathfrak p}$  contains  $0_R$ , but  $0_R\notin P_\tau=\{\tau\}$ . Hence

$$
D_{G(R)}(0_R)=\{P_\tau\}.
$$

So  $P_\tau$  is open as well as dense. ∎

---

Corollary B.13.  $\operatorname{Spec}(G(R))$  is irreducible, and every nonempty open subset contains  $P_\tau$ .

**Proof.** By Proposition B.12, $P_\tau$ is a generic point of $\operatorname{Spec}(G(R))$, so its closure is the whole space; hence the space is irreducible. Any nonempty open set in an irreducible space contains every generic point, in particular $P_\tau$. ∎


---

Proposition B.14. The subset

$$
Y_R:=\{P_{\mathfrak p}:\mathfrak p\in \operatorname{Spec}(R)\}
$$

is closed, namely

$$
Y_R=V(\{0_R,\tau\}),
$$

and  $Y_R$  is canonically homeomorphic to  $\operatorname{Spec}(R)$ .

Proof. A prime contains  $\{0_R,\tau\}$  iff it is not  $P_\tau$ . Hence  $Y_R=V(\{0_R,\tau\})$ .

The map  $\mathfrak p\mapsto P_{\mathfrak p}$  is bijective. Closed sets correspond because for every ideal  $J\triangleleft R$ ,

$$
V_R(J)\longleftrightarrow V_{G(R)}(J\cup\{\tau\})\cap Y_R.
$$

Thus the map is a homeomorphism. ∎

---

Theorem B.15. If  $R\neq 0$ , then

$$
\dim G(R)=\dim R+1.
$$

Proof. Any chain

$$
\mathfrak p_0\subsetneq \mathfrak p_1\subsetneq\cdots\subsetneq \mathfrak p_d
$$

in  $\operatorname{Spec}(R)$  yields

$$
P_\tau\subsetneq P_{\mathfrak p_0}\subsetneq\cdots\subsetneq P_{\mathfrak p_d}
$$

in  $\operatorname{Spec}(G(R))$ , so  $\dim G(R)\ge \dim R+1$ .

Conversely, every prime chain in  $\operatorname{Spec}(G(R))$  starts with at most one extra term  $P_\tau$ , and all later terms are of the form  $P_{\mathfrak p}$  and correspond to a chain in  $\operatorname{Spec}(R)$ . Hence  $\dim G(R)\le \dim R+1$ . ∎

This is the precise version of “one extra generic layer”.

7.  Congruences and quotients

Definition B.16. For an ideal  $J\triangleleft R$ , define two congruences on  $G(R)$ :

$$
x\,\rho_J\,y \iff \bigl(x=y=\tau\bigr) \ \text{or}\ \bigl(x,y\in R\ \text{and}\ x-y\in J\bigr),
$$

and

$$
x\,\rho'_J\,y \iff \pi_J(x)=\pi_J(y),
$$

where

$$
\pi_J:G(R)\to R/J,\qquad \pi_J(\tau)=0,\quad \pi_J(r)=r+J.
$$

Then

$$
G(R)/\rho_J\cong G(R/J),\qquad G(R)/\rho'_J\cong R/J.
$$

---

Theorem B.17. Every congruence on  $G(R)$  is either  $\rho_J$  or  $\rho'_J$  for a unique ideal  $J\triangleleft R$ .

Proof. Let  $\sim$  be a congruence on  $G(R)$ . Its restriction to  $R$  is a ring congruence, hence there is a unique ideal

$$
J=\{r\in R:r\sim 0_R\}
$$

such that

$$
a\sim b\quad\Longleftrightarrow\quad a-b\in J \qquad (a,b\in R).
$$

Now there are two cases.

Case 1:  $\tau\not\sim 0_R$ . If  $m\in R$  and  $m\sim \tau$ , then

$$
0_R=m\oplus(-m)\sim \tau\oplus(-m)=-m.
$$

So  $-m\in J$ , hence  $m\sim 0_R$ , and therefore  $\tau\sim 0_R$ , contradiction. Thus  $\tau$  is equivalent only to itself, so  $\sim=\rho_J$ .

Case 2:  $\tau\sim 0_R$ . Then for  $m\in R$ ,

$$
m\sim\tau\iff m\sim 0_R\iff m\in J.
$$

Hence  $\sim=\rho'_J$ .

Uniqueness of  $J$  comes from restriction to  $R$ . ∎

---

Corollary B.18. The congruence lattice of  $G(R)$  is a doubled copy of the ideal lattice of  $R$ : for ideals  $J,K\triangleleft R$ ,

$$
\rho_J\subseteq \rho_K \iff J\subseteq K,
$$
 
$$
\rho'_J\subseteq \rho'_K \iff J\subseteq K,
$$
 
$$
\rho_J\subseteq \rho'_K \iff J\subseteq K,
$$

and

$$
\rho'_J\not\subseteq \rho_K \quad\text{for all }J,K,
$$

because  $\rho'_J$  always identifies  $\tau$  with  $0_R$ , while  $\rho_K$  never does.

So the correct formal statement is: every ring quotient  $R/J$  comes with exactly two semiring quotients of  $G(R)$ , one separated and one collapsed.

8.  Localization and stalks

The note proves for  $R=\mathbf Z$  that if  $M\subset \mathbf Z$  is multiplicative and  $0\notin M$ , then

$$
S_M\cong G(\mathbf Z_M),
$$

while localizing at the full multiplicative subset  $\mathbf Z$  gives

$$
S_{\mathbf Z}\cong \mathbf B.
$$

This generalizes exactly.

**Proof.** Theorem B.17 says that every congruence is uniquely of the form $\rho_J$ or $\rho'_J$. The inclusion relations are checked directly from the definitions: if $J\subseteq K$, then congruence modulo $J$ is finer than congruence modulo $K$, both on the separated side and on the collapsed side, and likewise $\rho_J\subseteq\rho'_K$. On the other hand, $\rho'_J$ identifies $\tau$ with $0_R$ whereas $\rho_K$ never does, so $\rho'_J\not\subseteq\rho_K$ for all $J,K$. ∎


---

Theorem B.19. Let  $M\subseteq R$  be a multiplicative subset with  $0\notin M$ . Then

$$
G(R)_M\cong G(R_M).
$$

Proof. Define

$$
\Phi:G(R)_M\to G(R_M)
$$

by

$$
\Phi([\tau,m])=\tau,\qquad \Phi([r,m])=r/m.
$$

To see well-definedness, suppose  $(x_1,m_1)\sim(x_2,m_2)$ . If  $x_1=\tau$ , then there exists  $k\in M$  with

$$
k(x_1m_2)=k(x_2m_1).
$$

The left side is  $k\tau=\tau$ . If  $x_2\in R$ , then  $x_2m_1\in R$ , hence  $k(x_2m_1)\in R$ , contradiction. So  $x_2=\tau$ . Thus all  $\tau$ \-numerator classes map to  $\tau$ .

If  $x_1,x_2\in R$ , then the localization relation in  $G(R)$  is exactly the ordinary localization relation in  $R$ , so  $x_1/m_1=x_2/m_2$  in  $R_M$ .

The map is clearly a semiring homomorphism and surjective. Injectivity is proved by the same case split: a  $\tau$ \-class cannot equal a supported class, and equality of supported fractions in  $R_M$  is precisely the localization relation. ∎

---

Theorem B.20. Localizing at the full multiplicative subset  $R\subset G(R)$  yields

$$
G(R)_R\cong \mathbf B.
$$

Proof. Let  $C_0=[\tau,1]$ . Exactly as in the note, any class equal to  $C_0$  must have  $\tau$ \-numerator.

Let  $C_1=[1,1]$ . If  $[r_1,m_1]$  and  $[r_2,m_2]$  have  $r_i,m_i\in R$ , then choosing  $k=0\in R$  in the localization relation gives

$$
0(r_1m_2)=0=0(r_2m_1),
$$

so all supported fractions lie in the same class  $C_1$ .

These two classes are distinct, since otherwise some  $k\in R$  would satisfy

$$
k\tau=k,
$$

impossible because the left side is  $\tau$  and the right side lies in  $R$ .

The operations on  $\{C_0,C_1\}$  are forced and coincide with those of  $\mathbf B$ . ∎

---

Corollary B.21. For a prime  $\mathfrak p\in\operatorname{Spec}(R)$ ,

$$
\mathcal O_{P_\tau}\cong \mathbf B,\qquad \mathcal O_{P_{\mathfrak p}}\cong G(R_{\mathfrak p}).
$$

Proof. By definition, the stalk at a prime is the localization at the complement. For  $P_\tau$ , the complement is the whole supported copy  $R$ , so Theorem B.20 applies. For  $P_{\mathfrak p}$ , the complement is  $R\setminus \mathfrak p$ , so Theorem B.19 gives the result. ∎

If  $R$  is an integral domain with fraction field  $K$ , then  $\mathfrak p=(0)$  is prime and

$$
\mathcal O_{P_{(0)}}\cong G(K).
$$

This is the correct “arithmetic generic object”. The total localization

$$
G(R)_R\cong \mathbf B
$$

is instead the absolute Boolean collapse.

9.  Products and the global support bit

A clean structural fact, absent from the note but forced by the construction, is the exact product formula.

---

Theorem B.22. For nonzero commutative rings  $A,B$ ,

$$
G(A\times B)\cong G(A)\times_{\mathbf B} G(B),
$$

where the fiber product is taken with respect to the support characters

$$
\chi_A:G(A)\to \mathbf B,\qquad \chi_B:G(B)\to \mathbf B.
$$

Proof. Define

$$
\Psi:G(A\times B)\to G(A)\times_{\mathbf B} G(B)
$$

by

$$
\Psi(\tau)=(\tau,\tau),\qquad \Psi((a,b))=(a,b).
$$

This is well-defined because  $\chi_A(a)=1=\chi_B(b)$  for all  $(a,b)\in A\times B$ , and  $\chi_A(\tau)=\chi_B(\tau)=0$ .

Conversely, an element of the fiber product is either  $(\tau,\tau)$ , or  $(x,y)$  with  $\chi_A(x)=\chi_B(y)=1$ , hence  $x\in A$ ,  $y\in B$ . So define

$$
\Phi(\tau,\tau)=\tau,\qquad \Phi(x,y)=(x,y)\in A\times B.
$$

These maps are inverse semiring homomorphisms. ∎

Consequently  $G$  does not preserve nontrivial direct products. The correct statement is not

$$
G(A\times B)=G(A)\times G(B),
$$

but rather the fiber-product identity above. This is the exact formal content of the “one global support bit” intuition.

Applying this to Chinese remainder decompositions gives rigorous versions of the earlier informal claims about  $G(\mathbf Z/n\mathbf Z)$ : the refined quotient carries one global support bit, not one independent unsupported state per prime factor.

10.  Factorization for domains

The note proves for  $R=\mathbf Z$  that irreducibles are exactly  $\pm p$ , that  $0$  is prime in the divisibility sense but not irreducible, and therefore unique factorization fails.

globalization\_note

The clean general statement is this.

---

Theorem B.23. Let  $R$  be an integral domain.

1.  The units of  $G(R)$  are exactly the units of  $R$ .
2.  The irreducibles of  $G(R)$  are exactly the irreducibles of  $R$ .
3.  Every factorization of a nonzero supported element in  $G(R)$  is a factorization in  $R$ .
4.  If  $R$  has a nonunit, then  $0_R\in R\subset G(R)$  is prime in the divisibility sense but not irreducible. In particular,  $G(R)$  is not a unique factorization semiring.

Proof. If  $u\in G(R)$  is a unit, it cannot be  $\tau$ , since  $\tau x=\tau\neq 1$ . So  $u\in R$ , and its inverse must also lie in  $R$ . Hence units are exactly those of  $R$ .

If  $x\in G(R)$  is irreducible and  $x\neq \tau$ , then  $x\in R$ . Any factorization  $x=ab$  in  $G(R)$  cannot involve  $\tau$ , since then  $ab=\tau$ . So it is a factorization in  $R$ , and irreducibility in  $G(R)$  is equivalent to irreducibility in  $R$ . Conversely, irreducibles in  $R$  remain irreducible in  $G(R)$  for the same reason.

Any product of irreducibles in  $G(R)$  is therefore a nonzero supported element.

Now let  $a\in R$  be any nonunit. Then

$$
0_R=a\cdot 0_R,
$$

and neither factor is a unit, so  $0_R$  is reducible.

If  $0_R\mid xy$ , then  $xy=0_R\cdot c\in \{0_R,\tau\}$ . If  $x,y\in R\setminus\{0\}$ , then  $xy\in R\setminus\{0\}$ , impossible. Hence one factor lies in  $\{0_R,\tau\}$ , and either is divisible by  $0_R$ . So  $0_R$  is prime in the divisibility sense. ∎

Thus the exact factorization statement is:

*   away from the supported zero, factorization is exactly classical;
*   the obstruction is concentrated at the supported zero.

This is the precise replacement for the earlier informal phrase “almost factorial away from  $0$ ”.

III. Specialization to the note’s cases

1.  The case  $R=\mathbf Z$ 

All of the following are proved in the note:

$$
\operatorname{Spec}(G(\mathbf Z))=\{P_\tau,P_0,P_p\},
$$

with

$$
P_\tau=\{\tau\},\qquad P_0=\{0,\tau\},\qquad P_p=p\mathbf Z\cup\{\tau\},
$$

and

$$
P_\tau\subsetneq P_0\subsetneq P_p.
$$

Hence

$$
\dim G(\mathbf Z)=2.
$$

globalization\_note

The ideals are exactly

$$
\{\tau\},\qquad I_n=n\mathbf Z\cup\{\tau\}\quad (n\ge 0),
$$

all principal.

Every congruence is either  $\rho_n$  or  $\rho'_n$ , with

$$
G(\mathbf Z)/\rho_n\cong G(\mathbf Z/n\mathbf Z),\qquad G(\mathbf Z)/\rho'_n\cong \mathbf Z/n\mathbf Z.
$$

The canonical ideal zeta is

$$
\zeta_{G(\mathbf Z)}(s)=\zeta(s).
$$

The stalks are

$$
\mathcal O_{P_\tau}\cong \mathbf B,\qquad \mathcal O_{P_0}\cong G(\mathbf Q),\qquad \mathcal O_{P_p}\cong G(\mathbf Z_{(p)}),
$$

and the total localization is

$$
\operatorname{Frac}(G(\mathbf Z))\cong \mathbf B.
$$

The multiplicative monoid has prime ideals parameterized by arbitrary subsets of rational primes, so

$$
\dim \operatorname{Spec}((\mathbf Z,\times))=\infty,
$$

and therefore the semiring spectrum and monoid spectrum are not homeomorphic.

The contracted monoid algebra splits:

$$
\mathbf Z_0[M_S]\cong \mathbf Z\times \mathbf Z[M^\times],
$$

so its spectrum is disconnected:

$$
\operatorname{Spec}(\mathbf Z_0[M_S])\cong \operatorname{Spec}(\mathbf Z)\sqcup \operatorname{Spec}(\mathbf Z[M^\times]).
$$

The note’s blueprint remark records the formal reason: the semiring geometry is not recoverable from the multiplicative monoid alone; one must retain the pre-addition.

globalization\_note

2.  The case  $R=\mathcal O_K$ 

For a number field  $K$  with ring of integers  $\mathcal O_K$ , the note proves:

$$
\dim G(\mathcal O_K)=2,
$$

with prime ideals

$$
\{\tau\},\qquad \{0\}\cup\{\tau\},\qquad \mathfrak p\cup\{\tau\} \quad(\mathfrak p\neq 0\text{ prime in }\mathcal O_K).
$$

globalization\_note

The ideals are exactly

$$
\{\tau\},\qquad J\cup\{\tau\}\quad(J\triangleleft \mathcal O_K).
$$

If  $\mathcal O_K$  is a PID, then  $G(\mathcal O_K)$  is a principal ideal semiring.

globalization\_note

The class semigroup is unchanged:

$$
\operatorname{Cl}(G(\mathcal O_K))\cong \operatorname{Cl}(K),
$$

and the ideal zeta function is unchanged:

$$
\zeta_{G(\mathcal O_K)}(s)=\zeta_K(s).
$$

Under the unit action of  $\mathcal O_K^\times$ , the fixed-point subsemiring is

$$
G(\mathcal O_K)^{\mathcal O_K^\times}=\{0,\tau\}\cong \mathbf B.
$$

globalization\_note

So the note’s number-theoretic message is exact and limited:

*   ordinary ideal arithmetic is preserved,
*   ordinary class theory is preserved,
*   ordinary zeta theory is preserved,
*   the nonclassical part is the split zero, the extra generic point, and the doubled quotient theory.

IV. Final corrected synthesis

The real structure is this.

For every nonzero commutative ring  $R$ , the semiring  $G(R)$  is a fully faithful split-zero enlargement of  $R$ . It has two canonical quotients:

$$
p_R:G(R)\to R \qquad\text{and}\qquad \chi_R:G(R)\to \mathbf B,
$$

with kernels

$$
\ker(\chi_R)=\{\tau\}\subsetneq \{0_R,\tau\}=\ker(p_R).
$$

Its prime spectrum is obtained from  $\operatorname{Spec}(R)$  by adjoining one new least prime  $P_\tau$ , which is simultaneously open and dense:

$$
D_{G(R)}(0_R)=\{P_\tau\}.
$$

The old spectrum survives exactly as the closed stratum

$$
V(\{0_R,\tau\})\cong \operatorname{Spec}(R).
$$

Its dimension is exactly one larger:

$$
\dim G(R)=\dim R+1.
$$

Its quotient theory is doubled: every ideal  $J\triangleleft R$  gives precisely two congruences,

$$
\rho_J\quad\text{and}\quad \rho'_J,
$$

with quotients

$$
G(R/J)\quad\text{and}\quad R/J.
$$

Its local arithmetic is classical away from the total inversion of the supported layer:

$$
G(R)_M\cong G(R_M)\qquad(0\notin M),
$$

but

$$
G(R)_R\cong \mathbf B.
$$

When  $R$  is an integral domain, nonzero factorization is exactly classical, but the supported zero becomes prime in divisibility while remaining reducible. That is where unique factorization fails.

For  $R=\mathbf Z$  and  $R=\mathcal O_K$ , the note proves that this extra structure does not alter the classical ideal zeta or ideal class theory, while it does create one new Boolean generic layer and one doubled quotient sheet.

Everything beyond that in the prior thread that invoked undeclared boundary geometries, new zeta theories, “places at  $\mathbf F_1$ ”, thin-group analogies, or other speculative overlays is withdrawn. The corrected theorem-level content is exactly the structure above, together with the note’s explicit  $\mathbf Z$ \- and  $\mathcal O_K$ \-computations.

## Response:
4/14/2026, 11:07:37 PM

I’m extracting the formal theorem-level spine and then extending it beyond the note only where the extension is fully proved, not paraphrased or conjectural.

I have the theorem package in hand and am now developing the general  $G(R)$  theory for arbitrary commutative rings, including spectra, congruences, localization, products, and functoriality.

> **Addressing user feedback and refining response**
>
> I need to address the user's recent feedback, which implied they wanted a more formal and rigorous response based on an uploaded globalization note. I'll focus on providing a detailed, mathematical analysis, steering clear of superficiality. I’ll carefully review the note and any relevant previous conversations, ensuring that my response is original and adds value with new insights.
>
> **Clarifying user request and refining response**
>
> The user wants a rigorous extension of the globalization note with deeper implications, beyond just the paper’s scope. I'll focus on providing a formal, mathematical response that builds on the ideas in the note. I'll ensure to cite relevant definitions, theorems, and concepts from the note, analyzing the broader implications.
>
> **Refining response to user’s request**
>
> The user wants a rigorous mathematical analysis extending beyond the paper, applying concepts like primes and related structures. I'll focus on delivering properly developed theorem-style results, ensuring statements are precise, especially for zero divisors. I'll base it on the structure of G(R) and canonical injections, avoiding overgeneralizing.
>
> **Validating generalized properties for rings and semirings**
>
> I need to confirm that this construction works for any ring R. For the semiring B, it looks like R×B is componentwise, and
>
> **Defining category equivalence for semirings**
>
> I need to define a precise split-zero semiring. One possibility is considering a semiring with a distinguished element, like a “split-zero ring semiring.” I could also prove the full faithfulness between nonzero commutative rings and their globalizations, but I should be careful not to overcomplicate things by going too deep into other classes.
>
> **Proving full faithfulness and ideals for G(R')**
>
> I’ve shown that f(0_R) must belong to R', and if f(r) = τ, a contradiction arises, leading to the conclusion that f(R) ⊆ R'. This proving full faithfulness. For G(R)'s ideals, they’re either {τ} or J ∪ {τ}, where J is an ideal of R. Prime ideals are always {τ}.
>
> **Proving results for prime ideals and topology of Spec(G(R))**
>
> It looks like any nonzero commutative ring has prime ideals, and the dimension of a semiring may be one plus the ring's dimension, since {τ} is below all primes. For Spec(G(R)), I show {τ} is in every prime ideal, leading to a closed topology. The structure maps well.
>
> **Analyzing the topology of Spec(G(R)) and Spec(R) extension**
>
> It looks like closed subsets of Y_R are either the whole space or the image of closed sets from Spec(R). Open sets must contain {τ} since it's the closure. Therefore, open sets are either ∅ or {τ} ∪ image of open sets in Spec(R). This leads to a topological extension of Spec(R).
>
> **Exploring Spec(G(R)) and the role of the supported zero**
>
> Spec(G(R)) seems to arise from adjoining a dense open generic point, {τ}, to a closed copy of Spec(R). Since {τ} is open and dense, this changes the usual idea of a generic point. I also noted that Spec(G(R)) is quasi-compact if Spec(R) is quasi-compact, due to adding one point.
>
> **Analyzing the localization relation**
>
> I’m considering the scenario where M avoids 0_R but could contain zero divisors. If the product involves supported elements and τ, I realized that k(r2m1) cannot equal τ, because only products involving τ directly yield τ in G(R). This leads to the conclusion that G(R)_M ≅ G(R_M) when M avoids 0_R. Now, should I look into semiring localization in more detail?
>
> **Generalizing semiring localization for nonzero rings**
>
> In the case of Z, localization at all of Z, including 0, gives B. To generalize this for any nonzero ring R, I’m considering that semiring localization generally requires a multiplicative set containing 1
>
> **Analyzing the local-to-global decomposition**
>
> I’ve concluded that G(R)_R ≅ B generally, which is nice. For local stalks, the prime P_τ has residue {τ}, and P_p has residue by complementing supported elements. This means O_{P_p} ≅ G(R_p), and I need to consider the residue semiring and maximal ideals carefully, so the local-to-global decomposition makes sense.
>
> **Considering quotient in congruence lattice**
>
> I’m thinking about the quotient in the congruence lattice. J=R yields universal congruences, and when J equals R, ρ_R seems to give a quotient where all supported elements are equivalent. But I’m considering whether this works well for nonzero rings, as G(0) might be problematic.
>
> **Considering inclusion of all ideals in quotient**
>
> I'm thinking about whether to include all ideals (J), including R. The note for Z only allowed n≥0, but if n=1, I wonder if J=Z means all integers become equivalent, leading to a quotient. Could G(Z/Z) work? I need to double-check if they defined it as B or handled n=1 differently.
>
> **Refining response based on user feedback**
>
> The previous draft didn't quite hit the mark, likely because it was informal and incomplete. I need to make sure the logic is rigorous, especially when applying classical ideas to G(Z). The user probably wants a formal presentation of consequences. I should focus on specifying the theorem-style outcomes, without referring to old files or extra details.
>
> **Structuring a formal and in-depth response**
>
> The user wants a detailed, formal response rather than a concise one. I’ll structure it into two main parts: First, I'll talk about the general structural extension to an arbitrary ring, covering everything from pullbacks to localization. Then, I'll apply classical prime-locus methods to connect this with familiar results like prime factorizations and congruences. The response will be theorem-heavy to satisfy the user’s preferences.
>
> **Exploring ζ_cong generalizations and category theory**
>
> For n=1, the formula works out, so now I need to build upon it for higher structures. I’m trying to define ζ_cong for an arbitrary structure, moving into category-theoretic concepts like the "split-zero semiring". That said, proving everything here might be tricky, especially regarding the addition and multiplication in this semiring. But it's worth exploring!
>
> **Exploring map uniqueness and additive properties**
>
> I’m trying to figure out if the map from G(R) to B is unique. I know that for a unital semiring map, the identity plays a key role, and the additive identity in G(R) isn't just 0_R—it's τ. I also need to show that any element from R maps to 1 based on the given properties. Finding relations to fully prove this!
>
> **Exploring uniqueness and product behavior**
>
> I’ve proven that any element x in R maps to 1, so the map χ_R is unique. That’s exciting! Now, for the product behavior, G(A×B) is isomorphic to a fiber product, which differs from a direct product. This is interesting and connects to refined zeta, with new results for the Chinese remainder theorem.
>
> **Exploring prime counting logic and ideal monoids**
>
> I think the reasoning about prime counting aligns with the user’s "same logic" because the support bit is global. To extend, the ideal monoid of G(R) is isomorphic to the ideal monoid of R, and this can be generalized to any domain. This conclusion holds for both Dedekind domains and number rings.
>
> **Considering multiplicative monoids and ring decompositions**
>
> I’m thinking about the multiplicative monoid of an integral domain R. When considering the contracted monoid algebra, for a domain, the decomposition could be Z × Z[R\setminus{0}]. But for rings with zero divisors, the nonzero product could be zero, which complicates things. I think focusing on domains is simpler here.
>
> **Exploring semiring geometry and prime-locus relationships**
>
> The semiring geometry doesn't work when trying to recover it from the multiplicative monoid or contracted monoid algebra—there’s a disconnect, while the semiring spectrum stays irreducible. I think I can make this clearer in the note. 
> 
> Regarding prime-locus/valuation machinery, we can define the closed-prime stratum on G(Z), and classical valuation functions on ideals will transfer intact. The additive linearization via weights works just like classical Euler machinery for nonzero ideals.
>
> **Examining spectral properties and decomposition**
>
> There's a concern about the topology of Spec(G(R)) with D(0_R) being {τ}, and whether this makes the spectrum not spectral. Adding this open set to the spectral closed copy of Spec(R) likely keeps it spectral. I could note that Spec(G(R)) could have a two-layered structure—Boolean absolute points combined with classical ring geometry. Additionally, the space could decompose as an open point and closed classical stratum.
>
> **Considering structure of Spec(G(R)) and its sheaf**
>
> Spec(G(R)) could be written as the union of two parts: one from an open immersion and one from a closed immersion. At the sheaf level, the stalks at the open point are B, while the classical stratum has G(R_p). The closed copy of the classical scheme does not have the same structure sheaf as Spec(R), and certain topological properties should be treated carefully.
>
> **Examining residue objects and maps in specialization chain**
>
> This has a recollement topologically, with the ringed space possibly extending R by a Boolean point. We could discuss residue objects along the specialization chain. For an integral domain, the residues corresponding to various points (τ, 0, and p) form an exact sequence, though care is needed when mentioning any potential maps between them. I'll avoid unsupported chain maps and adhere strictly to the well-defined steps for factorization of ideals.
>
> **Clarifying factorization in UFDs and domains**
>
> For non-τ elements, their factorization doesn't involve τ, and units in G(R) are the same as those in R. If R is a UFD, nonzero factorizations remain, though 0 hinders global factorization. I can state that the factorization issue is focused on supported zero. Also, the domain assumption is crucial for the proof.
>
> **Exploring non-Eulerian and related theory**
>
> I might define the full invariant as the sum of two terms: ζ_K(s) and ζ_ref(s). It's distinct from the classic Eulerian form due to its approach to support. I could summarize that this new series recovers what the traditional zeta misses, highlighting its non-Eulerian properties. For Z, it simplifies neatly.
>
> **Explaining Euler product failure and spectral depth**
>
> For coprime
>
> **Clarifying depth and spectral geometry**
>
> I could define the depth for all primes P_𝔭 as ht_R(𝔭) + 1, and place τ at 0. This would make the spectral geometry not just one-parameter, which feels rigorous but maybe a bit too abstract. I might mention it briefly without overdoing it. Betti and Langlands stuff doesn’t seem relevant here.
>
> **Finalizing answer with appropriate citations**
>
> We've gathered enough information to craft the final answer. I'll make sure to cite everything from the note using citations derived from file_search. Since the user didn't ask for external references, I’ll focus on citations from the note itself. Where reasoning is purely my own, no citation is needed. I'll provide a structured response, using headers and numbered items where necessary, and avoid over-verbosity — but will keep the answer formal and detailed as requested.
>
> **Planning the answer structure**
>
> Let’s start with a concise orientation: The note proves the classification for S=G(Z)=Z⊔{τ} and shows it's not speculative. The key result extends to any nonzero commutative ring R, yielding a canonical "split-zero extension" G(R). I’ll cite results from the note on embedding, ideals, congruences, and localization, moving to present new consequences. The answer will include generalization to arbitrary R with explicit theorems, focusing on clean proofs, particularly for full faithfulness.
>
> **Working through the congruence package**
>
> I need to prove that for an ideal J, we can define ρ_J and ρ'_J, and every congruence is one of them. The quotient G(R)/ρ_J will be isomorphic to G(R/J), and G(R)/ρ'_J to R/J. I’ll include a proof for this and explore the special case when J=R, leading to the Boolean quotient and trivial quotient.
>
> **Clarifying localization and product consequences**
>
> I need to clarify that when localizing at full R, we use 0∈R. The semiring localization definitions discussed in the note work for Z, and the same argument can be applied to other rings. For the product theorem, the support coordinate being global means the Chinese remainder formula isn't multiplicative, making the Dirichlet series non-Eulerian. I'll define ζ_sep and proof these results.
>
> **Considering UFS and monoid geometry**
>
> G(R) is never a unique factorization semiring (UFS), assuming non-units exist, so principal ideal theory and element factorization are separate. This is more rigorous than the note suggests. The class group and ideal zeta remain unchanged for Dedekind domains since the nonzero ideal monoid is preserved. For semiring geometry, addition is a rigidifying factor, and semiring-theoretic models reveal the support split zero interpretation. I'll cite the note for these results.
>
> **Clarifying results and citations**
>
> The classical arithmetic stratum is preserved topologically, but the novelty comes from the open dense Boolean point and doubled congruence sheet. For generalizing the note, we’ll use the note as a foundation and include citations for base cases like Z/O_K. We also want to ensure accuracy in statements about homomorphisms. The section about no map B→S might need citation or reconsideration.
>
> **Clarifying proof and contradictions**
>
> To prove a semiring homomorphism from R to B doesn't work: If v:B→G(R) is unital, 1=v(1)=v(1+1)=1⊕1=2, which is impossible in any commutative ring since 1 ≠ 2. Additionally, semirings with characteristic 1 only have the zero ring. I also noticed that the open dense generic point is isolated, which is an unusual property.
>
> **Conceptualizing ideal monoid preservation**
>
> The localization at \( M = R \) is defined: \( (x, m) \sim (y, n) \) if there exists \( k \in R \) such that \( kx n = ky m \). Then, I deduce the ideal monoid preservation theorem, and I can generalize the concept of class semigroup/zeta conservation. It could be relevant to discuss arithmetic conservativity and the invariants connected to nonzero ideals and quotient sizes. I’ll start with a structure referencing a note for explicit classification.
>
> **Documenting key mathematical results**
>
> I’m laying out the important results: the dense Boolean generic point, raising dimension, doubled congruence lattice, and total localization to B. These results can be linked to the generalizations for Z and O_K, with citations to the note where needed. I might add theorem statements and maintain readability, maybe a numbered list for clarity. I’ll also formalize the proposition on universal ring quotient.
>
> **Refining mathematical reasoning and proof structure**
>
> I’m sketching out the crucial steps in the proof. If \( f(-1) = \tau \), the contradiction arises, confirming \( f(R) \subseteq R' \) and that ring homomorphisms are unique. I'll also touch on ideas about dimension, chain lengths in Spec, and the topology, explaining closed and open sets in this structure.
>
> **Clarifying quotient mappings and localization process**
>
> I’m proving that \( \tau \) is isolated and showing quotient structures are indeed \( G(R/J) \) and \( R/J \). For \( J = R \), I'll carefully address the case as the zero ring. Interestingly, defining proper maps could simplify and avoid confusion, including with semirings. I’ll keep these details concise and avoid zero ring complications.
>
> **Exploring ideal monoid preservation and fiber products**
>
> For Dedekind domains, I’m proving that a monoid map preserves ideal multiplication, yielding a class semigroup. This supports arithmetic conservativity. Specifically, the product for two ideals \( I_J \) and \( I_K \) is clearly \( JK \cup \{ \tau \} \), which ensures invariance for finite quotient sizes. I’ll elaborate more generally on ideal monoid invariance.
>
> **Concluding with note's results on multiplicative monoid**
>
> I should include the result from the note about \( G(\mathbb{Z}) \) and the infinite-dimensional multiplicative monoid spectrum. This shows that a semiring’s geometry is genuinely additive and cannot be recovered from the multiplicative monoid alone. I’ll cite the note to formalize this closing remark.
>
> **Writing the formalized final response**
>
> I need to craft a polished, final version of the answer, building on previous drafts. I’ll avoid simple copy-pasting and incorporate minimal yet essential citations. The goal is to present claims naturally from both the note and my own thinking. I also need to avoid emphasizing compliance directly, but will aim for a formal presentation, including propositions with proofs (but not exhaustive). The length should be around 2000-3000 words. Let’s get started!
>
> **Structuring the formal presentation**
>
> The key results here are structural and functorial, not just analogical. The Z-construction, which I should reference in the note’s abstract, applies to all nonzero commutative rings. I’ll start with defining \( G(R) \) and Proposition 1.1 for embedding and maps, but I need to ensure I include necessary sections about semiring homomorphisms and their limitations without overcomplicating things with too many sub-propositions. I'll also consider the possibility of special cases like the zero ring.
>
> **Explaining the open and generic points**
>
> I need to clarify that Spec(G(R)) is not formed by simply adding closed or generic points—instead, it incorporates a point that is both generic and open. This is a significant structural point that should be emphasized. I'll also mention the sheaf on \( Y_R \), explaining how it's topologically similar to Spec(R) but not exactly the same due to stalks being \( G(R_p) \). Then, I’ll highlight the key implication about quotient theory: every ring quotient leads to two semiring quotients.
>
> **Explaining localization and arithmetic implications**
>
> When localizing, there are two main approaches: one that localizes away from 0, resulting in \( G(R_M) \), and one that localizes at all supported elements, collapsing to \( B \). It’s important to note that the arithmetic generic object corresponds to the stalk at 0 in a domain. Next, regarding prime logic, we can transfer classical prime factorization and log-height tools directly to the finite-norm ideal sheet. For example, when \( R = \mathbb{Z} \), the ideal monoid \( M_{\text{fin}}(S) = \{ I_n \} \) is isomorphic to \( (N_{>0}, \times) \).
>
> **Understanding multiplicative height and ideal behavior**
>
> A single multiplicative norm can't fully parameterize the spectrum; instead, the intrinsic parameterization involves height plus norm on the closed stratum. This aligns with prime-locus logic. For instance, in the \( \mathbb{Z} \) case, I see that ideals like \( \{ \tau \} \) or \( I_n \) obey certain behaviors like \( I_0 I_n = I_0 \) and \( \{ \tau \} I_n = \{ \tau \} \), leading to a height of zero for exceptional ideals. This collapses generic ideals neatly and answers the question about structural similarity.
>
> **Exploring multiplicative height and zeta refinements**
>
> No positive multiplicative height exists on all ideals extending the norm
>
> **Addressing residue objects and quotients**
>
> This support-refined sheet is canonical since it correctly counts all finite congruences, not relying on ad hoc statistics. We should ensure no contradiction with the earlier note’s notation — specifically, ρ_n separated (τ distinct) and quotient G(Z/nZ), while ρ'_n collapsed gives quotient Z/nZ. I’ll also clarify "residue objects" and emphasize that the maps aren't natural morphisms. The residue rings/seminrings at P_τ, P_0, and P_p are B, Q, and F_p respectively. Additionally, for O_K, the ideal monoid’s preservation links to the Dedekind zeta.
>
> **Concluding remarks and citations**
>
> I should mention "forgetting addition explodes geometry" as a final remark, relating it to the Z-case monoid spectrum’s infinite dimensionality and the semiring’s 2D dimension, with implications for monoid algebra product decomposition. I’ll make sure to cite at the end of each paragraph discussing the note’s findings—either for direct facts or derived results. For pure propositions with proofs, I might not need a citation unless it uses facts beyond the note’s definitions.
>
> **Clarifying notation and citing results**
>
> For an ideal J◁R, I’ll define I_J := J∪{τ}. The ideal product satisfies I_J I_K = I_{JK}. This shows the ideal monoid is nonzero and isomorphic, which could imply class monoid preservation for number rings like O_K. The note proves this, so it's an example of a broader statement. I’m also considering how to describe Spec(G(R)) topologically.
>
> **Topological and sheaf-theoretical considerations**
>
> This seems to be a topological gluing process, possibly called "recollement," although I’m not sure if that’s necessary to mention. I should note that for the closed complement, the structure sheaf is G(O_R), not just O_R, so it's not a classical closed subscheme. The underlying space keeps Spec(R) as a closed subspace, but the sheaf-theoretic structure is enriched. On the stalk at P_p, we get G(R_p) instead of R_p, making this distinction important. The closed arithmetic stratum is topologically classical but thickened in the sheaf theory.
>
> **Formulating propositions and proof structure**
>
> I’ve outlined the propositions that should guide the work. Now, I'll draft the proofs carefully but concisely. One key point is ensuring that the homomorphisms between G(R) and A preserve additive inverses. This leads to identifying the uniqueness of χ_R for the map from G(R) to B, which is a necessary conclusion. I'll include this as a corollary.
>
> **Clarifying zeta and ideal monoid implications**
>
> Here's what's going on: The formulation for G(R; s) looks good now that I've corrected the second term. A zeta function result for Z is given by "2ζ(s) - 1." I should quickly prove the comparison to Dedekind zeta and mention the ideal monoid structure on Z. The direct answer regarding "same logic structurally" is to clarify how prime requirements apply to closed prime ideals and the limitations of this regarding the whole ideal monoid.
>
> **Including prime machinery in arithmetic section**
>
> In the arithmetic section, I'll present that for S = G(Z), finite-norm ideals are represented by I_n (with n ≥ 1). Their multiplication follows I_m I_n = I_{mn}, making the
>
> **Solidifying structure for final answer**
>
> After confirming that P_p are closed (since pZ is maximal and nested chain applies), I should mention that exceptional ideals have infinite norms due to collapsed quotients. I'll structure the final answer into six sections: ring construction, spectrum/localizations, quotients, ideal monoid machinery, new invariants, and factorization. Citations will wrap up each paragraph.
>
> **Setting up citations and structure**
>
> For the introduction, I'll mention elements like S=Z⊔{τ}, ideal structures, congruences, and O_K extensions. Citations should be placed properly: for explicit theorem-level results from the note, I’ll cite appropriately (e.g., turn10file14 for Z-related parts, and turn11file5 for localizations). I'll avoid citing our own proofs, but external sources supporting facts will be referenced.
>
> **Clarifying and refining the semiring discussion**
>
> It appears there's no map from \(R\) to \(B\) through \(\chi\), but that's good because it confirms the rigor. When discussing the supported layer, I’ll rephrase it better, noting that the subset \(R \subset G(R)\) isn't a semiring subobject as it doesn't include semiring zero \(\tau\). I'll detail Theorem 1, focusing on semiring maps and uniqueness of \(\chi_R\).
>
> **Refining proof and final presentation**
>
> I’m not going to overemphasize what’s missing from the note. But I’ll
>
> **Refining quotient and ideal monoid discussion**
>
> The quotients follow the expected structure: when \( J \neq R \), they're \( G(R/J) \) and \( R/J \); when \( J = R \), they're \( B \) and 1. With semiring quotients, careful attention is needed if all elements are equivalent but separated by \( \tau \). The ideal monoid product theorem is solid and applies to \( O_K \), preserving both norm and class group. We’ll label zeta correctly, and include the "finite separated quotient size" proof too.
>
> **Clarifying prime-height formalism and depth coordinate**
>
> For \( S = G(\mathbb{Z}) \), the finite-norm ideal monoid recovers classical arithmetic, but with a prime spectrum divided into strata: \( P_\tau \), \( P_0 \), and \( P_p \), each with different depth coordinates. A real-valued norm alone can’t capture the entire spectrum. I'll include a brief description of the ideal height introduction to highlight how this forms a two-coordinate structure combining specialization depth and classical norm.
>
> **Drafting the introduction for the generalization to \( G(R) \)**
>
> I'll start the introduction by stating that \( G(R) = R \sqcup \{\tau\} \), where \( \tau \) is the additive zero and multiplicative absorber. Then, I'll reference key results from the note, like Proposition 1.4, and mention theorems 2.2, 3.4, etc., to provide context without overwhelming the reader with citations.
>
> **Finalizing propositions and nuances in localization**
>
> I’m finalizing the proof for Proposition 1.2, noting that no semiring map exists from \( R \) to \( B \) or from \( B \) to \( G(R) \), which follows from prior results. I'll make sure to mention the classic stratum and topological nuances in the context of localization, clarifying that \( Y_R \) isn't simply the classical scheme \( \Spec(R) \).
>
> Thought for 30m 45s

Let  $R$  be a nonzero commutative ring with identity. Define

$$
G(R):=R\sqcup\{\tau\},
$$

where  $\tau\notin R$ , with operations

$$
r\oplus s=r+s,\qquad r\oplus\tau=r,\qquad \tau\oplus\tau=\tau,
$$

and

$$
rs=rs,\qquad r\tau=\tau r=\tau,\qquad \tau^2=\tau
$$

for all  $r,s\in R$ .

For  $R=\mathbf Z$ , this is exactly the semiring treated in the note; there the explicit classification of ideals, prime ideals, congruences, local stalks, the equality  $\operatorname{Frac}(G(\mathbf Z))\cong \mathbf B$ , the infinite-dimensionality of the multiplicative-monoid spectrum, the contracted monoid algebra decomposition, and the extension to  $G(\mathcal O_K)$  with  $\operatorname{Cl}(G(\mathcal O_K))\cong \operatorname{Cl}(K)$  and  $\zeta_{G(\mathcal O_K)}=\zeta_K$  are already proved.

What follows is a theorem-level development strictly beyond those case computations.

1\. Algebraic normal form
-------------------------

---

### Proposition 1.1

There is a canonical semiring isomorphism

$$
G(R)\xrightarrow{\sim} D_R:=\{(r,b)\in R\times \mathbf B:\ b=0\Rightarrow r=0_R\} =\{(0_R,0)\}\cup (R\times\{1\}),
$$

where  $\mathbf B=\{0,1\}$  is the Boolean semiring.

#### Proof

Define

$$
\iota:G(R)\to D_R,\qquad \iota(\tau)=(0_R,0),\qquad \iota(r)=(r,1)\quad(r\in R).
$$

This is bijective. The componentwise operations on  $R\times\mathbf B$  restrict to  $D_R$ , and on generators one has

$$
(r,1)+(s,1)=(r+s,1),\qquad (r,1)+(0,0)=(r,1),\qquad (0,0)+(0,0)=(0,0),
$$
 
$$
(r,1)(s,1)=(rs,1),\qquad (r,1)(0,0)=(0,0),\qquad (0,0)(0,0)=(0,0).
$$

Transporting these operations through  $\iota$  yields exactly the defining formulas for  $G(R)$ . ∎

Thus  $G(R)$  is not  $R\times\mathbf B$ ; it is the coupled subsemiring in which the Boolean coordinate may vanish only over arithmetic value  $0_R$ .

2\. The two canonical observables
---------------------------------

Define

$$
p_R:G(R)\to R,\qquad p_R(\tau)=0_R,\quad p_R(r)=r,
$$

and

$$
\chi_R:G(R)\to \mathbf B,\qquad \chi_R(\tau)=0,\quad \chi_R(r)=1\quad(r\in R).
$$

---

### Proposition 2.1

Both  $p_R$  and  $\chi_R$  are unital semiring homomorphisms, and

$$
(p_R,\chi_R):G(R)\hookrightarrow R\times \mathbf B
$$

identifies  $G(R)$  with  $D_R$ .

#### Proof

For  $p_R$ , all identities are immediate from the definitions:

$$
p_R(r\oplus s)=r+s=p_R(r)+p_R(s),\qquad p_R(rs)=rs=p_R(r)p_R(s),
$$
 
$$
p_R(r\oplus\tau)=r=p_R(r)+0,\qquad p_R(r\tau)=0=p_R(r)\cdot 0.
$$

For  $\chi_R$ ,

$$
\chi_R(r\oplus s)=1=1+1,\qquad \chi_R(rs)=1=1\cdot 1,
$$
 
$$
\chi_R(r\oplus\tau)=1=1+0,\qquad \chi_R(r\tau)=0=1\cdot 0,
$$

and similarly in the remaining cases. The final assertion is Proposition 1.1 rewritten in coordinates. ∎

The fiber structure is therefore exact:

$$
p_R^{-1}(0_R)=\{0_R,\tau\},\qquad p_R^{-1}(r)=\{r\}\ \ (r\neq 0_R),
$$

while

$$
\chi_R^{-1}(0)=\{\tau\},\qquad \chi_R^{-1}(1)=R.
$$

3\. Universal ring quotient
---------------------------

---

### Theorem 3.1

For every commutative ring  $A$ , composition with  $p_R$  induces a bijection

$$
\operatorname{Hom}_{\mathrm{Ring}}(R,A)\xrightarrow{\sim}\operatorname{Hom}_{\mathrm{SemiRing}}(G(R),A).
$$

#### Proof

Let  $f:G(R)\to A$  be a semiring homomorphism. Since  $\tau=0_{G(R)}$ ,

$$
f(\tau)=0_A.
$$

Also,

$$
f(0_R)=f(0_R\oplus 0_R)=f(0_R)+f(0_R),
$$

hence  $f(0_R)=0_A$  by subtraction in the ring  $A$ .

Define  $g:R\to A$  by  $g(r)=f(r)$ . Then for  $r,s\in R$ ,

$$
g(r+s)=f(r\oplus s)=f(r)+f(s)=g(r)+g(s),
$$
 
$$
g(rs)=f(rs)=f(r)f(s)=g(r)g(s),
$$

and  $g(1_R)=f(1_R)=1_A$ . Thus  $g$  is a ring homomorphism. Finally,

$$
(g\circ p_R)(\tau)=g(0_R)=0_A=f(\tau),\qquad (g\circ p_R)(r)=g(r)=f(r),
$$

so  $f=g\circ p_R$ . Uniqueness follows from surjectivity of  $p_R$ . ∎

Thus  $R$  is the maximal ring quotient of  $G(R)$ . No ring-valued invariant of  $G(R)$  can avoid factoring through  $R$ .

---

### Corollary 3.2

There is no semiring homomorphism  $s:R\to G(R)$  such that  $p_R\circ s=\operatorname{id}_R$ .

#### Proof

Since  $s$  preserves semiring zero,

$$
s(0_R)=\tau.
$$

Also  $s(1_R)=1_R$ . Because  $p_R(s(-1_R))=-1_R\neq 0_R$ , the element  $s(-1_R)$  is supported, hence belongs to  $R\subset G(R)$ . Therefore

$$
\tau=s(0_R)=s(1_R+(-1_R))=s(1_R)\oplus s(-1_R)=1_R\oplus s(-1_R),
$$

but the right-hand side is supported, contradiction. ∎

So  $G(R)\to R$  is a quotient, not a split extension in the semiring category.

4\. The Boolean character is canonical
--------------------------------------

---

### Theorem 4.1

 $\chi_R$  is the unique semiring homomorphism

$$
G(R)\to \mathbf B.
$$

#### Proof

Let  $u:G(R)\to \mathbf B$  be a semiring homomorphism. Then  $u(\tau)=0$  and  $u(1_R)=1$ .

First,

$$
u(0_R)=u(1_R\oplus (-1_R))=u(1_R)+u(-1_R)=1+u(-1_R)=1
$$

in  $\mathbf B$ .

Now let  $r\in R$ . If  $u(r)=0$ , then

$$
1=u(0_R)=u(r0_R)=u(r)\,u(0_R)=0\cdot 1=0,
$$

contradiction. Hence  $u(r)=1$  for every  $r\in R$ . Therefore  $u=\chi_R$ . ∎

---

### Corollary 4.2

There is no semiring homomorphism  $R\to\mathbf B$ .

#### Proof

If  $v:R\to\mathbf B$  were such a homomorphism, then

$$
0=v(0_R)=v(1_R+(-1_R))=v(1_R)+v(-1_R)=1+v(-1_R)=1,
$$

contradiction. ∎

---

### Corollary 4.3

There is no unital semiring homomorphism  $\mathbf B\to G(R)$ .

#### Proof

Let  $w:\mathbf B\to G(R)$  be unital. Then  $w(1)=1_R$ . Since  $1+1=1$  in  $\mathbf B$ ,

$$
1_R=w(1)=w(1+1)=w(1)\oplus w(1)=1_R\oplus 1_R=1_R+1_R.
$$

The last equality is computed in the supported copy of  $R$ . Subtracting  $1_R$  gives  $1_R=0_R$ , contradiction. ∎

The Boolean structure is therefore intrinsic but not a unital base object.

5\. Full faithfulness of  $R\mapsto G(R)$ 
------------------------------------------

---

### Theorem 5.1

For nonzero commutative rings  $R,R'$ , restriction induces a bijection

$$
\operatorname{Hom}_{\mathrm{SemiRing}}(G(R),G(R'))\xrightarrow{\sim}\operatorname{Hom}_{\mathrm{Ring}}(R,R').
$$

#### Proof

Let  $f:G(R)\to G(R')$  be a semiring homomorphism. Since  $f$  preserves semiring zero,

$$
f(\tau)=\tau.
$$

Now  $\chi_{R'}\circ f:G(R)\to\mathbf B$  is a semiring homomorphism, hence equals  $\chi_R$  by Theorem 4.1. Therefore for every  $r\in R$ ,

$$
\chi_{R'}(f(r))=\chi_R(r)=1,
$$

so  $f(r)\in R'$ . Thus  $f|_R:R\to R'$  is a map of sets into  $R'$ .

For  $r,s\in R$ ,

$$
f(r+s)=f(r\oplus s)=f(r)\oplus f(s)=f(r)+f(s),
$$
 
$$
f(rs)=f(r)f(s),
$$

and

$$
f(0_R)=f(0_R\oplus 0_R)=f(0_R)+f(0_R),
$$

so  $f(0_R)=0_{R'}$ . Also  $f(1_R)=1_{R'}$ . Hence  $f|_R$  is a ring homomorphism.

Conversely, given a ring homomorphism  $g:R\to R'$ , define

$$
G(g):G(R)\to G(R'),\qquad G(g)(\tau)=\tau,\quad G(g)(r)=g(r).
$$

A direct check shows that  $G(g)$  is a semiring homomorphism.

These constructions are inverse to each other. ∎

---

### Corollary 5.2

 $G(R)\cong G(R')$  as semirings if and only if  $R\cong R'$  as rings.

#### Proof

This is immediate from Theorem 5.1: a semiring isomorphism $G(R)\to G(R')$ restricts to a ring isomorphism $R\to R'$, and a ring isomorphism $R\to R'$ extends uniquely by sending $\tau$ to $\tau$. ∎


---

### Corollary 5.3

$$
\operatorname{End}_{\mathrm{SemiRing}}(G(R))\cong \operatorname{End}_{\mathrm{Ring}}(R), \qquad \operatorname{Aut}_{\mathrm{SemiRing}}(G(R))\cong \operatorname{Aut}_{\mathrm{Ring}}(R).
$$

Thus the construction is fully faithful: it adds structure, but it does not forget ring structure.

6\. Ideals
----------

For an ideal  $J\triangleleft R$ , write

$$
I_J:=J\cup\{\tau\}\subseteq G(R).
$$

#### Proof

Apply Theorem 5.1 with $R'=R$. This identifies semiring endomorphisms of $G(R)$ with ring endomorphisms of $R$, and invertible endomorphisms with automorphisms. ∎


---

### Theorem 6.1

The ideals of  $G(R)$  are exactly

$$
\{\tau\} \qquad\text{and}\qquad I_J=J\cup\{\tau\}\quad(J\triangleleft R).
$$

#### Proof

Let  $I$  be an ideal of  $G(R)$ . Since  $\tau=0_{G(R)}$ , one has  $\tau\in I$ . Put  $J:=I\cap R$ .

If  $J=\varnothing$ , then  $I=\{\tau\}$ .

Assume  $J\neq\varnothing$ . If  $a,b\in J$ , then  $a,b\in I$ , hence

$$
a+b=a\oplus b\in I,
$$

so  $a+b\in J$ . If  $r\in R$  and  $a\in J$ , then  $ra=r\cdot a\in I$ , hence  $ra\in J$ . Therefore  $J\triangleleft R$ . Also  $I=J\cup\{\tau\}$ .

Conversely, for any ideal  $J\triangleleft R$ , the set  $J\cup\{\tau\}$  is closed under  $\oplus$  and under multiplication by arbitrary elements of  $G(R)$ . ∎

7\. Prime ideals and the prime spectrum
---------------------------------------

For a prime ideal  $\mathfrak p\in\operatorname{Spec}(R)$ , write

$$
P_{\mathfrak p}:=\mathfrak p\cup\{\tau\}, \qquad P_\tau:=\{\tau\}.
$$

---

### Theorem 7.1

The prime ideals of  $G(R)$  are exactly

$$
P_\tau \qquad\text{and}\qquad P_{\mathfrak p}\quad(\mathfrak p\in\operatorname{Spec}(R)).
$$

#### Proof

 $P_\tau$  is prime because  $xy=\tau$  holds if and only if  $x=\tau$  or  $y=\tau$ .

Now let  $J\triangleleft R$  be proper. Then  $I_J=J\cup\{\tau\}$  is prime in  $G(R)$  if and only if  $J$  is prime in  $R$ .

If  $I_J$  is prime and  $ab\in J$  with  $a,b\in R$ , then  $ab\in I_J$ , so  $a\in I_J$  or  $b\in I_J$ . Since  $a,b\in R$ , this means  $a\in J$  or  $b\in J$ ; thus  $J$  is prime.

Conversely, if  $J$  is prime and  $xy\in I_J$ , then either one of  $x,y$  is  $\tau$ , or both lie in  $R$  and  $xy\in J$ ; in the latter case primality of  $J$  gives  $x\in J$  or  $y\in J$ . Hence  $I_J$  is prime. ∎

---

### Corollary 7.2

The map

$$
i:\operatorname{Spec}(R)\to \operatorname{Spec}(G(R)),\qquad \mathfrak p\mapsto P_{\mathfrak p},
$$

is an order embedding with image

$$
Y_R:=\{P_{\mathfrak p}:\mathfrak p\in\operatorname{Spec}(R)\}.
$$

Moreover  $P_\tau\subseteq P_{\mathfrak p}$  for all  $\mathfrak p$ .

#### Proof

Theorem 7.1 identifies the primes of $G(R)$ exactly as $P_\tau$ and $P_{\mathfrak p}$ for $\mathfrak p\in\operatorname{Spec}(R)$. Moreover,

$$
P_{\mathfrak p}\subseteq P_{\mathfrak q}\iff \mathfrak p\subseteq \mathfrak q,
$$

because both sides mean precisely that every supported element of $\mathfrak p$ lies in $\mathfrak q$. Also $P_\tau=\{\tau\}$ is contained in every $P_{\mathfrak p}$ because $\tau\in P_{\mathfrak p}$ for all $\mathfrak p$. Hence $i$ is an order embedding with the stated image. ∎


---

### Proposition 7.3

 $Y_R$  is closed and canonically homeomorphic to  $\operatorname{Spec}(R)$ . In fact,

$$
Y_R=V(\{0_R,\tau\}).
$$

#### Proof

A prime ideal of  $G(R)$  contains  $\{0_R,\tau\}$  if and only if it is not  $P_\tau$ . Hence  $Y_R=V(\{0_R,\tau\})$ .

The map  $i$  is bijective onto  $Y_R$ . For an ideal  $J\triangleleft R$ ,

$$
i\bigl(V_R(J)\bigr)=Y_R\cap V_{G(R)}(I_J),
$$

because

$$
P_{\mathfrak p}\supseteq I_J \iff \mathfrak p\supseteq J.
$$

Therefore  $i$  is a homeomorphism. ∎

---

### Proposition 7.4

$$
D_{G(R)}(0_R)=\{P_\tau\}.
$$

Hence  $P_\tau$  is open and dense.

#### Proof

Every prime  $P_{\mathfrak p}$  contains  $0_R$ , whereas  $P_\tau=\{\tau\}$  does not. So the only prime not containing  $0_R$  is  $P_\tau$ . Since  $P_\tau$  is contained in every prime ideal, its closure is the whole space. ∎

Thus  $\operatorname{Spec}(G(R))$  is obtained from  $\operatorname{Spec}(R)$  by adjoining one new least prime which is simultaneously open and generic.

---

### Proposition 7.5

For every  $\mathfrak p\in\operatorname{Spec}(R)$ ,

$$
\operatorname{ht}_{G(R)}(P_{\mathfrak p})=\operatorname{ht}_R(\mathfrak p)+1, \qquad \operatorname{ht}_{G(R)}(P_\tau)=0.
$$

#### Proof

A chain ending in  $P_{\mathfrak p}$  is exactly

$$
P_\tau\subsetneq P_{\mathfrak p_0}\subsetneq\cdots\subsetneq P_{\mathfrak p_r}=P_{\mathfrak p},
$$

where

$$
\mathfrak p_0\subsetneq\cdots\subsetneq \mathfrak p_r=\mathfrak p
$$

is a chain in  $\operatorname{Spec}(R)$ . The formula follows. ∎

In particular, if  $\dim R=d<\infty$ , then

$$
\dim G(R)=d+1.
$$

8\. Localization, stalks, residues
----------------------------------

Let  $M\subseteq R$  be multiplicative.

---

### Theorem 8.1

If  $0_R\notin M$ , then

$$
G(R)_M\cong G(R_M).
$$

#### Proof

Elements of  $G(R)_M$  are classes  $[x,m]$  with  $x\in G(R)$ ,  $m\in M$ , under the relation

$$
(x,m)\sim (y,n) \iff \exists k\in M:\ kxn=kym.
$$

Define

$$
\Phi:G(R)_M\to G(R_M)
$$

by

$$
\Phi([\tau,m])=\tau,\qquad \Phi([r,m])=r/m.
$$

If  $(\tau,m)\sim (y,n)$ , then for some  $k\in M$ ,

$$
k\tau n=ky m.
$$

The left side is  $\tau$ . If  $y\in R$ , the right side lies in  $R$ , impossible. Hence  $y=\tau$ . Thus  $\Phi$  is well defined on  $\tau$ \-classes. If  $r,s\in R$  and  $(r,m)\sim (s,n)$ , then

$$
krn=ksm
$$

for some  $k\in M$ , which is precisely the usual equality relation in  $R_M$ . Hence  $\Phi$  is well defined.

It is plainly a semiring homomorphism and surjective. For injectivity, if  $\Phi([x,m])=\Phi([y,n])$ , then either both images are  $\tau$ , forcing both numerators to be  $\tau$ , or both images are supported fractions equal in  $R_M$ , which means exactly that  $(x,m)\sim(y,n)$ . ∎

---

### Theorem 8.2

Localizing  $G(R)$  at the full multiplicative subset  $R\subset G(R)$  yields

$$
G(R)_R\cong \mathbf B.
$$

#### Proof

Let  $C_0:=[\tau,1]$ . All pairs with numerator  $\tau$  represent  $C_0$ .

Let  $C_1:=[1,1]$ . For  $r_1,r_2,m_1,m_2\in R$ , choosing  $k=0_R\in R$  gives

$$
0_R(r_1m_2)=0_R=0_R(r_2m_1),
$$

so  $[r_1,m_1]=[r_2,m_2]$ . Hence every supported fraction is  $C_1$ .

These two classes are distinct: if  $C_0=C_1$ , then some  $k\in R$  satisfies

$$
k\tau = k,
$$

impossible because the left side is  $\tau$  and the right side is supported. Thus  $G(R)_R$  has exactly two elements  $C_0,C_1$ , and their operation table is the Boolean one. ∎

---

### Corollary 8.3

For a prime  $\mathfrak p\in\operatorname{Spec}(R)$ ,

$$
\mathcal O_{P_\tau}\cong \mathbf B, \qquad \mathcal O_{P_{\mathfrak p}}\cong G(R_{\mathfrak p}).
$$

#### Proof

By definition, the stalk at a prime is the localization at the complement. For  $P_\tau$ , the complement is the whole supported copy  $R$ , so Theorem 8.2 applies. For  $P_{\mathfrak p}$ , the complement is  $R\setminus\mathfrak p$ , so Theorem 8.1 applies. ∎

If  $R$  is an integral domain with fraction field  $K$ , then for the prime  $(0)$ ,

$$
\mathcal O_{P_{(0)}}\cong G(K).
$$

Hence there are two genuinely different generic local objects:

$$
\text{arithmetic generic stalk }G(K), \qquad \text{absolute generic stalk }\mathbf B.
$$

For  $R=\mathbf Z$ , the note computes exactly

$$
\mathcal O_{P_\tau}\cong \mathbf B,\qquad \mathcal O_{P_0}\cong G(\mathbf Q),\qquad \mathcal O_{P_p}\cong G(\mathbf Z_{(p)}),
$$

and  $\operatorname{Frac}(G(\mathbf Z))\cong \mathbf B$ .

---

### Proposition 8.4

Let  $\mathfrak p\in\operatorname{Spec}(R)$ . The residue semiring at  $P_{\mathfrak p}$  is canonically

$$
\kappa(P_{\mathfrak p})\cong \kappa(\mathfrak p),
$$

while

$$
\kappa(P_\tau)\cong \mathbf B.
$$

If  $R$  is a domain, then

$$
\kappa(P_{(0)})\cong \operatorname{Frac}(R).
$$

#### Proof

At  $P_\tau$ , the stalk is already  $\mathbf B$ . At  $P_{\mathfrak p}$ , the stalk is  $G(R_{\mathfrak p})$  and the maximal ideal is  $\mathfrak pR_{\mathfrak p}\cup\{\tau\}$ . Quotienting by it collapses  $\tau$  and  $\mathfrak pR_{\mathfrak p}$  to zero, leaving

$$
R_{\mathfrak p}/\mathfrak pR_{\mathfrak p}=\kappa(\mathfrak p).
$$

The domain case is the special case  $\mathfrak p=(0)$ . ∎

For  $R=\mathbf Z$ , this gives

$$
\kappa(P_\tau)=\mathbf B,\qquad \kappa(P_0)=\mathbf Q,\qquad \kappa(P_p)=\mathbf F_p.
$$

9\. Congruence classification
-----------------------------

Let  $J\triangleleft R$ . Define relations on  $G(R)$  by

$$
x\,\rho_J\,y \iff \bigl(x=y=\tau\bigr)\ \text{or}\ \bigl(x,y\in R\ \text{and}\ x-y\in J\bigr),
$$

and

$$
x\,\rho'_J\,y \iff \pi_J(x)=\pi_J(y),
$$

where

$$
\pi_J:G(R)\to R/J,\qquad \pi_J(\tau)=0,\quad \pi_J(r)=r+J.
$$

Then

$$
G(R)/\rho_J\cong G(R/J), \qquad G(R)/\rho'_J\cong R/J.
$$

---

### Theorem 9.1

Every congruence on  $G(R)$  is either  $\rho_J$  or  $\rho'_J$  for a unique ideal  $J\triangleleft R$ .

#### Proof

Let  $\sim$  be a congruence on  $G(R)$ . Define

$$
J:=\{r\in R:r\sim 0_R\}.
$$

Then  $J\triangleleft R$ : if  $a,b\in J$ , then  $a\sim 0_R$  and  $b\sim 0_R$ , so

$$
a+b=a\oplus b\sim 0_R\oplus 0_R=0_R.
$$

If  $r\in R$  and  $a\in J$ , then

$$
ra\sim r0_R=0_R.
$$

Thus  $J$  is an ideal.

Moreover, for  $a,b\in R$ ,

$$
a\sim b \iff a\oplus(-b)\sim b\oplus(-b)=0_R \iff a-b\in J.
$$

So the restriction of  $\sim$  to  $R$  is exactly congruence modulo  $J$ .

Now distinguish two cases.

If  $\tau\not\sim 0_R$ , then no supported element is equivalent to  $\tau$ . Indeed, if  $r\in R$  and  $r\sim \tau$ , then

$$
0_R=r\oplus(-r)\sim \tau\oplus(-r)=-r,
$$

hence  $-r\in J$ , so  $r\in J$ , so  $r\sim 0_R$ , contradicting  $\tau\not\sim 0_R$ . Therefore  $\tau$  forms a singleton class and  $\sim=\rho_J$ .

If  $\tau\sim 0_R$ , then for  $r\in R$ ,

$$
r\sim \tau \iff r\sim 0_R \iff r\in J.
$$

Hence  $\sim$  is exactly the kernel congruence of  $\pi_J$ , so  $\sim=\rho'_J$ .

Uniqueness of  $J$  is clear from the restriction to  $R$ . ∎

Thus every ring quotient  $R/J$  gives rise to two semiring quotients:

$$
G(R/J)\qquad\text{and}\qquad R/J.
$$

The first remembers the split zero. The second collapses it.

For  $R=\mathbf Z$ , this is exactly the classification proved in the note:

$$
G(\mathbf Z)/\rho_n\cong G(\mathbf Z/n\mathbf Z),\qquad G(\mathbf Z)/\rho_n'\cong \mathbf Z/n\mathbf Z. \text{ }
$$ 

10\. Product theorem and the global support bit
-----------------------------------------------

---

### Theorem 10.1

For nonzero commutative rings  $A,B$ ,

$$
G(A\times B)\cong G(A)\times_{\mathbf B} G(B),
$$

the fiber product being taken with respect to  $\chi_A,\chi_B$ .

#### Proof

Define

$$
\Phi:G(A\times B)\to G(A)\times_{\mathbf B}G(B)
$$

by

$$
\Phi(\tau)=(\tau,\tau),\qquad \Phi((a,b))=(a,b).
$$

This is well defined, since  $\chi_A(a)=\chi_B(b)=1$  for  $(a,b)\in A\times B$ , and  $\chi_A(\tau)=\chi_B(\tau)=0$ .

Conversely, an element of the fiber product is either  $(\tau,\tau)$ , or a pair  $(x,y)$  with  $\chi_A(x)=\chi_B(y)=1$ , hence  $x\in A$  and  $y\in B$ . So define

$$
\Psi(\tau,\tau)=\tau,\qquad \Psi(x,y)=(x,y)\in A\times B.
$$

These are inverse semiring homomorphisms. ∎

Thus  $G$  does not preserve direct products; it preserves them only after imposing one shared Boolean support coordinate.

### Example 10.2

By the Chinese remainder theorem,

$$
\mathbf Z/6\mathbf Z\cong \mathbf F_2\times \mathbf F_3,
$$

hence

$$
G(\mathbf Z/6\mathbf Z)\cong G(\mathbf F_2)\times_{\mathbf B}G(\mathbf F_3).
$$

The right-hand side has exactly  $6+1=7$  elements: six supported pairs and one common unsupported state  $(\tau,\tau)$ . It is strictly smaller than  $G(\mathbf F_2)\times G(\mathbf F_3)$ , which has  $3\cdot 4=12$  elements. The missing points are precisely the “partially unsupported” states  $(\tau,y)$  and  $(x,\tau)$ .

This is the exact algebraic content of the statement that  $\tau$  is a global support bit.

11\. Ideal multiplication and class monoids
-------------------------------------------

---

### Theorem 11.1

The map

$$
J\mapsto I_J=J\cup\{\tau\}
$$

is a bijection from the ideal lattice of  $R$  onto the ideals of  $G(R)$  distinct from  $\{\tau\}$ , and it preserves multiplication:

$$
I_J I_K = I_{JK}.
$$

#### Proof

Bijectivity is Theorem 6.1. For multiplication, every product of an element of  $I_J$  with an element of  $I_K$  is either  $\tau$  or an element of  $JK$ , so  $I_JI_K\subseteq I_{JK}$ .

Conversely,  $\tau\in I_JI_K$ . Every element of  $JK$  is a finite sum  $\sum_\nu a_\nu b_\nu$  with  $a_\nu\in J$ ,  $b_\nu\in K$ , and each  $a_\nu b_\nu\in I_JI_K$ ; therefore the sum lies in  $I_JI_K$ . Hence  $I_{JK}\subseteq I_JI_K$ . ∎

Suppose  $R$  is an integral domain. Define on nonzero ideals of  $R$  the usual principal-scaling equivalence

$$
J_1\sim_R J_2 \iff \exists a,b\in R\setminus\{0\}: aJ_1=bJ_2.
$$

Define on nontrivial ideals of  $G(R)$ 

$$
I_{J_1}\sim_G I_{J_2} \iff \exists a,b\in R\setminus\{0\}: aI_{J_1}=bI_{J_2}.
$$

---

### Proposition 11.2

$$
J_1\sim_R J_2 \iff I_{J_1}\sim_G I_{J_2}.
$$

Hence the ideal class monoid of  $R$  is canonically isomorphic to the class monoid of nontrivial ideals of  $G(R)$ .

#### Proof

If  $aJ_1=bJ_2$ , then

$$
aI_{J_1}=aJ_1\cup\{\tau\}=bJ_2\cup\{\tau\}=bI_{J_2}.
$$

Conversely, if

$$
aI_{J_1}=bI_{J_2},
$$

intersect both sides with  $R$ ; since  $a,b\neq 0$ , one obtains

$$
aJ_1=bJ_2.
$$

∎

For  $R=\mathcal O_K$ , a Dedekind domain, this recovers the note’s class-semigroup theorem

$$
\operatorname{Cl}(G(\mathcal O_K))\cong \operatorname{Cl}(K). \text{ :contentReference[oaicite:3]{index=3}}
$$

12\. Classical zeta versus separated-sheet zeta
-----------------------------------------------

Assume from now on that every nonzero ideal quotient  $R/J$  is finite; this includes  $R=\mathbf Z$  and  $R=\mathcal O_K$ .

Define

$$
N(J):=|R/J|
$$

for nonzero ideals  $J$ .

The note proves that for  $R=\mathcal O_K$ , the ideal zeta of  $G(\mathcal O_K)$  equals the classical Dedekind zeta.

The structural reason is now transparent.

---

### Proposition 12.1

The classical ideal zeta of  $G(R)$ , formed from ideal norms of the collapsed quotients, is

$$
\zeta^{\mathrm{idl}}_{G(R)}(s)=\sum_{0\neq J\triangleleft R}N(J)^{-s}.
$$

The support-separated congruence sheet is

$$
\zeta^{\mathrm{sep}}_{G(R)}(s):=\sum_{0\neq J\triangleleft R}\bigl(N(J)+1\bigr)^{-s},
$$

and the full finite-congruence zeta is

$$
\zeta^{\mathrm{cong}}_{G(R)}(s)=\zeta^{\mathrm{idl}}_{G(R)}(s)+\zeta^{\mathrm{sep}}_{G(R)}(s).
$$

#### Proof

The quotient attached to the ideal  $I_J$  by collapsing  $\tau$  is exactly  $R/J$ , so the classical ideal norm is  $N(J)$ . The separated quotient is  $G(R/J)$ , whose cardinality is  $|R/J|+1=N(J)+1$ . The formulas follow. ∎

---

### Proposition 12.2

If  $N$  is multiplicative on nonzero ideals, then the weight

$$
w(J):=N(J)+1
$$

is not multiplicative. Hence  $\zeta^{\mathrm{sep}}_{G(R)}$  is not an Euler product indexed by prime ideals.

#### Proof

For nonzero ideals  $J,K$ ,

$$
w(JK)=N(JK)+1=N(J)N(K)+1,
$$

while

$$
w(J)w(K)=(N(J)+1)(N(K)+1)=N(J)N(K)+N(J)+N(K)+1.
$$

The difference is  $N(J)+N(K)$ , which is positive. ∎

---

### Proposition 12.3

 $\zeta^{\mathrm{sep}}_{G(R)}$  and  $\zeta^{\mathrm{idl}}_{G(R)}$  have the same abscissa of absolute convergence.

#### Proof

For every nonzero ideal  $J$  and every  $\sigma>0$ ,

$$
N(J)\le N(J)+1\le 2N(J),
$$

hence

$$
2^{-\sigma}N(J)^{-\sigma}\le (N(J)+1)^{-\sigma}\le N(J)^{-\sigma}.
$$

Comparison gives the claim. ∎

### Example 12.4

For  $R=\mathbf Z$ ,

$$
\zeta^{\mathrm{idl}}_{G(\mathbf Z)}(s)=\sum_{n\ge 1}n^{-s}=\zeta(s),
$$
 
$$
\zeta^{\mathrm{sep}}_{G(\mathbf Z)}(s)=\sum_{n\ge 1}(n+1)^{-s}=\zeta(s)-1,
$$

and therefore

$$
\zeta^{\mathrm{cong}}_{G(\mathbf Z)}(s)=2\zeta(s)-1.
$$

For  $R=\mathcal O_K$ ,

$$
\zeta^{\mathrm{idl}}_{G(\mathcal O_K)}(s)=\zeta_K(s),
$$

while

$$
\zeta^{\mathrm{sep}}_{G(\mathcal O_K)}(s)=\sum_{0\neq J\triangleleft \mathcal O_K}(N(J)+1)^{-s}
$$

is a canonically defined non-Eulerian refinement.

13\. Element-theoretic factorization over a domain
--------------------------------------------------

Assume now that  $R$  is an integral domain.

---

### Proposition 13.1

The units of  $G(R)$  are exactly the units of  $R$ . Every nonzero supported irreducible of  $G(R)$  is exactly an irreducible of  $R$ , and conversely.

#### Proof

If  $u\in G(R)$  is a unit, then  $u\neq \tau$  since  $\tau x=\tau\neq 1$ . Thus  $u\in R$ , and its inverse must also lie in  $R$ . Hence units of  $G(R)$  are units of  $R$ .

Now let  $x\in R\setminus\{0\}$ . If  $x=ab$  in  $G(R)$ , then neither factor can be  $\tau$ , since otherwise  $ab=\tau$ . Hence  $a,b\in R$ , so factorization of  $x$  in  $G(R)$  is the same as factorization in  $R$ . The irreducibility statement follows. ∎

---

### Theorem 13.2

The supported zero  $0_R\in R\subset G(R)$  is prime in the divisibility sense and reducible.

#### Proof

It is reducible because

$$
0_R=0_R\cdot 0_R,
$$

and  $0_R$  is not a unit.

For divisibility-primality, suppose  $0_R\mid xy$ . Then

$$
xy=0_R\cdot c
$$

for some  $c\in G(R)$ . If  $c=\tau$ , then  $xy=\tau$ . If  $c\in R$ , then  $xy=0_R$ . Thus

$$
xy\in\{0_R,\tau\}.
$$

If  $x,y\in R\setminus\{0\}$ , then  $xy\in R\setminus\{0\}$ , impossible. Hence  $x\in\{0_R,\tau\}$  or  $y\in\{0_R,\tau\}$ , so  $0_R\mid x$  or  $0_R\mid y$ . ∎

Thus factorization is classical away from the supported zero, and fails precisely at the supported zero.

For  $R=\mathbf Z$ , this is exactly the phenomenon isolated in the note.

globalization\_note

14\. Scalar multiplicative norms cannot see the new generic layer
-----------------------------------------------------------------

Assume  $R$  is an integral domain with a multiplicative ideal norm  $N$  on nonzero ideals, and assume there exists a proper nonzero ideal  $J$  with  $N(J)>1$ . This applies to  $R=\mathbf Z$  and to rings of integers.

Let

$$
I_{(0)}=\{0_R,\tau\}.
$$

---

### Proposition 14.1

Let

$$
h:\{\text{ideals of }G(R)\}\to [0,\infty)
$$

satisfy

$$
h(I_1I_2)=h(I_1)h(I_2)
$$

for all ideals and

$$
h(I_J)=N(J)
$$

for every nonzero ideal  $J\triangleleft R$ . Then

$$
h(I_{(0)})=0,\qquad h(\{\tau\})=0.
$$

#### Proof

Choose a proper nonzero ideal  $J$  with  $N(J)>1$ . Since

$$
I_{(0)}I_J=I_{(0)},
$$

one has

$$
h(I_{(0)})=h(I_{(0)})h(I_J)=h(I_{(0)})N(J).
$$

Because  $N(J)\neq 1$ , it follows that  $h(I_{(0)})=0$ .

Similarly,

$$
\{\tau\}I_J=\{\tau\},
$$

so

$$
h(\{\tau\})=h(\{\tau\})N(J),
$$

hence  $h(\{\tau\})=0$ . ∎

Therefore any single positive multiplicative norm extending the classical norm is impossible on the full ideal set; if one allows the value  $0$ , both exceptional ideals collapse to the same boundary value. A one-parameter norm sees the classical ideal sheet and necessarily loses the semiring-specific generic doublet.

15\. The  $\mathbf Z$ \-case and the monoid comparison
------------------------------------------------------

For  $S=G(\mathbf Z)$ , the note proves:

$$
\operatorname{Spec}(S)=\{P_\tau,P_0,P_p\}, \qquad P_\tau\subsetneq P_0\subsetneq P_p,
$$
 
$$
\mathcal O_{P_\tau}\cong \mathbf B,\qquad \mathcal O_{P_0}\cong G(\mathbf Q),\qquad \mathcal O_{P_p}\cong G(\mathbf Z_{(p)}),
$$
 
$$
\operatorname{Frac}(S)\cong \mathbf B,
$$
 
$$
\operatorname{Spec}(M_S)\ \text{has infinite dimension},
$$

and

$$
\mathbf Z_0[M_S]\cong \mathbf Z\times \mathbf Z[M^\times].
$$

These statements imply the following formal consequence.

---

### Corollary 15.1

The multiplicative monoid of  $S$  does not determine the semiring geometry of  $S$ . More precisely, the passage

$$
S\mapsto M_S
$$

destroys the rigid one-point extension pattern:

$$
\dim \operatorname{Spec}(S)=2, \qquad \dim \operatorname{Spec}(M_S)=\infty,
$$

and ringization of the monoid,

$$
\mathbf Z_0[M_S],
$$

is disconnected:

$$
\operatorname{Spec}(\mathbf Z_0[M_S])\cong \operatorname{Spec}(\mathbf Z)\sqcup \operatorname{Spec}(\mathbf Z[M^\times]).
$$

Thus the rigidification is not multiplicative; it is genuinely semiring-theoretic and uses addition together with the split-zero coupling.

16\. Final synthesis
--------------------

#### Proof

For $S=G(\mathbf Z)$, the note proves $\dim\operatorname{Spec}(S)=2$, $\dim\operatorname{Spec}(M_S)=\infty$, and

$$
\mathbf Z_0[M_S]\cong \mathbf Z\times \mathbf Z[M^\times].
$$

The first two equalities show that passing to the multiplicative monoid destroys the rigid one-point semiring extension pattern. The ring product decomposition gives

$$
\operatorname{Spec}(\mathbf Z_0[M_S])\cong \operatorname{Spec}(\mathbf Z)\sqcup \operatorname{Spec}(\mathbf Z[M^\times]),
$$

so ringization of the monoid is disconnected. ∎


---

### Theorem 16.1

For every nonzero commutative ring  $R$ , the semiring  $G(R)$  satisfies the following.

First,  $G(R)$  is a fully faithful split-zero enlargement of  $R$ : it is canonically the subsemiring

$$
\{(r,b)\in R\times\mathbf B:\ b=0\Rightarrow r=0_R\},
$$

every semiring map  $G(R)\to A$  to a ring factors uniquely through  $p_R:G(R)\to R$ ,  $\chi_R:G(R)\to\mathbf B$  is the unique Boolean character, and

$$
\operatorname{Hom}(G(R),G(R'))\cong \operatorname{Hom}(R,R').
$$

Second, its prime geometry is exactly the classical prime geometry with one additional least prime:

$$
\operatorname{Spec}(G(R))=\{P_\tau\}\sqcup \{P_{\mathfrak p}:\mathfrak p\in\operatorname{Spec}(R)\},
$$

the closed stratum

$$
Y_R=V(\{0_R,\tau\})
$$

is canonically homeomorphic to  $\operatorname{Spec}(R)$ , and

$$
D(0_R)=\{P_\tau\}.
$$

If  $R$  is finite-dimensional, then  $\dim G(R)=\dim R+1$ .

Third, its local arithmetic is classical away from total inversion:

$$
G(R)_M\cong G(R_M)\qquad (0_R\notin M),
$$

but

$$
G(R)_R\cong \mathbf B.
$$

For domains this yields two distinct generic local objects,

$$
G(\operatorname{Frac}(R))\quad\text{and}\quad \mathbf B.
$$

Fourth, its quotient theory is doubled:  
every ideal  $J\triangleleft R$  yields exactly two congruences,

$$
\rho_J,\qquad \rho'_J,
$$

with quotients

$$
G(R/J),\qquad R/J.
$$

Fifth, its nontrivial ideal multiplication is classically conservative:

$$
I_JI_K=I_{JK},
$$

so ideal class theory and classical ideal zeta survive unchanged on number rings, exactly as in the note. On the other hand, the separated quotient sheet contributes the non-Eulerian Dirichlet series

$$
\sum_{0\neq J}(N(J)+1)^{-s}.
$$

Sixth, for integral domains, element-factorization is classical away from  $0_R$ , but  $0_R$  becomes divisibility-prime and reducible, so the factorization defect is concentrated at the supported zero.

This is the formal structure. It is neither a new ring nor a mere copy of the old one. It is  $R$  together with one global Boolean support coordinate, coupled to  $R$  only along the zero fiber.

## Response:
4/17/2026, 7:19:33 PM

Thought for 27m 4s

**Theorem A.**  
Let  $R$  be a nonzero commutative ring with identity, and let

$$
S:=G(R)=R\sqcup\{\tau\}
$$

with

$$
r\oplus s=r+s,\qquad r\oplus\tau=r,\qquad \tau\oplus\tau=\tau,
$$
 
$$
rs=rs,\qquad r\tau=\tau r=\tau,\qquad \tau^{2}=\tau .
$$

Write

$$
e:=0_R\in R\subset S, \qquad \mathbf B:=\{0,1\}.
$$

Relative to the classical arithmetic of  $R$ , the passage  $R\rightsquigarrow G(R)$  changes exactly the following structures.

1.  It introduces a canonical idempotent semiring endomorphism
    $$
    \nu_R:S\to S,\qquad \nu_R(x)=ex,
    $$
    whose image is the Boolean subsemiring  $\{\tau,e\}\cong \mathbf B$ .
2.  It introduces, for every left  $S$ \-semimodule  $M$ , a canonical idempotent projector
    $$
    \varepsilon_M(m)=em,
    $$
    whose image is a  $\mathbf B$ \-semimodule and whose kernel is an  $R$ \-module. In particular, the full subcategory of cancellative  $S$ \-semimodules is canonically equivalent to  $R$ \-Mod.
3.  It changes finite products into Boolean fiber products:
    $$
    G(A\times B)\cong G(A)\times_{\mathbf B}G(B).
    $$
4.  It is not determined by the multiplicative monoid alone: for a UFD  $R$  with infinitely many nonassociate irreducibles, the prime spectrum of the multiplicative monoid of  $S$  has infinite dimension, while the contracted monoid algebra is disconnected.
5.  On the zeta side, it produces a canonical shifted-norm deformation
    $$
    L_t(s)=\sum_{n\ge1}a_n(n+t)^{-s},
    $$
    whose  $n$ \-th  $t$ \-jet is
    $$
    \partial_t^{\,n}L_t(s)=(-1)^n(s)_nL_t(s+n),
    $$
    and whose logarithmic deformation is governed by universal partition polynomials in the shifted ratios  $L_t(s+m)/L_t(s)$ .

Conversely, the ring-reflective, cancellative, and ideal-theoretic parts of classical arithmetic are preserved: ring-valued morphisms out of  $S$  factor through  $R$ , cancellative linear algebra over  $S$  is exactly  $R$ \-linear algebra, and the baseline ideal/class/zeta sheet remains classical.

**Proof.**  
The preservational assertions are part of the baseline theory of  $G(R)$ .  
The new assertions are Theorems 1.1, 2.1, 2.3, 3.1, 3.4, 3.5, 4.2, 6.1, and 6.3 below. ∎

**Standing Hypothesis 0.1.**  
The baseline generalization package for  $G(R)$  is assumed: the classification of ideals, prime ideals, congruences, and localizations away from  $0_R$ ; the ring reflection

$$
p_R:S\to R,\qquad p_R(\tau)=0_R,\ p_R(r)=r;
$$

and the support character

$$
\chi_R:S\to\mathbf B,\qquad \chi_R(\tau)=0,\ \chi_R(r)=1\quad(r\in R).
$$

Only extensions beyond that package are stated and proved below.

1\. The supported-zero projector and its local meaning
------------------------------------------------------

**Theorem 1.1.**  
Define

$$
\nu_R:S\to S,\qquad \nu_R(x):=ex=0_Rx.
$$

Then:

1.   $\nu_R$  is a semiring endomorphism of  $S$ .
2.   $\nu_R^2=\nu_R$ .
3.   $\operatorname{Im}(\nu_R)=\{\tau,e\}$ .
4.   $\{\tau,e\}$  is a subsemiring of  $S$ , canonically isomorphic to  $\mathbf B$ .
5.  There is a factorization
    $$
    \nu_R=s_R\circ\chi_R,
    $$
    where
    $$
    s_R:\mathbf B\to S,\qquad s_R(0)=\tau,\ s_R(1)=e,
    $$
    is a semiring homomorphism, but not a unit-preserving one.
6.  For every ring homomorphism  $f:R\to R'$ ,
    $$
    G(f)\circ \nu_R=\nu_{R'}\circ G(f).
    $$

**Proof.**  
By definition,

$$
\nu_R(\tau)=e\tau=\tau,\qquad \nu_R(r)=er=0_Rr=0_R=e \qquad(r\in R).
$$

Hence the image is contained in  $\{\tau,e\}$ , and both  $\tau$  and  $e$  occur.

Now

$$
\tau\oplus\tau=\tau,\qquad \tau\oplus e=e,\qquad e\oplus e=e,
$$

because  $e\oplus e=0_R+0_R=0_R=e$  inside the supported copy of  $R$ . Also

$$
\tau^2=\tau,\qquad \tau e=e\tau=\tau,\qquad e^2=e.
$$

Thus  $\{\tau,e\}$  is a subsemiring of  $S$ . The map

$$
\{\tau,e\}\to\mathbf B,\qquad \tau\mapsto 0,\ e\mapsto 1
$$

is plainly a semiring isomorphism, with inverse  $s_R$ .

Since  $\chi_R(\tau)=0$ ,  $\chi_R(r)=1$ , and  $s_R(0)=\tau$ ,  $s_R(1)=e$ , one has

$$
(s_R\circ\chi_R)(\tau)=\tau=\nu_R(\tau),\qquad (s_R\circ\chi_R)(r)=e=\nu_R(r).
$$

Therefore

$$
\nu_R=s_R\circ\chi_R.
$$

Because both  $s_R$  and  $\chi_R$  are semiring homomorphisms,  $\nu_R$  is a semiring endomorphism.

Further,

$$
\nu_R^2=s_R\chi_R s_R\chi_R=s_R(\chi_R s_R)\chi_R=s_R\operatorname{id}_{\mathbf B}\chi_R=\nu_R,
$$

because  $\chi_R(\tau)=0$  and  $\chi_R(e)=1$ , whence  $\chi_R\circ s_R=\operatorname{id}_{\mathbf B}$ .

Finally, if  $f:R\to R'$  is a ring homomorphism, then  $G(f)(e)=0_{R'}=:e'$ , and for every  $x\in S$ ,

$$
G(f)(\nu_R(x))=G(f)(ex)=G(f)(e)G(f)(x)=e'G(f)(x)=\nu_{R'}(G(f)(x)).
$$

Thus  $G(f)\circ \nu_R=\nu_{R'}\circ G(f)$ . ∎

**Corollary 1.2.**  
The fixed-point set of  $\nu_R$  is exactly  $\{\tau,e\}$ .

**Proof.**  
If  $x=\tau$  or  $x=e$ , then  $\nu_R(x)=x$ . If  $x=r\in R\setminus\{0_R\}$ , then  $\nu_R(r)=e\neq r$ . ∎

**Corollary 1.3.**  
Let  $P_\tau=\{\tau\}$  and  $P_{\mathfrak p}=\mathfrak p\cup\{\tau\}$  for  $\mathfrak p\in\operatorname{Spec}(R)$ . Then

$$
D_S(e)=\{P_\tau\}.
$$

**Proof.**  
One has  $e\notin P_\tau$ , since  $e\in R$  and  $e\neq \tau$ . On the other hand,

$$
e=0_R\in \mathfrak p\subset P_{\mathfrak p}
$$

for every prime ideal  $\mathfrak p\subset R$ . Hence  $P_\tau$  is the unique prime of  $S$  not containing  $e$ . ∎

**Theorem 1.4.**  
Let  $r\in R\subset S$ , and let  $S_r$  denote localization of  $S$  at the multiplicative set  $\{1,r,r^2,\dots\}$ .

1.  If  $r$  is nilpotent in  $R$ , then
    $$
    D_S(r)=\{P_\tau\}, \qquad S_r\cong \mathbf B.
    $$
2.  If  $r$  is not nilpotent in  $R$ , then
    $$
    D_S(r)=\{P_\tau\}\cup \{P_{\mathfrak p}:r\notin\mathfrak p\},
    $$
    and
    $$
    S_r\cong G(R_r).
    $$

**Proof.**

(1) Suppose  $r^N=0_R=e$ . Since every prime ideal of  $R$  contains all nilpotent elements,  $r\in\mathfrak p$  for every  $\mathfrak p\in\operatorname{Spec}(R)$ . Therefore  $r\in P_{\mathfrak p}$  for all  $\mathfrak p$ , while  $r\notin P_\tau$  because  $P_\tau=\{\tau\}$  contains no supported element. Hence

$$
D_S(r)=\{P_\tau\}.
$$

Now localizing at  $r$  also inverts  $e=r^N$ . Conversely, in  $S_e$  one has  $e=1$ , hence

$$
r^N=e=1,
$$

so  $r$  is invertible in  $S_e$ . By the universal property of localization,

$$
S_r\cong S_e.
$$

It remains to prove  $S_e\cong \mathbf B$ .

Since  $e^2=e$ , the multiplicative set is  $\{1,e\}$ . Let  $C_0$  be the class of  $(\tau,1)$ . All fractions with numerator  $\tau$  represent  $C_0$ .

Let  $C_1$  be the class of  $(1,e)$ . If  $a\in R$ , then

$$
(a,1)\sim (1,e),
$$

because multiplying by  $e$  gives

$$
e\cdot e\cdot a=ea=e,\qquad e\cdot 1\cdot 1=e.
$$

Similarly,

$$
(a,e)\sim(1,e),
$$

because

$$
1\cdot e\cdot a=ea=e,\qquad 1\cdot e\cdot1=e.
$$

Thus every supported fraction is  $C_1$ .

A supported fraction cannot equal  $C_0$ : if  $(a,t)\sim (\tau,u)$  with  $a\in R$ , then for some  $c\in\{1,e\}$ ,

$$
cua=ct\tau=\tau,
$$

but the left side is supported and the right side is not. Contradiction.

Hence  $S_e$  has exactly two elements  $C_0,C_1$ , and their operations are

$$
C_0+C_0=C_0,\quad C_0+C_1=C_1,\quad C_1+C_1=C_1,
$$
 
$$
C_0C_0=C_0,\quad C_0C_1=C_0,\quad C_1C_1=C_1.
$$

Therefore  $S_e\cong \mathbf B$ , and so  $S_r\cong \mathbf B$ .

(2) If  $r$  is not nilpotent, then by the nilradical theorem there exists at least one prime  $\mathfrak p\subset R$  with  $r\notin \mathfrak p$ . Therefore

$$
D_S(r)=\{P_\tau\}\cup\{P_{\mathfrak p}:r\notin\mathfrak p\}.
$$

The localization statement

$$
S_r\cong G(R_r)
$$

is the baseline localization theorem applied to the multiplicative set  $\{1,r,r^2,\dots\}$ , which does not contain  $0_R$  because  $r$  is not nilpotent. ∎

**Corollary 1.5.**  
Assume  $r\in R$  is not nilpotent. Under the identifications

$$
\Gamma(D_S(r),\mathcal O_S)\cong G(R_r), \qquad \Gamma(D_S(e),\mathcal O_S)\cong \mathbf B,
$$

the restriction map

$$
\Gamma(D_S(r),\mathcal O_S)\to \Gamma(D_S(e),\mathcal O_S)
$$

is exactly the support character

$$
\chi_{R_r}:G(R_r)\to \mathbf B.
$$

**Proof.**  
By Theorem 1.4,

$$
\Gamma(D_S(r),\mathcal O_S)\cong S_r\cong G(R_r),
$$

while

$$
\Gamma(D_S(e),\mathcal O_S)\cong S_e\cong\mathbf B.
$$

Passing from  $D_S(r)$  to  $D_S(e)$  amounts to further localization at  $e=0_{R_r}$ . By the proof of Theorem 1.4(1), this localization collapses every supported element to  $1\in\mathbf B$  and sends  $\tau$  to  $0\in\mathbf B$ . This is precisely  $\chi_{R_r}$ . ∎

2\. Semimodule theory
---------------------

**Theorem 2.1.**  
Let  $M$  be a left  $S$ \-semimodule. Define

$$
\varepsilon_M:M\to M,\qquad \varepsilon_M(m):=em.
$$

Let

$$
L_M:=\operatorname{Im}(\varepsilon_M),\qquad K_M:=\ker(\varepsilon_M)=\{m\in M:em=0_M\}.
$$

Then:

1.   $\varepsilon_M$  is an additive idempotent  $S$ \-semimodule endomorphism.
2.  For every  $m\in M$ ,
    $$
    m+\varepsilon_M(m)=m.
    $$
3.   $L_M$  is an idempotent commutative monoid. Equivalently,  $L_M$  is a  $\mathbf B$ \-semimodule.
4.  Every supported scalar acts trivially on  $L_M$ :
    $$
    r\ell=\ell\qquad(r\in R,\ \ell\in L_M).
    $$
5.   $K_M$  is canonically an  $R$ \-module.
6.  The map
    $$
    \varepsilon_M:M\twoheadrightarrow L_M
    $$
    is a surjective  $S$ \-semimodule homomorphism with kernel  $K_M$ .

**Proof.**

(1) Additivity:

$$
\varepsilon_M(m+n)=e(m+n)=em+en=\varepsilon_M(m)+\varepsilon_M(n).
$$

Idempotence:

$$
\varepsilon_M^2(m)=e(em)=e^2m=em=\varepsilon_M(m).
$$

 $S$ \-linearity: if  $r\in R$ ,

$$
\varepsilon_M(rm)=e(rm)=(er)m=em,
$$

and

$$
r\varepsilon_M(m)=r(em)=(re)m=em.
$$

Also

$$
\varepsilon_M(\tau m)=e(\tau m)=(e\tau)m=\tau m=0_M=\tau(em)=\tau\varepsilon_M(m).
$$

Hence  $\varepsilon_M$  is an  $S$ \-semimodule endomorphism.

(2) Since  $1\oplus e=1$  in  $S$ ,

$$
m+\varepsilon_M(m)=1\cdot m+e\cdot m=(1\oplus e)m=1m=m.
$$

(3) Let  $\ell=\varepsilon_M(m)\in L_M$ . Then

$$
\ell+\ell=em+em=(e\oplus e)m=em=\ell,
$$

because  $e\oplus e=e$ . Thus every element of  $L_M$  is additively idempotent.

(4) If  $r\in R$  and  $\ell=em$ , then

$$
r\ell=r(em)=(re)m=em=\ell,
$$

because  $re=0_Rr=0_R=e$ . Also

$$
\tau\ell=\tau(em)=(\tau e)m=\tau m=0_M.
$$

Thus the  $S$ \-action on  $L_M$  factors through the two-element semiring  $\mathbf B$ , with all supported scalars acting by  $1$  and  $\tau$  acting by  $0$ .

(5) If  $m,n\in K_M$ , then

$$
e(m+n)=em+en=0_M,
$$

so  $m+n\in K_M$ . If  $r\in R$  and  $m\in K_M$ , then

$$
e(rm)=r(em)=0_M,
$$

so  $rm\in K_M$ . To obtain additive inverses, let  $m\in K_M$ . Then

$$
m+(-1)m=(1\oplus(-1))m=0_Rm=em=0_M.
$$

Hence  $(-1)m$  is an additive inverse of  $m$ . Therefore  $K_M$  is an abelian group under addition, stable under the action of  $R$ , hence an  $R$ \-module.

(6) Surjectivity is tautological from the definition of  $L_M$ . The kernel is exactly  $K_M$ . ∎

**Corollary 2.2.**  
If the additive monoid of  $M$  is cancellative, then

$$
\varepsilon_M=0, \qquad L_M=0, \qquad M=K_M,
$$

and  $M$  is canonically an  $R$ \-module.

**Proof.**  
By Theorem 2.1(2),

$$
m+\varepsilon_M(m)=m
$$

for every  $m\in M$ . Cancellation gives  $\varepsilon_M(m)=0_M$ . Thus  $M=K_M$ , and Theorem 2.1(5) applies. ∎

**Theorem 2.3.**  
Restriction along  $p_R:S\to R$  induces an equivalence of categories

$$
R\text{-}\mathbf{Mod}\simeq S\text{-}\mathbf{SMod}^{\mathrm{canc}},
$$

where the right-hand side is the full subcategory of cancellative left  $S$ \-semimodules.

**Proof.**  
If  $A$  is an  $R$ \-module, define an  $S$ \-action by

$$
r\cdot a:=ra\quad(r\in R),\qquad \tau\cdot a:=0.
$$

This makes  $A$  a cancellative  $S$ \-semimodule.

Conversely, if  $M$  is a cancellative  $S$ \-semimodule, then Corollary 2.2 shows that  $M$  is canonically an  $R$ \-module and that the  $S$ \-action factors uniquely through  $p_R$ .

These constructions are mutually inverse on objects. On morphisms, nothing further is required: an  $R$ \-linear map is automatically  $S$ \-linear for the induced  $S$ \-action, and an  $S$ \-linear map between cancellative  $S$ \-semimodules is  $R$ \-linear because the  $S$ \-action factors through  $R$ . ∎

**Corollary 2.4.**  
For the free  $S$ \-semimodule  $S^n$ ,

$$
K_{S^n}=0, \qquad L_{S^n}\cong \mathbf B^n.
$$

**Proof.**  
The operator  $\varepsilon_{S^n}$  acts coordinatewise. A coordinate  $x\in S$  satisfies  $ex=\tau$  if and only if  $x=\tau$ . Hence the only vector killed by  $\varepsilon_{S^n}$  is  $(\tau,\dots,\tau)$ , i.e. the zero vector. Thus  $K_{S^n}=0$ .

Its image consists exactly of vectors whose coordinates lie in  $\{\tau,e\}$ . By Theorem 1.1,  $\{\tau,e\}\cong \mathbf B$ , so  $L_{S^n}\cong \mathbf B^n$ . ∎

3\. Products, monoids, and reconstruction from the multiplicative side
----------------------------------------------------------------------

**Theorem 3.1.**  
For nonzero commutative rings  $A,B$ ,

$$
G(A\times B)\cong G(A)\times_{\mathbf B}G(B),
$$

where the fiber product is taken with respect to the support characters

$$
\chi_A:G(A)\to\mathbf B,\qquad \chi_B:G(B)\to\mathbf B.
$$

**Proof.**  
Define

$$
\Phi:G(A\times B)\to G(A)\times_{\mathbf B}G(B)
$$

by

$$
\Phi(\tau)=(\tau,\tau),\qquad \Phi((a,b))=(a,b).
$$

This is well-defined because  $\chi_A(a)=\chi_B(b)=1$  for  $(a,b)\in A\times B$ , while  $\chi_A(\tau)=\chi_B(\tau)=0$ .

Conversely, an element of the fiber product is either  $(\tau,\tau)$ , or a pair  $(x,y)$  with  $\chi_A(x)=\chi_B(y)=1$ , hence  $x\in A$  and  $y\in B$ . Define

$$
\Psi(\tau,\tau)=\tau,\qquad \Psi(x,y)=(x,y)\in A\times B.
$$

The maps  $\Phi$  and  $\Psi$  are inverse semiring homomorphisms. ∎

**Corollary 3.2.**  
For a finite family of nonzero commutative rings  $R_1,\dots,R_m$ ,

$$
G\!\Bigl(\prod_{i=1}^{m}R_i\Bigr)\cong G(R_1)\times_{\mathbf B}\cdots\times_{\mathbf B}G(R_m).
$$

**Proof.**  
Induction on  $m$ , using Theorem 3.1. ∎

**Corollary 3.3.**  
If

$$
R/J\cong \prod_{i=1}^{m} R_i,
$$

then

$$
G(R/J)\cong G(R_1)\times_{\mathbf B}\cdots\times_{\mathbf B}G(R_m).
$$

**Proof.**  
Apply Corollary 3.2 to  $R/J$ . ∎

**Theorem 3.4.**  
Let  $M_S=(S,\cdot)$  be the multiplicative monoid of  $S$ . Let  $T(S)$  be the quotient of the free commutative semiring  $\mathbb N[M_S]$  by the semiring congruence generated by

$$
[a]+[b]\sim[a+b]\qquad(a,b\in R),
$$

and

$$
[x]+[\tau]\sim[x]\qquad(x\in M_S).
$$

Then

$$
T(S)\cong S.
$$

**Proof.**  
Define

$$
\Phi:\mathbb N[M_S]\to S
$$

by  $\Phi([x])=x$ . The generating relations are valid in  $S$ : if  $a,b\in R$ , then

$$
a\oplus b=a+b,
$$

and for every  $x\in M_S$ ,

$$
x\oplus\tau=x.
$$

Therefore  $\Phi$  factors through a semiring homomorphism

$$
\overline\Phi:T(S)\to S.
$$

Conversely, define

$$
\Psi:S\to T(S),\qquad \Psi(x)=[x].
$$

This is multiplicative by construction. It is additive because

$$
\Psi(a\oplus b)=\Psi(a+b)=[a+b]=[a]+[b]=\Psi(a)+\Psi(b) \qquad(a,b\in R),
$$

and

$$
\Psi(x\oplus\tau)=\Psi(x)=[x]=[x]+[\tau]=\Psi(x)+\Psi(\tau) \qquad(x\in M_S).
$$

Hence  $\Psi$  is a semiring homomorphism.

The compositions  $\overline\Phi\Psi$  and  $\Psi\overline\Phi$  are the identity on generators, hence on the whole semirings. Thus  $T(S)\cong S$ . ∎

**Corollary 3.5.**  
The multiplicative monoid  $M_S$  does not determine  $S$  by itself; the missing datum is exactly the preaddition generated by

$$
[a]+[b]\equiv[a+b],\qquad [x]+[\tau]\equiv[x].
$$

**Proof.**  
This is Theorem 3.4 rephrased. In the standard terminology, monoids with zero and semirings both embed into the category of blueprints, and blueprint congruences correspond to quotients. ∎

**Theorem 3.6.**  
Assume that  $R$  is a UFD with infinitely many pairwise nonassociate irreducibles. Let  $\Pi$  be a fixed set of representatives of the irreducible classes. For  $\Sigma\subseteq\Pi$ , define

$$
\mathfrak p_\Sigma:= \{\tau,0_R\}\cup \{x\in R\setminus\{0\}: p\mid x \text{ for some }p\in\Sigma\}.
$$

Then:

1.   $\mathfrak p_\Sigma$  is a prime ideal of the commutative monoid  $M_S$ .
2.  For  $\Sigma_1,\Sigma_2\subseteq\Pi$ ,
    $$
    \mathfrak p_{\Sigma_1}\subseteq \mathfrak p_{\Sigma_2} \iff \Sigma_1\subseteq \Sigma_2.
    $$
3.   $\operatorname{Spec}(M_S)$  has infinite Krull dimension.

**Proof.**

(1) Let  $x\in\mathfrak p_\Sigma$ ,  $y\in M_S$ . If  $x=\tau$ , then  $yx=\tau\in\mathfrak p_\Sigma$ . If  $x=0_R$ , then  $yx\in\{0_R,\tau\}\subseteq\mathfrak p_\Sigma$ . If  $x\in R\setminus\{0\}$  is divisible by some  $p\in\Sigma$ , then for  $y=\tau$  one has  $yx=\tau$ , and for  $y\in R$  one has  $yx\in R$  still divisible by  $p$ . Thus  $\mathfrak p_\Sigma$  is an ideal.

It is proper because  $1\notin\mathfrak p_\Sigma$ .

Now suppose  $ab\in\mathfrak p_\Sigma$ . If  $ab=\tau$ , then  $a=\tau$  or  $b=\tau$ , so one factor lies in  $\mathfrak p_\Sigma$ . If  $ab=0_R$ , then  $a,b\in R$ , and since  $R$  is a domain,  $a=0_R$  or  $b=0_R$ . If  $ab\neq0_R$  and  $ab$  is divisible by some  $p\in\Sigma$ , then  $a,b\in R\setminus\{0\}$ , and irreducibles are prime in a UFD, so  $p\mid a$  or  $p\mid b$ . Hence  $a\in\mathfrak p_\Sigma$  or  $b\in\mathfrak p_\Sigma$ . Thus  $\mathfrak p_\Sigma$  is prime.

(2) If  $\Sigma_1\subseteq\Sigma_2$ , then  $\mathfrak p_{\Sigma_1}\subseteq\mathfrak p_{\Sigma_2}$  is immediate.

Conversely, assume  $\mathfrak p_{\Sigma_1}\subseteq\mathfrak p_{\Sigma_2}$ . Let  $p\in\Sigma_1$ . Then  $p\in\mathfrak p_{\Sigma_1}\subseteq\mathfrak p_{\Sigma_2}$ . By definition of  $\mathfrak p_{\Sigma_2}$ , some  $q\in\Sigma_2$  divides  $p$ . Since  $p,q$  are irreducible, they are associate. Because  $\Pi$  contains one representative per associate class,  $q=p$ . Hence  $p\in\Sigma_2$ . Therefore  $\Sigma_1\subseteq\Sigma_2$ .

(3) Choose pairwise distinct  $p_1,p_2,\dots\in\Pi$ . Then

$$
\{\tau\}\subsetneq \mathfrak p_{\{p_1\}} \subsetneq \mathfrak p_{\{p_1,p_2\}} \subsetneq \cdots \subsetneq \mathfrak p_{\{p_1,\dots,p_n\}}
$$

is a strictly increasing chain of prime ideals of arbitrary finite length. Hence  $\dim\operatorname{Spec}(M_S)=\infty$ . ∎

**Theorem 3.7.**  
Assume that  $R$  is an integral domain. Let  $R^\bullet:=R\setminus\{0\}$ , regarded as a multiplicative monoid. Let

$$
\mathbf Z_0[M_S]:=\mathbf Z[M_S]/([\tau]).
$$

Then

$$
\mathbf Z_0[M_S]\cong \mathbf Z[M]\cong \mathbf Z\times \mathbf Z[R^\bullet],
$$

where  $M=(R,\cdot)$  is the multiplicative monoid of  $R$ . Consequently,

$$
\operatorname{Spec}(\mathbf Z_0[M_S])\cong \operatorname{Spec}(\mathbf Z)\sqcup \operatorname{Spec}(\mathbf Z[R^\bullet]).
$$

**Proof.**  
Killing  $[\tau]$  removes the absorbing element  $\tau$ , so

$$
\mathbf Z_0[M_S]\cong \mathbf Z[M].
$$

Define

$$
\Phi:\mathbf Z[M]\to \mathbf Z\times \mathbf Z[R^\bullet]
$$

on basis elements by

$$
\Phi([0_R])=(1,0), \qquad \Phi([r])=(1,[r])\quad(r\neq0).
$$

Extend  $\mathbf Z$ \-linearly.

If one factor is  $[0_R]$ , then in  $\mathbf Z[M]$ ,

$$
[0_R][m]=[0_R]
$$

for every  $m\in M$ , and in the target,

$$
(1,0)\Phi([m])=(1,0)=\Phi([0_R]).
$$

If  $r,s\neq0$ , then  $rs\neq0$  because  $R$  is a domain, and

$$
\Phi([r])\Phi([s])=(1,[r])(1,[s])=(1,[rs])=\Phi([rs]).
$$

Thus  $\Phi$  is multiplicative.

Define

$$
\Psi:\mathbf Z\times \mathbf Z[R^\bullet]\to \mathbf Z[M]
$$

by

$$
\Psi\!\left(c,\sum_{r\neq0} a_r[r]\right)= \left(c-\sum_{r\neq0}a_r\right)[0_R]+\sum_{r\neq0}a_r[r].
$$

A direct computation gives  $\Psi\Phi=\operatorname{id}$  and  $\Phi\Psi=\operatorname{id}$ . Hence  $\Phi$  is an isomorphism.

The last statement follows from the elementary fact that the spectrum of a product ring is the disjoint union of the spectra of the factors. ∎

4\. Universal shifted-zeta deformation
--------------------------------------

**Definition 4.1.**  
Let

$$
L(s)=\sum_{n\ge1} a_n n^{-s}
$$

be a Dirichlet series with abscissa of absolute convergence  $\sigma_a$ . For  $|t|<1$ , define

$$
L_t(s):=\sum_{n\ge1} a_n(n+t)^{-s}.
$$

Define the shift operator  $T$  and the universal deformation generator  $D$  by

$$
(Tf)(s):=f(s+1),\qquad D:=sT.
$$

**Theorem 4.2.**  
For  $|t|<1$  and  $\Re(s)>\sigma_a$ ,

$$
\boxed{ L_t(s)=\sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^mL(s+m). }
$$

Equivalently,

$$
\boxed{ L_t=e^{-tD}L }
$$

as a convergent formal expansion in  $t$ .

**Proof.**  
For  $|u|<1$ , the binomial expansion gives

$$
(1+u)^{-s}=\sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}u^m.
$$

Apply this with  $u=t/n$ . Since  $|t|<1$ , one has  $|t/n|<1$  for every  $n$ , and

$$
(n+t)^{-s}=n^{-s}\Bigl(1+\frac{t}{n}\Bigr)^{-s} = \sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^m n^{-s-m}.
$$

Therefore

$$
L_t(s)=\sum_{n\ge1}a_n\sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^m n^{-s-m}.
$$

Absolute convergence for  $\Re(s)>\sigma_a$  allows interchange of sums:

$$
L_t(s)=\sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^m\sum_{n\ge1}a_n n^{-s-m} = \sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^mL(s+m).
$$

Finally,

$$
D^mL(s)=(s)_mL(s+m)
$$

by induction on  $m$ . Hence

$$
e^{-tD}L= \sum_{m\ge0}\frac{(-t)^m}{m!}D^mL = \sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^mL(s+m)=L_t.
$$

∎

**Corollary 4.3.**  
For every integer  $n\ge0$ ,

$$
\boxed{ \partial_t^{\,n}L_t(s)=(-1)^n(s)_nL_t(s+n). }
$$

In particular,

$$
\boxed{ \partial_t^{\,n}L_t(s)\big|_{t=0}=(-1)^n(s)_nL(s+n). }
$$

**Proof.**  
Differentiate termwise:

$$
\partial_t^{\,n}(m+t)^{-s}=(-1)^n(s)_n(m+t)^{-s-n}.
$$

Hence

$$
\partial_t^{\,n}L_t(s)= \sum_{m\ge1}a_m(-1)^n(s)_n(m+t)^{-s-n} = (-1)^n(s)_nL_t(s+n).
$$

Set  $t=0$ . ∎

**Theorem 4.4.**  
Assume that  $L$  extends meromorphically to  $\mathbf C$ . Fix  $N\ge1$  and  $|t|<1$ . Then, on the half-plane  $\Re(s)>\sigma_a-N$ ,

$$
\boxed{ L_t(s)=\sum_{m=0}^{N-1}(-1)^m\frac{(s)_m}{m!}t^mL(s+m)+H_{N,t}(s), }
$$

where  $H_{N,t}(s)$  is holomorphic on  $\Re(s)>\sigma_a-N$ .

**Proof.**  
For  $f_s(u)=(1+u)^{-s}$ , Taylor’s theorem with integral remainder gives

$$
f_s(u)=\sum_{m=0}^{N-1}\frac{f_s^{(m)}(0)}{m!}u^m +\frac{u^N}{(N-1)!}\int_0^1(1-\theta)^{N-1}f_s^{(N)}(\theta u)\,d\theta.
$$

Since

$$
f_s^{(N)}(u)=(-1)^N(s)_N(1+u)^{-s-N},
$$

we obtain, with  $u=t/n$ ,

$$
(n+t)^{-s} = \sum_{m=0}^{N-1}(-1)^m\frac{(s)_m}{m!}t^m n^{-s-m} + t^N n^{-s-N}R_N\!\left(\frac{t}{n},s\right),
$$

where  $R_N$  is holomorphic in  $s$  and uniformly bounded on compact subsets of  $\Re(s)>\sigma_a-N$ .

Multiply by  $a_n$  and sum over  $n$ . The first  $N$  terms give the stated finite sum. The remainder series

$$
t^N\sum_{n\ge1} a_n n^{-s-N}R_N\!\left(\frac{t}{n},s\right)
$$

converges absolutely and uniformly on compact subsets of  $\Re(s)>\sigma_a-N$ , because  $\sum |a_n|n^{-\Re(s)-N}$  does. Hence it defines a holomorphic function  $H_{N,t}(s)$ . ∎

**Corollary 4.5.**  
Assume that  $L$  has only one pole, namely a simple pole at  $s=1$ . Then every  $L_t$  has the same property, and

$$
\operatorname*{Res}_{s=1}L_t(s)=\operatorname*{Res}_{s=1}L(s).
$$

**Proof.**  
Apply Theorem 4.4 with arbitrary  $N$ . Every possible pole of  $L_t$  arises from a shifted term  $L(s+m)$ . At  $s=1$ , only the  $m=0$  term can contribute, because  $L(s+m)$  is regular there for  $m\ge1$ . Hence the residue is unchanged. ∎

**Corollary 4.6.**  
Let  $K$  be a number field, let  $a_K(n)$  denote the number of nonzero ideals of  $\mathcal O_K$  of norm  $n$ , and define

$$
\zeta_{K,t}(s):=\sum_{n\ge1} a_K(n)(n+t)^{-s} = \sum_{0\neq J\triangleleft \mathcal O_K}(N(J)+t)^{-s}.
$$

Then, for  $|t|<1$ ,

$$
\zeta_{K,t}(s)=\sum_{m\ge0}(-1)^m\frac{(s)_m}{m!}t^m\zeta_K(s+m),
$$

and  $\zeta_{K,t}$  extends meromorphically to  $\mathbf C$  with the same simple pole at  $s=1$  and the same residue as  $\zeta_K$ .

**Proof.**  
The classical Dedekind zeta function  $\zeta_K$  has a meromorphic continuation to  $\mathbf C$  with a unique simple pole at  $s=1$ . [Wikipedia](https://en.wikipedia.org/wiki/Dedekind_zeta_function?utm_source=chatgpt.com)  
Therefore Theorem 4.2 and Corollary 4.5 apply with  $L=\zeta_K$ . ∎

5\. The Hurwitz specialization
------------------------------

**Definition 5.1.**  
Set

$$
F_t(s):=\zeta_t(s)=\sum_{n\ge1}(n+t)^{-s} \qquad (0\le t\le1).
$$

Then

$$
F_t(s)=\zeta(s,1+t).
$$

**Proposition 5.2.**  
For  $0\le t\le1$ , the following identities hold.

1.   $F_t$  extends meromorphically to  $\mathbf C$  with only one pole, namely a simple pole at  $s=1$  of residue  $1$ .
2.  For  $\Re(s)>1$ ,
    $$
    F_t(s)=\frac1{\Gamma(s)}\int_0^\infty \frac{x^{s-1}e^{-tx}}{e^x-1}\,dx.
    $$
3.  Near  $s=1$ ,
    $$
    F_t(s)=\frac1{s-1}-\psi(1+t)+O(s-1).
    $$
4.  For every integer  $m\ge0$ ,
    $$
    F_t(-m)=-\frac{B_{m+1}(1+t)}{m+1}.
    $$
5.  One has
    $$
    F_t'(0)=\log\Gamma(1+t)-\frac12\log(2\pi).
    $$
6.  For  $0<t<1$ ,
    $$
    F_t(s)= -t^{-s} +2\Gamma(1-s)(2\pi)^{s-1} \left[ \sin\frac{\pi s}{2}\sum_{n\ge1}\frac{\cos(2\pi nt)}{n^{1-s}} +\cos\frac{\pi s}{2}\sum_{n\ge1}\frac{\sin(2\pi nt)}{n^{1-s}} \right].
    $$

**Proof.**  
The identity  $F_t(s)=\zeta(s,1+t)$  is the definition of the Hurwitz zeta at  $a=1+t$ . The meromorphic continuation and the simple pole at  $s=1$  are standard properties of the Hurwitz zeta. The integral representation follows from termwise Mellin inversion. The Laurent expansion, the Bernoulli-polynomial values at negative integers, the derivative at  $0$ , and Hurwitz’s formula are standard Hurwitz-zeta identities. [dlmf.nist.gov+3dlmf.nist.gov+3Wikipedia+3](https://dlmf.nist.gov/25.11#:~:text=The%20function%20was%20introduced%20in,function%20is%20a%20special%20case) ∎

**Corollary 5.3.**  
Define

$$
D_t(s):=\zeta(s)-F_t(s)=\zeta(s)-\zeta(s,1+t).
$$

Then:

1.   $D_t$  is entire.
2.  For every integer  $m\ge0$ ,
    $$
    D_t(-m)=\frac{B_{m+1}(1+t)-B_{m+1}}{m+1}.
    $$
3.  One has
    $$
    D_t'(0)=-\log\Gamma(1+t), \qquad e^{-D_t'(0)}=\Gamma(1+t).
    $$

**Proof.**  
Both  $\zeta(s)$  and  $F_t(s)$  have the same simple pole at  $s=1$  with residue  $1$ , by Proposition 5.2, so the difference is entire.

Now

$$
D_t(-m)=\zeta(-m)-F_t(-m).
$$

Using

$$
\zeta(-m)=-\frac{B_{m+1}}{m+1}, \qquad F_t(-m)=-\frac{B_{m+1}(1+t)}{m+1},
$$

we obtain

$$
D_t(-m)=\frac{B_{m+1}(1+t)-B_{m+1}}{m+1}.
$$

Finally,

$$
D_t'(0)=\zeta'(0)-F_t'(0).
$$

Since

$$
\zeta'(0)=-\frac12\log(2\pi), \qquad F_t'(0)=\log\Gamma(1+t)-\frac12\log(2\pi),
$$

one gets

$$
D_t'(0)=-\log\Gamma(1+t).
$$

Exponentiation gives the last identity. ∎

**Corollary 5.4.**  
For every integer  $q\ge0$ ,

$$
F_q(s)=\zeta(s)-\sum_{n=1}^{q}n^{-s}, \qquad D_q(s)=\sum_{n=1}^{q}n^{-s}.
$$

**Proof.**  
Since

$$
F_q(s)=\zeta(s,1+q)=\sum_{m\ge0}(m+1+q)^{-s}=\sum_{n\ge q+1}n^{-s},
$$

subtraction from  $\zeta(s)=\sum_{n\ge1}n^{-s}$  gives both formulas. ∎

**Corollary 5.5.**  
For every integer  $q\ge0$  and every  $m\ge0$ ,

$$
D_q(-m)=\sum_{n=1}^{q}n^m.
$$

In particular,  $D_t(-m)$  is the polynomial interpolation of the finite power sums.

**Proof.**  
Evaluate the identity of Corollary 5.4 at  $s=-m$ . ∎

**Corollary 5.6.**  
For every integer  $q\ge0$ ,

$$
e^{-D_q'(0)}=q!.
$$

**Proof.**  
This is Corollary 5.3 with  $t=q$ , since  $\Gamma(1+q)=q!$ . ∎

**Theorem 5.7.**  
Assume  $0<t<1$ . Then  $F_t$  is not an ordinary Dirichlet series in the variable  $n^{-s}$ . Consequently it admits no Euler product indexed by the integers or by the primes.

**Proof.**  
Assume, towards a contradiction, that

$$
F_t(s)=\sum_{n\ge1} b_n n^{-s}
$$

for  $\Re(s)$  sufficiently large. Let  $n_0$  be the smallest integer with  $b_{n_0}\neq0$ . Then as  $\sigma\to+\infty$ ,

$$
\sum_{n\ge1} b_n n^{-\sigma} = b_{n_0}n_0^{-\sigma}(1+o(1)),
$$

so its leading exponential scale is  $n_0^{-\sigma}$ .

On the other hand,

$$
F_t(\sigma)=\sum_{n\ge1}(n+t)^{-\sigma} = (1+t)^{-\sigma} \left( 1+O\!\left(\Bigl(\frac{1+t}{2+t}\Bigr)^\sigma\right) \right),
$$

so its leading exponential scale is  $(1+t)^{-\sigma}$ .

Therefore one must have

$$
n_0=1+t.
$$

But  $1+t\in(1,2)$  is not an integer. Contradiction. ∎

6\. The  $n$ \-th order deformation of the logarithm
----------------------------------------------------

**Definition 6.1.**  
Let  $L_t(s)$  be as in Definition 4.1, and assume  $L_t(s)\neq0$ . Define

$$
A_n(t;s):=(s)_n\frac{L_t(s+n)}{L_t(s)} \qquad (n\ge1).
$$

Define also

$$
\kappa_n(t;s):=\partial_t^{\,n}\log L_t(s).
$$

**Proposition 6.2.**  
For every  $n\ge1$ ,

$$
\partial_t A_n(t;s)=A_1(t;s)A_n(t;s)-A_{n+1}(t;s).
$$

**Proof.**  
Differentiate:

$$
A_n(t;s)=(s)_n\frac{L_t(s+n)}{L_t(s)}.
$$

Hence

$$
\partial_t A_n = (s)_n\frac{\partial_t L_t(s+n)}{L_t(s)} - (s)_n\frac{L_t(s+n)\partial_t L_t(s)}{L_t(s)^2}.
$$

By Corollary 4.3,

$$
\partial_t L_t(s+n)=-(s+n)L_t(s+n+1), \qquad \partial_t L_t(s)=-sL_t(s+1).
$$

Therefore

$$
\partial_t A_n = -(s)_{n+1}\frac{L_t(s+n+1)}{L_t(s)} + (s)_n\frac{L_t(s+n)}{L_t(s)}\cdot s\frac{L_t(s+1)}{L_t(s)},
$$

which is

$$
\partial_t A_n=-A_{n+1}+A_nA_1.
$$

∎

**Theorem 6.3.**  
For every  $n\ge1$ ,

$$
\boxed{ \kappa_n(t;s)= (-1)^n \sum_{\pi\in\Pi_n} (-1)^{|\pi|-1}(|\pi|-1)! \prod_{B\in\pi} A_{|B|}(t;s), }
$$

where  $\Pi_n$  is the set of set partitions of  $\{1,\dots,n\}$ .

**Proof.**  
Let

$$
m_n(t;s):=\frac{\partial_t^{\,n}L_t(s)}{L_t(s)}.
$$

By Corollary 4.3,

$$
m_n(t;s)=(-1)^nA_n(t;s).
$$

Define exponential generating functions

$$
M(z):=\sum_{n\ge0}m_n\frac{z^n}{n!}, \qquad K(z):=\sum_{n\ge1}\kappa_n\frac{z^n}{n!}.
$$

Taylor expansion gives

$$
L_{t+z}(s)=L_t(s)M(z).
$$

On the other hand,

$$
\log L_{t+z}(s)-\log L_t(s)=K(z),
$$

so

$$
L_{t+z}(s)=L_t(s)e^{K(z)}.
$$

Therefore

$$
M(z)=e^{K(z)}, \qquad K(z)=\log M(z).
$$

The coefficient formula for the logarithm of an exponential generating series is the classical moment-cumulant identity:

$$
\kappa_n= \sum_{\pi\in\Pi_n} (-1)^{|\pi|-1}(|\pi|-1)! \prod_{B\in\pi} m_{|B|}.
$$

Substituting  $m_{|B|}=(-1)^{|B|}A_{|B|}$ , and noting that the total sign is  $(-1)^n$ , yields the stated formula. ∎

**Corollary 6.4.**  
The first four logarithmic deformation coefficients are

$$
\kappa_1=-A_1,
$$
 
$$
\kappa_2=A_2-A_1^2,
$$
 
$$
\kappa_3=-A_3+3A_1A_2-2A_1^3,
$$
 
$$
\kappa_4=A_4-4A_1A_3-3A_2^2+12A_1^2A_2-6A_1^4.
$$

**Proof.**  
Expand the partition formula of Theorem 6.3 for  $n=1,2,3,4$ . ∎

**Theorem 6.5.**  
For every integer  $r\ge1$ ,

$$
Q_r(s):=\frac{\zeta(s+r)}{\zeta(s)}
$$

has a Dirichlet expansion

$$
Q_r(s)=\sum_{n\ge1}\alpha_r(n)n^{-s},
$$

where  $\alpha_r$  is multiplicative and

$$
\alpha_r(p^k)=-\frac{p^r-1}{p^{rk}} \qquad (k\ge1).
$$

Equivalently,

$$
\boxed{ \alpha_r(n)=(-1)^{\omega(n)} \frac{\prod_{p\mid n}(p^r-1)}{n^r}. }
$$

**Proof.**  
Using the Euler product for  $\zeta$ ,

$$
Q_r(s)=\prod_p \frac{1-p^{-s}}{1-p^{-s-r}}.
$$

At a fixed prime  $p$ , set  $u=p^{-s}$ . Then

$$
\frac{1-u}{1-u/p^r} = (1-u)\sum_{k\ge0}p^{-rk}u^k = 1+\sum_{k\ge1}\bigl(p^{-rk}-p^{-r(k-1)}\bigr)u^k = 1-\sum_{k\ge1}\frac{p^r-1}{p^{rk}}u^k.
$$

Therefore the local coefficients are

$$
\alpha_r(p^0)=1, \qquad \alpha_r(p^k)=-\frac{p^r-1}{p^{rk}} \quad(k\ge1).
$$

Multiplicativity follows from the Euler product. For

$$
n=\prod_{p\mid n}p^{v_p(n)},
$$

one has

$$
\alpha_r(n)= \prod_{p\mid n}\left(-\frac{p^r-1}{p^{r v_p(n)}}\right) = (-1)^{\omega(n)} \frac{\prod_{p\mid n}(p^r-1)}{n^r}.
$$

∎

**Corollary 6.6.**  
At  $t=0$ ,

$$
A_r(0;s)=(s)_r Q_r(s) = (s)_r\sum_{n\ge1}\alpha_r(n)n^{-s}.
$$

In particular,

$$
\partial_t \log \zeta_t(s)\Big|_{t=0} = -s\sum_{n\ge1}\alpha_1(n)n^{-s},
$$

and

$$
\partial_t^2 \log \zeta_t(s)\Big|_{t=0} = (s)_2\sum_{n\ge1}\alpha_2(n)n^{-s} - s^2\left(\sum_{n\ge1}\alpha_1(n)n^{-s}\right)^2.
$$

**Proof.**  
The first identity is the definition of  $A_r$ . The logarithmic derivatives are Corollary 6.4 at  $t=0$ . ∎

**Corollary 6.7.**  
The second-order deformation is not primewise local. Its quadratic term already contains Dirichlet convolution of the first-order kernel with itself.

**Proof.**  
By Corollary 6.6,

$$
\left(\sum_{n\ge1}\alpha_1(n)n^{-s}\right)^2 = \sum_{n\ge1}(\alpha_1*\alpha_1)(n)n^{-s}.
$$

Thus the second-order term couples distinct prime supports through convolution. ∎

7\. Exact Eulerian defects for integer sheets and the two-point Stone model
---------------------------------------------------------------------------

**Definition 7.1.**  
For an integer  $m\ge0$ , define

$$
F_m(s):=\zeta(s,m+1)=\sum_{n\ge m+1}n^{-s}, \qquad D_m(s):=\zeta(s)-F_m(s)=\sum_{n=1}^{m}n^{-s}.
$$

For  $u\in\mathbf C$ , define

$$
\mathcal Z_{m,u}(s):=\zeta(s)+uF_m(s).
$$

**Theorem 7.2.**  
The Dirichlet coefficients of  $F_m$  are

$$
a_m(n)=\mathbf 1_{n>m}.
$$

For coprime  $r,s$ , define

$$
\Delta_m(r,s):=a_m(rs)-a_m(r)a_m(s).
$$

Then

$$
\Delta_m(r,s)= \mathbf 1_{rs>m}-\mathbf 1_{r>m}\mathbf 1_{s>m}.
$$

In particular,

$$
F_m \text{ has a classical Euler product } \iff m=0.
$$

**Proof.**  
The coefficient formula is immediate from the definition of  $F_m$ . The defect formula is the same identity rewritten.

If  $m=0$ , then  $F_0=\zeta$ , which is Eulerian.

If  $m=1$ , then  $a_1(1)=0$ , but any multiplicative coefficient function for an Euler product must satisfy  $a(1)=1$ . Hence  $F_1$  is not Eulerian.

If  $m\ge2$ , choose  $r=2$  and  $s$  an odd prime  $>m$ . Then  $(r,s)=1$ ,  $a_m(2)=0$ ,  $a_m(s)=1$ , but  $a_m(2s)=1$ . Hence  $\Delta_m(2,s)=1$ , so  $a_m$  is not multiplicative. ∎

**Theorem 7.3.**  
The Dirichlet coefficients of  $D_m$  are

$$
c_m(n)=\mathbf 1_{n\le m}.
$$

For coprime  $r,s$ , define

$$
\delta_m(r,s):=c_m(rs)-c_m(r)c_m(s).
$$

Then

$$
\delta_m(r,s)= \mathbf 1_{rs\le m}-\mathbf 1_{r\le m}\mathbf 1_{s\le m}.
$$

In particular,

$$
D_m \text{ has a classical Euler product } \iff m=1 \text{ or } m=2.
$$

**Proof.**  
The coefficient and defect formulas are immediate.

For  $m=1$ ,  $D_1(s)=1$ , which is trivially Eulerian.

For  $m=2$ ,

$$
D_2(s)=1+2^{-s}=(1+2^{-s})\prod_{p\neq2}1,
$$

so  $D_2$  is Eulerian.

Assume  $m\ge3$ . If  $m$  is odd, choose  $r=2$ ,  $s=m$ ; then  $r,s\le m$ ,  $(r,s)=1$ , and  $rs=2m>m$ , so  $\delta_m(r,s)=-1$ . If  $m$  is even, choose  $r=2$ ,  $s=m-1$ ; then  $r,s\le m$ ,  $(r,s)=1$ , and  $rs=2m-2>m$ , so again  $\delta_m(r,s)=-1$ . Thus  $c_m$  is not multiplicative. ∎

**Theorem 7.4.**  
The Dirichlet coefficients of  $\mathcal Z_{m,u}$  are

$$
b_{m,u}(n)= \begin{cases} 1,& n\le m,\\[1mm] 1+u,& n>m. \end{cases}
$$

For coprime  $r,s$ , define

$$
\Delta_{m,u}(r,s):=b_{m,u}(rs)-b_{m,u}(r)b_{m,u}(s).
$$

Then

$$
\Delta_{m,u}(r,s)= \begin{cases} u,& r,s\le m \text{ and } rs>m,\\[1mm] -u(1+u),& r,s>m,\\[1mm] 0,& \text{otherwise}. \end{cases}
$$

Consequently,

$$
\mathcal Z_{m,u}\text{ is Eulerian } \iff u=0 \text{ or } (u=-1 \text{ and } m=1,2).
$$

**Proof.**  
The coefficient formula follows from

$$
\mathcal Z_{m,u}(s)=\sum_{n\le m}n^{-s}+(1+u)\sum_{n>m}n^{-s}.
$$

Now inspect the cases:

*   If  $r,s\le m$  and  $rs>m$ , then  $b(r)=b(s)=1$ ,  $b(rs)=1+u$ , so  $\Delta_{m,u}=u$ .
*   If  $r,s>m$ , then  $b(r)=b(s)=1+u$ ,  $b(rs)=1+u$ , so
    $$
    \Delta_{m,u}=(1+u)-(1+u)^2=-u(1+u).
    $$
*   In all remaining cases, one factor is  $\le m$  and the other  $>m$ , or all three are  $\le m$ ; in each such case the multiplicativity defect is  $0$ .

The Eulerian classification follows. If  $u=0$ , then  $\mathcal Z_{m,0}=\zeta$ . If  $u=-1$ , then  $\mathcal Z_{m,-1}=D_m$ , and Theorem 7.3 applies. For all other  $u$ , one of the two nonzero defect regimes survives. ∎

**Definition 7.5.**  
Let

$$
e:=\mathbf 1_{\{1\}}, \qquad f:=\mathbf 1_{\mathbf N_{\ge2}}
$$

as functions on  $\mathbf N$ . Let  $X=\{\xi_1,\xi_\ast\}$  be the Stone spectrum of the Boolean algebra generated by  $e,f$ . The multiplication on  $\mathbf N$  induces a semigroup law on  $X$ :

$$
\xi_1\xi_1=\xi_1,\qquad \xi_1\xi_\ast=\xi_\ast\xi_1=\xi_\ast,\qquad \xi_\ast\xi_\ast=\xi_\ast.
$$

Let  $\Delta$  be the comultiplication on functions on  $X$ , defined by pullback along multiplication:

$$
(\Delta g)(x,y):=g(xy).
$$

Let

$$
\mathcal D(a)(s):=\sum_{n\ge1}a(n)n^{-s}
$$

denote the Dirichlet transform.

**Theorem 7.6.**  
With the notation above:

1.  One has
    $$
    \mathcal D(e)=1,\qquad \mathcal D(f)=\zeta(s)-1.
    $$
2.  The comultiplication formulas are
    $$
    \Delta(e)=e\otimes e, \qquad \Delta(f)=f\otimes e+e\otimes f+f\otimes f.
    $$
3.  Hence
    $$
    \Delta(f)-f\otimes f=f\otimes e+e\otimes f.
    $$
    After coprime Dirichlet summation, this yields
    $$
    \sum_{(m,n)=1} \bigl(\Delta(f)-f\otimes f\bigr)(m,n)\,m^{-s}n^{-t} = \zeta(s)+\zeta(t)-2.
    $$
4.  For
    $$
    a_\lambda:=e+\lambda f, \qquad \lambda=1+u,
    $$
    one has
    $$
    \Delta(a_\lambda)-a_\lambda\otimes a_\lambda = (\lambda-\lambda^2)f\otimes f = -u(1+u)\,f\otimes f.
    $$
5.  Consequently, the coprime defect-generating series of  $\mathcal Z_{1,u}(s)=(1+u)\zeta(s)-u$  is
    $$
    \mathfrak D_u(s,t):= \sum_{(m,n)=1}\Delta_{1,u}(m,n)m^{-s}n^{-t} = -u(1+u) \left( \frac{\zeta(s)\zeta(t)}{\zeta(s+t)} -\zeta(s)-\zeta(t)+1 \right).
    $$

**Proof.**  
(1) Immediate from the definitions.

(2) Evaluate at the four pairs  $(\xi_1,\xi_1)$ ,  $(\xi_1,\xi_\ast)$ ,  $(\xi_\ast,\xi_1)$ ,  $(\xi_\ast,\xi_\ast)$ .

(3) Subtract the formulas in (2). The coprime Dirichlet sum of  $f\otimes e$  is

$$
\sum_{\substack{(m,n)=1\\ m\ge2,\ n=1}}m^{-s}n^{-t} = \sum_{m\ge2}m^{-s} = \zeta(s)-1,
$$

and similarly the coprime Dirichlet sum of  $e\otimes f$  is  $\zeta(t)-1$ .

(4) Expand:

$$
\Delta(a_\lambda)=\Delta(e)+\lambda\Delta(f) = e\otimes e+\lambda(f\otimes e+e\otimes f+f\otimes f),
$$

while

$$
a_\lambda\otimes a_\lambda = e\otimes e+\lambda(f\otimes e+e\otimes f)+\lambda^2 f\otimes f.
$$

Subtracting gives the stated identity.

(5) The coefficient function of  $\mathcal Z_{1,u}$  is  $a_\lambda$ , with  $\lambda=1+u$ . Thus its defect on coprime pairs is  $(\lambda-\lambda^2)$  on the interior sector  $m,n>1$ , and  $0$  otherwise. Therefore

$$
\mathfrak D_u(s,t) = (\lambda-\lambda^2) \sum_{\substack{(m,n)=1\\m,n>1}}m^{-s}n^{-t}.
$$

Now

$$
\sum_{(m,n)=1}m^{-s}n^{-t} = \prod_p \left( 1+\sum_{a\ge1}p^{-as}+\sum_{b\ge1}p^{-bt} \right) = \prod_p\frac{1-p^{-s-t}}{(1-p^{-s})(1-p^{-t})} = \frac{\zeta(s)\zeta(t)}{\zeta(s+t)}.
$$

Subtract the cases  $m=1$  or  $n=1$ :

$$
\sum_{\substack{(m,n)=1\\m,n>1}}m^{-s}n^{-t} = \frac{\zeta(s)\zeta(t)}{\zeta(s+t)}-\zeta(s)-\zeta(t)+1.
$$

Multiply by  $\lambda-\lambda^2=-u(1+u)$ . ∎

**Corollary 7.7.**  
At the doubled endpoint  $u=1$ , one has

$$
\mathcal Z_{1,1}(s)=2\zeta(s)-1, \qquad \mathfrak D_1(s,t)= -2\left( \frac{\zeta(s)\zeta(t)}{\zeta(s+t)}-\zeta(s)-\zeta(t)+1 \right).
$$

**Proof.**  
Substitute  $u=1$  into Theorem 7.6. ∎

**Corollary 7.8.**  
At the origin,

$$
F_1(0)=-\frac32, \qquad \mathcal Z_{1,1}(0)=-2, \qquad \mathfrak D_1(0,0)=-3.
$$

**Proof.**  
From  $\zeta(0)=-\frac12$ ,

$$
F_1(0)=\zeta(0)-1=-\frac32, \qquad \mathcal Z_{1,1}(0)=2\zeta(0)-1=-2.
$$

Also

$$
\frac{\zeta(0)\zeta(0)}{\zeta(0)}-\zeta(0)-\zeta(0)+1 = -\frac12+\frac12+\frac12+1=\frac32.
$$

Therefore

$$
\mathfrak D_1(0,0)=-2\cdot \frac32=-3.
$$

The value  $\zeta(0)=-\tfrac12$  is standard. [Wikipedia+1](https://en.wikipedia.org/wiki/Riemann_zeta_function?utm_source=chatgpt.com) ∎

8\. Final synthesis
-------------------

**Theorem 8.1.**  
Let  $S=G(R)$ . Relative to classical arithmetic over  $R$ , the passage  $R\rightsquigarrow S$  has the following exact effect.

1.  It preserves the ring-reflective part: every ring-valued morphism out of  $S$  factors through  $R$ .
2.  It preserves the cancellative linear part: cancellative  $S$ \-semimodules are exactly  $R$ \-modules.
3.  It preserves the ordinary ideal sheet: ideal multiplication, ideal class theory, and the classical ideal zeta remain unchanged on the baseline sheet.
4.  It adds a support projector
    $$
    \nu_R(x)=0_Rx
    $$
    and therefore a Boolean shadow on every  $S$ \-semimodule.
5.  It adds an absolute localization boundary: the supported zero  $e=0_R$  cuts out the unique basic open
    $$
    D_S(e)=\{P_\tau\},
    $$
    and localization at a nilpotent supported element collapses to  $\mathbf B$ .
6.  It changes finite products into Boolean fiber products:
    $$
    G(A\times B)\cong G(A)\times_{\mathbf B}G(B).
    $$
7.  It is not determined by its multiplicative monoid: forgetting addition produces an infinite-dimensional prime spectrum in the UFD case, and the contracted monoid algebra becomes disconnected.
8.  On the quotient-size side it adds a non-Eulerian shifted deformation
    $$
    L_t(s)=\sum a_n(n+t)^{-s},
    $$
    whose entire  $n$ \-th order deformation theory is controlled by shifted copies  $L_t(s+n)$ , equivalently by the shifted tower  $L(s+n)$  at  $t=0$ .
9.  In the Riemann case, the split-zero deformation interpolates finite power sums and factorials through
    $$
    D_t(-m)=\frac{B_{m+1}(1+t)-B_{m+1}}{m+1}, \qquad e^{-D_t'(0)}=\Gamma(1+t).
    $$

**Proof.**  
Items (1) and (3) are baseline. Item (2) is Theorem 2.3. Item (4) is Theorem 1.1 and Theorem 2.1. Item (5) is Corollary 1.3 and Theorem 1.4. Item (6) is Theorem 3.1. Item (7) is Theorem 3.6 and Theorem 3.7. Item (8) is Theorem 4.2, Corollary 4.3, and Theorem 6.3. Item (9) is Corollary 5.3 and Corollary 5.5. ∎

---

**Sources:**

- [Dedekind zeta function](https://en.wikipedia.org/wiki/Dedekind_zeta_function?utm_source=chatgpt.com)
- [DLMF: §25.11 Hurwitz Zeta Function ‣ Related Functions ‣ Chapter 25 Zeta and Related Functions](https://dlmf.nist.gov/25.11#:~:text=The%20function%20was%20introduced%20in,function%20is%20a%20special%20case)

## Response:
4/19/2026, 6:44:22 AM





---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)

---
