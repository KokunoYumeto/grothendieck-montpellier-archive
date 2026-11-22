"""Read selected pages from the public Montpellier PDF using HTTP ranges.

Research-only source excerpt; do not include this copyrighted source in delivery.
"""
import io
import urllib.request
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from pypdf.generic import NameObject


class RangeFile(io.RawIOBase):
    def __init__(self, url, length, block=262144):
        self.url = url
        self.length = length
        self.block = block
        self.pos = 0
        self.cache = {}
        self.cache_dir = Path(__file__).with_name("archive1_ranges")
        self.cache_dir.mkdir(exist_ok=True)

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        base = (0, self.pos, self.length)[whence]
        self.pos = base + offset
        if self.pos < 0:
            raise ValueError("negative seek")
        return self.pos

    def get_block(self, number):
        if number not in self.cache:
            lo = number * self.block
            hi = min(self.length - 1, lo + self.block - 1)
            saved = self.cache_dir / f"{lo}-{hi}.bin"
            if saved.exists():
                data = saved.read_bytes()
            else:
                req = urllib.request.Request(self.url, headers={"Range": f"bytes={lo}-{hi}"})
                with urllib.request.urlopen(req, timeout=20) as response:
                    if response.status != 206:
                        raise RuntimeError(f"Expected partial response, got {response.status}")
                    expected = f"bytes {lo}-{hi}/{self.length}"
                    if response.headers.get("Content-Range") != expected:
                        raise RuntimeError("wrong partial-response position")
                    data = response.read()
                saved.write_bytes(data)
            if len(data) != hi - lo + 1:
                raise RuntimeError("incomplete partial response")
            self.cache[number] = data
            print(f"Fetched bytes {lo}-{hi}; blocks {len(self.cache)}", flush=True)
        return self.cache[number]

    def read(self, size=-1):
        if size < 0:
            size = self.length - self.pos
        end = min(self.length, self.pos + size)
        out = bytearray()
        while self.pos < end:
            number, at = divmod(self.pos, self.block)
            data = self.get_block(number)
            take = min(end - self.pos, len(data) - at)
            out.extend(data[at:at + take])
            self.pos += take
        return bytes(out)


source = RangeFile("https://grothendieck.umontpellier.fr/1.pdf", 84267714)
reader = PdfReader(source, strict=True)
page_root = reader.trailer["/Root"]["/Pages"]
print(f"Original page count: {page_root['/Count']}; root children: {len(page_root['/Kids'])}", flush=True)


def selected_page(reference, index, inherited=None):
    """Target this scanned document's page tree without reader.pages flattening.

    The equal-count leaf shortcut is checked against the actual scanned footer
    after rendering. It is an extraction optimization, not a generic PDF parser.
    """
    node = reference.get_object()
    inherited = dict(inherited or {})
    for key in ("/Resources", "/MediaBox", "/CropBox", "/Rotate"):
        if key in node:
            inherited[NameObject(key)] = node.raw_get(key)
    if node["/Type"] == "/Page":
        if index:
            raise RuntimeError("bad leaf index")
        page = PageObject(reader, reference)
        page.update(inherited)
        page.update(node)
        return page
    kids = node["/Kids"]
    if int(node["/Count"]) == len(kids):
        child = kids[index]
        if child.get_object()["/Type"] == "/Page":
            return selected_page(child, 0, inherited)
    for child in kids:
        obj = child.get_object()
        count = 1 if obj["/Type"] == "/Page" else int(obj["/Count"])
        if index < count:
            return selected_page(child, index, inherited)
        index -= count
    raise IndexError("page outside tree")


writer = PdfWriter()
selected_scans = tuple(map(int, sys.argv[1:])) or (79, 80, 111, 112)
for archive_scan in selected_scans:
    writer.add_page(selected_page(page_root, archive_scan))
    print(f"Added archive scan {archive_scan}", flush=True)
suffix = "_".join(map(str, selected_scans))
dest = Path(__file__).with_name(f"archive_1_selected_{suffix}.pdf")
with dest.open("wb") as stream:
    writer.write(stream)
print(str(dest), dest.stat().st_size, flush=True)
