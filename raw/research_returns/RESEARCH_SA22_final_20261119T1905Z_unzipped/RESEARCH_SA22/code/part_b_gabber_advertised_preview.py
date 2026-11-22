#!/usr/bin/env python3
"""Inspect normal Gabber publisher metadata for explicitly advertised previews.

Only an actually advertised page-one preview may be followed. The subscription
PDF is not requested, and no page, permission, or preview parameter is changed.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import gzip, hashlib, json, time

root = Path(__file__).resolve().parents[1]
started = time.monotonic()
records = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and key in ('href', 'src', 'data-src'):
                self.urls.append((tag, key, value))

def fetch(url, purpose):
    begin = time.monotonic()
    record = {'url': url, 'purpose': purpose}
    payload = None
    try:
        with urlopen(Request(url, headers={'User-Agent':'ResearchSourceAudit/1.0'}), timeout=25) as response:
            payload = response.read(5*1024*1024+1)
            record.update(http_status=response.status, bytes=len(payload),
                          final_url=response.url,
                          content_type=response.headers.get('Content-Type', ''))
        if payload[:2] == b'\x1f\x8b':
            payload = gzip.decompress(payload)
        if len(payload) > 5*1024*1024:
            record['status'] = 'Response cap reached; not inspected'
            payload = None
        else:
            record['status'] = 'Public response received'
    except Exception as error:
        record.update(status='Request failed; no bypass or retry', error=str(error))
    record['elapsed_seconds'] = time.monotonic()-begin
    records.append(record)
    return record, payload

landing, payload = fetch('https://link.springer.com/article/10.1007/BF02773001',
                         'Inspect normal metadata HTML for an advertised public preview')
if payload is not None:
    text = payload.decode('utf8', 'replace')
    (root/'sources/part_b_gabber_preview_landing.html').write_text(text)
    parser = Page()
    parser.feed(text)
    links = sorted(set(urljoin(landing['final_url'], value)
                       for tag, key, value in parser.urls
                       if 'page-one.springer.com/pdf/preview/' in value))
    landing['advertised_public_preview_links'] = links
    landing['preview_mentions'] = [text[max(0, pos-150):pos+400]
        for pos in [text.find('page-one'), text.find('pdf/preview'), text.find('Look Inside')]
        if pos >= 0]
    if not links:
        landing['status'] = 'No advertised page-one PDF preview found in actual HTML; no guessed endpoint or subscription PDF requested'
    else:
        preview, data = fetch(links[0], 'Follow exact advertised public preview URL')
        if data is not None:
            if not data.startswith(b'%PDF'):
                preview['status'] = 'Response is not PDF; no mathematical original read'
                (root/'sources/part_b_gabber_preview_nonpdf.html').write_bytes(data)
            else:
                path = root/'sources/part_b_gabber_preview.pdf'
                path.write_bytes(data)
                import fitz
                doc = fitz.open(path)
                extracted = '\n'.join(page.get_text() for page in doc)
                (root/'sources/part_b_gabber_preview.txt').write_text(extracted)
                preview.update(status='Original PDF preview fetched; visual inspection required',
                               pages=len(doc), sha256=hashlib.sha256(data).hexdigest(),
                               text_characters=len(extracted))

output = {'records': records, 'elapsed_seconds': time.monotonic()-started}
(root/'code/part_b_gabber_advertised_preview_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
