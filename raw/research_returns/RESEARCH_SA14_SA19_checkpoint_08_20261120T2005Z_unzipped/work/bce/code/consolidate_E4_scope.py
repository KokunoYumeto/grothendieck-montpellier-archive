from pathlib import Path
import csv
p=Path('work/bce')
e=p/'section_E.tex'
s=e.read_text()
fragment=(p/'new_E4_scope_310.tex').read_text()
if '\\subsection{The two marginal notes on 57:310: mathematics and reading}' not in s:
 s+='\n'+fragment+'\n'
provenance='''\\paragraph{Provenance.}
The smooth-curve argument above was already given by K\\k{e}stutis
\\v{C}esnavi\\v{c}ius in his answer of 28 April 2015 to Poonen's question
\\cite{BCECesnavicius2015}. We independently checked the cited BLR and
finite-quotient statements before locating that answer. No novelty is
claimed for Theorem E4.Curve.

'''
marker='\\paragraph{Why the genus-one torsor counterexample route fails.}'
if 'BCECesnavicius2015' not in s:s=s.replace(marker,provenance+marker)
e.write_text(s)
n=p/'new_E4_curves.tex'; s=n.read_text()
if 'BCECesnavicius2015' not in s:s=s.replace(marker,provenance+marker)
n.write_text(s)
b=p/'references.bib';s=b.read_text()
if '@misc{BCECesnavicius2015,' not in s:
 s+='''\n@misc{BCECesnavicius2015,
 author={\\v{C}esnavi\\v{c}ius, K\\k{e}stutis},
 title={Answer to: Does every relative curve have a Picard scheme?},
 year={2015}, howpublished={MathOverflow, 28 April 2015},
 url={https://mathoverflow.net/questions/186723/does-every-relative-curve-have-a-picard-scheme},
 note={Provenance of the smooth-curve derivation from BLR6.6 Theorem2(c) and finite quotients. Read20November2026. Primary theorem dependencies are separately cited to BLR and the Stacks Project.}
}
'''
b.write_text(s)
f=p/'results.csv'
with f.open(newline='') as h:
 reader=csv.DictReader(h); fields=reader.fieldnames;rows=list(reader)
for r in rows:
 if r['id']=='E4-3105diagram':
  r['status']='Refuted for multiplication openness; reading qualifier uncertain'
  r['proved_result_or_precise_gate']='Theorem E4.H explicitly makes multiplication by2 nonopen for a smooth projective family. The mathematical openness assertion is refuted. Original scan310 confirms Non exemple and the branch diagram, but the surrounding surjectivity/component qualifier remains illegible; no additional assertion is invented.'
 if r['id']=='E4-3106criterion':
  r['status']='Picard-scope conditions proved; exact iff reading uncertain'
  r['proved_result_or_precise_gate']='For proper flat fp cohomologically-flat-in-degree-zero families over noetherian S, Pic-tau is fp; both defensible above-open and outside-open finite-component conditions therefore hold for closed irreducible base changes. The exact broader iff quantifiers remain unreadable. An explicit infinite-branch etale group refutes the generic-open component-count criterion for arbitrary lft groups; it is not a Picard realization.'
  r['source']='Official MPL57 scan310; new_E4_scope_310.tex; Laurent-Schroer2.1'
 if r['id']=='E4-315schemeNormal':
  r['proved_result_or_precise_gate']='Projective families, normal noetherian dimension-one bases, and all geometrically normal curve families over arbitrary bases are schematic. The remaining gate is arbitrary-base higher-dimensional geometrically normal families; no genuine Picard counterexample or general proof is obtained. See E4_schematicity_attempts.md.'
  r['source']='Raynaud1970 Thm3.3.1; Theorem E4.Curve; BLR6.6(2c); Cesnavicius2015 provenance'
 if r['id']=='E4-315schemeIntegral':
  r['proved_result_or_precise_gate']='Artin gives a separated algebraic space. Projective families and smooth proper curves over arbitrary bases are schematic. Integral singular curves and higher-dimensional integral families remain. The standard nonsplit conic has reducible geometric special fibre and does not refute this question; arbitrary nonschematic group spaces also do not provide Picard realizations.'
  r['source']='Laurent-Schroer2.1; Raynaud1970 Thm3.3.1; Theorem E4.Curve; E4_schematicity_attempts.md'
 if r['id']=='E4-315schemeCurve':
  r['source']+='; prior derivation Cesnavicius2015'
with f.open('w',newline='') as h:
 w=csv.DictWriter(h,fieldnames=fields);w.writeheader();w.writerows(rows)
r=p/'report.md';s=r.read_text()
update='''## Update 2026-11-20 18:38 UTC: exact remaining schematicity gate and provenance

The full Picard scheme question on 57:315 remains unsettled for higher-dimensional geometrically normal families and for geometrically integral singular curve families over arbitrary scheme bases. Smooth curves, hence geometrically normal curves, are settled; the standard nonsplit-conic example does not satisfy geometric integrality. The detailed file `E4_schematicity_attempts.md` records the attempted torsor, singular-genus-one, relative Chow modification, normalization, and group-space realization routes and their precise missing steps. No arbitrary group-space example is presented as a Picard counterexample.

The smooth-curve proof is an existing derivation: Kestutis Cesnavicius gave the BLR6.6(2c) plus finite-quotient argument on MathOverflow on28April2015. That provenance is now explicitly cited alongside the independently opened BLR and Stacks/SGA3 theorem dependencies. No priority is claimed.

The two marginal notes on57:310 are separated from their mathematical outcomes. Multiplication openness is **refuted** by E4.H; its pale qualifier does not leave that mathematical row open. For the proper-flat-fp cohomologically-flat Picard setting over noetherian bases, finite presentation of Pic-tau already supplies both defensible finite-component conditions. The exact broad iff wording remains uncertain. A fully specified infinite-branch etale group shows why a generic-component-count-only criterion for arbitrary locally finite-type groups would be false; this is not a Picard realization and is not counted as new movement on the main gate.

A targeted separate AI audit of FHI's F10/F10b was completed at18:28:56UTC. Krishna-Majumder2026v2 Theorem9.4, Corollary9.7, Lemma3.2 and the hypotheses onp2 were read. The rank-one conductor bound, finite inertia deduction, and fixed-cover purity descent passed the audit. The audit does not cover F10c/F11 or certify the full new preprint.

'''
if '## Update 2026-11-20 18:38 UTC:' not in s:s=s.replace('INCOMPLETE\n\n','INCOMPLETE\n\n'+update,1)
r.write_text(s)
with (p/'CHECK_EVENTS.tsv').open('a') as h:
 h.write('2026-11-20T18:38:00Z\tE4 scope and provenance\tregister/source consolidation\tMPL57scan310; Cesnavicius2015; primary BLR dependencies\tMultiplication openness refuted mathematically; remaining ink qualifier separate. Smooth-curve prior provenance recorded. Full schematicity gate unchanged.\n')
print('Updated section_E, new_E4_curves, references, results, report and CHECK_EVENTS')
