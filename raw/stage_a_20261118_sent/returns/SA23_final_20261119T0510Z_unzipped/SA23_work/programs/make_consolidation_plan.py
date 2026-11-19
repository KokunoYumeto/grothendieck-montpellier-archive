#!/usr/bin/env python3
"""Serialize manually reviewed decisions; this program does no fuzzy matching."""
import json,collections,copy,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[1]
def read(p):return json.loads((W/p).read_text())
plan={'date':'2026-11-19','author':'GPT-6 Astra Pro, source owners and root integration','basis':'All mergers were decided by direct source comparison and reviewed manually. No headings, keywords or similarity scores generate a verdict. Component mappings preserve complete source_records and exact scope.','item_merges':[],'claim_merges':[],'problem_merges':[],'record_updates':[],'additional_links':[],'kept_distinct':[],'review_trail':[],'source_observations':[]}
base=read('integration/root_consolidation.json')
for k in ['item_merges','claim_merges','problem_merges']:plan[k]+=base[k]
for row in read('parts/ega/cross_owner_review/indexed_duplicate_proposals.json'):
 target=row['target_item'];sources=[i for i in row['merge_items']if i!=target]
 plan['item_merges'].append({'target':target,'sources':sources,'reason':row['source_based_reason']+' Preserve: '+'; '.join(row['preserve']),'review_record':row['id'],'overrides':{'statement':row['common_statement']+' The broader topological, formal-parameter or degreewise variants remain separately specified in source_records and the claim map.'}})
scope=read('integration/cocharacter_scope_updates.json')
for k in ['record_updates','additional_links']:plan[k]+=scope[k]
plan['direction_consolidations']=read('integration/direction_consolidation.json')
concordance=read('parts/forms/cote24_25_concordance.json')
for row in concordance['rows']:
 if not row['action'].startswith('merge'):
  plan['kept_distinct'].append(row);continue
 targets=row['targets']
 if row['kind']=='claim':
  # A source assertion is not made the author of a present-run R refinement.
  # Those mathematical repairs are cross-referenced and remain independently
  # numbered, with their own proof events.
  repairs=[t for t in targets if t.endswith('R')]
  targets=[t for t in targets if not t.endswith('R')]
  if repairs:plan['kept_distinct'].append({'source':row['source'],'related_present_run_refinements':repairs,'reason':'The source assertion maps to the corresponding source clauses. R records remain independent reconstructions, not additional authorial occurrences.','concordance':row})
 for target in targets:
  spec={'target':target,'sources':[row['source']],'reason':row['relation']+': '+row['scope']+'. '+row['reason'],'review_record':'parts/forms/cote24_25_concordance.json','review_details':row}
  plan[row['kind']+'_merges'].append(spec)

# Root accepted this bounded source-based review. Retain the full decisions,
# including the distinctions that prohibit further claim/problem mergers.
review_path='integration/groupes_spaces_review.json'
review=read(review_path)
for key in ['item_merges','claim_merges','problem_merges','record_updates','additional_links','kept_distinct']:
 for decision in review[key]:
  decision=copy.deepcopy(decision)
  decision.setdefault('review_record',review_path)
  plan[key].append(decision)
plan['review_trail'].append({'review_record':review_path,'sha256':hashlib.sha256((W/review_path).read_bytes()).hexdigest(),'acceptance':'Explicitly accepted by root for integration on 2026-11-19.','scope':review['scope'],'summary':review['summary'],'source_checks':review['source_checks'],'input_snapshots_at_review':review['input_snapshots']})
for observation in review['source_locator_observations']:
 plan['source_observations'].append(dict(copy.deepcopy(observation),review_record=review_path,interpretation='Observation at the review snapshot; subsequent owner locator additions are retained, not overwritten.'))

# This is structural validation only. Multiple targets for a compound source
# are allowed; repeated edges, conflicting patches, and implicit merge chains
# are not. Appending source locations never replaces an owner's current list.
records={kind:[r for p in (W/'parts').iterdir()if(p/(kind+'.json')).exists()for r in read(str((p/(kind+'.json')).relative_to(W)))]for kind in ['items','claims','problems']}
errors=[];checks={}
protected={'id','source_records','integration_record_before_update','integration_updates','integration_update_reasons'}
for kind,rows in records.items():
 duplicates=[sid for sid,n in collections.Counter(r['id']for r in rows).items()if n>1]
 if duplicates:errors.append({'check':'unique owner IDs','kind':kind,'duplicates':duplicates})
 checks[kind+'_original_records']=len(rows)
removed_by_kind={}
for kind in ['item','claim','problem']:
 key=kind+'_merges';targets={x['target']for x in plan[key]};removed={s for x in plan[key]for s in x['sources']}
 removed_by_kind[kind+'s']=removed
 if targets&removed:errors.append({'check':'merge chains must be flattened manually','kind':kind,'ids':sorted(targets&removed)})
 ids={r['id']for r in records[kind+'s']}
 if (targets|removed)-ids:errors.append({'check':'review plan has absent records','kind':kind,'ids':sorted((targets|removed)-ids)})
 edges=collections.Counter((x['target'],s)for x in plan[key]for s in x['sources'])
 if any(n>1 for n in edges.values()):errors.append({'check':'unique merge edges','kind':kind,'duplicates':[[*edge,n]for edge,n in edges.items()if n>1]})
 overrides={}
 for spec in plan[key]:
  for field,value in spec.get('overrides',{}).items():
   if field in protected:errors.append({'check':'protected merge field','target':spec['target'],'field':field})
   ident=(spec['target'],field)
   if ident in overrides and overrides[ident]!=value:errors.append({'check':'conflicting merge overrides','target':spec['target'],'field':field})
   overrides[ident]=value

seen_updates=set();sets={};appends=set();updated_targets=set()
for spec in plan['record_updates']:
 kind=spec['kind'];sid=spec['id'];updated_targets.add((kind,sid))
 ids={r['id']for r in records.get(kind,[])}
 if sid not in ids or sid in removed_by_kind.get(kind,set()):errors.append({'check':'record update targets surviving original','kind':kind,'id':sid})
 token=json.dumps(spec,sort_keys=True,ensure_ascii=False)
 if token in seen_updates:errors.append({'check':'duplicate record update','kind':kind,'id':sid})
 seen_updates.add(token)
 for field,value in spec.get('set_fields',{}).items():
  ident=(kind,sid,field)
  if field in protected:errors.append({'check':'protected record field','kind':kind,'id':sid,'field':field})
  if ident in sets and sets[ident]!=value:errors.append({'check':'conflicting set_fields','kind':kind,'id':sid,'field':field})
  sets[ident]=value
 for field in spec.get('append_fields',{}):
  if field in protected:errors.append({'check':'protected record field','kind':kind,'id':sid,'field':field})
  appends.add((kind,sid,field))
for kind,sid,field in set(sets)&appends:
 errors.append({'check':'order-dependent set/append patch','kind':kind,'id':sid,'field':field})

item_by_id={r['id']:r for r in records['items']};item_targets=collections.defaultdict(set)
for spec in plan['item_merges']:
 for sid in spec['sources']:item_targets[sid].add(spec['target'])
for sid,targets in item_targets.items():
 if len(targets)>1 and item_by_id.get(sid,{}).get('sources'):errors.append({'check':'indexed item has multiple targets','id':sid,'targets':sorted(targets)})
for observation in plan['source_observations']:
 claim=next((r for r in records['claims']if r['id']==observation['claim']),None)
 observation['current_owner_locators']=claim['lines']if claim else None
checks.update(record_updates=len(plan['record_updates']),distinct_updated_records=len(updated_targets),review_trail_records=len(plan['review_trail']),source_observations=len(plan['source_observations']))
validation={'scope':'Structural validation of explicitly reviewed integration decisions; no mathematical verdict is generated.','checks':checks,'errors':errors,'passed':not errors}
(W/'integration/plan_builder_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
assert not errors,errors
(W/'integration/consolidation_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'merge_rows':{k:len(plan[k])for k in ['item_merges','claim_merges','problem_merges']},'removed_sources':{k:len({s for r in plan[k]for s in r['sources']})for k in ['item_merges','claim_merges','problem_merges']},'record_updates':len(plan['record_updates']),'kept_distinct':len(plan['kept_distinct']),'validation':validation},ensure_ascii=False))
