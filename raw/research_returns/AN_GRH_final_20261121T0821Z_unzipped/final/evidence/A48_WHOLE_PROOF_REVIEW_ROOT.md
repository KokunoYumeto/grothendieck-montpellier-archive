# A48: root whole-proof review

Date: 2026-11-21, completed approximately06:28 UTC.
Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH /root.
Event: targeted proof check, whole written proof. Verdict: PASS.

I read the entire first4a7d80fb manuscript, including all four steps and the final scope, and then the entire final source SHA256 `0f942d786563c2fabee27b995042a70d8567bd77f430dd4f656c25699ea8324c`. The final changes correct TeX and specify the exact Katz and Tate-module duality inputs. This is a same-model reading and not a formal verification.

The geometric character line bundles are nontrivial of degree zero and have coherent H1 dimension g-1. The stable-part comparison is deck-functorial; dualizing inverts characters without changing the dimension bound. Thus the actual primitive p-torsion space has total dimension at most(g-1)phi(n). The proof explicitly uses the full faithful character collection and imposes no ordinary hypothesis.

For a constant geometric deck group, Frobenius commutes with every character idempotent. A twist multiplies each eigenvalue by the faithful character value of sigma^t. Each eigenvalue forbids at most one t; using algebraic multiplicity is a safe union bound in the presence of Jordan blocks. A fixed vector over the splitting field exists exactly when the Fp matrix has nonzero fixed space, and nonzero rational p-primary torsion contains p-torsion. This proves the unpointed supply count. The n forms over C are distinct because the full geometric automorphism group of this Galois cover over C is precisely its cyclic deck group.

On the fixed P fibre, the original Frobenius is translation by a. Exactly t=-a gives a rational point. If another twist is pointed after degree m constants, m(a+t)=0; the entire descent action, not merely the action on a selected character, then equals the pointed model's mth Frobenius. The cover and actual primitive factor identify over that extension and the original rational subgroup injects. Thus an unpointed good twist cannot be used to evade the original pointed obstruction by a later field extension.

For nonconstant action a, I checked the affine formula a^m x+N_m(a)t and the sign of the conjugation exponent N_m(a)t-(1-a^m)x. A fixed point makes that exponent zero, giving an isomorphism of the covers over the extension. The proof makes no unjustified count of nonconstant twists. The scope correctly leaves changes of geometric cover, conductor or base available, and does not infer prescribed-point success from an average or prime density.

Primary-source scope: the source Katz comparison is precisely located and its all-genus/all-characteristic hypotheses were directly reread by the author and /effective_galois, with retained audit records. This root event records a whole reading of the new argument, not a new root reading of the entire Katz paper.
