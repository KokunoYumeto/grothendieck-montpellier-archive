#!/usr/bin/env python3
"""Exact cubic BCH and Massey identities; no arithmetic nonvanishing claim."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import sympy as sp

s, t = sp.symbols("s t")
ug, vg, wg, uh, vh, wh, uk, vk, wk = sp.symbols(
    "ug vg wg uh vh wh uk vk wk")
ag, bg, ah, bh, mg, ng, mh, nh = sp.symbols(
    "ag bg ah bh mg ng mh nh")
I = sp.eye(3)
X = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
Y = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, -1, 0]])
Z = sp.diag(1, -2, 1)
U = sp.Matrix([[0, 1, 0], [0, 0, -1], [0, 0, 0]])
V = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
Dc = sp.diag(-1, 1, -1)


def trunc(x):
    return sp.expand(sum(c * s**i * t**j
                         for (i, j), c in sp.Poly(sp.expand(x), s, t).terms()
                         if i + j <= 3))


def tm(M):
    return M.applyfunc(trunc)


def exp3(M):
    M2 = tm(M * M)
    return tm(I + M + M2 / 2 + tm(M2 * M) / 6)


def compose(g, h, a, b):
    u, v, w = g
    x, y, z = h
    return (u + a*x, v + b*y,
            w + a*b*z + (u*b*y-v*a*x)/2)


def obstruction(g, h, a, b):
    u, v, w = g
    x, y, z = h
    ax, by, cz = a*x, b*y, a*b*z
    F = u*by-v*ax
    plus = -sp.Rational(3, 2)*(u*cz-w*ax) - (u-ax)*F/4
    minus = sp.Rational(3, 2)*(v*cz-w*by) + (v-by)*F/4
    return sp.expand(plus), sp.expand(minus)


g, h, k = (ug, vg, wg), (uh, vh, wh), (uk, vk, wk)
gh, hk = compose(g, h, ag, bg), compose(h, k, ah, bh)
op, om = obstruction(g, h, ag, bg)
Lg = s*ug*X + t*vg*Y + s*t*wg*Z + s*s*t*mg*U + s*t*t*ng*V
Lh = (s*ag*uh*X + t*bg*vh*Y + s*t*ag*bg*wh*Z
      + s*s*t*ag*ag*bg*mh*U + s*t*t*ag*bg*bg*nh*V)
Lgh = (s*gh[0]*X + t*gh[1]*Y + s*t*gh[2]*Z
       + s*s*t*(mg+ag*ag*bg*mh+op)*U
       + s*t*t*(ng+ag*bg*bg*nh+om)*V)
checks = {
    "XY_bracket": X*Y-Y*X == Z,
    "XZ_bracket": X*Z-Z*X == -3*U,
    "YZ_bracket": Y*Z-Z*Y == 3*V,
    "cubic_BCH_identity": tm(exp3(Lg)*exp3(Lh)-exp3(Lgh)) == sp.zeros(3),
    "determinant_one": trunc(exp3(Lg).det()) == 1,
}
for name, M, sign in (("X", X, 1), ("Y", Y, -1), ("Z", Z, -1),
                      ("U", U, -1), ("V", V, 1)):
    checks["kappa_"+name] = -Dc*J*M.T*J*Dc == sign*M

for index, action, name in ((0, ag*ag*bg, "plus"), (1, ag*bg*bg, "minus")):
    delta = (action*obstruction(h, k, ah, bh)[index]
             - obstruction(gh, k, ag*ah, bg*bh)[index]
             + obstruction(g, hk, ag, bg)[index]
             - obstruction(g, h, ag, bg)[index])
    checks[name+"_is_two_cocycle"] = sp.expand(delta) == 0

# d f(g,h)=f(g)+rho(g)f(h)-f(gh).
a_g, a_h = -wg-ug*vg/2, -wh-uh*vh/2
b_g, b_h = wg-ug*vg/2, wh-uh*vh/2
a_gh = -gh[2]-gh[0]*gh[1]/2
b_gh = gh[2]-gh[0]*gh[1]/2
checks["first_Massey_defining_cochain"] = sp.expand(
    a_g+ag*bg*a_h-a_gh-ug*bg*vh) == 0
checks["second_Massey_defining_cochain"] = sp.expand(
    b_g+ag*bg*b_h-b_gh-vg*ag*uh) == 0
theta = ug*ag*bg*b_h + a_g*ag*uh
boundary = ug*ug*vg + ag*ag*bg*uh*uh*vh - gh[0]*gh[0]*gh[1]
checks["Massey_class_identity"] = sp.expand(
    op + sp.Rational(3, 2)*theta - boundary/4) == 0
assert all(checks.values()), checks
path = Path(__file__).resolve()
report = {
    "verified_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro",
    "effort": "not exposed",
    "script_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "coefficient_ring": "Q[scalar symbols,s,t]/(s,t)^4",
    "scope": "Exact matrix and cochain identities only; no arithmetic nonvanishing or source-point assertion",
    "checks": checks,
}
path.with_suffix(".json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({"all_pass": True, "checks": len(checks),
                  "script_sha256": report["script_sha256"]}))
