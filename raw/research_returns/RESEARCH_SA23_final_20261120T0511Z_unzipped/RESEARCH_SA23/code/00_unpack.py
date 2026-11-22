from pathlib import Path
import zipfile, hashlib, csv, time
start=time.perf_counter()
archive=Path('upload/SA23_EGA_drafts_and_letters_cotes_1-2_21-26_161_night.zip')
dest=Path('inputs'); dest.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    for info in z.infolist():
        p=Path(info.filename)
        assert not p.is_absolute() and '..' not in p.parts
    z.extractall(dest)
    print('Entries:', len(z.infolist()))
    print('Uncompressed bytes:',sum(i.file_size for i in z.infolist()))
    for info in z.infolist(): print(info.filename, info.file_size)
print('Archive SHA256:', hashlib.sha256(archive.read_bytes()).hexdigest())
print('Elapsed seconds:',time.perf_counter()-start)
