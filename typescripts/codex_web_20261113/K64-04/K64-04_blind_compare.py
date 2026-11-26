"""Compare the blind image log with the checked TeX passages. Run beside the page files."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
ID='K64-04'
def read(name):
    with (ROOT/(ID+'_'+name)).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
def fmt(s):
    return s.replace('|',r'\|').replace('\n',' ').replace('\x60','′')
def main():
    blind=read('blind.tsv');key=read('blind_key.tsv')
    assert len(blind)==len(key)
    report=['# Blind comparison, cote 64, scans 40–52','',
            'The blind record was written from the scans before the corresponding first-pass page file was reopened. Its wording includes descriptions of ink, so a literal character difference need not be a different reading. The comparison key pairs those observations with first-pass TeX excerpts, the reading on which the comparison turned, and a literal passage in the delivered page file.','']
    table=[];same=0
    for obs,k in zip(blind,key):
        assert (obs['scan'],obs['place'])==(k['scan'],k['place'])
        page=(ROOT/'pages'/f"{ID}_64_scan{int(k['scan']):03d}.tex").read_text(encoding='utf8')
        if k['delivered_passage'] not in page:
            raise ValueError(f"Missing expected page passage at {k['scan']} / {k['place']}")
        if k['comparison']=='agreement':
            same+=1
        else:
            assert k['resolution'] and k['first_reading']
            table.append('| '+' | '.join(map(fmt,[k['scan'],k['place'],k['first_reading'],obs['what_the_crop_shows'],k['resolution'],k['delivered_passage']]))+' |')
    report.extend([f'{len(key)} places compared. {same} agreed on the reading. {len(table)} had a different reading, level of certainty, or treatment of a cancellation.','',
                  '| Scan | Place | First reading | Blind observation | Decision on the crop, before the witness | Delivered TeX passage |','|---|---|---|---|---|---|',*table,''])
    (ROOT/(ID+'_blind_compare.md')).write_text('\n'.join(report),encoding='utf8',newline='\n')
    print(f'{len(key)} paired places, {len(table)} differences, {same} agreements. All TeX passages located.')
if __name__=='__main__':main()
