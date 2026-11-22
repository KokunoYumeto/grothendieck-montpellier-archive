"""Persist the exact documentary scope after actual original-page inspection."""
import datetime
import hashlib
import json
import pathlib
base=pathlib.Path(__file__).resolve().parents[1]
output={
 'utc_recorded':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'actual_visual_readings':[
  {'source':'Horn1950','printed_pages':[374,375],'scope':'Entire two-page original article, including communication date and all references; article starts in lower part of374'},
  {'source':'Schatten1960','printed_pages':['V','VI',36,37,80,81],'scope':'Full preface and bibliography, plus both pages of actual public trace-chapter preview; remaining book not read'},
  {'source':'Dunford1958','printed_pages':[217,221,223,225,272,273,274],'scope':'Selected original pages and complete bibliography; entire58page native text searched, not all pages visually read'},
 ],
 'not_opened':['Horn1954 original paper','Schatten1960 full trace chapter and full monograph','Dunford-Schwartz original English PartII historical notes'],
 'correction':'Dunford1958 p221 letter footnote is3 in original, misread8 by nativeOCR; p223 letter footnote6 concerns Fixman',
 'result':'No dated Grothendieck proof/letter/enclosure identification or cote1 manuscript date established',
 'source_hashes':{},
}
for name in ['horn1950_p374.png','horn1950_p375.png','schatten1960_front.pdf','schatten1960_back.pdf','schatten1960_preview.pdf','dunford1958_survey.pdf']:
 path=base/f'sources/algebra_spectral_{name}'
 output['source_hashes'][str(path.relative_to(base))]={'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
event='\t'.join([
 'geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run',
 'Bounded early spectral reception: original Horn1950 pp374-375; Schatten1960 preface V-VI, bibliography80-81 and public preview36-37; Dunford1958 selected original pages and full native-text search inspected. No dated Grothendieck proof, letter, enclosure or cote1 identification. Horn1954 and full Schatten/Dunford-Schwartz notes remain unopened; access stops recorded.',
 'notes/algebra_spectral_reception_source_search.md;notes/algebra_spectral_query_manifest.json;logs/algebra_spectral_fetch48.json;logs/algebra_spectral_render49.json;logs/algebra_spectral_fetch50.json;logs/algebra_spectral_analyze51.json;logs/algebra_spectral_record52.json',
])
event_path=base/'notes/algebra_history_CHECK_EVENTS.tsv'
if event not in event_path.read_text():
 with event_path.open('a') as stream:stream.write(event+'\n')
output['event_added']=event
payload=json.dumps(output,ensure_ascii=False,indent=2)
(base/'logs/algebra_spectral_record52.json').write_text(payload+'\n');print(payload)
