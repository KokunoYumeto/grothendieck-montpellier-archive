"""Serialize hand-checked endpoint relations plus exact publication mappings."""
from pathlib import Path
import json,csv,datetime
P=Path(__file__).resolve().parents[1]
I={x['id']:x for x in json.loads((P/'items.json').read_text())}
C=json.loads((P/'claims.json').read_text())
R={x['key']:x for x in json.loads((P/'references.json').read_text())}
rows=[]
def a(kind,fr,to,what,evidence,ids):
 rows.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=';'.join('SA06-'+str(i) for i in ids)))
a('folder','cote14/088,090','cote14/077,079,082,084,086 (K14-06)','SGA4 redaction continuations supply propositions and proofs missing from the selected Pro range.','Both endpoints fully read: Pro44–69,95–120; K14-06:131–170,244–279,357–385,436–468,494–529.',[205,206,301,302])
a('folder','cote14/058 (K14-04, early part)','cote14/059–061 (K14-05)','Proposition2.1 continues across the package boundary. Merge early SA06-103/C-SA06-90 with the overlapping late SA06-288/C-SA06-261.','Late continuation read at K14-05:3–48; opening read and exact link confirmed by cote14_early in this run.',[288])
a('folder','cote14/051 (early part)','cote14/071 (K14-05)','The first integral Albanese inverse question recurs. Early C-SA06-89 and late C-SA06-270 concern the same question; the second inverse question C-SA06-271 remains distinct.','Late question read at K14-05:215–217; early endpoint confirmed by cote14_early.',[292])
a('folder','cote14/073 (K14-05)','cote14/074,078 (K14-06)','Picard/Kummer and abelianized fundamental-group comparison continues; preserve the torsion term and prime-to-characteristic hypotheses.','K14-05:222–257; K14-06:4–39,181–234 read in full.',[293,294,295,297])
a('folder','cote14/092','cote14/117','Equivalence chart is clarified by the later explicit notation A_r,J,N. N is not automatically numerical equivalence.','Pro130–177 and928–950; the later notation was used to disambiguate, not silently replace, the earlier chart.',[203,204,239,260])
a('folder','cote14/094–096,098,100','cote14/093','Cover title groups the ampleness and higher-cycle cone leaves; it does not date them or prove continuity.','Pro181–236,237–329,346–365,389–446.',[216,218,219,221,222,223,283])
a('folder','cote14/101,103,104,106–109,111–116','K14-08 transcription','Overlapping Pro/Codex witnesses have been compared; differences remain readings, not emendations.','Full assigned K14-08 and Pro excerpts read; readings.tsv records ≥/=, indices, twists and cancellation differences.',[210,211,212,225,226,227,228,229,230,231,232,233,234,235,236,237,238])
a('folder','cote14/121','cote14/123','Conditions on bounded cycles continue around the unrelated transporter sheet122.','Pro1010–1025 and1047–1054; the chain of implications is contiguous mathematically, not in scan order.',[249])
a('folder','cote14/124','cote14/122','Transporter typescript page2 precedes page3 despite archive scan order. Both selected leaves are cancelled.','Pro1055–1090 and1026–1046; typed pagination checked.',[213,286])
a('folder','cote14/129','cote14/127','Cartan typescript24bis precedes25; scan127 explicitly restores text struck out by mistake.','Pro1226–1240 and1128–1148; restoration instruction read.',[214,286])
a('folder','cote14/118,126,128','cote14/115–116','Rectangle relation, Albanese inverse and bounded zero-cycle questions explain conditional low-dimensional OK marks; none proves rational=Albanese equivalence.','Pro838–926,952–978,1091–1127,1149–1225 read.',[237,238,240,241,246])
a('folder','cote14/087–089,092,117','cote16/003–006 (external): lines27–203','Correspondence rings, projectors and grading questions provide a genuine endpoint for the earlier ring-versus-motive comparison.','Both current and retrieved endpoints read; contextual_endpoint_audit.md records scope.',[252,253,267])
a('folder','cote14/112; earlier contextual notes59–68','cote16/007–018 (external): lines204–724','Inverse lowering, universal-ring matrices, and essential grading-projector conditions are explicit. They are not automatically the standard sl₂ normalization or a motivic Galois action.','External endpoint read in full; independent coefficient/unit calculations saved.',[253,254,255,256,257,259])
a('folder','cote14/073–074 (Codex)','cote16/021 (external): lines860–897','Kummer inverse limits and NS ℓ-primary torsion comparison.','Both endpoints read; external exact sequence assumes Pic extension by a divisible group and finite mod-ℓH².',[293,294,295])
a('folder','cote14/127,129','cote16/026 (external): lines1063–1112','SGA3 editorial correction on spreading out a generic Cartan subgroup.','Both endpoints read; this is a precise editorial parallel, not a new arithmetic normalizer theorem.',[214,270])
a('folder','cote14/107–113; contextual note70','cote16/034,036,038,040 (external): lines1317–1585','Hyperplane restriction, primitive projectors and unit-normalized Λ formulas.','Actual mathematics lies on the even-numbered listed leaves; reused printed scans35,37,39 are excluded from the argument.',[233,254,258,259,263])
a('folder','cote14/106–107,113–114; contextual note71','cote16/047 (external): lines1785–1796','Explicit singular-hypersurface programme following Serre’s simple-connectedness objection.','External programme read; current pages use regular punctured X,Y and do not construct the requested singular theory.',[264,265])
a('folder','cote14/112–113; contextual notes65–68','cote16/048–051 (external): lines1797–1882','Historical conjecture letters, inverse algebraicity, semisimplicity yoga and product-quantified weak variants.','Letter dated6January1966 read; do not transfer its letter definitions into late cote14 where none are given.',[258,259,260,263])
a('folder','cote14/065–071,078–083; contextual notes68–69','cote47/003–011 (external): lines2086–2572','Fourier/convolution correspondence, inversion/shift/determinant factors and integral cycle divisibility.','External proof admits Mumford vanishing and leaves a fibre compatibility check at47/008;47/009 asks validity modulo torsion.',[261,262,268,289,290,291,292,297,298,299])
a('folder','cote14/073,078; contextual note82','cote54/003,005 (external): lines2609–2655,2682–2704','Universal vector extension and Hodge–de Rham duality of abelian varieties.','Characteristic-zero qualification and subsequent Cartier-duality question read; unrelated flatness drafts interleave.',[262,273,293,297])
a('folder','cote14/092,106–112','cote44/002,004,006,008–009 (external): lines2780–3012','Intermediate-Jacobian programme, height/intersection formula and polarization question.','Seven proposed theorems and letter12August1964 read. Primitive-decomposition warning remains; no proof inferred from the programme heading.',[203,227,229,230,232,233])
a('folder','cote14/092,107–113','cote15/170,205 (root-owned)','Positivity via divisors, pencils and blow-ups, and Hodge/coniveau questions form a thematic bridge to the root’s late cote15 material.','Current endpoint read here; cote15 endpoint checked by root, not independently re-proved by this part. Merge crosslink with root item identifiers.',[203,229,230,233,263])

# Exact theorem matches and qualified comparisons already adjudicated claim by claim.
for c in C:
 for key in c['refs']:
  r=R[key]
  ids=[int(s.split('-')[-1])for s in c['items']]
  a('published work',c['id']+'; cote14/'+','.join(map(str,c['scans'])),key+'; '+r['url'],c['fate'],'Locator: '+' | '.join(r.get('locators',[]))+' Verification: '+r.get('verification','')+' Limit: '+r.get('limitations',''),ids)

project=[
 ('LM7 E.23','Open; section-class image/fibres in metabelian and marked depth-two quotients. Excerpt truncated; no arithmetic transfer.',[266,278]),
 ('FLAGGED_149 B9','Open; remaining prime-to-p point question. Excerpt truncated; no solution imported.',[266,278]),
 ('LM6 A.22','Open; procyclic subgroup with arithmetic normalizer. Excerpt truncated.',[269,270]),
 ('LM6 A.50','Proved by prior return; affine hyperbolic-curve normalizer statement truncated after prime choice. Full hypotheses not reconstructed.',[269,270]),
 ('LM7 C.1','Known in prior return; Picard1-motive/generalized-Jacobian duality.',[266,268,269]),
 ('LM7 C.8','Refuted in prior return; not every generalized-Jacobian weight splitting occurs.',[256,268,269]),
 ('LM7 C.5','Proved in prior return; D↦[D] extension, ordern and no uniform exponent.',[262,269]),
 ('LM1 A.8','Refuted in prior return; det⁻¹ twist fixes SL₂ but not GL₂. Endpoint read, external proof not newly certified.',[255,256]),
 ('WG H9','Unchecked hunch about the height/intersection formula; cote44/004 endpoint verified but the reduction is not proved here.',[229,230,233]),
 ('WG2 §1.1 #3','Unchecked book-organization plan; current cover titles and retrieved cote16/44/47/54 endpoints agree at subject level.',[252,285]),
 ('WG2 §2.3 #12','Unchecked intermediate-Jacobian programme comparison; cote44 statements read.',[203,229,230]),
 ('WG2 §2.3 #7','Unchecked semisimplicity/nilpotence comparison; Jannsen used only with his stated hypotheses.',[260]),
 ('WG2 §1.1 #2','Unchecked organizing comparison among rings, Fourier transforms, vector extensions and height pairings.',[252,261,273]),
 ('WG2 §2.3 #2','Unchecked rational sl₂/universal-ring translation; normalization and coefficients separately checked.',[253,254]),
 ('WG2 §2.4 #3','Unchecked motive-category/sl₂ bridge; tensor unit obstruction rules out automatic inclusion.',[252,255,256,257]),
 ('WG2 §Summary #2','Unchecked combined-book synopsis; endpoint subjects confirmed, no structural theorem inferred.',[252,261,285]),
 ('WG2 B16 (§1.2)','Unchecked bridge from abelian rational Chow motives to the lefschetzien ring; Künnemann’s exact setting retained.',[261]),
 ('WG2 S28 (§1.7)','Unchecked integral order/divisibility project. Cote16/014 and47/009 endpoints confirmed; later integral counterexamples materially restrict it.',[254,262,292]),
 ('WG2 §2.1 #5','Unchecked seven-theorem synopsis; the current audit confirms programme status in cote44.',[203,229,230]),
 ('WG2 §2.3 #13','Unchecked algebraic-representative comparison. Only the checked Kahn codimension2 theorem is used in current claims.',[203]),
 ('WG2 §2.3 #3','Unchecked prior calculation lead: integral exterior model at16/014. This run independently recomputed the denominator/coefficient obstruction.',[254,262]),
 ('WG2 §2.4 #4','Unchecked search for a second Fourier witness and earlier Jacobian forms. No missing compatibility check is supplied by this part.',[261]),
 ('WG2 §6 #9','Unchecked proposed LEFSCHETZ_RINGS project. Current calculations do not constitute the requested full project.',[253,254,255]),
 ('WG2 §Lookups #3','Unchecked ACMV lookup lead; no theorem from the truncated excerpt is asserted by this part.',[203,229,230]),
 ('Hua 14-nakai-euler-characteristic-criterion','Intake says new to us, not novel. The actual criterion on14/094–095 agrees with Euler growth and the exact Mumford–Oda theorem.',[216,218])]
for target,what,ids in project:
 a('our projects',';'.join('SA06-'+str(i)for i in ids),target,what,'Both the current item and the endpoint label/status/excerpt in retrieved notes/RESULTS_STATE.md were read. External proof not certified here; see contextual_endpoint_audit.md. Parent checks full LM/FLAGGED/Hua records separately.',ids)

fields=['kind','from','to','what','evidence','note_ids']
with(P/'links.tsv').open('w',newline='')as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
with(P/'progress.log').open('a')as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tLINKS_SAVED\t{len(rows)} endpoint and publication links.\n')
print({'links':len(rows)})
