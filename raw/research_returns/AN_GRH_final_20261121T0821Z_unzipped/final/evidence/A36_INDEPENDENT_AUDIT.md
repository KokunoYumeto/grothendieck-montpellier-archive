# Independent whole-proof review of A36

- Date: 2026-11-21 UTC.
- Checker: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.
- Source read in full: `work/gt_certificates/positive_rank_theta/A36_REFLECTION_NO_FIVE.tex`.
- Source SHA-256: `0ba06d3c9f2ee2cfa017511ca9c27c662b1c764cfcff92fcf8768a65f0479573`.
- Outcome: **PASS**.
- Formal verification: false.

## Mathematical checks

The degree-five Lang quotient uses the unique order-five Sylow subgroup because the verified Jacobian order is `65520 = 5*13104` with `5` not dividing `13104`. The supplied nonzero projected generator and complete cycle prove surjectivity. Pullback of the connected isogeny along the Abel map is geometrically connected by the checked A12 input, and its fibre over the chosen Weierstrass point is split.

The occupancies give `76 + 45*(zeta+...+zeta^4) = 31` for every faithful character. The genus-two character polynomial has top coefficient 256 because the pointing is Weierstrass. Thus the whole new factor has numerator `(1+31T+256T^2)^4`; its modulo-two degree is four, so it is ordinary of dimension four.

The unique geometric reflection fixing the selected rational lift is Galois invariant, hence is defined over the same finite field. Consequently both reflection maps used in the A33 isogeny are defined there. The isogeny to `J_E^2` yields the square-root numerator with constant coefficient one, and its value at one is `288^2 = 2^10*3^4`. A fixed rational canonical class has unchanged geometric order after any field extension. The conclusion correctly concerns these fixed classes; it does not exclude new five-primary classes at newly rational points or a three-primary detector.

The full Picard-group identity was checked independently. The exact pullback/norm relation gives `T^2 = T_2 + 2`. The five terms of `1+T+T_2` form the degree-five fibre. At a branch fibre the orbit decomposition is one simple point and two double points, agreeing with the divisor multiplicities. Hence `(T^2+T-1)L = deg(L)*F` holds before restriction to degree zero. Substitution of the Raynaud theta characteristic gives `b_0=(T+3)a`; the polynomial identity gives `(2-T)(T+3)=5` and `(2-T)b_0=5a`. These endomorphisms are invertible on every prime-primary group away from five. The argument does not divide by two or infer a nonzero five-primary component from these equations.

## Exact finite arithmetic evidence inspected

I read both complete retained implementations and their JSON outputs:

1. Root's binary-linear interpolation calculation:
   - code `work/root/verify_A36_quintic_linear.py`, SHA-256 `0c8c269abbcbd40f28b93d2b660c81ef5d19f8043599f7a81d9f03617a862614`;
   - JSON SHA-256 `ce2910cec3a96126ae2ecda86110d023e8bc00ec20810808ac8f6ee82dc9d9ea`.
2. Row agent's extended-GCD Cantor calculation:
   - code `work/row_audit/verify_A36_conductor5_cantor.py`, SHA-256 `e8a90caf30608422df566d6ccf9203a3f2dd72d1ad15bf156b183bb54ef00688`;
   - JSON SHA-256 `4504d5214dce26b8afcc69396ad42d7f04eb5c94ee53ac8128e3a34dff04cec7`.

The two group-law implementations are distinct. I checked their invariant-preserving reduction formulas and their field conventions against the written reciprocal curve. A separate exact JSON comparison confirms that **all 256 point images**, the **entire five-element cycle**, generator, occupancy vector, character polynomial, and reflection numerator agree point for point.

This review did **not** introduce a third implementation, rerun either supplied producer, or formally verify the group-law code. The existing independent executions remain attributed to their original producers/checkers.
