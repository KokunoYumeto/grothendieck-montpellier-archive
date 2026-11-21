import csv,datetime,pathlib
p=pathlib.Path(__file__).resolve().parent
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).isoformat(timespec='seconds')
fields=['statement_id','date','who','type','outcome','how','model','effort','run']
checks={
'P-F1':'Recomputed the generating series, unimodular inverse and area; checked the entire higher-ambient affine-hull stabilization and interval-increment contradiction.',
'P-F2':'Read every selector, boundedness and bit-description step; integer selectors and u multiplicity give exactly the coefficient; no construction of Hilbert data is assumed.',
'P-F3':'Rechecked Haar invariance, projection image, self-adjointness, spectrum and both multiplicity realizations; retained the full-space cost qualification.',
'P-F4':'Computed both C2 values, irreducible coefficients and the two eigenvalues of the kernel matrix.',
'P-F5':'Read the full proof after replacing embedding by homomorphism; central scalar spectra distinguish the two maps even without the irreducibility argument.',
'P-F6':'Checked finite actual direct sums in the split Grothendieck group and specialization precisely at v=1; parity prose now uses the rank-one Frobenius-1 example.',
'P-F7':'Read the full Chinese-remainder construction, characteristic-two case, empty scheme, purity/cohomology, parsimonious count and explicitly presented-family complexity scope.',
'P-F8':'Checked contrapositive restriction-surjection proof, degreewise semisimplicity, equal-character coordinate axes and positive multiplicities under BIP.',
'P-F9':'Read the entire proper-rational/binomial-basis argument, positive common-period numerator and shifted product coefficient proof, including r=1.',
'P-F10':'Recomputed residue uniqueness, early zero case, exact worst constituent and both index definitions; underlying affine plane remains fixed.',
'P-F11':'Re-read the complete final proof: Cauchy disk bounds, local Laurent normalization, unique highest pole under gcd1, coefficientwise binomial comparison, numerical constants, real coefficients, gcd scaling, further real shifts, numerator convolution and integer final shift.',
'P-F12':'Read the entire proof: Weyl growth, positive-form stars-and-bars lower bound, upper counting bound, all parameter substitutions, GL_m numerator bit sizes, compressed-input caveat and explicit numerator-index clash counterexample.',
'C-GRH-03':'Read the complete x^3-2 proof; Eisenstein gives degree3 for every root, Galois closure would include zeta3, and abelian-extension subfields are Galois. Scope is the proposed solution-field restriction only.'
}
rows=[]
for sid,how in checks.items():
 rows.append(dict(statement_id=sid,date=now,who='GPT-6 Astra Pro; effort not exposed; run /root',type='targeted proof check',outcome='PASS for the stated scope; whole-proof reading completed; no formal certificate claimed.',how=how,model='GPT-6 Astra Pro',effort='not exposed by runtime',run='/root'))
for sid,how in {
'P-K1':'Matched KM Theorem5 and Remark6 to GCTVI Hyp1.6.4 fixed-inner stretching and the exact six residues.',
'P-K2':'Matched BOR Theorem2.4 specialized ray and distinguished the revised index conjectures.',
'P-K3':'Read IMW Theorem1.3 and Fischer-Ikenmeyer Theorem3.1 scopes; hardness gives a conditional P=NP consequence, not an assumed separation.',
'P-K4':'Read Deligne WeilII3.3.1,3.3.4-6,3.3.9 in the primary PDF text and Haines2.0.1,5.0.4. Corrected the tentative mistaken Cor3.3.10 locator and replaced uninspected original KL4.3 with verified primary Haines locators.',
'P-K5':'Read BIP Theorem1.4 on the actual closures with n>=m^25; occurrence support is distinguished from multiplicities.'
}.items():
 rows.append(dict(statement_id=sid,date=now,who='GPT-6 Astra Pro; effort not exposed; run /root',type='used and rechecked in this run',outcome='PASS for exact cited scope; not an independent proof of the cited theorem.',how=how,model='GPT-6 Astra Pro',effort='not exposed by runtime',run='/root'))
with (p/'root_positivity_checks.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)
print('root_events',len(rows))
