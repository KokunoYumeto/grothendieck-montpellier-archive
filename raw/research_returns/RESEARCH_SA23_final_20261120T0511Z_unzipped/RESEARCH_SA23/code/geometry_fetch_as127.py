"""Retrieve a publicly indexed primary seminar scan; retain status and timing."""
from pathlib import Path
from time import perf_counter
from urllib.request import urlopen

url='https://yhzhumath.github.io/Mordell2024/AS-127.pdf'
out=Path(__file__).resolve().parents[1]/'notes'/'geometry_AS127.pdf'
t=perf_counter()
try:
    with urlopen(url, timeout=180) as response:
        data=response.read()
    assert data.startswith(b'%PDF')
    out.write_bytes(data)
    print(url, len(data), 'bytes', round(perf_counter()-t,2), 'seconds')
except Exception as exc:
    print(type(exc).__name__, str(exc), round(perf_counter()-t,2), 'seconds')
