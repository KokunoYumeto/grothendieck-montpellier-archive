"""Explicit final corrections made after the primary-source audit; no inferred verdicts."""
from pathlib import Path
p=Path('deliverable/shards/p3/code/claims_core.py')
s=p.read_text()
s=s.replace("'stated without proof','A',\n 'The kernel is exactly the primitive subgroup", "'stated without proof','E',\n 'The kernel is exactly the primitive subgroup")
# Direct individual record edits below avoid touching other classifications.
start=s.index('claim(300,'); end=s.index('claim(301,',start)
b=s[start:end].replace("'A',","'E',",1)
b=b.replace('The exact sequence is an established application of primitive torsors and the theorem of the cube.', 'The exactness at the rigidified-torsor term is a formal consequence of the checked primitive-torsor criterion; no exact published identification of the full NS target is asserted.')
s=s[:start]+b+s[end:]
start=s.index('claim(311,'); b=s[start:]
b=b.replace("['SGA7VII','Deligne1974HodgeIII']","['SGA7VIII','Deligne1974HodgeIII']")
b=b.replace('The derived-tensor biextension formalism of SGA7VII and Deligne10.2.1 explains the edge map;', 'Original SGA7VIII1.1.3–1.1.4 and1.3.4, printed pages220–222, provide the Tor and finite-pairing comparison; Deligne10.2.1 supplies the complex formulation;')
s=s[:start]+b
s=s.replace("computation='computations.py: bounded-P transition test and nonzero phi_r(a,b/ell^r)=ab/ell.')", "computation='computations.py: bounded-P transition test and nonzero phi_r(a,b/ell^r)=ab/ell.',authorship='Idea of the earlier Pro run, independently checked here')")
s=s.replace("computation='computations.py: Dirac masses for m=1,2,3,7.')", "computation='computations.py: Dirac masses for m=1,2,3,7.',authorship='Interpretation of the earlier Pro run, independently checked here')")
# Explicit reviewer authorship for the two diagnostic counterexamples.
for n,nxt in [(276,277),(277,278)]:
    start=s.index(f'claim({n},');end=s.index(f'claim({nxt},',start)
    b=s[start:end]
    at=b.rfind(')')
    b=b[:at]+",authorship='Reviewer diagnostic counterexample; not an assertion copied from Grothendieck'"+b[at:]
    s=s[:start]+b+s[end:]
p.write_text(s)
p=Path('deliverable/shards/p3/code/a36_records.py');s=p.read_text()
s=s.replace("['SGA7XXI','AchterCasalainaVial2017']", "['SGA7XXI','BenoistOttem2021','AchterCasalainaVial2017']")
p.write_text(s)
print('Applied explicit authorship, Tor-source, NS-class and coniveau-reference corrections.')
