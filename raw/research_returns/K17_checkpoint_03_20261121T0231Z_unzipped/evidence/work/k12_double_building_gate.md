# K17-K12-DOUBLE: a finite double-building gate

Date: 2026-11-21 UTC. Author/checker: /root/vandiver_k,
GPT-6 Astra Pro, reasoning effort not exposed.
Status: proved conditional reduction, full argument read back. The three
new homology vanishings in the hypothesis are not established here.

Let R=Z[1/13!]. Write T²(Z^N) for the double building of pairs of
compatible proper direct-summand flags, as in Miller--Patzt--Putman,
arXiv:2509.01559v1, §1.7 and §23.4. Let St_r denote the integral
Steinberg module, with St_1=Z.

## Statement

Assume

    H~_10(T²(Z^9);R)=0,
    H~_11(T²(Z^9);R)=0,
    H~_11(T²(Z^10);R)=0.                         (DB)

Then

    H_4(GL_9(Z); St_9⊗R)=0,
    H_3(GL_10(Z); St_10⊗R)=0.

Together with the already checked K17-K12-TWO-RANKS reduction this
would prove K12(Z)=0. The claim is the displayed implication only.

## Proof

For i>=-1 define the augmented decomposition complex

    S_i(Z^N)= ⊕_(V_1⊕...⊕V_(i+2)=Z^N) St(V_1)⊗...⊗St(V_(i+2)),

where every summand V_j has positive rank. Thus S_-1=St_N.
The differential multiplies adjacent Steinberg apartment classes, with
the usual alternating signs. These are precisely the source's §23.3
and §30.4 definitions.

Theorem 23.3, p.49, identifies

    H_i(S_•(Z^N)) = H~_(i+N-1)(T²(Z^N)).

The same equality holds after tensoring with R, by flatness. Theorem D'
on p.64 proves exactness at S_-1,S_0,S_1 for every N>=4.
For N=9, (DB) adds exactness at S_2,S_3. Therefore

    S_4⊗R -> S_3⊗R -> ... -> S_0⊗R -> St_9⊗R -> 0

is exact. For N=10, the last part of (DB) adds exactness at S_2,
so the corresponding sequence starting at S_3⊗R is exact.

In either case put d=4 for N=9 and d=3 for N=10. Add the kernel of
S_d⊗R -> S_(d-1)⊗R as a term in degree d+1. This gives an exact
resolution by R-free modules, not necessarily projective group modules.
The standard hyperhomology spectral sequence converges to
H_*(GL_N(Z);St_N⊗R); for 0<=p<=d its first page is

    E^1_(p,q)= ⊕_(r_1+...+r_(p+2)=N, r_j>=1)
      H_q(∏_j GL_(r_j)(Z); ⊗_j (St_(r_j)⊗R)).       (1)

This is exactly the proof of MPP Lemma 23.5, pp.50--51, applied at a
single rank. For completeness, GL_N(Z) is transitive on ordered direct
sum decompositions having a given rank tuple; its stabilizer is the
product of the corresponding general linear groups. Thus each chain
term is induced from that product and Shapiro's lemma gives (1).
The extra kernel term has p=d+1 and cannot lie on total degree d.

We check every term of (1) with p+q=d. DEKM Table 5, p.17, together
with its explicit Theorem 4.5 and Proposition 1.5, gives the following
complete low-degree data over R:

- For 1<=r<=8 and 0<=q<=4, the only nonzero groups are
  H_0(GL_1;St_1⊗R)=R and H_3(GL_3;St_3⊗R)=
  H_3(GL_4;St_4⊗R)=R.
- For r=9, H_q(GL_9;St_9⊗R)=0 for 0<=q<=3.

The first item includes the GL_1 assertion directly because GL_1(Z)
has order two. All indicated localizations in the table are contained
in R. In these ranges every homology module is zero or R, hence free,
so the iterated Künneth formula has no Tor contributions in the degrees
under consideration.

For N=9, every proper factor has rank at most eight. A nonzero
Künneth tensor contributing in degree q<=4 would have either:

1. only rank-one factors, each in degree zero; or
2. one rank-three or rank-four factor in degree three, with every other
   factor rank one in degree zero.

The first possibility forces q=0,p=4 and total rank p+2=6, not nine.
The second forces q=3,p=1 and has three factors of total rank at most
4+1+1=6, again not nine. Thus every total-degree-four term is zero.

For N=10, factors have rank at most nine, but rank-nine factors have
zero homology through degree three. The same Künneth list applies.
Only rank-one factors would force q=0,p=3 and total rank five.
One rank-three or rank-four factor would force q=3,p=0 and total rank
at most 4+1=5. Neither gives rank ten. Every total-degree-three term
is therefore zero.

The spectral sequences consequently give the two asserted vanishings.
The previously checked two-rank implication then supplies the last
conditional conclusion about K12. No statement about differentials,
connectivity, or torsion beyond the explicit hypotheses was inserted.

## What this changes

MPP's general Theorem C assumes a connectivity range at every rank.
The implication above needs only the three displayed extra homology
groups at ranks nine and ten. Existing n-connectivity supplies the
lower groups automatically. This is a more local sufficient gate, not
a solution of the gate and not a new numerical K-group vanishing.

## Actual check

The complete argument above was read after writing. The index shift
i+N-1, exactness endpoints S_3/S_2, the extra kernel degree, all
Künneth possibilities, and the absence of low-degree Tor terms were
reconstructed. MPP Theorem 23.3 and the entire proof of Lemma 23.5
were read; DEKM Table 5 was inspected visually. The cited general
source theorems are background inputs, not newly re-proved here.
