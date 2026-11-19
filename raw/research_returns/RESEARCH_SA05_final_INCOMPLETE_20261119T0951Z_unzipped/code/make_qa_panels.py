"""Split the current PDF-render sample into legible nine-page contact panels."""
from pathlib import Path
from PIL import Image, ImageDraw
import json

root = Path(__file__).resolve().parents[1]
pages = json.loads((root / 'code/pdf_qa_output.json').read_text())['rendered_pages']
directory = root / 'build/qa'
panels = []
for start in range(0, len(pages), 9):
    sample = pages[start:start + 9]
    sheet = Image.new('RGB', (1245, 600 * ((len(sample) + 2) // 3)), 'white')
    for index, page in enumerate(sample):
        im = Image.open(directory / f'page_{page:03d}.png').convert('RGB')
        im.thumbnail((395, 565))
        tile = Image.new('RGB', (415, 600), '#dddddd')
        tile.paste(im, ((415 - im.width) // 2, 12))
        ImageDraw.Draw(tile).text((12, 580), f'Page {page}', fill='black')
        sheet.paste(tile, ((index % 3) * 415, (index // 3) * 600))
    path = directory / f'panel_{start // 9 + 1:02d}.png'
    sheet.save(path)
    panels.append({'path': str(path), 'pages': sample})
(root / 'code/qa_panels_output.json').write_text(json.dumps(panels, indent=2) + '\n')
print(json.dumps(panels, indent=2))
