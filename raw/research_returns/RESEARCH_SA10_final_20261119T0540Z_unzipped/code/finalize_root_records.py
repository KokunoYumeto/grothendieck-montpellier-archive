"""Record the root's actual late proof/source checks and precise A dependencies."""
from pathlib import Path
import csv,time
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
who='GPT-6 Astra (OpenAI); effort not separately exposed; ChatGPT Pro; /root'
events=[]
def event(ids,kind,outcome):
    for ident in ids.split(','):
        events.append(dict(statement_id=ident.strip(),date='2026-11-19',who=who,type=kind,outcome=outcome))
event('SA10-C3-08,SA10-S3-K1','used and rechecked in this run',
      'A2.2 verifies support-defined R failure when a stratum is empty and proves the order-defined repair; finite check_A_finite.py output retained.')
event('SA10-S3-K2','used and rechecked in this run',
      'A2.2 gives an explicit three-point-chain counterexample to the aside R_jk intersection S_jk = lower X_i; direct finite calculation retained.')
event('SA10-C3-09,SA10-C3-10,SA10-C3-11','targeted proof check',
      'Recomputed the displayed lower unions and support deletions used in A1.3 and A2.2; nonempty-stratum proviso retained, and both overwritten readings on151/060 handled. No unrestricted empty-stratum claim adopted.')
event('SA10-C3-13','used and rechecked in this run',
      'Closed-crible intersection identity follows from the a-d lower-index union; used with the explicit comparison in A3.1.')
event('SA10-C3-15,SA10-S3-K4','used and rechecked in this run',
      'Original151/070 visually inspected: strict inequality is present. A4.1 proves that its literal use forces X empty under local finiteness; nonstrict replacement is stated explicitly.')
event('SA10-R151b-25,SA10-K151b-05','independent re-proof',
      'A1.1 gives a direct subterminal proof of the neighborhood-topos collapse for closed Y in regular Hausdorff X; no paracompactness-without-separation inference.')
event('151/057,151/060,151/070','used and rechecked in this run',
      'Root visually opened original primary scan renderings; checked support definition, overwritten i/j index and strict intersection cutoff. Mathematical conclusions hold for both relevant doubtful readings.')
event('A1.2,A1.3,A1.4,A1.5','targeted proof check',
      'Final type audit distinguishes ordinary Topos, synchronized 2-Pro(Topos), and infinity-topoi; finite delta<=2 indexing, actual overlap obstruction, subset-indexed minimal arities, and T1 membership-groupoid test checked.')
event('A2.1,A2.2,A2.3,A3.1,A3.2,A4.1,A4.2,A4.3,A4.4,A4.5','targeted proof check',
      'Final written proof audit: neighborhood cofinality, open-immersion and empty-stratum failures, closed-crible preservation, extension by empty sheaf, closed quotient, finite identification repair and full stable-graph classification checked.')
event('B1.1,B1.2,B1.3,B1.4,B1.5,B2.1,B2.2,B2.3,B2.4,B3.1,B3.2,B3.3,B4.1,B4.2,B4.3','targeted proof check',
      'Root read the full B_levels.tex contribution and checked compatibility with Part A; particular risks reviewed: uniform neighborhoods for infinite stalks, topoi versus infinity-topoi, fixed-tame pro-cover homotopy pushout, correct truncation and coherent groupoid flag assembly.')
event('B5.1,B5.2,B5.3,B5.4,B5.5,B5.6,B5.7,B5.8,B5.9,B5.10,B6.1,B6.2,B6.3','targeted proof check',
      'Root read full final B56.tex; checked ordinary left-exactness versus hypercompletion, original Artin-Mazur pi0-after-limit typing, all-index subdivision filling, exact finite-set presentation substitutions and two ink readings. This is a targeted proof audit, not machine formalization.')
event('C1.04,C1.B1,C1.B2,C1.B2a,C1.B3,C2.03,C2.05,C3.04,C4.01,C4.02,C4.03,C4.04,C4.05,C4.06,C5.06','targeted proof check',
      'Root reviewed included proofs and delegated independent audits; corrected positive radius, retained outer faces, full chain groupoids, variable-radius tube horns and canonical normal derivative. Read complete Hurewicz construction; primary ABP and Ferry locators checked. Exact scope retained.')
event('GoreskyMacPherson1988','used and rechecked in this run',
      'Full author-hosted Stratified Morse Theory PDF opened online, PartI1.4-1.6 pp40-43; local urllib retrieval failed403 and is separately logged. Not used to conceal any missing conical-control hypothesis.')
event('AFT-8.2.3-8.2.5','used and rechecked in this run',
      'Final source-locator check in opened AFT1-2016.tex lines5406-5565: Prop8.2.3 is tubular neighborhoods of strata, Prop8.2.5 is regular neighborhoods of proper constructible embeddings. The latter supplies the broader refinement-form cone presentation cited in C1.04; the former is the ordinary stratum tube used in PartA.')
with (root/'CHECK_EVENTS_ROOT_FINAL.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(events)
deps={
 'A1.1':'','A1.2':'A4.1','A1.3':'A1.1','A1.4':'A1.2','A1.5':'',
 'A2.1':'','A2.2':'A2.1','A2.3':'A1.2; A2.1; A2.2',
 'A3.1':'A2.1; A2.2','A3.2':'B1.1','A4.1':'','A4.2':'',
 'A4.3':'A4.2','A4.4':'A4.1','A4.5':'A4.4; Schmitt'
}
with (root/'RESULTS_A.csv').open(newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows: row['depends_on']=deps[row['id']]
with (root/'RESULTS_A.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print(f'Recorded {len(events)} actual root check events; annotated {len(rows)} A result dependencies.')
print(f'Runtime {time.perf_counter()-start:.9f} seconds.')
