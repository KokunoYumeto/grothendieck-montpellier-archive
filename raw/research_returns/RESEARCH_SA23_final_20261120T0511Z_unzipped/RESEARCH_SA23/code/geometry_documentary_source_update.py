from pathlib import Path
import csv,json,hashlib,datetime
base=Path("/workspace/scratch/a7ef7e55112c/RESEARCH_SA23")
p=base/"notes/geometry_results.csv"
with p.open(newline="") as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
for row in rows:
    if row["id"]=="geo-H-history":
        if "algGrothendieckTrace1961" not in row["depends_on"]:
            row["depends_on"]+=";algGrothendieckTrace1961"
        row["notes"]+=" The1961 trace paper (received20June1960) uses the full Hilbert trace theorem in proof(2)(a),p142, but gives no older-manuscript date; its Cartier1961 reference is explicitly a proof addition."
with p.open("w",newline="") as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
event=["geo-H-history","2026-11-20","GPT-6 Astra Pro, inherited effort, geometry_analysis","targeted source check","Independently visually read both original spreads of Grothendieck1961 The trace of certain operators, printed141-143. Proof(2)(a),p142 assumes summable Hilbert eigenvalues and trace equality; p143 prints receipt20June1960 and a CartierFebruary1961 reference explicitly added in proof. Integrated later dated use with no genus-zero proof, no older-folio identification, and no inference from a broad career period. Bibliography key owned by algebra: algGrothendieckTrace1961. Numbered statement count unchanged."]
with (base/"notes/geometry_CHECK_EVENTS.tsv").open("a",newline="") as f:csv.writer(f,delimiter="\t").writerow(event)
changed=[]
for p in [base/"notes/geometry_Pietsch_Gohberg_documentary_route.md",base/"code/geometry_GohbergKrein1965_retrieve.py",base/"code/geometry_GohbergKrein1965_render.py"]:
 s=p.read_text()
 t=s.replace('notes/geometry_GohbergKrein1965.djvu','sources/geometry_GohbergKrein1965.djvu')
 if t!=s:p.write_text(t);changed.append(str(p.relative_to(base)))
# The raw keyword hits are retrievable source-text caches, not compact run logs.
# Retain their exact bytes in excluded *_full.txt caches; keep page/hash metadata
# in the original log locations. No source content is lost.
cache_records=[]
for stem in ["Pietsch2007","GohbergKrein1965"]:
 p=base/f"logs/geometry_{stem}_hits.json"
 raw=p.read_bytes();obj=json.loads(raw)
 cache=base/f"notes/geometry_{stem}_hits_full.txt"
 cache.write_bytes(raw)
 def compact(v):
  if isinstance(v,list):return [compact(x) for x in v]
  if isinstance(v,dict):
   z={k:compact(x) for k,x in v.items() if k!="text"}
   if "text" in v:z.update({"text_sha256":hashlib.sha256(v["text"].encode()).hexdigest(),"text_chars":len(v["text"])})
   return z
  return v
 small=compact(obj)
 if isinstance(small,dict):small["_raw_cache"]=str(cache.relative_to(base))
 p.write_text(json.dumps(small,ensure_ascii=False,indent=2))
 cache_records.append({"log":str(p.relative_to(base)),"raw_cache":str(cache.relative_to(base)),"raw_sha256":hashlib.sha256(raw).hexdigest(),"raw_bytes":len(raw)})
log={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"H_source_key":"algGrothendieckTrace1961","numbered_rows":len(rows),"paths_updated_after_root_cache_move":changed,"raw_keyword_source_caches":cache_records,"source_move_receipt":"logs/root_move_documentary_cache.json","no_archive_created":True}
(base/"logs/geometry_documentary_source_update.json").write_text(json.dumps(log,ensure_ascii=False,indent=2))
with (base/"notes/geometry_research_log.md").open("a") as f:
 f.write("\n## Later dated use: Grothendieck1961\n\nIndependently read the original two spreads covering pp.141-143 supplied by algebra. Integrated the later trace-theorem assumption at proof(2)(a),p142, its20June1960 receipt line, and the expressly added-in-proof Cartier1961 reference into geo-H-history. This refines the source chronology and guards against dating undated sheets solely by a broad career period; it creates no new numbered statement and closes no manuscript-date gate. Source key algGrothendieckTrace1961 remains in algebra's bibliography. Root moved the original Gohberg-Krein DjVu unchanged into sources/; geometry pointers now follow it. Raw keyword-hit page texts were preserved as excluded retrievable caches and replaced by page/hash metadata in run logs.\n")
print(json.dumps(log))

