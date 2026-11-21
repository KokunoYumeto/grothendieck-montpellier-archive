"""Read selected pages from a range-capable primary PDF without a full download.

Usage: python range_pdf.py URL OUT.pdf FIRST_INDEX LAST_INDEX [HEAD_CACHE]
Indices are zero based and inclusive. Cache files are expendable source bytes.
"""
import concurrent.futures
import io
import pathlib
import sys
import threading
import urllib.request

from pypdf import PdfReader, PdfWriter


class RangeFile(io.RawIOBase):
    def __init__(self, url, head_cache=None):
        self.url = url
        self.pos = 0
        self.block = 65536
        self.cache = {}
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=6)
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"Range": "bytes=0-1023"}), timeout=45)
        if r.status != 206:
            raise RuntimeError("Server did not honor byte range")
        self.length = int(r.headers["Content-Range"].split("/")[-1])
        print("source_length", self.length, flush=True)
        r.close()
        if head_cache:
            data = pathlib.Path(head_cache).read_bytes()
            for i in range(len(data) // self.block):
                self.cache[i] = data[i*self.block:(i+1)*self.block]

    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos

    def seek(self, offset, whence=0):
        self.pos = offset if whence == 0 else (self.pos if whence == 1 else self.length) + offset
        if self.pos < 0: raise ValueError("negative seek")
        return self.pos

    def fetch(self, i):
        print("fetch_block", i, flush=True)
        lo = i*self.block
        hi = min(self.length-1, lo+self.block-1)
        request = urllib.request.Request(self.url, headers={"Range": f"bytes={lo}-{hi}"})
        for trial in range(3):
            try:
                with urllib.request.urlopen(request, timeout=60) as r:
                    if r.status != 206: raise RuntimeError("range response lost")
                    data = r.read()
                if len(data) != hi-lo+1: raise RuntimeError("short byte range")
                self.cache[i] = data
                return
            except Exception:
                if trial == 2: raise

    def read(self, n=-1):
        if n is None or n < 0: n = self.length-self.pos
        end = min(self.length, self.pos+n)
        if end <= self.pos: return b""
        indices = range(self.pos//self.block, (end-1)//self.block+1)
        missing = [i for i in indices if i not in self.cache]
        list(self.pool.map(self.fetch, missing))
        start = self.pos
        data = b"".join(self.cache[i] for i in indices)
        self.pos = end
        offset = start % self.block
        return data[offset:offset+end-start]


if __name__ == "__main__":
    url, out, lo, hi, *head = sys.argv[1:]
    remote = RangeFile(url, head[0] if head else None)
    reader = PdfReader(remote)
    print("pages", len(reader.pages), "bytes", remote.length, flush=True)
    writer = PdfWriter()
    for i in range(int(lo), int(hi)+1):
        writer.add_page(reader.pages[i])
        print("page", i, "cached_blocks", len(remote.cache), flush=True)
    with open(out, "wb") as f: writer.write(f)
    print("saved", out, "source_bytes", sum(map(len, remote.cache.values())), flush=True)
