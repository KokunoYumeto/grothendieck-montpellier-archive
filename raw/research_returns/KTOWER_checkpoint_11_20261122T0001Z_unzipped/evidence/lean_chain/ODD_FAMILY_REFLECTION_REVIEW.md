# Independent review of the odd-family rational mirror scope

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21. No Lean kernel build was run.

PASS: the entire 45-line proof of `KT-ODD-FAMILY-RATIONAL-MIRROR` was read. Its reviewed SHA256 is `658a1bb2ccd183bac1019c146269bfcdbd7c25c7b7ff612ad01a04fd3d480b87`.

For p congruent to 3 modulo 4 and `e=(p-3)/2+(p-1)t`, the mirror exponent `e+1` is the quadratic exponent `(p-1)/2`. The imaginary quadratic class number of Q(sqrt(-p)) is less than p, by the same explicitly cited finite-character class-number formula used in the already reviewed odd-discriminant family. For H of order `(p-1)/2`, extension followed by norm is the sum of the H action on the cyclotomic class group. It annihilates H-invariant p-primary classes because the quadratic base class group has no p-part; multiplication by the prime-to-p order of H is invertible. Thus the quadratic mirror eigenspace is zero.

The reflection step uses the even representative `e0=(p-3)/2` in `[2,p-3]`. I reread the whole carried K17-REFLECTOR proof in input `K17.tex:4533–4619` and its all-positive-k comparison at `696–705`. Its reflection half turns zero mirror component into zero `[-e0]` component. The all-weight conclusion uses periodicity only of the class-group character exponent, followed by the carried K-theory comparison; it does not claim periodicity of K-group orders.

This precisely shows that the explicit auxiliary-field family does not settle a previously uncontrolled rational component. It leaves its third auxiliary unit as a distinct unproved statement and gives no generic rank-three exclusion.
