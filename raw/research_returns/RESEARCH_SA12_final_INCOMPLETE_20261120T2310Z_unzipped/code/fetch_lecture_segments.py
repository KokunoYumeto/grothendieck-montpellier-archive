"""Download only the public CC-BY lecture interval needed for source checking.

The public streaming URL is read from the source page, never put in logs.
No account credentials or private endpoints are used.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import json, re, time, subprocess

root = Path(__file__).resolve().parents[1]
folder = root / 'sources/GO2008'
dest = folder / 'lecture_segments'
dest.mkdir(exist_ok=True)
html = (folder / 'Gabber2015_page.html').read_text()
base = re.findall(r'https?[^"<> ]+\.m3u8[^"<> ]*', html)[0]
start, finish = 1885, 2025
started = time.perf_counter()

def fetch(url, byte_range=None):
    error = None
    for attempt in range(3):
        try:
            headers = {'User-Agent':'Mozilla/5.0'}
            limit = 2_000_000
            if byte_range is not None:
                offset, length = byte_range
                headers['Range'] = f'bytes={offset}-{offset+length-1}'
                limit = length
            with urlopen(Request(url, headers=headers), timeout=25) as r:
                if byte_range is not None and r.status != 206:
                    raise RuntimeError('Server did not honor the HLS byte range; no body downloaded.')
                data = r.read(limit+1)
                if len(data)>limit:
                    raise RuntimeError('Response exceeded the expected byte range or manifest size.')
                return data
        except Exception as exc:
            error = exc
    raise error

def prepare(name, playlist):
    url = urljoin(base, playlist)
    lines = fetch(url).decode().splitlines()
    elapsed = 0.0
    duration = None
    current_range = None
    next_offset = 0
    chosen = []
    init = None
    for line in lines:
        if line.startswith('#EXT-X-MAP:'):
            uri = re.search(r'URI="([^"]+)"', line).group(1)
            match = re.search(r'BYTERANGE="(\d+)@(\d+)"', line)
            brange = (int(match.group(2)),int(match.group(1))) if match else None
            init = (uri,brange)
        elif line.startswith('#EXT-X-BYTERANGE:'):
            value = line.split(':',1)[1]
            parts = value.split('@')
            length = int(parts[0])
            offset = int(parts[1]) if len(parts)>1 else next_offset
            current_range = (offset,length)
            next_offset = offset+length
        elif line.startswith('#EXTINF:'):
            duration = float(line.split(':',1)[1].split(',')[0])
        elif line and not line.startswith('#') and duration is not None:
            if elapsed + duration > start and elapsed < finish:
                chosen.append((duration, line, current_range))
            elapsed += duration
            duration = None
            current_range = None
    jobs = []
    output = ['#EXTM3U','#EXT-X-VERSION:6','#EXT-X-TARGETDURATION:20','#EXT-X-MEDIA-SEQUENCE:0']
    if init:
        local = name + '_init.mp4'
        jobs.append((urljoin(url, init[0]), local, init[1]))
        output.append('#EXT-X-MAP:URI="'+local+'"')
    for i, (duration, remote, brange) in enumerate(chosen):
        local = f'{name}_{i:03d}.m4s'
        jobs.append((urljoin(url, remote), local, brange))
        output.extend([f'#EXTINF:{duration},',local])
    output.append('#EXT-X-ENDLIST')
    (dest / f'{name}.m3u8').write_text('\n'.join(output)+'\n')
    return jobs, {'kind':name,'segments':len(chosen),'seconds':sum(d for d,_,_ in chosen)}

jobs = []
stats = []
for name, playlist in [('video','20247-hls_5.m3u8'),('audio','20247-hls_1.m3u8')]:
    more, stat = prepare(name, playlist)
    jobs.extend(more)
    stats.append(stat)

def one(job):
    url, local, brange = job
    path = dest / local
    if not path.exists():
        path.write_bytes(fetch(url,brange))
    return path.stat().st_size

with ThreadPoolExecutor(max_workers=8) as pool:
    sizes = list(pool.map(one, jobs))

out = folder / 'Gabber2015_excerpt.mp4'
cmd = ['ffmpeg','-y','-loglevel','error','-protocol_whitelist','file,crypto,data',
       '-i',str(dest/'video.m3u8'),'-i',str(dest/'audio.m3u8'),
       '-c','copy','-shortest',str(out)]
result = subprocess.run(cmd,capture_output=True,text=True,timeout=60)
log = {'source':'https://av.tib.eu/media/20247','source_start_seconds':start,
       'requested_end_seconds':finish,'streams':stats,'bytes_downloaded':sum(sizes),
       'seconds':time.perf_counter()-started,'returncode':result.returncode,
       'stderr':result.stderr}
(root/'code/output/Gabber2015_segments.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log,indent=2))
