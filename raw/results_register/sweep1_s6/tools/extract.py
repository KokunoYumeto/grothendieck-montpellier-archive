"""Sweep 1, scope s6: compact dumps of the S6 rows of REGISTER.tsv for reading (read-only on the register).
Written by Claude Opus 5.5 at effort max (sweep 1, scope s6), 18 Nov 2026."""
import csv, sys, os, re, collections
csv.field_size_limit(10**9)
REG = r'C:/Users/user/Documents/results_register'
W = r'C:/Users/user/Documents/s6_pro_prompts_20261112_work'
CP35 = W + '/returns/S6_06_BLIND_checkpoint_35_20261118T1208Z_unzipped/S6_06_BLIND/S6_06_BLIND_results.csv'
S6 = ['S6_01_INVARIANTS','S6_02_FAMILY','S6_02_PUSH','S6_03_CDP','S6_04_MAPS_MANIFOLDS','S6_05_ARITHMETIC','S6_06_BLIND','Q03_DEPOSIT']
def load():
    rows = [r for r in csv.DictReader(open(REG+'/REGISTER.tsv', encoding='utf-8'), delimiter='\t') if r['run'] in S6]
    cp = {r['id']: r for r in csv.DictReader(open(CP35, encoding='utf-8'))}
    flags = [r for r in csv.DictReader(open(REG+'/FLAGS.tsv', encoding='utf-8'), delimiter='\t') if r['tag'].split(':')[0] in S6]
    edges = [r for r in csv.DictReader(open(REG+'/EDGES.tsv', encoding='utf-8'), delimiter='\t') if r['from'].split(':')[0] in S6 or r['to'].split(':')[0] in S6]
    led = collections.defaultdict(list)
    for r in csv.DictReader(open(W+'/S6_10_REVISION/S6_CHECK_LEDGER.tsv', encoding='utf-8'), delimiter='\t'):
        led[(r['source_run'], r['source_id'])].append(r)
    return rows, cp, flags, edges, led
if __name__ == '__main__':
    rows, cp, flags, edges, led = load()
    out = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    os.makedirs(out, exist_ok=True)
    for run in S6:
        with open(f'{out}/{run}.txt', 'w', encoding='utf-8') as f:
            for r in rows:
                if r['run'] != run: continue
                st = re.sub(r'\s+', ' ', r['statement'])[:n]
                dep = re.sub(r'\s+', ' ', r['depends_on'])[:80]
                extra = ''
                if run == 'S6_06_BLIND' and r['id'] in cp:
                    c = cp[r['id']]; extra = f" |cmp:{c['stated_value_compared (run and id)'][:60]}/{c['agrees_with_stated_value'][:12]} |item:{c['item_of_the_prompt'][:20]}"
                f.write(f"{r['id']}|{r['status_raw'][:12]}|{st}|dep:{dep}{extra}\n")
    print(collections.Counter(r['flag'][:30] for r in flags), len(edges))
