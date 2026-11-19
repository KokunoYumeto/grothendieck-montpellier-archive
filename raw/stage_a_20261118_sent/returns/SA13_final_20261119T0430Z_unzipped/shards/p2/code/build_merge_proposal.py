#!/usr/bin/env python3
"""Serialize manually chosen semantic merges. No automatic duplicate decisions."""
import json
from pathlib import Path
base=Path(__file__).resolve().parents[1]
shards=base.parent
records={}
for sh in ('p1','p2'):
 for kind in ('items','claims','problems'):
  for rec in json.loads((shards/sh/(kind+'.json')).read_text()): records[rec['id']]=rec

item_pairs=[
 ('SA13-100','SA13-34','Same local correspondence pairing resumed after cancellation; preserve local versus proper global scope.'),
 ('SA13-102','SA13-2','Same duality exchange, applied to pr2 with explicit constructible biduality on150.'),
 ('SA13-110','SA13-36','Same bounded trace model issue continuing146→148→158.'),
 ('SA13-168','SA13-52','Same reused Roos source dossier; preserve different Zariski and étale theorems.'),
 ('SA13-183','SA13-49','Same blowup-chart Lemma1 used explicitly in definition on141.'),
 ('SA13-187','SA13-39','Same operator source dossier, source identification facet only.'),
 ('SA13-198','SA13-38','Same SGA trace publication comparison; exact textual descent remains unproved.'),
 ('SA13-210','SA13-1','Same earlier-run context/register; no underlying prior project proof supplied.'),
 ('SA13-211','SA13-1','Same returned-package register; preserve all44 additional rows and their lead status.'),
 ('SA13-212','SA13-61','Same earlier-run bibliography and comparison apparatus; current checks remain independent.')]
problem_pairs=[
 ('MP-SA13-30','MP-SA13-09','Named inverse-Hom construction subproblem for the local pairing; retain its own hypotheses and fate.'),
 ('MP-SA13-31','MP-SA13-09','Same local-to-global trace compatibility proposed on144 and resumed148/158.'),
 ('MP-SA13-32','MP-SA13-07','Same definition/descent of perfect-complex trace, including bounded representative issue.')]
claim_pairs=[
 ('C-SA13-102','C-SA13-001','Same exchange identity; retain150 internal-Hom application and dependency to C-SA13-120.'),
 ('C-SA13-156','C-SA13-072','One full blowup-chart lemma and its explicitly cited localization consequence.'),
 ('C-SA13-157','C-SA13-064','Literal continuous Lemma2:173/printed12→137/printed13→135/printed14. Restore two-ring hypotheses.')]
def make_rows(kind,pairs):
 out=[]
 for old,new,why in pairs:
  a,b=records[old],records[new]
  out.append({'kind':kind,'from':old,'canonical':new,'reason':why,
    'from_source_locators':a.get('lines',a.get('occurrences',[])),
    'canonical_source_locators':b.get('lines',b.get('occurrences',[])),
    'preserve_source_ids':a.get('sources',[])+b.get('sources',[]),
    'status':'proposed; root assembly owns application'})
 return out
out={'date':'2026-11-19','who':'GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p2',
 'scope':'p1/p2 semantic audit; no shard rewritten',
 'reviewed_counts':{'p1_items':61,'p2_items':108,'p1_claims':76,'p2_claims':142,'p1_problems':10,'p2_problems':49},
 'rules':['Preserve every Pro verdict row; change canonical link and keep alias table.',
  'Union source occurrences, exact quotations, page statuses, bibliography and check events.',
  'Do not force distinct claims to merge merely because their parent item is merged.',
  'Resolve aliases before validating references; preserve old IDs as redirects.'],
 'merges':make_rows('item',item_pairs)+make_rows('problem',problem_pairs)+make_rows('claim',claim_pairs),
 'canonical_patches':{
  'MP-SA13-09':{'title':'Local correspondence pairing: construction and global-trace compatibility',
   'preserve_subproblems':['inverse external-Hom comparison150–156','local absence of properness','global trace compatibility144/148/158','shifted sign and type alarms']},
  'C-SA13-064':{'statement':'Let R⊂Rbar be same-dimensional noetherian regular local domains with Rbar centered on m, mRbar=mbar, and the same residue field. Then R/m^q→Rbar/mbar^q is an isomorphism for every q and the completions agree. For every ideal J of R, JRbar∩R=J, J is principal iff JRbar is principal, and Frac(R)∩Rbar=R in the common fraction overfield.',
   'items':['SA13-184','SA13-185'],
   'remove_inaccurate_restriction':'The bar on Rbar does not require Rbar to be the completion of R; that is only a special case.',
   'exact_continuation':'p2scan173global744–748→p1scan137global957–983→p1scan135global908–910'},
  'C-SA13-072':{'append':'For S=R[x2/x1,...,xn/x1], S/x1S is canonically the polynomial ring over κ(m) in n−1 residue variables. A maximal localization containing x1 is regular local of dimensionn, centered on m, with finite residue extension; x1 belongs to a regular system of parameters.'}},
 'do_not_merge':[
  ['C-SA13-028','C-SA13-029','C-SA13-038','C-SA13-100'],
  ['C-SA13-029','C-SA13-038','C-SA13-101'],
  ['C-SA13-028','C-SA13-120'],['C-SA13-036','C-SA13-124'],
  ['C-SA13-013','C-SA13-015','C-SA13-016','C-SA13-103','C-SA13-104','C-SA13-167'],
  ['C-SA13-074','C-SA13-075','C-SA13-076','C-SA13-130','C-SA13-131'],
  ['C-SA13-040','C-SA13-041','C-SA13-159','C-SA13-160','C-SA13-161'],
  ['C-SA13-073','C-SA13-158'],['C-SA13-064','C-SA13-147'],['C-SA13-058','C-SA13-148'],
  ['SA13-54','SA13-207']],
 'evidence_note':'cross_package_merge_audit.md gives exact textual joins and reasons for nonmerges.'}
assert len({x['from'] for x in out['merges']})==16
for row in out['merges']:
 assert row['from'] in records and row['canonical'] in records
dest=base/'cross_package_merge_map.json';dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output':str(dest),'item_merges':10,'problem_merges':3,'claim_merges':3,'status':'all IDs validated; no source shard altered'}))
