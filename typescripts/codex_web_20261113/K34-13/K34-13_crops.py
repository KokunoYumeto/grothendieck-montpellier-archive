"""Recreate the individual doubt crops from the supplied scan archive."""
import argparse
import io
import re
from pathlib import Path
from zipfile import ZipFile
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent
BOX = re.compile(r'`(\d{3}\.\d+-[a-zA-Z0-9_-]+\.jpg)` \((\d+), (\d+), (\d+), (\d+)\)')

def restore(archive, dest):
    register = (ROOT / 'K34-13_doubts.md').read_text(encoding='utf-8')
    table = register.split('## Witness check', 1)[1]
    entries = BOX.findall(table)
    assert entries and len(entries) == len({entry[0] for entry in entries})
    dest.mkdir(parents=True, exist_ok=True)
    with ZipFile(archive) as source:
        current = None
        for filename, *bounds in entries:
            scan = filename[:3]
            if current != scan:
                filename_in_archive = f'K34-13_34_scan{scan}.jpg'
                with Image.open(io.BytesIO(source.read(filename_in_archive))) as face:
                    original = face.convert('L')
                current = scan
            left, top, right, bottom = map(int, bounds)
            assert 0 <= left < right <= original.width
            assert 0 <= top < bottom <= original.height
            im = original.crop((left, top, right, bottom))
            im = ImageEnhance.Contrast(im).enhance(1.55)
            im = im.resize((3 * im.width, 3 * im.height), Image.Resampling.LANCZOS)
            im.save(dest / filename, quality=91)
    return len(entries)

if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('archive', type=Path)
    cli.add_argument('destination', nargs='?', type=Path, default=ROOT.parent / 'crops')
    args = cli.parse_args()
    print(f'{restore(args.archive, args.destination)} crops written.')
