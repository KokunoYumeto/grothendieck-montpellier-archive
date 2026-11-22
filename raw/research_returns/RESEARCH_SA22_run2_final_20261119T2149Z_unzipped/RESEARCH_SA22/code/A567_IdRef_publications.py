#!/usr/bin/env python3
"""One author-scoped query against the advertised public IdRef endpoint."""
import json
from urllib.parse import urlencode
from A567_IdRef_public_followup import ROOT, retrieve

query = '''SELECT DISTINCT ?record ?role ?property ?value
WHERE {
  ?record ?role <http://www.idref.fr/076074897/id> .
  ?record ?property ?value .
}
LIMIT 2000'''
url='https://data.idref.fr/sparql?'+urlencode({
    'query':query,'format':'application/sparql-results+json','timeout':'10000'})
row=retrieve('Gabber_publications.json',url)
row['query']=query
row['query_count']=1
row['limit']=2000
if row.get('http_status')==200:
    obj=json.loads((ROOT/row['saved']).read_text())
    bindings=obj.get('results',{}).get('bindings',[])
    row['bindings_count']=len(bindings)
    row['limit_reached']=len(bindings)>=2000
    row['distinct_records_count']=len({x['record']['value'] for x in bindings})
    row['literal_values']=[{k:v['value'] for k,v in x.items()} for x in bindings
                           if x['value']['type']=='literal']
(ROOT/'logs/A567_IdRef_publications_query.json').write_text(json.dumps(row,indent=2)+'\n')
print(json.dumps(row,indent=2))
