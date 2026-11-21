"""Independent check of KT-U3-SECOND: 7^d tr(T_7 | M_d) for d=5 on the definite U(3) of the lattice O_E^3, E=Q(sqrt-3).
Gamma = monomial matrices with entries in mu_6 (order 1296). Character of the harmonic rep of highest weight (d,0,-d):
chi_d(g) = h_d(g) conj(h_d(g)) - h_{d-1}(g) conj(h_{d-1}(g)) for unitary g. For A with A*A = 7I we use
7^d chi_d(A/sqrt7) = h_d(A)conj(h_d(A)) - 7 h_{d-1}(A)conj(h_{d-1}(A))."""
import itertools, numpy as np
w = np.exp(2j*np.pi/3); z6 = [np.exp(2j*np.pi*k/6) for k in range(6)]
pi_ = 3 + w; pib = np.conj(pi_)
def h(eig, d):
    # complete homogeneous symmetric polynomial via Newton identities
    p = [None] + [np.sum(eig**k) for k in range(1, d+1)]
    H = [1.0+0j]
    for k in range(1, d+1):
        H.append(sum(p[i]*H[k-i] for i in range(1, k+1))/k)
    return H
Gam = []
for perm in itertools.permutations(range(3)):
    for ks in itertools.product(range(6), repeat=3):
        M = np.zeros((3,3), complex)
        for i in range(3): M[i, perm[i]] = z6[ks[i]]
        Gam.append(M)
assert len(Gam) == 1296
def chi_scaled(A, d, scale):
    e = np.linalg.eigvals(A); H = h(e, d)
    return (H[d]*np.conj(H[d]) - scale*H[d-1]*np.conj(H[d-1])) if d >= 1 else 1
for d in [5, 11]:
    dim = sum(chi_scaled(g, d, 1) for g in Gam)/1296
    tot = 0
    for r, m in [(1,3),(2,18),(3,36)]:
        J = np.zeros((3,3)); J[:r,:r] = 1.0/r
        U = pi_*np.eye(3) + (w**(r-1)*pib - pi_)*J
        assert np.allclose(U.conj().T@U, 7*np.eye(3))
        tot += m*sum(chi_scaled(U@g, d, 7) for g in Gam)
    print(f"d={d}: dim M_d = {dim.real:.6f}; 7^d tr(T_7|M_d) = {(tot/1296).real:.4f} (imag {(tot/1296).imag:.2e})")
