"""Merge statement/event tables; retain specific evidence descriptions."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
allowed = {'targeted proof check', 'independent re-proof',
           'computation or formal certificate', 'used and rechecked in this run',
           'carried as background without fault found'}
for filename, delimiter in [('RESEARCH_SA21_results.csv', ','), ('CHECK_EVENTS.tsv', '\t')]:
    name = 'results.csv' if filename.endswith('.csv') else filename
    sources = sorted((root/'parts').glob('*/'+name)) + sorted((root/'parts').glob('*/supports_'+name))
    if delimiter == '\t':
        sources += sorted((root/'parts').glob('*/cross_CHECK_EVENTS.tsv'))
    allrows = []
    header = None
    for source in sources:
        with source.open(newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            source_header = next(reader)
            if header is None:
                header = source_header[:5] if delimiter == '\t' else source_header
            assert source_header[:len(header)] == header, (source, source_header, header)
            for row in reader:
                if len(row) > len(header):
                    row[len(header)-1] += '; ' + '; '.join(row[len(header):])
                if delimiter == '\t':
                    # A source check is not relabelled as a mathematical proof.
                    recorded_type = row[3]
                    if recorded_type not in allowed and not recorded_type.startswith('refuted,'):
                        row[3] = 'targeted proof check' if recorded_type.startswith('targeted proof check') else 'used and rechecked in this run'
                        row[4] = 'Recorded check detail: ' + recorded_type + '. ' + row[4]
                allrows.append(row[:len(header)])
    with (root/filename).open('w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(header or [])
        writer.writerows(allrows)
print('Merged per-part tables')
