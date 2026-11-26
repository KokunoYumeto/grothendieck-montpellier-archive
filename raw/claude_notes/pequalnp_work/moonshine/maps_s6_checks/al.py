# Numerical check of Atkin-Lehner and Fricke actions on T6 (Gamma_0(6) Hauptmodul), and of j = P(T6)/Q(T6)
import mpmath as mp
mp.mp.dps = 40

def eta(tau):
    q = mp.exp(2j*mp.pi*tau)
    return mp.exp(2j*mp.pi*tau/24)*mp.qp(q)

def T6(tau):
    return eta(tau)**5*eta(3*tau)/(eta(2*tau)*eta(6*tau)**5)

def mob(M, tau):
    a, b, c, d = M
    return (a*tau + b)/(c*tau + d)

tau = mp.mpc('0.1234', '0.4567')
t = T6(tau)
# Fricke W6 = [[0,-1],[6,0]] : tau -> -1/(6 tau)
w6 = T6(mob((0, -1, 6, 0), tau))
print("T6(W6 tau)*T6(tau) =", mp.nstr(w6*t, 20))
# W3 = [[3a, b],[6c, 3d]] det 3 : [[3,1],[6,3]]
w3 = T6(mob((3, 1, 6, 3), tau))
print("T6(W3 tau) =", mp.nstr(w3, 15), " predicted -9(T+8)/(T+9) =", mp.nstr(-9*(t+8)/(t+9), 15))
# W2 = [[2a, b],[6c, 2d]] det 2: [[2,1],[6,4]] det 8-6 = 2
w2 = T6(mob((2, 1, 6, 4), tau))
print("T6(W2 tau) =", mp.nstr(w2, 15), " predicted -8(T+9)/(T+8) =", mp.nstr(-8*(t+9)/(t+8), 15))
# j from E4, Delta
def j(tau):
    q = mp.exp(2j*mp.pi*tau)
    E4 = 1 + 240*mp.nsum(lambda n: n**3*q**n/(1-q**n), [1, mp.inf])
    D = q*mp.qp(q)**24
    return E4**3/D
P = (t+12)**3*(t**3+252*t**2+3888*t+15552)**3
Q = t**6*(t+8)**2*(t+9)**3
print("j(tau) =", mp.nstr(j(tau), 15), "  P/Q =", mp.nstr(P/Q, 15))
# Hesse / CHH check:  j = 27 tH^3 (8 - tH^3)^3/(1+tH^3)^3 with gamma = -tH^-3 ; j = 27(1+8g)^3/(g(1-g)^3)
g = mp.mpf('0.3')
print("hesse identity:", mp.nstr(27*(1+8*g)**3/(g*(1-g)**3), 12), mp.nstr((lambda tH: 27*tH**3*(8-tH**3)**3/(1+tH**3)**3)((-1/g)**(mp.mpf(1)/3) if g<0 else -(1/g)**(mp.mpf(1)/3)), 12))
