"""Render the original preceding definition sheet; no finite mathematical check."""
import datetime, json, pathlib, time
import fitz
root=pathlib.Path(__file__).resolve().parents[1]
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.perf_counter()
source=root/'sources/cote68.pdf'; target=root/'qa/part_c_functor_scan043.png'
with fitz.open(source) as doc:
    page=doc[42]; page.get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(target)
    text=page.get_text()
out={'started_utc':started,'elapsed_seconds':time.perf_counter()-tick,'source':str(source.relative_to(root)),'pdf_page_one_based':43,'image':str(target.relative_to(root)),'embedded_text':text,'network_requests':0,'mathematical_finite_checks':0}
destination=root/'code/part_c_functor_audit_source_page_output.json'
destination.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
