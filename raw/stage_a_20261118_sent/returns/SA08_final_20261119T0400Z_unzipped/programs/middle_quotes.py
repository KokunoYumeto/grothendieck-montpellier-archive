"""Manual, passage-by-passage quotation audit for the middle dossier.

Every range below was selected after rereading the actual transcription.  The
program only copies those selections, checks their scan boundaries, and refreshes
problem occurrences.  It does not decide note verdicts or mathematical status.
No source transcription is edited.  A later literature comparison has no invented
author quotation: its manuscript anchors and its reconstruction remain separate.
"""
import csv, re


def audit(b):
    P,Q=b.P,b.Q
    C={int(x['id'].split('C')[1]):x for x in b.claims}
    I={int(x['id'].split('-')[1]):x for x in b.items}
    page={}
    for p,lines in b.texts.items():
        current=None;page[p]={}
        for n,line in enumerate(lines,1):
            m=re.search(r'\\scanpage\{(\d+)\}',line)
            if m: current=int(m.group(1))
            page[p][n]=current
    def bounds(r):
        q=r.split('-');return int(q[0]),int(q[-1])
    def passage(p,r):
        a,z=bounds(r);scans={page[p][n] for n in range(a,z+1)}
        assert len(scans)==1 and None not in scans,(p,r,scans)
        return {'file':f'{p}_transcription.tex','scan':next(iter(scans)),
                'lines':r,'text':'\n'.join(b.texts[p][a-1:z]).strip()}
    def fmt(blocks):
        return '; '.join(f"{x['file']}:{x['lines']} (scan {x['scan']})" for x in blocks)
    def apply(obj,p,quotes,evidence=(),field='his_statement'):
        qp=[passage(p,r) for r in quotes]
        ranges=list(dict.fromkeys(list(quotes)+list(evidence)))
        ep=[passage(p,r) for r in ranges]
        obj[field]='\n[…]\n'.join(x['text'] for x in qp)
        obj['lines']=fmt(ep)
        obj['scans']=sorted({x['scan'] for x in ep})
        obj['quote_passages']=qp
        obj['source_passages']=[{k:v for k,v in x.items() if k!='text'} for x in ep]
        obj.pop('additional_locators',None)
    # Tuple = exact quotation range(s), followed by further relevant passages.
    # Discontinuous ranges are deliberate: no interleaved SGA or letter leaf is
    # silently included in a live De Rham claim.
    first={
      101:(['45-51'],['36-64']),
      102:(['105'],['60-64','94-105','213-218']),
      103:(['99'],['96-105','132-137','213-218']),
      104:(['132-137'],[]),
      105:(['149-153','165-171'],['139-177']),
      106:(['213-218'],['207-218']),
      107:(['294'],['220','246-267','295-324']),
      108:(['367-379'],['341-395']),
      109:(['430-438'],['417-444','474-492']),
      110:(['526-540'],['474-492','542-547']),
      111:(['599-607'],['574-607']),
      112:(['620-622'],['618-623']),
      113:(['620'],['622-623']),
      114:(['649'],['627-629','647-676']),
      115:(['654-660','663-676'],['647-650']),
      116:(['710-718','735-748'],['685-704','720-732']),
      117:(['816-818'],['775-795','847-858']),
      118:(['801-803'],['805-814']),
      119:(['860-868'],['894-896']),
      120:(['898-906'],['894-904']),
      121:(['935-942'],['908-912','929-944']),
      122:(['946-957','984-988'],['990-1014']),
      123:(['1046-1056','1059-1066'],[]),
      124:(['1136-1144','1147-1155'],['1122-1164']),
      125:(['1213-1221'],['1205-1208','1223-1235']),
      126:(['1245-1259'],['1240-1262']),
      127:(['1321-1326'],['1307-1327']),
      128:(['1368-1374'],['1329-1376']),
      129:(['406-410'],['400-410']),
      130:(['116-125'],['112-125','240']),
      131:(['330-332'],[]),
      132:(['8-16'],['18-22','274-282','184-186']),
      133:(['192-198'],['188-198']),
      134:(['78-87'],['72-87']),
      135:(['229-234'],['227-234']),
      136:(['500-515'],['450-468','554-568']),
      137:(['973'],['969-979','1037-1041','1073-1095','918-924']),
      138:(['825-839'],['880-887']),
      139:(['759-769'],['842']),
      140:(['769'],['755-769']),
      141:(['1172-1187'],['1189-1191']),
      142:(['1276','1284-1290'],['1278-1298']),
      188:(['647-649'],[]),
      189:(['724-731'],['710-732']),
      190:(['847-851'],['785-794']),
      191:(['853'],['847-858']),
      192:(['1003-1014'],['984-1014','855-868']),
      193:(['404'],['400-410']),
      194:(['400'],['402','410']),
      195:(['406-408'],['410']),
      196:(['410'],['400-408']),
      197:(['975'],['969-977','1037-1041']),
      198:(['1030-1033'],['1022-1041','1081-1095']),
      199:(['878'],['924','880-887','825-839']),
      501:(['554-556'],['500-515','1172-1189']),
      502:(['922'],['918-924']),
    }
    second={
      143:(['56-74','105-108'],['21-51','99-144']),
      144:(['119-127'],['130-145']),
      145:(['200-207'],['209-222','308-345','373-408']),
      146:(['404-408','467'],['443-471']),
      147:(['278','308-320'],['256-278','301-345']),
      148:(['512-529'],['531-539']),
      149:(['567-572'],['558-575']),
      150:(['615-623'],[]),
      151:(['624-635'],['567-575']),
      152:(['694-704','737'],['669-704','722-757']),
      153:(['781-795'],[]),
      154:(['851-860','866-876'],['826-876']),
      155:(['934-943'],['928-944','1011-1020','1025-1037']),
      156:(['947-953'],['988-1001','1007-1009']),
      157:(['960-966'],['958-966','988-1001']),
      158:(['974-980'],['969-982','1011-1020']),
      159:(['944','982'],['928-944','969-982']),
      160:(['988','995-1001'],['990-1003']),
      161:(['1011-1020'],[]),
      162:(['1033-1037'],['1025-1037']),
      163:(['1007'],['1009']),
      164:(['1050-1054'],['1039-1054']),
      165:(['1062-1079'],['1081-1112','1149-1167']),
      166:(['1181-1182','1201-1210'],['1173-1228']),
      167:(['1271-1281'],['1283-1305']),
      168:(['1304-1305'],['1271-1305','1370-1374']),
      169:(['1307-1310'],[]),
      170:(['1312-1318'],['1355-1374']),
      171:(['1355-1362'],[]),
      172:(['1392-1404'],['1377-1404']),
      173:(['1470-1475'],['1445-1475']),
      174:(['1481-1488'],[]),
      175:(['8-14'],['87-89','152-187']),
      176:(['295','229-231'],['285-295','353-367']),
      177:(['421-425','361'],['353-367','427-435']),
      178:(['483','499'],['485-499']),
      179:(['548-550'],['546-552']),
      180:(['651-664'],['582-604','644-664']),
      181:(['768-770'],['772','711-715']),
      182:(['1514-1525','1430-1439'],['1409-1439','1323-1327']),
      183:(['1328-1337'],['1323-1337']),
      184:(['1339-1349'],[]),
      185:(['1493-1512'],[]),
      186:(['1251-1265'],['1233-1265']),
      187:(['811-815','888-892'],['802-821','882-892','914-922']),
    }
    assert set(first)|set(second)==set(C),(set(C)-set(first)-set(second))
    for p,m in [(P,first),(Q,second)]:
        for n,(quotes,evidence) in m.items():apply(C[n],p,quotes,evidence)
    C[501]['statement']='Over a henselian trait, an abelian variety with semistable reduction has an integral, ℓ-independent separating monodromy pairing; an ample polarization gives a positive definite symmetric form. The donor announces reduction of the deeper theorem to Jacobians.'
    # No automatic extraction is used to identify what an item is about.  These
    # associations were individually checked against the note and the sources.
    item_claims={
      201:[110,109,111,114],202:[110,112,113],203:[101,105,117,119],
      205:[139,130,131,132,133,134,135,136,137,138,141,142],
      206:[101,102,103,106],207:[104],208:[107],209:[108],210:[109,110],
      211:[111,112,113],212:[114,115,188],213:[116,189],214:[117,118,190,191],
      215:[119,120,123],216:[122,121,123,192],217:[124],218:[125],219:[126],
      220:[127,128],221:[196,129,193,194,195],223:[132,130,131,133],
      224:[134,135],225:[136,501],226:[137,138,197,198,199,502],227:[139,140],
      228:[141,142],229:[109,123],230:[109,116],231:[122],232:[127,128],
      233:[119,120],234:[114,115],235:[116,123],236:[116,119],
      237:[111,114,127],238:[114,115,120],239:[147,145],240:[145],241:[146],
      242:[145],243:[144],244:[147],245:[148],246:[149,151],247:[150],248:[149],
      249:[152],252:[153],253:[155,156,157,158],254:[159],255:[157,156],
      256:[161,155,158],257:[161],258:[155,158,161,150],259:[162],260:[163],
      261:[164],262:[165],264:[166],265:[167],266:[168],267:[169],268:[170],
      269:[171],270:[172],271:[173],272:[174],273:[172,173],274:[149,151,145],
      275:[153,167],276:[173,172],277:[153,154,173],278:[173,174],279:[172,173],
      280:[153,173],281:[173],282:[173],283:[153,173],284:[173],285:[175],
      286:[176],287:[177],288:[178],289:[179],290:[180],291:[183,182],292:[184],
      293:[185],294:[186],295:[187],296:[154],303:[173,174],
      305:[111,112,114,127],306:[111,112,114,127],307:[111,112,114,127],
      308:[109,114],309:[114,115],310:[109,114,173],311:[109,110,173],
      312:[116,119,192],313:[111,173],314:[122,123,124],
    }
    no_author=set(range(229,239))|set(range(273,285))|{303,314}|set(range(305,314))
    for n,nums in item_claims.items():
        source=[]
        for cn in nums:
            for x in C[cn]['source_passages']:
                if x not in source:source.append(x.copy())
        I[n]['source_passages']=source
        I[n]['lines']=fmt(source)
        I[n]['scans']=sorted({x['scan'] for x in source})
        if n in no_author:
            I[n]['his_words']=''
            I[n]['quote_passages']=[]
            I[n]['reconstruction']='No author statement asserts this comparison or diagnostic; the locators are manuscript anchors only. '+I[n]['reconstruction']
        else:
            I[n]['his_words']=C[nums[0]]['his_statement']
            I[n]['quote_passages']=[x.copy() for x in C[nums[0]]['quote_passages']]
    specific={
      204:(P,['417','682','1122'],['36-64']),
      222:(P,['636'],['413-414','610-615','638-644']),
      239:(Q,['263-278'],['200-222','301-345']),
      250:(Q,['739-757'],['685-704']),
      251:(Q,['105-108'],['699-704','722-735']),
      263:(Q,['1149-1167'],['1116-1147']),
      269:(Q,['1355-1362','1370-1374'],[]),
      298:(Q,['1057-1058'],[]),
      299:(Q,['1492'],['1322','1232','3-4']),
      300:(Q,['778','926','1062'],['781-795','928-953','958-982']),
      301:(Q,['644','1233-1234'],['646-664']),
      302:(Q,['779','1061'],[]),
      304:(P,['218'],['213-218']),
    }
    for n,(p,q,e) in specific.items():apply(I[n],p,q,e,field='his_words')
    I[297]['his_words']=''
    I[297]['lines']=f'{Q}_transcription.tex:2 (scan 189); 777 (scan 215 after absent 214); 1057-1058 (scan 224); 1491-1528 (scan 234)'
    I[297]['quote_passages']=[]
    I[297]['source_passages']=[{k:v for k,v in passage(Q,r).items() if k!='text'} for r in ['2','777','1057-1058','1491-1528']]
    I[297]['reconstruction']='Scan count and missing/blank-face observations are our inventory of the supplied transcription, not a quoted statement by the author.'
    # Every occurrence is refreshed AFTER all corrections, including newly added
    # claims.  This is the crucial correction to the former stale-copy defect.
    occurrence_count=0
    for problem in b.problems:
        for occurrence in problem['occurrences']:
            claim_id=occurrence.get('claim')
            if claim_id:
                c=C[int(claim_id.split('C')[1])]
                occurrence.update(cote=c['cote'],scans=c['scans'],lines=c['lines'],
                                  his_words=c['his_statement'])
                occurrence_count+=1
    rows=[]
    for objects,kind,key in [(b.claims,'claim','his_statement'),(b.items,'item','his_words')]:
        for obj in objects:
            for x in obj.get('quote_passages',[]):
                expected=passage(x['file'].replace('_transcription.tex',''),x['lines'])
                assert expected['text']==x['text'],obj['id']
            rows.append({'id':obj['id'],'record_type':kind,'quote_status':
                         'exact manually selected transcription passage(s)' if obj[key] else
                         'no author quotation; inventory, earlier-run idea or literature comparison',
                         'quote_locators':fmt(obj.get('quote_passages',[])),
                         'coverage_locators':obj['lines']})
    for problem in b.problems:
        for occurrence in problem['occurrences']:
            if 'claim' in occurrence:
                c=C[int(occurrence['claim'].split('C')[1])]
                assert occurrence['his_words']==c['his_statement']
                assert occurrence['lines']==c['lines']
    with (b.OUT/'quotation_audit.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print(f'Quotation audit: {len(C)} claims, {len(I)} items, {occurrence_count} problem occurrences. Exact source selections validated; no source text changed.')
    print('MP-SA08-30 primary claim quotation: '+C[103]['his_statement'])
