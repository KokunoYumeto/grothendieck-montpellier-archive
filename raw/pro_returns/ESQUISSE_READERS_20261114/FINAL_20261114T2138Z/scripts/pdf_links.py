"""Map every URI annotation rectangle to its embedded logical-link identifier."""
import collections

def external_link_groups(doc):
    groups={};issues=[];annotations=[]
    for i,page in enumerate(doc):
        for link in page.get_links():
            if not link.get('uri'):continue
            kind,ident=doc.xref_get_key(link['xref'],'EsquisseLinkID')
            annotation={'pdf_page':i+1,'xref':link['xref'],'uri':link['uri'],'rectangle':list(link['from']),'logical_id':ident if kind=='string' else None}
            annotations.append(annotation)
            if kind!='string' or not ident.startswith('edlink-'):
                issues.append({'problem':'URI annotation lacks a logical-link identifier','pdf_page':i+1,'xref':link['xref']});continue
            group=groups.setdefault(ident,{'id':ident,'uri':link['uri'],'rectangles':[]})
            if group['uri']!=link['uri']:issues.append({'problem':'One logical identifier has differing URI targets','id':ident})
            group['rectangles'].append(annotation)
    return {'logical_links':list(groups.values()),'annotation_rectangles':annotations,'issues':issues}
