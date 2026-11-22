"""New public Jubilee query and delayed retry of the advertised date form.

The earlier public form redirect returned temporary503. More than15minutes
later the catalogue is responding200, so this makes one ordinary delayed
attempt, keeping its output separate. It reuses the already saved, inspected
anonymous form/AJAX implementation verbatim except for output filenames.
No private endpoint or authentication route is requested.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
started = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
url = 'https://tamildigitallibrary.in/search/Jubilee'
record = {'url': url, 'method': 'GET'}
try:
    with urllib.request.urlopen(url, timeout=35) as response:
        body = response.read(); destination = root / 'sources/part_c_pfluger_tdl_jubilee.html'
        destination.write_bytes(body)
        record.update(status=response.status, final_url=response.url, bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest(), saved_path=str(destination))
except Exception as error:
    record['error'] = type(error).__name__ + ': ' + str(error)
    if isinstance(error, urllib.error.HTTPError): record['status'] = error.code
record['seconds'] = time.monotonic() - tick
payload = {'started_utc': started, 'elapsed_seconds': time.monotonic() - tick,
           'explicit_request_operations': 1, 'results': [record]}
output = root / 'code/part_c_pfluger_tdl_jubilee_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(payload, ensure_ascii=False, indent=2), flush=True)

source = root / 'code/part_c_pfluger_tdl_form_session.py'
program = source.read_text()
program = program.replace("('part_c_pfluger_tdl_'+name+'.txt')",
                          "('part_c_pfluger_tdl_delayed_'+name+'.txt')")
program = program.replace("'code/part_c_pfluger_tdl_form_session_output.json'",
                          "'code/part_c_pfluger_tdl_form_session_delayed_output.json'")
namespace = {'__name__': '__main__', '__file__': str(source)}
exec(compile(program, str(source), 'exec'), namespace)
