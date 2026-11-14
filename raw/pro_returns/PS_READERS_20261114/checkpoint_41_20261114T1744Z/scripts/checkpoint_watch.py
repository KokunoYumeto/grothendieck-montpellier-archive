"""Persist complete immutable checkpoints at each ten-page milestone or hour.

The transfer helper is obtained from the Library skill in the execution session;
it is a runtime dependency, not part of the edition or a supplied source.
"""
from pathlib import Path
import json,subprocess,time,sys
P=Path(__file__).resolve().parents[1];W=P.parent
state=json.loads((P/'records/CHECKPOINT_STATE.json').read_text())
last_count=len(list((P/'checked_pages').glob('*.tex')))
last_time=time.monotonic()
history=P/'records/CHECKPOINT_HISTORY.jsonl'
print(json.dumps({'watching':True,'initial_checked_pages':last_count}),flush=True)
while not (P/'logs/STOP_CHECKPOINT_WATCHER').exists():
    count=len(list((P/'checked_pages').glob('*.tex')))
    if count>=last_count+10 or time.monotonic()-last_time>=3500:
        time.sleep(2)
        result=subprocess.run([sys.executable,str(P/'scripts/checkpoint.py')],cwd=W,capture_output=True,text=True)
        if result.returncode:
            print(json.dumps({'checkpoint_creation_failed':True}),flush=True);time.sleep(15);continue
        snap=json.loads(result.stdout.strip().splitlines()[-1]);filename=snap['checkpoint']
        request={'uploads':[{'local_path':str(W/filename),'purpose':'create_library_file','library_artifact_type':'other'}]}
        transfer=subprocess.run([sys.executable,str(W/'.ps_library_helpers/library_upload.py')],input=json.dumps(request),cwd=W,capture_output=True,text=True)
        record={'checkpoint':filename,'checked_pages':snap['checked_pages'],'sha256':snap['sha256'],'saved':False}
        for line in reversed(transfer.stdout.splitlines()):
            try:reply=json.loads(line)
            except ValueError:continue
            if 'results' in reply:
                item=reply['results'][0];record['saved']=item.get('status')=='succeeded';record['library_file_id']=item.get('library_file_id');break
        with history.open('a') as f:f.write(json.dumps(record)+'\n')
        print(json.dumps(record),flush=True)
        if not record['saved']:
            print('Automatic checkpoint save failed; the complete ZIP remains locally available.',flush=True)
            break
        last_count=snap['checked_pages'];last_time=time.monotonic()
    time.sleep(5)
