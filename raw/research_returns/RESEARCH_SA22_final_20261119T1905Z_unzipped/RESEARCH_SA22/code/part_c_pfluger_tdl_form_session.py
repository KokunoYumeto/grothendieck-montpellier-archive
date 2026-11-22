"""Follow the actual public advanced-search form with ordinary anonymous cookies.
The earlier urllib form submission did not retain cookies across its redirect;
its dynamic listing therefore supplied no search results and was inconclusive.
Here normal CookieJar handling preserves the form's anonymous filter state,
then executes the read-only AJAX request explicitly present in the returned
public page's Front_search_Book function. No login or challenge is involved.
"""
import datetime
import hashlib
import html.parser
import http.cookiejar
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

root=pathlib.Path(__file__).resolve().parents[1]
prior=json.loads((root/'code/part_c_pfluger_tdl_filters_output.json').read_text())
form=next(x for x in prior['results'] if x['name']=='periodical_1959_1962')
class Inputs(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.fields={};self.csrf=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='input':
            if a.get('id'):self.fields[a['id']]=a.get('value','')
            if 'csrf' in a.get('class','').split() and self.csrf is None:self.csrf=a.get('value')
started=datetime.datetime.now(datetime.timezone.utc).isoformat();clock=time.monotonic()
redirects=[]
class Redirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        redirects.append({'from':req.full_url,'status':code,'to':newurl})
        return super().redirect_request(req,fp,code,msg,headers,newurl)
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),Redirects())
results=[]
def request(name,url,fields):
    tick=time.monotonic();record={'name':name,'url':url,'method':'POST','fields':{k:('[anonymous form token]' if 'csrf' in k else v) for k,v in fields.items()}}
    body=None
    try:
        req=urllib.request.Request(url,data=urllib.parse.urlencode(fields).encode())
        with opener.open(req,timeout=35) as response:
            body=response.read();dest=root/'sources'/('part_c_pfluger_tdl_'+name+'.txt');dest.write_bytes(body)
            record.update(status=response.status,final_url=response.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),saved_path=str(dest))
            if 'json' in response.headers.get('Content-Type',''):
                try:record['response']=json.loads(body)
                except json.JSONDecodeError:pass
    except Exception as error:
        record['error']=type(error).__name__+': '+str(error)
        if isinstance(error,urllib.error.HTTPError):record['status']=error.code
    record['seconds']=time.monotonic()-tick;results.append(record)
    return body
body=request('periodical_session_page',form['url'],form['fields'])
if body is not None and results[-1].get('status')==200:
    text=body.decode('utf-8','replace');parser=Inputs();parser.feed(text)
    if "url: 'book-list-data-ajax-new'" in text and parser.csrf:
        f=parser.fields
        fields={'process':'36','searchtext':f.get('searchbox',''),'limit':f.get('lazy_records','0'),'category':f.get('category_id',''),'sorting':'','book_view':f.get('book_view_rcd',''),'checkval':'hide','item_per_page':f.get('item_per_page','24'),'csrf_test_name':parser.csrf}
        for key in ('author_search','subject_search','source_search','language_search','fformat_search','resource_category_search','resource_search','location_of_site_search','village_search','ruler_search','historic_period_search'):fields[key]='[]'
        for key in ('header_cat_id','header_sub_cat_id','header_inner_cat_id','header_today_recommendations'):fields[key]=f.get(key,'')
        request('periodical_session_results','https://tamildigitallibrary.in/book-list-data-ajax-new',fields)
payload={'started_utc':started,'elapsed_seconds':time.monotonic()-clock,'explicit_request_operations':len(results),'automatic_redirects':redirects,'results':results}
out=root/'code/part_c_pfluger_tdl_form_session_output.json';out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
summary={'started_utc':started,'elapsed_seconds':payload['elapsed_seconds'],'explicit_request_operations':len(results),'automatic_redirects':redirects,'results':[{k:v for k,v in x.items() if k!='response'}|({'response_keys':list(x['response']),'count':x['response'].get('count'),'html':x['response'].get('html','')[:5000]} if isinstance(x.get('response'),dict) else {}) for x in results]}
print(json.dumps(summary,ensure_ascii=False,indent=2))
