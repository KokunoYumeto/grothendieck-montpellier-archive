from pathlib import Path
import datetime, json
base=Path(__file__).resolve().parents[1]
old=json.loads((base/'notes/geometry_final_package_plan_cp04_initial.json').read_text())
new=json.loads((base/'notes/geometry_final_package_plan_cp04.json').read_text())
old_content={(x['sha256'],x['bytes']) for x in old['canonical_files']}
added=[x for x in new['canonical_files'] if (x['sha256'],x['bytes']) not in old_content]
old_names={x['member']:x for x in old['canonical_files']}
added.sort(key=lambda x:x['estimated_deflated_bytes'],reverse=True)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'activity':'packaging only; not mathematical movement','old_plan_utc':old['created_utc'],'new_plan_utc':new['created_utc'],'added_distinct_contents':len(added),'added_estimated_compressed_bytes':sum(x['estimated_deflated_bytes'] for x in added),'largest_additions':[{**x,'path_existed_in_old_plan':x['member'] in old_names} for x in added[:25]],'archive_created':False}
(base/'logs/geometry_package_growth_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
