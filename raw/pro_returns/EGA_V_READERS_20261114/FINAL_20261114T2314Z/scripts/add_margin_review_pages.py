"""Add four-row note pages to existing review sets without changing PDF bytes."""
import json
from pdf_review import EDITION,lock,manifest_path,rows,FREEZES,write_table,filehash


def main():
    additions=[]
    with lock():
        for path in sorted((EDITION/'build').glob('*/audit/report.json')):
            report=json.loads(path.read_text());name=report['reader']
            pdf=path.parents[1]/(name+'.pdf')
            if not pdf.is_file() or filehash(pdf)!=report.get('pdf_sha256'):continue
            keys={r['key'] for r in report.get('margin_content_routes',[]) if r['measured_lines']==4}
            report['margin_line_limit_review_source_keys']=sorted(keys)
            required=set(report.get('required_visual_review_pages',[]));prior=set(required)
            starts=report.get('source_physical_pages',{})
            ordered=sorted(starts.values())
            for key in keys:
                if key not in starts:continue
                begin=starts[key];following=[n for n in ordered if n>begin]
                end=min(following)-1 if following else report['pdf_pages']
                for number in range(begin,end+1):
                    required.add(number)
                    if number not in prior:additions.append(dict(reader=name,pdf_sha256=report['pdf_sha256'],pdf_page=number,source_key=key,reason='Four measured rows at margin width: explicitly inspect the required body placement after the line-limit repair.'))
            report['required_visual_review_pages']=sorted(required)
            path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
            manifest=manifest_path(name,report['pdf_sha256'])
            if manifest.is_file():
                data=json.loads(manifest.read_text());data['required_visual_review_pages']=sorted(required)
                data['margin_line_limit_review_source_keys']=sorted(keys)
                manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        ledger=EDITION/'records/MARGIN_REVIEW_ADDITIONS.tsv'
        if additions:write_table(ledger,rows(ledger)+additions)
    print(json.dumps(dict(added_review_pages=additions)))

if __name__=='__main__':main()
