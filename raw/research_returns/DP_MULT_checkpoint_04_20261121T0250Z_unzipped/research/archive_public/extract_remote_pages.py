"""Extract selected pages of observed public PDFs with verified HTTP ranges.

This is an intermediate retrieval helper, not a mathematical deliverable.
Run using CODEX_PRIMARY_RUNTIME_PYTHON (pypdf is provided there).
Page arguments are one-based PDF page numbers; archive scan labels must be
verified visually rather than inferred from this numbering.
"""

import argparse
import io
import json
import re
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter, PageObject
from pypdf.generic import NameObject


class MissingRange(BaseException):
    """Stop rather than let PDF recovery trigger a whole-document download."""


class RangeReader(io.IOBase):
    def __init__(self, url, length, cache, offline=False):
        self.url = url
        self.length = length
        self.cache = Path(cache)
        self.cache.mkdir(exist_ok=True, parents=True)
        self.position = 0
        self.block = 262144
        self.offline = offline

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=0):
        base = (0, self.position, self.length)[whence]
        self.position = base + offset
        if self.position < 0:
            raise ValueError("Negative seek")
        return self.position

    def read(self, size=-1):
        if size is None or size < 0:
            raise MissingRange("Whole-stream fallback is intentionally disabled")
        end = min(self.position + size, self.length)
        chunks = []
        while self.position < end:
            start = self.position // self.block * self.block
            stop = min(start + self.block, self.length)
            target = self.cache / f"{start}-{stop - 1}.bin"
            if not target.exists() or target.stat().st_size != stop - start:
                if self.offline:
                    raise MissingRange(f"Uncached source bytes {start}-{stop-1}")
                partial = target.with_suffix(".partial")
                headers = target.with_suffix(".headers")
                subprocess.run([
                    "curl", "--location", "--fail", "--max-time", "35",
                    "--silent", "--show-error", "--range", f"{start}-{stop - 1}",
                    "--dump-header", str(headers), "--output", str(partial), self.url,
                ], check=True)
                hs = headers.read_text().lower()
                expected = f"content-range: bytes {start}-{stop-1}/{self.length}"
                if expected not in hs or partial.stat().st_size != stop - start:
                    raise ValueError(f"Unexpected HTTP range response for {start}-{stop-1}")
                partial.replace(target)
                print(json.dumps({"retrieved": self.url, "range": [start, stop - 1]}), flush=True)
            data = target.read_bytes()
            take = min(end, stop) - self.position
            off = self.position - start
            chunks.append(data[off:off + take])
            self.position += take
        return b"".join(chunks)


def page_by_tree(reader, index):
    """Find one page without flattening and reading every page dictionary."""
    def descend(ref, i, inherited):
        node = ref.get_object()
        inherited = dict(inherited)
        for key in ("/Resources", "/MediaBox", "/CropBox", "/Rotate"):
            if key in node:
                inherited[key] = node.raw_get(key)
        if node.get("/Type") == "/Page":
            if i != 0:
                raise IndexError(index)
            page = PageObject(reader, ref)
            for key, value in inherited.items():
                if key not in page:
                    page[NameObject(key)] = value
            return page
        for child in node["/Kids"]:
            child_dict = child.get_object()
            count = int(child_dict.get("/Count", 1))
            if i < count:
                return descend(child, i, inherited)
            i -= count
        raise IndexError(index)
    return descend(reader.root_object.raw_get("/Pages"), index, {})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cote", type=int)
    parser.add_argument("length", type=int)
    parser.add_argument("pages", type=int, nargs="+")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    url = f"https://grothendieck.umontpellier.fr/{args.cote}.pdf"
    stream = RangeReader(url, args.length, here / f"range_cache_{args.cote}", args.offline)
    reader = PdfReader(stream, strict=True)
    writer = PdfWriter()
    for page in args.pages:
        writer.add_page(page_by_tree(reader, page - 1))
    tag = "_".join(map(str, args.pages))
    output = here / f"cote{args.cote}_pdfpages_{tag}.pdf"
    with output.open("wb") as out:
        writer.write(out)
    check = PdfReader(output, strict=True)
    assert len(check.pages) == len(args.pages)
    print(json.dumps({"output": str(output), "original_pdf_pages": args.pages,
                      "original_url": url,
                      "page_count": int(reader.root_object["/Pages"]["/Count"])}), flush=True)


if __name__ == "__main__":
    main()
