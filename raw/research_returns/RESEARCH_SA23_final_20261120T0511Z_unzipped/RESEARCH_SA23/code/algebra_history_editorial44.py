"""Classify actual source access and log targeted secondary-page readings."""
import datetime, hashlib, json, pathlib, re
import fitz
base=pathlib.Path(__file__).resolve().parents[1]
out={'utc_recorded':datetime.datetime.now(datetime.timezone.utc).isoformat()}
out['access_classification']=[
 {'route':'Chicago finding-aids index','status':'HTTP403; stopped; no inventory content'},
 {'route':'Chicago old select.html link','status':'HTTP200 redirected to turnstile challenge; not counted as source access; no challenge attempted'},
 {'route':'Brown collection overview','status':'HTTP200; actual institutional description opened and saved; catalogue links separately403 and stopped'},
 {'route':'Texas TARO00353','status':'HTTP200 only1394-byte JavaScript application shell; no finding-aid content inspected'},
 {'route':'Briscoe agent page','status':'web-reader403; stopped; collection abstract available only in indexed search results'},
]
out['secondary_readings']=[]
for filename,pages,url in [
 ('category_date_Schneps_chapter3.pdf',[14],'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Mathematics/chap3.pdf'),
 ('category_date_Schneps_chapter4.pdf',[4,5],'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Mathematics/chap4.pdf'),
]:
 path=base/'notes'/filename
 raw=path.read_bytes()
 doc=fitz.open(path)
 out['secondary_readings'].append({'url':url,'path':str(path.relative_to(base)),'sha256':hashlib.sha256(raw).hexdigest(),'pdf_pages':len(doc),'read_physical_pages':pages,'access':'Modern secondary narrative, extracted text; not original correspondence','texts':[{'page':p,'text':doc[p-1].get_text()} for p in pages]})
event='\t'.join(['geo-H-history','2026-11-20','GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','Bounded Memoir16 editorial route: Brown AMS collection overview and Chicago mathematics finding aid read; no original editorial letter or item-level Hilbert enclosure identified. Brown linked catalogues403, Chicago index403/challenge stopped, TARO onlyJSshell. Schneps November1952 and MacLane/Bastien passages are secondary narrative, not manuscript dating evidence.','notes/algebra_memoir_editorial_search.md;logs/algebra_history_editorial43.json;logs/algebra_history_editorial44.json;notes/algebra_history_web85.json;notes/algebra_history_web86.json;notes/algebra_history_web87.json;notes/algebra_history_web88.json;notes/algebra_history_web89.json;notes/algebra_history_web90.json;notes/algebra_history_web91.json;notes/algebra_history_web92.json;notes/algebra_history_web93.json;notes/algebra_history_web94.json;notes/algebra_history_web95.json;notes/algebra_history_web96.json'])
with (base/'notes/algebra_history_CHECK_EVENTS.tsv').open('a') as stream:stream.write(event+'\n')
out['event_added']=event
payload=json.dumps(out,ensure_ascii=False,indent=2)
(base/'logs/algebra_history_editorial44.json').write_text(payload+'\n')
print(payload)
