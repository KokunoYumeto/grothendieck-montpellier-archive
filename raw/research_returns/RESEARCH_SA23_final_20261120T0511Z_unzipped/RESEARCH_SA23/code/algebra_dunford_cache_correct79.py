"""Correct discovery metadata and relocate raw source pages without byte changes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

start=time.monotonic()
base=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
log={"started_utc":stamp,"source_relocations":[],"authored_note_corrections":[]}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

old=base/"notes/algebra_dunford_ru1966_pages"
new=base/"sources/algebra_dunford_ru1966_pages"
assert old.exists() and not new.exists()
new.mkdir()
for p in sorted(old.iterdir()):
    assert p.is_file()
    target=new/p.name
    h=sha(p)
    size=p.stat().st_size
    p.rename(target)
    assert sha(target)==h
    log["source_relocations"].append({"old_path":str(p.relative_to(base)),"new_path":str(target.relative_to(base)),"sha256":h,"bytes":size,"byte_for_byte_preserved":True})
old.rmdir()

note=base/"notes/algebra_dunford_ru1966_source_audit.md"
before=sha(note)
s=note.read_text().replace("images and corrected per-page text in `notes/algebra_dunford_ru1966_pages/`", "images and corrected per-page text now in `sources/algebra_dunford_ru1966_pages/`")
s+="\n## Source-cache relocation\n\nAfter the original page reading, the raw images and extracted per-page text were moved unchanged from `notes/algebra_dunford_ru1966_pages/` to `sources/algebra_dunford_ru1966_pages/`, following the project source-cache policy. The executed retrieval/render programs and their original logs retain their historical paths. `logs/algebra_dunford_cache_correct79.json` records every old/new path, byte count and SHA256; no file bytes changed during the move.\n"
note.write_text(s)
log["authored_note_corrections"].append({"path":str(note.relative_to(base)),"before_sha256":before,"after_sha256":sha(note),"reason":"Current raw-cache paths and exact relocation record"})

manifest=base/"notes/algebra_dunford_ru1966_manifest.json"
d=json.loads(manifest.read_text())
d["current_original_page_image_and_text_directory"]="sources/algebra_dunford_ru1966_pages"
d["initial_original_page_image_and_text_directory"]="notes/algebra_dunford_ru1966_pages"
d["source_cache_relocation_log"]="logs/algebra_dunford_cache_correct79.json"
manifest.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")

note=base/"notes/algebra_gohberg_lidskii_followup_search.md"
before=sha(note)
s=note.read_text()
old_sentence="A public institutional NBUV result identified O. V. Bulgakov's 2013 custodial survey of Krein correspondence"
new_sentence="A public institutional NBUV result identified the 2013 custodial survey of Krein correspondence (the initial discovery note provisionally gave author initials O. V.; root's subsequently opened original header identifies **Yurii Bulgakov / Юрій Булгаков**)"
assert old_sentence in s
s=s.replace(old_sentence,new_sentence)
s+="\nMetadata correction at the current source-record update: the provisional discovery initials O. V. were not verified from the article. Root's independent original-header reading, documented in `notes/root_krein_correspondence_date_audit.md`, establishes Yurii Bulgakov (Юрій Булгаков). This note adopts that correction with attribution; algebra_letters still did not open the survey itself. The raw search results and original record78 output are retained unchanged as historical records. The 2012 related article above remains a metadata-only lead; its authorship was not independently collated here.\n"
note.write_text(s)
log["authored_note_corrections"].append({"path":str(note.relative_to(base)),"before_sha256":before,"after_sha256":sha(note),"reason":"Root original-header audit corrects provisional discovery author initials; no new original reading by this agent"})

manifest=base/"notes/algebra_gohberg_lidskii_followup_manifest.json"
d=json.loads(manifest.read_text())
d["custodial_survey_author_correction"]={"provisional_discovery_initials":"O. V.","corrected_name":"Yurii Bulgakov (Юрій Булгаков)","basis":"Root's opened original header; notes/root_krein_correspondence_date_audit.md","not_independently_opened_by_algebra_letters":True}
manifest.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")

log["ended_utc"]=datetime.now(timezone.utc).isoformat()
log["elapsed_seconds"]=round(time.monotonic()-start,3)
log["paper_or_bibliography_changed"]=False
log["executed_original_programs_and_logs_changed"]=False
log["source_bytes_preserved"]=True
(base/"logs/algebra_dunford_cache_correct79.json").write_text(json.dumps(log,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"started_utc":log["started_utc"],"ended_utc":log["ended_utc"],"elapsed_seconds":log["elapsed_seconds"],"files_relocated":len(log["source_relocations"]),"source_bytes_preserved":True,"note_corrections":log["authored_note_corrections"],"log":"logs/algebra_dunford_cache_correct79.json"},ensure_ascii=False,indent=2))
