"""Stop this task's own OCR process after detecting OpenMP oversubscription."""
import psutil
for p in psutil.process_iter(['pid','cmdline']):
    cmd=p.info['cmdline'] or []
    if len(cmd)>1 and cmd[1]=='SA08_work/programs/ocr_reference.py':
        print('Stopping task OCR',p.pid)
        for c in p.children(recursive=True):c.terminate()
        p.terminate()
