import os
OUT = r"<local>/Documents/reports_20261124/INTAKE_PILE_20261124"
WHO = "Claude Opus 5.5 at effort high, ZETA_GRH cluster reader of the intake pile (launched by main session 329fb1e6)"
D = "2026-11-24"
EV = {
"GRH_ALGORITHMS_FINISH": [
 ("GRH-P148 (lem:cyclotomic-primary-quotient, Lemma 16.3)", "targeted proof check",
  "confirmed (posted TeX l.4178-4259): K_l=Q(zeta_l)^{H_l} of degree r^b is real since h_l=(l-1)/r^b is even; Gaussian periods are an integral basis (orbit sums of the permutation basis zeta^a, 1<=a<=l-1); ord_l(p) | d | r-1 so Frobenius is trivial in the r-group and p splits completely; gcd(Phi_l, eta_j(T)-t_j) selects exactly the h_l roots restricting to the residue map (periods and 1=-sum eta_j generate O_K; the root set is Frobenius-stable); gcd(h_l,r)=1 since b=v_r(l-1)"),
 ("GRH-P149 (thm:bounded-congruence-cofactor, Thm 1.2)", "targeted proof check",
  "confirmed given P147 (posted TeX l.4261-4340): the order-l element eps, nonconstant on each rank-r component, lies in <theta> there, so some comparison with theta^j gives a proper factor f of X^r-z of degree j in (0,r); b=(-1)^j f(0), b^r=z^j, Bezout; the norm n=N_{B/A}(y) has n^r=z^{h_l} with gcd(h_l,r)=1, and Bezout gives x^r=z in A; the closing rank obstruction for partial subfields of degree r^j, j<b, is also right"),
 ("GRH-P147 (prop:quantitative-real-residue, Prop 16.1)", "targeted proof check",
  "read in part (posted TeX l.3714-4139). Confirmed: the sole conditional step (a prime q in the index-4 coset q=3 mod 4, (p/q)=1 of (Z/QZ)^*, Q=4pD_K P_0, so q>Q_0 automatically; (-q/p)=(p/q)=1 by reciprocity); the CM type {(g,1): g not 1} u {(1,c)} has trivial left and right stabilizers for m>=3; the masks e_tau=(tau pi)^{p-1} separate the primes above p via the trivial right stabilizer of Phi^{-1}. Not re-derived: the statement of LLS Thm 1.4, the theta atlas, the von Kanel-Kret height bound, the Pazuki comparison, the extension of the marking, Pila's algorithm"),
 ("edition vs run cp07 text, section 16.2 (Lemma 16.3 and proof of Thm 1.2)", "used and rechecked in this run",
  "diff of the run's cp07 grh_algorithms.tex against the posted Codex edition: only Codex's two edits differ (the explicit b=(-1)^j f(0) with Bezout; 'at most one prime-order auxiliary algebra open at a time' during each simultaneous-root call, replacing the run's too-strong 'at most one prime-order auxiliary adjunction on any base branch')"),
],
"GRH_ALGORITHMS": [
 ("GRH-P125 (thm:fixed-wild-cm), auxiliary imaginary quadratic field", "targeted proof check",
  "confirmed (posted TeX l.3245-3290): the indicator (1/4)(1-chi_{-4})(1+chi_{D_p}) with D_p=p or 4p fundamental gives four characters mod 4p, only one principal; A gives main term x/4 and error O(sqrt(x) log 2p), so q<<log^2 p; (-q/p)=(p/q)=1 for q=3 mod 4; p splits completely in R_b because p^d=1 mod r^b and d | r-1. The rest of P125/P126 (theta, Pila) not re-derived here (same chain as P147)"),
],
"GRH_NIGHT": [
 ("MT-S506 (S506.5, S506.6)", "computation or formal certificate",
  "own script (scratchpad/zg/s5.py): the seven S5 characters built from chi_V=#Fix-1, chi_W=(chi_V^2+chi_V(g^2))/2-1-chi_V, chi_X=(chi_V^2-chi_V(g^2))/2 are orthonormal; Ind_J 1=1+V, Ind_J eta=eta+V eta, Ind_F20 1=1+W eta, Ind_F20 eta=eta+W, Ind_F20 tau=X, Ind_T alpha=V+X, Ind_T(alpha eta)=V eta+X; sign restricted to F20 equals tau^2. The seven order inequalities and (S506.3) re-derived from the table"),
 ("CX-ALG-016", "computation or formal certificate",
  "recomputed: in F_7[X]/(X^3-2), alpha^7=4alpha, alpha^49=2alpha, L=alpha+4alpha^7+2alpha^49=(1+16+4)alpha=21alpha=0; X^3-2 is irreducible since 2 is not a cube mod 7"),
],
"ZETA_HEAT": [
 ("thm:cosine-lower-rate", "targeted proof check",
  "confirmed given Mori (rh-alone 2026) Lemmas 3.3-3.5, Mori (sharp 2026) Lemma 2.2 and Voss 1999 Thm 2 and Cor 1: weighted-norm algebra ((2/k) int u w(u/k) du = kB; archimedean term <= A l+ (L+ + C)^2/k); positive pair average (each ordered pair at distance <h, the diagonal included, contributes >= 2pi(1-C/k)); packing max{N_J-P_h, N_J^2/(N_J+2P_h)}; exact scalar comparison (difference (1-b)((3-A)b-A)/(2b) for b>=3/5; 50/57>7/8 below); rescaling with eps=1/s and D=O(s mu^{1/d}); Weil normalization F(x)=fhat(pi x/L) in PW_pi with ||F||^2=2L||f||^2. Numerics (scratchpad/zg/cos.py): d=0.83625035, 1/d=1.19581415, A=1.00613<=51/50, B=0.32137<=1/3, A+B=1.32750=1/2+c cot c=3-2d. Note: the gain over Mori is 6/5 -> 1.19581 in the power of mu"),
],
"ZETA_NEXT": [
 ("NG01", "targeted proof check",
  "confirmed given Deligne-Milne Prop 6.5, 6.23, Thm 6.25 and Commelin 4.13-4.16 (noncm/findings.tex l.31-105): D_M=(G_M^0)^der is characteristic in G_M^0 hence normal in G_M; the trivial and nontrivial D_M-isotypic parts are G_M-stable, so the projector is an idempotent endomorphism of M over Q; the identity component acting on V^{D_M} is a quotient of the torus G_M^0/D_M, hence potentially CM; the connected semisimple D_M maps trivially to a torus, which gives maximality of C(M); realizations preserve idempotents"),
 ("NX-L01 (example)", "computation or formal certificate",
  "y^2=x^3-x over F_5: x^3-x takes the values 0,0,1,4,0 at x=0..4, so 7 affine points, #E(F_5)=8, a_5=-2; the affine zeta function is (1+2t+5t^2)/(1-5t), inverse roots of modulus sqrt 5"),
],
"ZETA_TWO": [
 ("IA09", "independent re-proof",
  "confirmed: sum_a a^2 - sum_a a(p-a) = p(p-1)(p-2)/6, so the mean of |L(1,chi)|^2 over the (p-1)/2 odd characters mod p is pi^2(p-1)(p-2)/(6p^2) < pi^2/6, and some odd chi has |L(1,chi)| <= pi/sqrt 6"),
 ("IA09", "computation or formal certificate",
  "own script (scratchpad/zg/ia09.py), p=3,5,7,11,13,101,211,997: the mean square equals the formula to 6 digits; the minima 0.6046, 0.8886, 0.8976, 0.7586, 0.5990, 0.5368, 0.3527, 0.3382 are all <= pi/sqrt 6 = 1.2825"),
],
"THETA3": [
 ("THETA3-C32", "targeted proof check",
  "cohomological and numerical steps confirmed (THETA3.tex l.14285-14807): weights (1,3,2,2,2,2) of y^4=t prod(t-b_j)^2 (degree 9 gives weight 3 at infinity); genus 4; rho has eigenvalues +-i of multiplicity 4 and z^j dz/y has eigenvalue i (j even), -i (j odd), so the determinant lines have type (2,2); N-invariance forces equal characters, so the primitive part of H^4(W_0) is wedge^4 H^1_i + wedge^4 H^1_{-i}; |G|=4^3*4!=1536; on P_0 the norm l_0 l_inf^3 prod l_bj^2 is a scalar times (u1 u2 u3)^4; c(Omega^1(1))=1-H+H^2, so (Q0-Q2)^2=2; 1536*2=3072; a: H^4 -> A has generic degree 24 and a^* identifies W_{Q(i)}(A) with q^*U_0; 24*3072=73728. The blowup inertia argument (C32l-C32n) read, not independently re-derived"),
],
"TRACE_DET": [
 ("DET-18", "targeted proof check",
  "whole proof confirmed (TRACE_DET.tex l.1765-1993; earlier only read in part): paired factors F_chi F_chi^vee are invariant under s->1-s since eps_chi eps_chi^vee=1; the central order is even (m_chi(1/2)=m_chi^vee(1/2); the zeta factor is even in s-1/2); ord_rho P_M = M S_rho; D_M(1/4-z^2)=E(z) has order <=1/2, so a genus-zero Hadamard product; diagonal trace-class C; the log-derivative with v'=1-2s gives the resolvent identity including the central pole; GRH gives entries (1/4+t^2)^{-1} in (0,4]"),
],
"HECKE_DIV": [
 ("HECKE_DIV-R21", "targeted proof check",
  "confirmed (HECKE_DIV.tex l.106-131): the Chow components on which the flat difference cl(Z+)-cl(Z-)-Nt vanishes are open and closed and proper over S, so S_C is closed; (i) covers S by countably many closed S_C, Baire on a ball in the smooth locus gives one with interior, irreducibility gives S_C=S; (ii)=>(iii) likewise; (iv)=>(iii) by closedness"),
],
"DEG_L": [
 ("DEG-L.B20", "targeted proof check",
  "confirmed (DEG_L.tex l.3135-3215): the generic fibre of h restricted to Z_0 is x+(ker h cap Stab Z_0); h^*h_* = deg h on rational cohomology gives ||e_A h_* w|| = sqrt(deg h) ||w||; alpha I_0 is O_E-stable in Lambda hence in Lambda^-, so deg h=[Lambda:alpha I_0]>=J. B7 (comass bound) carried"),
 ("DEG-L.B21", "targeted proof check",
  "confirmed (DEG_L.tex l.3257-3335): the universal stabilizer in A_0 x Hilb is closed, proper over Hilb, with finite fibres (a positive-dimensional stabilizer would be A_0 by simplicity), hence finite, so |Stab Z_0| is bounded uniformly by local generator counts; with B18 (||e_0[Z_0]||>=sqrt2/R) and B20 this gives deg Z_h >= sqrt2 n! sqrt V sqrt J/(R S). B18 carried"),
],
"SIGN_NEXT": [
 ("SN-12 (the field F)", "computation or formal certificate",
  "sympy: T^4-5T^2+T+1 is irreducible with roots -2.29041, -0.36199, 0.58277, 2.06963 (totally real), discriminant 6809=11*619 not a square, resolvent cubic z^3+5z^2-4z-21 irreducible, so the Galois group is S4. The NS-rank and Weil-line claims were not recomputed"),
],
}
for run, rows in EV.items():
    p = os.path.join(OUT, f"INTAKE_{run}_20261124_CHECK_EVENTS.tsv")
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("statement_id\tdate\twho\ttype\toutcome\n")
        for sid, typ, out in rows:
            for s in (sid, typ, out):
                assert "\t" not in s and "\n" not in s
            fh.write(f"{sid}\t{D}\t{WHO}\t{typ}\t{out}\n")
    print(p, len(rows))
