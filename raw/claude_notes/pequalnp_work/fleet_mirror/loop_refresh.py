"""Run refresh_fleet_mirror.py every INTERVAL seconds (default 3600) for at most LIMIT seconds (default 43200), until a
file named STOP appears in this folder. Logs one line per run to loop_refresh.log.
usage: python -I -B loop_refresh.py [INTERVAL] [LIMIT]"""
import datetime, pathlib, subprocess, sys, time

HERE = pathlib.Path(__file__).resolve().parent
interval = int(sys.argv[1]) if len(sys.argv) > 1 else 3600
limit = time.time() + (int(sys.argv[2]) if len(sys.argv) > 2 else 43200)
while time.time() < limit:
    for _ in range(interval):
        if (HERE / "STOP").exists():
            sys.exit(0)
        time.sleep(1)
    r = subprocess.run([sys.executable, "-I", "-B", str(HERE / "refresh_fleet_mirror.py")], capture_output=True,
                       text=True, timeout=1800)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    with open(HERE / "loop_refresh.log", "a", encoding="utf-8") as fh:
        fh.write(f"{stamp} exit {r.returncode} {(r.stdout or '').strip()[-300:]} {(r.stderr or '').strip()[-300:]}\n")
