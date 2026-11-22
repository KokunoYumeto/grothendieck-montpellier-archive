"""Extract three cited archive pages using HTTP ranges, avoiding a full scan download."""
from pathlib import Path
from urllib.request import Request, urlopen
import io

from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from pypdf.generic import NameObject

BASE = Path(__file__).resolve().parents[1]
URL = "https://grothendieck.umontpellier.fr/43.pdf"
SIZE = 78615706
PREFIX = BASE / "sources/Montpellier43.partial"


class RangeReader(io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.blocksize = 262144
        self.cache = {}

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        self.pos = offset if whence == 0 else self.pos + offset if whence == 1 else SIZE + offset
        if self.pos < 0:
            raise ValueError("negative position")
        return self.pos

    def getblock(self, index):
        if index not in self.cache:
            start = index * self.blocksize
            end = min(SIZE, start + self.blocksize)
            if PREFIX.exists() and PREFIX.stat().st_size >= end:
                with PREFIX.open("rb") as f:
                    f.seek(start)
                    data = f.read(end - start)
            else:
                req = Request(URL, headers={"Range": f"bytes={start}-{end-1}"})
                with urlopen(req, timeout=40) as response:
                    if response.status != 206:
                        raise RuntimeError("server did not honor range")
                    data = response.read()
                print(f"Fetched block {index}: {len(data)} bytes", flush=True)
            if len(data) != end - start:
                raise IOError("short HTTP range")
            self.cache[index] = data
        return self.cache[index]

    def read(self, size=-1):
        if size < 0:
            size = SIZE - self.pos
        end = min(SIZE, self.pos + size)
        chunks = []
        while self.pos < end:
            index, within = divmod(self.pos, self.blocksize)
            block = self.getblock(index)
            count = min(end - self.pos, len(block) - within)
            chunks.append(block[within:within+count])
            self.pos += count
        return b"".join(chunks)


reader = PdfReader(RangeReader(), strict=True)
pages_root = reader.root_object["/Pages"]
print(f"Page count: {pages_root['/Count']}; root children: {len(pages_root['/Kids'])}", flush=True)


def select_page(node_ref, index, inherited=None):
    node = node_ref.get_object()
    inherited = dict(inherited or {})
    for key in ("/Resources", "/MediaBox", "/CropBox", "/Rotate"):
        if key in node:
            inherited[key] = node[key]
    if node.get("/Type") == "/Page":
        if index:
            raise IndexError(index)
        page = PageObject(reader, node_ref)
        page.update(node)
        for key, value in inherited.items():
            if key not in page:
                page[NameObject(key)] = value
        return page
    kids = node["/Kids"]
    if len(kids) == node["/Count"]:
        return select_page(kids[index], 0, inherited)
    for child in kids:
        child_node = child.get_object()
        count = child_node.get("/Count", 1)
        if index < count:
            return select_page(child, index, inherited)
        index -= count
    raise IndexError(index)


writer = PdfWriter()
for number in (64, 65, 66):
    page = select_page(reader.root_object.raw_get("/Pages"), number - 1)
    writer.add_page(page)
    print(f"Added scan {number}", flush=True)
target = BASE / "sources/Montpellier43_scans64_66.pdf"
with target.open("wb") as f:
    writer.write(f)
print(f"Saved {target}: {target.stat().st_size} bytes", flush=True)
