#!/usr/bin/env python3
"""Finite exact illustration of the diagonalizable torsion formula."""
import json,math,pathlib
n=4;moduli=(6,4);root_order=12
chars=[(a,b) for a in range(6) for b in range(4)]
killed=[(a,b) for a,b in chars if (n*2*a)%root_order==0 and (n*3*b)%root_order==0]
expected=math.gcd(n,6)*math.gcd(n,4)
assert len(killed)==expected==8
out={'M':'Z/6 x Z/4','n':n,'characters_into_mu12':len(chars),'n_torsion_character_count':len(killed),'cardinality_M_mod_nM':expected,'n_torsion_characters':killed,'scope':'Finite exact illustration; the general proof uses character factorization and integrality of the group-algebra basis.'}
p=pathlib.Path(__file__).resolve().parents[1]/'outputs'/'torsion_grading_checks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
