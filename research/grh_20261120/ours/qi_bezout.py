"""Q(i), n=2: polarization type of Theta|B for the (+-i)-Prym of an unramified Z/4 cover C->X, g(X)=3, g(C)=9,
the Bezout detector bound D0(Q(i)) and the extraction constants C4(Q(i)). Claude Opus 5.5 at effort high, 21 Nov 2026."""
from fractions import Fraction
from math import factorial, isqrt
gX, d = 3, 4
gC = d*(gX-1)+1
assert gC == 9
# complement of B is pi2^*J(C'), C'=C/sigma^2 (genus 5): K = eta^perp/eta in J(C')[2] -> (Z/2)^8 = B[2]
gCp = 2*(gX-1)+1
K_B_order = 2**(2*gCp) // 4
assert K_B_order == 2**8 == 2**(2*4)       # equals |B[2]|: type (2,2,2,2), Theta|B = 2M, M principal
# complement of N = ker Nm^0 (dim 6) is pi^*J(X): K = (Z/4)^4, type of Theta|N = (1,1,1,1,4,4), Pf = 16
Pf_N = 16
deg3_W4 = 3**4 * factorial(gC) // factorial(gC-4)  // 1
deg3_W4 = 3**4 * Fraction(factorial(gC), factorial(gC-4)*1)  # int Theta^9/(5!) * 3^4 ; Theta^9 = 9!
deg3_W4 = 3**4 * factorial(9) // factorial(5)
deg3_T0 = 3**6 * factorial(6) * Pf_N
print("deg_{3Theta} W_4(C) =", deg3_W4, " deg_{3Theta} T_0 =", deg3_T0)
degTheta_Z = Fraction(deg3_W4*deg3_T0, 9)
D0 = 4*degTheta_Z          # phi^*M <= 2 Theta on surfaces => factor 4
assert D0.denominator == 1
D0 = int(D0)
print("D0(Q(i)) =", D0)
# extraction: projector e_W=(1+R)(4-S)/16, R=[i]^*, S=[1+i]^*; generator T=[2+i]^*, lambda=(2+i)^4=-7+24i
lam = complex(2,1)**4
assert lam == complex(-7,24)
# eigenvalue checks on wedge^a V_s (x) wedge^{4-a} V_sbar
for a in range(5):
    R = (1j)**a * (-1j)**(4-a); S = (1+1j)**a*(1-1j)**(4-a)
    e = (1+R)*(4-S)/16
    assert abs(e - (1 if a in (0,4) else 0)) < 1e-9, (a,e)
# u = 16 e_W[Z]: parts <= 8D ; d=<u,u> <= (16*D/2)^2 = 64 D^2 ; Gram d[[1,-7],[-7,625]], Delta=576 d^2
# Delta*delta*t = a u + b Tu, |a|<=800 delta sqrtT d^{3/2}, |b|<=32 delta sqrtT d^{3/2}
# degrees <= 8D(|a| + 25|b|) <= 12800 delta sqrtT D d^{3/2} <= 6553600 delta sqrtT D^4 ; N <= 576*4096 delta D^4
print("N   <= ", 576*64**2, "* delta * D0^4")
print("deg <= ", 8*(800+25*32)*512, "* delta * sqrt(T) * D0^4")
print("C4(Q(i)) = delta * D0^4 * max(2359296, 6553600*sqrt(T)); D0^4 =", D0**4)
print("e.g. delta=1, T=4:", max(2359296, 6553600*2)*D0**4)
