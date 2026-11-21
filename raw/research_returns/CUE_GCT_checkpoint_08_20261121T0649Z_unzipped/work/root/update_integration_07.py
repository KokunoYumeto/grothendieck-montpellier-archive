from pathlib import Path
from datetime import datetime, timezone
import csv

R=Path(__file__).resolve().parent
OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'findings.tex'; s=p.read_text(); assert '\\label{G-16}' not in s
p.write_text(s+'\n'+(R/'g16_fragment.tex').read_text())
with (R/'questions.tsv').open('a') as f:
    f.write('G-Q17\tPrompt Q1/Q2; R20 nonrectangular strip; G16 enhanced invariant quotient\tCan one specify exact nonrectangular highest weights throughout the dimension-certified padded range, including n>=4m/3?\tPROVED G-16: lambda=(d(n-m)+md/4,(md/4)^3), 4 divides md, has a positive gap at a bounded first degree and on an explicit progression whenever dim(P_m4)+3>2n²+2. No 4m/3 upper padding restriction remains for this label family.\n')
events=[
 ('G-16','targeted proof check','PASS complete independent root rederivation: Segre-Veronese graded image ring without projective normality; exact SL4 single-label extraction with duals; equal-norm enhanced Fermat moment map; off-diagonal vanishing; projective Lie stabilizer; arbitrary-padding stability and quotient dimensions; finite kernel and action coefficient degree n+3a; determinant parameter degree n+a; cumulative weighted Hilbert comparison; explicit standard Veronese and every-degree progression; four-variable inheritance and both example labels.'),
 ('G-B13','used and rechecked in this run','Root reopened the primary Derksen2001 author PDF and read Theorem1.1 and Proposition1.2 on printed p956. Confirmed finite-kernel hypothesis and sigma<=H^(t-dimG) A^dimG, then beta<=max(2,3s sigma²/8). This supports the enhanced tensor representation in G16, with t16,dimG15,H4,A=n+3a; no reliance on symmetric-power Example2.1 alone.')
]
with (R/'integration_07_check_events.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n'); w.writerow(['statement_id','date','who','type','outcome'])
    for identifier,kind,result in events:w.writerow([identifier,now,who,kind,result])
p=R/'sources.md'; s=p.read_text(); old='The Veronese generation bound and ensuing orbit-closure comparison in G11 are proved separately.'
new='The Veronese generation bound and ensuing orbit-closure comparison in G11 are proved separately. For G16, the general finite-kernel Proposition1.2 and Theorem1.1 were reread on p956; the action on Sym^n(V) tensor Sym^a(V*) has coefficient degree n+3a, giving the stated enhanced-representation bound. This is distinct from its determinant parametrization degree n+a.'
assert old in s;p.write_text(s.replace(old,new))
p=R/'grothendieck.tex'; s=p.read_text(); marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{G-16. An auxiliary dual line selects a nonrectangular Schur class.}
Form the Segre--Veronese cone of the degree-$n$ coefficient scheme with
the $a$th Veronese of the dual rank-four bundle. Its degree-$d$
coordinate module is exactly the original degree-$d$ module tensored
with $\operatorname{Sym}^{ad}V$. The D-S3 invariant functor and the
D-S6 Schur decomposition select precisely
$(ad+md/4,md/4,md/4,md/4)$. The auxiliary dual line cancels the padding
weight of the explicit Fermat point, so the enhanced cone has a stable
point for every positive padding exponent. D-FGA and the reductive
quotient locators in G-11 give the quotient dimensions; the separate
action and parameter degrees give the effective Hilbert bounds.
Thus the same dimension gap determines an actual nonrectangular
highest weight and a degree progression. The proof does not infer a
highest-weight label from a total dimension inequality alone.

'''
assert marker in s;p.write_text(s.replace(marker,new+marker))
p=R/'intro.tex';s=p.read_text()
s=s.replace('R-20 also certifies four-row gaps beyond that boundary in its stated dimension range, where the weights must be nonrectangular.', 'R-20 also certifies four-row gaps beyond that boundary in its stated dimension range, where the weights must be nonrectangular. G-16 specifies such a weight throughout the dimension-certified range: $\\lambda=(d(n-m)+md/4,md/4,md/4,md/4)$, with explicit first-degree and progression bounds. An auxiliary dual line removes the rectangular stability restriction.')
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('R-20 also forces nonrectangular four-row gaps in its larger dimension-certified range.', 'R-20 also forces nonrectangular four-row gaps in its larger dimension-certified range, and G-16 specifies the exact family $\\lambda=(d(n-m)+md/4,(md/4)^3)$ there and throughout the dimension-certified padded range.')
p.write_text(s)
p=R.parents[1]/'work/assemble.py'; s=p.read_text()
s=s.replace('Algebraic permanent-image dimensions and invariant quotients produce explicit rectangular multiplicity gaps in a range of genuine padding, with a separate rectangular exclusion threshold.', 'Algebraic permanent-image dimensions and invariant quotients produce the exact eventual four-row rectangular padding range, and an enhanced tensor construction specifies nonrectangular highest weights throughout the dimension-certified range.')
p.write_text(s)
with (OUT/'IMPLICATIONS.md').open('a') as f:
    f.write('''

### Explicit nonrectangular labels beyond the rectangular boundary

G16 proves that every dimension-certified padded pair with n>m>=3 has a positive multiplicity gap at the exact shape (d(n−m)+md/4,md/4,md/4,md/4), with 4 dividing md. It gives both a first successful degree bounded by a number whose logarithm is O(n²logn) and an explicit progression on which every degree works. Unlike the rectangular family, this construction has no additional n<4m/3 stability condition. The proof adjoins an auxiliary dual line: the degree-d invariant space of the Segre-Veronese cone extracts exactly this Schur multiplicity, and the dual line cancels the padding weight at an explicit stable Fermat tensor. The dimension criterion itself is unchanged, so this does not extend the separation into the unrestricted asymptotic GCT regime.

For the certified pair (m,n)=(15,20), it gives shapes (35r,15r,15r,15r) at successful degrees d=4r. For (m,n)=(16,22), it gives shapes (10d,4d,4d,4d). Ordinary four-row rectangles are excluded in both cases by G12. The same label family applies to R20's unbounded nonrectangular strip.
''')
with (OUT/'LEDGER.md').open('a') as f:
    f.write('\n\n## '+now+' — a specified nonrectangular label in every certified padded range\n\n')
    f.write('G-Q17 changes to PROVED by G16. The enhanced Segre-Veronese cone extracts lambda=(d(n-m)+md/4,(md/4)^3); its stable Fermat tensor exists for arbitrary padding, so all dimension-certified pairs receive this exact nonrectangular family and explicit degree bounds. Root independently rederived the full proof and reopened the general Derksen finite-kernel bound on primary p956. This is an ordinary progress entry, not a scheduled review.\n')
print(now)
