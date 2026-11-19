"""Separate the faulty within-block hint from the already checked positive theorem."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'scripts/build_claims.py';s=p.read_text()
block="""add(567,[487],[40,42],'036-070','53,111','b_(n+1)=b_n z^(i−1)x^(-1)','With v=xy−z^(i−1)T and v′=Σ b_n x^(−n−1)T^n, the within-block exact recurrence is y b_(n+1)=z^(i−1)b_n. The printed division by x is inconsistent with this normalization; division by y is valid when the chosen powers of y make each coefficient integral.','false as stated','E','Independent coefficient multiplication gives the correction. The positive Samuel construction matched in Samuel1964TIFR chapterI §9 uses the same block mechanism; C-SA14-565 supplies its full valid proof. The discrepancy is a scan-reading alarm, not a transcription change.','Samuel1964TIFR;Samuel1964Mechants','LF-S15','CALC-25','Refuted even with positive coprime exponents in A=Q[x,y,z]/(z²−x⁵−y⁷), i=2,j=5,k=7. The proposed first coefficient has numerator y^t z(y−x) over x², whose numerator is nonzero modulo x. The refined recurrence is stated in this record.',attribution='reused printed Bourbaki hint')
"""
if 'add(567,' not in s:s=s.replace('def save():\n',block+'def save():\n');p.write_text(s)
p=R/'scripts/calculations.py';s=p.read_text()
tail="print('\\nALL ASSERTIONS PASSED. Finite examples certify the stated examples; general statements require the separately supplied proofs/hypotheses.')"
block="""section('CALC-25 within-block printed denominator')
x,y,z=s.symbols('x y z')
ii,jj,kk=2,5,7
assert ii*jj*kk-ii*jj-jj*kk-kk*ii==11
assert s.gcd(ii,jj)==s.gcd(jj,kk)==s.gcd(ii,kk)==1
numerator=y**10*z*(y-x)
G=s.groebner([z**2-x**5-y**7,x],z,x,y,domain=s.QQ)
remainder=G.reduce(numerator)[1]
assert remainder==y**11*z and remainder!=0
print('A=Q[x,y,z]/(z²-x⁵-y⁷), i=2,j=5,k=7; inequality value=11. The quotient by x is Q[y,z]/(z²-y⁷), a domain because gcd(2,7)=1; x is prime and y is not divisible by x.')
print('Using printed b1=b0*z/x, b0=y^10, the T coefficient of vv-prime is y^10*z*(y-x)/x².')
print('Its numerator modulo (x,z²-x⁵-y⁷) is',remainder,'and therefore the coefficient is not in A.')
print('Correct within-block equation: y*b_(n+1)=z^(i-1)*b_n. The positive recurrence in CALC-22 uses it.')
"""
if 'CALC-25 within-block' not in s:s=s.replace(tail,block+tail);p.write_text(s)
p=R/'scripts/build_auxiliary.py';s=p.read_text()
old="alarm(42,'036-070','109–111','Cut power-series relation and inequality indices','Recover full relation before interpreting the recurrence','Samuel1961 Theorem4.1 matches the inequality after relabelling, but the draft antecedent is truncated.','high','medium')"
new="alarm(40,'036-070','53','Within-block b_(n+1)=b_n z^(i−1)x^(-1)','Use y^(-1) for the displayed b_n normalization, or recover a different coefficient convention','Multiplying the displayed v and v′ forces y b_(n+1)=z^(i−1)b_n. The printed x^(-1) fails even for positive coprime exponents2,5,7; C-SA14-567 and CALC-25.','high','high')"
assert old in s;s=s.replace(old,new);p.write_text(s)
p=R/'proof_notes.md';s=p.read_text().replace('through `CALC-24`','through `CALC-25`')
anchor='The nonassociate argument uses the coefficient of T'
paragraph='''**C-SA14-567: a separate within-block hint error.** Scan40 line53 prints b_(n+1)=b_n z^(i−1)x^(-1). With the series normalization on scan42, direct multiplication instead requires y b_(n+1)−z^(i−1)b_n=0 within a block. This discrepancy persists in the fully positive setting. Let A=Q[x,y,z]/(z²−x⁵−y⁷), i=2,j=5,k=7. The ring is a domain; A/(x)=Q[y,z]/(z²−y⁷) is a domain since the two exponents are coprime, so x is prime. The element y is not in (x), hence Ax∩Ay=Axy. All three elements are nonzero, the defining relation is exactly the required relation, and ijk−ij−jk−ki=11. For b₀=y^t the printed rule gives b₁=y^t z/x. The coefficient of T in vv′ is y^t z(y−x)/x². Its numerator remains y^(t+1)z≠0 modulo x, so it is not in A. CALC-25 checks t=10 exactly; the same argument works for every positive t. The correct recurrence divides by y, with the chosen initial powers of y guaranteeing integrality, as in the general proof above. The scan may reveal a different symbol or convention; no transcription is altered here.\n\n'''
assert anchor in s;s=s.replace(anchor,paragraph+anchor);p.write_text(s)
p=R/'scripts/build_check_events.py';s=p.read_text().replace('proof([503,565],10','proof([503,565,567],10').replace("refinements={424:","refinements={567:'C-SA14-567, modern statement (within-block division by y)',424:");p.write_text(s)
for fn in ['synthesis.md','literature_notes.md','directions.md']:
 p=R/fn;s=p.read_text()
 if fn=='synthesis.md':
  s=s.replace('166, IDs C-SA14-401 through C-SA14-566','167, IDs C-SA14-401 through C-SA14-567').replace('12 false as stated','13 false as stated').replace('E130','E131').replace('| Computation sections | 24,','| Computation sections | 25,')
  s=s.replace('| Companion formal series | The literal allowance i,j,k≥0 fails for i=1,j=k=0. The positive-exponent construction has a full block proof. | C-SA14-503,565; CALC-22 |','| Companion formal series | The nonnegative range fails; the separate within-block hint divides by the wrong variable. The positive-exponent theorem has a full corrected block proof. | C-SA14-503,565,567; CALC-22,25 |')
 elif fn=='literature_notes.md':
  s=s.replace('without deciding whether the discrepancy is in the ink or the transcription.','without deciding whether the discrepancy is in the ink or the transcription. The separate within-block x^(-1) hint is also refuted under positive coprime exponents; the displayed coefficient normalization requires division by y (C-SA14-567, CALC-25).')
 elif fn=='directions.md':
  s=s.replace('C-SA14-462–503,564–565','C-SA14-462–503,564–567')
 p.write_text(s)
print('Separate within-block discrepancy recorded; source transcription unchanged.')
