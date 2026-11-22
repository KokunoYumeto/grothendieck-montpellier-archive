#!/usr/bin/env python3
"""Exact characteristic-two checks for the resolution of the fierce-cover source."""
import json
import time
from pathlib import Path
import sympy as sp

started = time.perf_counter()
c,d,t,z,w,r,tau,delta,x,y,rho,xi,s = sp.symbols(
    'c d t z w r tau delta x y rho xi s')
checks = []

def zero(label, expression, variables):
    numerator = sp.cancel(expression).as_numer_denom()[0]
    p = sp.Poly(numerator, *variables, modulus=2)
    assert p.is_zero, (label, p.as_expr())
    checks.append(label)

H = d**2+(c**4+t**3+t**4*c**2)*d+t*c**5+t**2*c**7+t**4*c**6+t**6*c**5
G = w**2+(1+t*z**4+t**3*z**2)*w+z**5+t**3*z**7+t**4*z**6+t**5*z**5
J = delta**2+(tau**3+r+r**3*tau**4)*delta+tau+r**3*tau**2+r**4*tau**4+r**5*tau**6
zero('source t-chart substitution',H.subs({c:t*z,d:t**3*w})-t**6*G,(t,z,w))
zero('source c-chart substitution',H.subs({c:r,t:r*tau,d:r**3*delta})-r**6*J,(r,tau,delta))
zero('overlap of source resolution charts',
     tau**6*G.subs({t:r*tau,z:1/tau,w:delta/tau**3},simultaneous=True)-J,(r,tau,delta))
zero('exceptional curve on t-chart',G.subs(t,0)-(w**2+w+z**5),(z,w))
zero('source t-chart derivative on exceptional curve',sp.diff(G,w).subs(t,0)-1,(z,w))
zero('source infinity derivative',sp.diff(J,tau).subs({r:0,tau:0,delta:0})-1,(r,))
zero('first c-zero point',G.subs({t:0,z:0,w:0}),(t,))
zero('second c-zero point',G.subs({t:0,z:0,w:1}),(t,))
zero('transversality at first c-zero point',sp.diff(G,w).subs({t:0,z:0,w:0})-1,(t,))
zero('transversality at second c-zero point',sp.diff(G,w).subs({t:0,z:0,w:1})-1,(t,))

Y = y**2+(1+t*x**2)*y+x**5
zero('finite map of resolution t-charts',
     Y.subs({x:z**2+t*z,y:w+z**5},simultaneous=True)-G,(t,z,w))
zero('exceptional map is Frobenius in y',
     (w+z**5)-w**2-(w**2+w+z**5),(z,w))
A = 1+r*tau**2
B = 1+tau**2*delta
rho_map = r*B/A**2
xi_map = A**5/B**2
s_map = tau*A**2/B
zero('infinity finite-map coordinate a',rho_map**2*xi_map-r**2*A,(r,tau,delta))
zero('infinity finite-map coordinate b',rho_map**5*xi_map**2-r**5*B,(r,tau,delta))
zero('infinity finite-map coordinate t',rho_map*s_map-r*tau,(r,tau,delta))
Yinf = xi**2*(1+xi+rho*s**2)+s**5
zero('infinity finite-map strict-transform identity',
     Yinf.subs({rho:rho_map,xi:xi_map,s:s_map},simultaneous=True)
       -tau**4*A**10/B**6*J,(r,tau,delta))

C = w**2+w+z**5
zero('exceptional Frobenius sends h1 to h2',
     z**2*((w/z)**2+w/z**2+z**3)-C,(z,w))
zero('exceptional Frobenius kills h2',
     z**4*((w/z**2)**2+w/z**4+z)-C,(z,w))
wp = w+t*z**4+t**4*z+t**5
zp = z+t
zero('deck action on t-chart',
     G.subs({z:zp,w:wp},simultaneous=True)-G,(t,z,w))
zero('deck action square z',zp.subs(z,zp)-z,(t,z))
zero('deck action square w',wp.subs({z:zp,w:wp},simultaneous=True)-w,(t,z,w))
weights = [sum(e*a for e,a in zip(m,(1,3,1)))
           for m,k in sp.Poly(H,c,d,t,modulus=2).terms()]
assert sorted(weights)==[6,6,6,7,9,9,10,11]
checks.append('source weighted terms and isolated weighted initial form')

output = {'characteristic':2,'assertions_passed':len(checks),
          'elapsed_seconds':time.perf_counter()-started,'checks':checks,
          'scope':'Exact polynomial/chart identities only; the companion proof establishes properness, intersection numbers, purity and the strict-local pro-two assertions.'}
path = Path(__file__).resolve().parents[1]/'output'/'wild_genus2_source.json'
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
