# alpha(M) for Kodaira monodromies via the eta^2 multiplier: eta(M t)^2 = nu(M) (c t + d) eta(t)^2, nu = e(alpha/12)
import mpmath as mp
mp.mp.dps = 30
def eta(t):
    q = mp.e**(2j*mp.pi*t); return mp.e**(2j*mp.pi*t/24)*mp.qp(q)
def alpha(M):
    a, b, c, d = M
    t = mp.mpc('0.137', '1.23')
    nu = eta((a*t+b)/(c*t+d))**2/((c*t+d)*eta(t)**2)
    x = mp.arg(nu)/(2*mp.pi)*12
    return int(mp.nint(x)) % 12, mp.nstr(abs(nu), 8)
K = {'I1 (T)': (1,1,0,1), 'I2': (1,2,0,1), 'I0* (-I)': (-1,0,0,-1), 'I1*': (-1,-1,0,-1),
     'II': (1,1,-1,0), 'III': (0,1,-1,0), 'IV': (0,1,-1,-1), 'IV*': (-1,-1,1,0), 'III*': (0,-1,1,0), 'II*': (0,-1,1,1),
     'S': (0,-1,1,0), 'a=[[0,1],[-1,-1]]': (0,1,-1,-1), 'C1=[[-1,-1],[1,0]]': (-1,-1,1,0), 'C2=[[0,1],[-1,0]]': (0,1,-1,0)}
e = {'I1 (T)': 1, 'I2': 2, 'I0* (-I)': 6, 'I1*': 7, 'II': 2, 'III': 3, 'IV': 4, 'IV*': 8, 'III*': 9, 'II*': 10}
for k, M in K.items():
    al, mod = alpha(M)
    print(f"{k:22s} alpha = {al:2d}   Euler number = {e.get(k, '-')}   |nu| = {mod}")
