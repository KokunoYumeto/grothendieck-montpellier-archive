# Boundary of a first-uniformizer curvature image-length proposal

This is an all-rank zero calculation for one proposed detector, not a vanishing theorem for a representation class or for C.1.

Let A be a dyadic DVR with uniformizer pi and 2=v*pi^e, where e>=2. Put R=A/pi^3 and let T be any finite free R-involution. Lift T to a matrix over A. Its two Tate differentials are d0=T-I and d1=T+I. On reduction modulo pi these are the same matrix d=Tbar-I, with d^2=0. Thus the two residual Tate homology groups identify with the same space H=ker(d)/im(d).

The first pi-Bocksteins on these two copies of H are induced by dividing the corresponding lifted differential of a lifted residual cycle by pi. The two divided vectors differ by (2/pi) times that cycle. Since e>=2, 2/pi lies in pi*A. Their residues therefore coincide, and so the two Bockstein maps beta0 and beta1 on H are identical.

Their curvature matrices are also identical: both lifted Tate products equal Ttilde^2-I, so both are C=(Ttilde^2-I)/pi^3. Any well-defined induced curvature operator c on H is consequently the same in both parities. On every residual c-primary part, the two images of the first pi-Bockstein are therefore the same module. Their composition lengths agree, not merely modulo3.

Accordingly the proposed quantity

    h_q = length(im beta0 on H_q) - length(im beta1 on H_q) modulo3

is identically zero for all such involutions. This conclusion needs no general additivity claim: equality of the two images already forces the value to vanish. In particular it cannot detect the first unresolved normal node 2=v*pi^2, xy=pi^3*u by specialization to A/pi^3.

This differs from the previously refuted second-page parity proposal. That earlier proposal could be nonzero but was not additive on actual admissible extensions. The present first-page image difference is zero even before an additivity question can help.

## Exact finite record

The program `code/C_finish_ramified_firstpi_curvature_zero.py` uses the exact eight-element ring Z[pi]/(pi^2-2,pi^3). It checks all rank-one and rank-two involutions and every member of the 530-extension family used in the earlier second-page counterexample. It explicitly evaluates both divided differentials on every residual cycle vector in those cases, and checks that the common exact curvature preserves the residual differential.

The saved output is `logs/C_finish_ramified_firstpi_curvature_zero.json`. Its finite scope does not replace the arbitrary-rank argument above. No code output asserts that any node lattice class vanishes.

The executed certificate checked 2 rank-one and 112 rank-two involutions, all 530 prior-family extensions, and 37,552 residual cycle vectors. Runtime was 0.8078069770126604 seconds.
