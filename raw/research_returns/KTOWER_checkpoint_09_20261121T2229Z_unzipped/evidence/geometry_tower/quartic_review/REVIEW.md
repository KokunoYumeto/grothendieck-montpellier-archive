# Independent quartic/quintic review

Reviewer: `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed.
Check time: 2026-11-21 21:16:01 UTC. Project: KTOWER.

## Scope and verdict

**PASS** for the complete written proof in
`evidence/unitary_audit/reducible_comparison/quartic_quintic_obstruction.tex`,
SHA256 `9eadd4eaa1e94cbf4e3bbd7ed9f395aabb1a4313a5e6479d0ec8adfe477650a0`.
All 371 lines were read. The corresponding complete BCH program was read
and a byte-identical copy was freshly executed here. Every mathematical
report field agreed with the author's report; the execution UTC was
necessarily different.

This review uses the already checked ordinary-component, auxiliary-unit,
Poitou–Tate, Euler, and étale-excision inputs. The relevant definitions and
proof chain in `cubic_massey_condition.tex` and `cubic_excision_norm.tex`
were read for their applicability. It is not a fresh whole-proof audit of
Milne's foundational duality or class-field-theory theorems.

## Specific checks

- The integer torus weights and involution signs admit exactly the three
  quartic and two quintic lines displayed. In particular the positive
  quartic line cannot be omitted.
- The Cartier dual of the positive quartic character is the even
  character `eta*omega^(1-2e)`. Its local invariants vanish at the residue
  prime and at the primes of the quadratic discriminant. Full upper-root
  local freedom therefore leaves precisely raw global H2. Strict
  class-field identification has no quotient by prime classes, because
  those permutation modules have no component in that character.
- The given unit at exponent `2e` kills both the negative quartic strict
  group and its even mirror. Global H1 and local H1 have dimension one,
  giving the stated isomorphism and zero relative obstruction.
- The diagonal calculation correctly descends through the away-prime
  unramified conditions to ramification only at the residue prime. The
  degree-p cyclotomic character generates global H1 and maps nontrivially
  onto local H1 modulo unramified H1. Global H2 is zero. Thus its relative
  degree-two obstruction group is zero.
- In the lower quintic line, ordinary flag changes give coboundaries,
  so the local cohomology condition remains zero. If raw global H2 has
  dimension `r`, global Euler gives global H1 dimension `r`; local H1
  has dimension one. The localization kernel has dimension `d`, since
  restriction to the cyclotomic field identifies it with equivariant
  homomorphisms from its p-class group, and the unique prime above p is
  principal. The relative exact sequence therefore gives dimension
  `(1-r+d)+r=1+d`.
- Differences between acceptable quartic lifts in the negative and
  diagonal directions are global coboundaries and can be removed by
  permitted degree-four conjugations. The remaining positive difference
  brackets only into the upper quintic line. Consequently the lower
  relative class is independent of the quartic lift for the fixed cubic
  family.

## Computation

The independently replayed program builds matrix exponentials, multiplies
them, and computes the logarithm in bivariate polynomials truncated at
degree four. It does not assume the proposed BCH coefficient expressions.
It checks all five degree-four monomials, six bracket identities, and five
involution signs. This proves exact rational polynomial identities only;
it does not compute any arithmetic cocycle, Massey value, or source jet.

Script SHA256:
`a70ac2fc09a1e7cd848a46bdb725c62b989e1d44ecebe595327b140acd4459bf`.
Fresh report SHA256:
`a89e510fa45565eb881862a8f62ca24dd7408c12963559a79484f430f29402c7`.

No injectivity or nonzero arithmetic obstruction is inferred from the
dimension count. No new main-gate movement is claimed by this review.
