#!/bin/sh
# English layer of the second-pass pages, package by package in priority order, Flex only (no other tier, no fallback).
# A package starts only if this job's measured spend plus the package's estimate stays within CAP.
# 17 Nov 2026, Claude Opus 5.5 at effort high.
R=/c/Users/user/Documents/grothendieck_archive_transcription_20261110/translations_en_20261117
A=/c/Users/user/Documents/olp_status_20261115/api_finish_20261117/api
CAP=${CAP:-7.5}; RATE=${RATE:-8.6}
cd $R
for pkg in $(cut -f5 _work2/files.tsv | tail -n +2 | awk '!s[$0]++'); do
  ids=$(awk -F'\t' -v p="$pkg" '$5==p{print $1}' _work2/files.tsv | tr '\n' ' ')
  [ -z "$ids" ] && continue
  ok=$(python -I -B -c "
import json,pathlib,csv,sys
st=json.load(open('_work2/runs/state.json')) if pathlib.Path('_work2/runs/state.json').exists() else {}
spent=sum(((v.get('input_tokens',0)-v.get('cached_tokens',0))+0.1*v.get('cached_tokens',0)+5*v.get('output_tokens',0))/1e6 for v in st.values())
b=sum(int(r['bytes']) for r in csv.DictReader(open('_work2/files.tsv',encoding='utf-8'),delimiter='\t') if r['package']=='$pkg' and st.get(r['id'],{}).get('status')!='completed')
est=b/1e6*$RATE
print('yes' if spent+est<=$CAP else 'no', round(spent,3), round(est,3))")
  echo "$(date +%H:%M) $pkg: $ok" >> _work2/layer.log
  case "$ok" in yes*) ;; *) echo "$(date +%H:%M) STOP at $pkg (cap \$$CAP)" >> _work2/layer.log; break;; esac
  sh $A/scripts/flexloop.sh $R _work2 120 $ids >> _work2/layer.log 2>&1
done
echo "$(date +%H:%M) DONE" >> _work2/layer.log
