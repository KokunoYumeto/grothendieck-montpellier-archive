"""Recreate the registered 3x crops from the attached JPGs, without text recognition."""
from pathlib import Path
import argparse,csv,zipfile,io
from PIL import Image,ImageEnhance,ImageOps
def main():
    a=argparse.ArgumentParser();a.add_argument('scans_zip',type=Path);a.add_argument('target',type=Path);opts=a.parse_args()
    opts.target.mkdir(exist_ok=True,parents=True)
    reg=Path(__file__).with_name('K36-01_crop_locations.tsv')
    with reg.open() as f,zipfile.ZipFile(opts.scans_zip) as z:
        source={Path(n).name:n for n in z.namelist() if not n.startswith('hua/') and n.endswith('.jpg')}
        previous=None
        for r in csv.DictReader(f,delimiter='\t'):
            n=int(r['scan'])
            if n!=previous:
                im=Image.open(io.BytesIO(z.read(source[f'K36-01_36_scan{n:03}.jpg']))).copy()
                if n in (30,32,34):
                    upright=io.BytesIO()
                    im.transpose(Image.Transpose.ROTATE_180).save(upright,format='JPEG',quality=96)
                    upright.seek(0)
                    im=Image.open(upright).copy()
                previous=n
            part=im.crop(tuple(int(r[k]) for k in ('x0','y0','x1','y1'))).convert('L')
            part=ImageEnhance.Contrast(ImageOps.autocontrast(part,cutoff=.3)).enhance(1.3)
            part.resize((part.width*3,part.height*3),Image.Resampling.LANCZOS).save(opts.target/r['crop'],quality=91)
if __name__=='__main__':main()
