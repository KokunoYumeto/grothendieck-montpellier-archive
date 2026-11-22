"""Extract a brief public CC-BY lecture segment for source verification."""
from pathlib import Path
import re,json,subprocess,time
root=Path(__file__).resolve().parents[1]
folder=root/'sources/GO2008'
html=(folder/'Gabber2015_page.html').read_text()
url=re.findall(r'https?[^"<> ]+\.m3u8[^"<> ]*',html)[0]
t=time.perf_counter()
args=['ffmpeg','-y','-loglevel','error','-ss','00:31:25','-i',url,'-t','00:02:20','-vf','scale=960:-2','-c:v','libx264','-preset','ultrafast','-crf','27','-c:a','aac',str(folder/'Gabber2015_excerpt.mp4')]
p=subprocess.run(args,capture_output=True,text=True)
log={'start':'00:31:25','duration':'00:02:20','source':'https://av.tib.eu/media/20247','returncode':p.returncode,'seconds':time.perf_counter()-t,'stderr':re.sub(r'https?://\S+','[public media URL]',p.stderr)}
(root/'code/output/Gabber2015_excerpt.json').write_text(json.dumps(log,indent=2)+'\n')
print({k:v for k,v in log.items() if k!='stderr'})
if p.returncode:print(log['stderr'][-1500:])

