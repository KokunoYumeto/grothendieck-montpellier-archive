"""Public searches using only the observed TDL handler and periodical form.
The exact full journal phrase returned 'No results found'; shorter title
and Golden Jubilee terms avoid punctuation/definite-article differences.
The final POST submits the actual read-only periodical search form.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

root=pathlib.Path(__file__).resolve().parents[1]
forms=json.loads((root/'code/part_c_pfluger_tdl_forms_output.json').read_text())['forms']
form=next(x for x in forms if x['attributes'].get('id')=='advance_search_Periodical_filter_data_form')
fields={x['attributes']['name']:x['attributes'].get('value','') for x in form['controls'] if x['tag']!='button' and 'name' in x['attributes']}
fields.update(advance_search_Periodical_filter_category_id='21',advance_search_Periodical_title1='Mathematical',advance_search_Periodical_filter_publication_fdate='1959',advance_search_Periodical_filter_publication_edate='1962')
tasks=[
 ('mathematical','https://tamildigitallibrary.in/search/'+urllib.parse.quote('Mathematical',safe=''),None),
 ('golden_jubilee','https://tamildigitallibrary.in/search/'+urllib.parse.quote('Golden Jubilee',safe=''),None),
 ('periodical_1959_1962',form['attributes']['action'],fields)
]
started=datetime.datetime.now(datetime.timezone.utc).isoformat();tick=time.monotonic();results=[]
for name,url,params in tasks:
    now=time.monotonic();item={'name':name,'url':url,'method':'POST' if params else 'GET','fields':params}
    req=urllib.request.Request(url,data=urllib.parse.urlencode(params).encode() if params else None)
    try:
        with urllib.request.urlopen(req,timeout=35) as response:
            body=response.read();dest=root/'sources'/('part_c_pfluger_tdl_'+name+'.html');dest.write_bytes(body)
            item.update(status=response.status,final_url=response.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),saved_path=str(dest))
    except Exception as error:
        item['error']=type(error).__name__+': '+str(error)
        if isinstance(error,urllib.error.HTTPError):item['status']=error.code
    item['seconds']=time.monotonic()-now;results.append(item)
    if item.get('status') in (401,403,429):break
payload={'started_utc':started,'elapsed_seconds':time.monotonic()-tick,'requests':len(results),'results':results}
out=root/'code/part_c_pfluger_tdl_filters_output.json';out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload,ensure_ascii=False,indent=2))
