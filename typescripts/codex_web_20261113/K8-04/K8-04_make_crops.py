"""Rebuild the indexed crops from the supplied scan archive. Usage: python K8-04_make_crops.py ZIP CROPS_DIR"""
from pathlib import Path
from zipfile import ZipFile
from PIL import Image, ImageEnhance
import csv, io, sys
root=Path(__file__).resolve().parent
dest=Path(sys.argv[2])
dest.mkdir(parents=True, exist_ok=True)
with ZipFile(sys.argv[1]) as z, (root/'K8-04_crop_index.tsv').open() as f:
    by_name={Path(n).name:n for n in z.namelist() if n.lower().endswith('.jpg')}
    for row in csv.DictReader(f,delimiter='\t'):
        name='K8-04_8_scan'+str(int(row['scan'])).zfill(3)+'.jpg'
        im=Image.open(io.BytesIO(z.read(by_name[name])))
        im=im.rotate(int(row['whole_rotation_ccw']),expand=True)
        im=im.crop(tuple(int(row[k]) for k in ['x_left','y_top','x_right','y_bottom']))
        if int(row['crop_rotation_ccw']):
            im=im.rotate(int(row['crop_rotation_ccw']),expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
        im=ImageEnhance.Contrast(im).enhance(float(row['contrast']))
        m=int(row['magnification'])
        im.resize((im.width*m,im.height*m),Image.Resampling.LANCZOS).save(dest/row['crop'])
