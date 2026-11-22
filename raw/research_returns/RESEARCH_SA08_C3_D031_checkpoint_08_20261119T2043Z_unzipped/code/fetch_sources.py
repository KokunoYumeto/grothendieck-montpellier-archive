#!/usr/bin/env python3
"""Download opened primary sources and record hashes, without interpreting contents."""
import hashlib, json, pathlib, sys, time, urllib.request

def fetch(url, destination):
    target = pathlib.Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        with urllib.request.urlopen(url, timeout=45) as response:
            data = response.read()
        target.write_bytes(data)
        return dict(url=url, destination=str(target), bytes=len(data),
                    sha256=hashlib.sha256(data).hexdigest(),
                    seconds=round(time.monotonic()-started, 3), status='downloaded')
    except Exception as error:
        return dict(url=url, destination=str(target), status='failed',
                    seconds=round(time.monotonic()-started, 3), error=repr(error))

if __name__ == '__main__':
    url, destination, log = sys.argv[1:]
    result = fetch(url, destination)
    pathlib.Path(log).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
