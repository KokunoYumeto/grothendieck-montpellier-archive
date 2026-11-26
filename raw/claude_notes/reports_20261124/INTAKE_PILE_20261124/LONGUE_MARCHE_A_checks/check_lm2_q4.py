import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('g', 'check_lm2_graded.py')
src = "#" + open("check_lm2_graded.py").read().split("# ---------- method 2")[1]
ns = {}
exec('import numpy as np\n' + src.split("for P in (1000003")[0], ns)
ns['P'] = 1000003
P = ns['P']; memo = {}
bv = lambda w: ns['bracket_vec'](w, memo)
X, Y = 0, 1
q4 = (bv((X,X,X,Y)) - 4*bv((X,X,Y,Y)) + bv((X,Y,Y,Y))) % P
n = 4
e1 = (q4 + ns['subst'](q4, n, ns['S_'])) % P
e2 = (q4 + ns['subst'](q4, n, ns['R1']) + ns['subst'](q4, n, ns['R2'])) % P
xv = np.array([1,0]); yv = np.array([0,1]); xy = xv + yv
w2 = ns['subst'](q4, n, ns['JM'])
J = (np.kron(xv, q4) - np.kron(q4, xv) - (np.kron(xy, w2) - np.kron(w2, xy))) % P
claim = (2*bv((X,X,X,X,Y)) - 3*bv((X,X,X,Y,Y)) + bv((X,X,Y,X,Y)) - 3*bv((X,X,Y,Y,Y)) - 2*bv((X,Y,X,Y,Y)) + 2*bv((X,Y,Y,Y,Y))) % P
print('two-cycle zero:', not e1.any(), ' three-cycle zero:', not e2.any(), ' J nonzero:', J.any())
print('J equals claimed defect:', np.array_equal(J % P, claim % P), ' J equals minus claimed:', np.array_equal(J % P, (-claim) % P))
