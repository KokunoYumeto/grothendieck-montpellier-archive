"""Exact next-degree exploration, keeping the preceding frozen files unchanged."""
from pathlib import Path
import argparse
import importlib.util
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'compute_harmonic_hecke.py'
spec = importlib.util.spec_from_file_location('u3_frozen_discovery', SOURCE)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
model.BASE = HERE
model.NEIGHBORS = HERE.parent.parent / 'hecke_level_one/u3_weight5_exact_exploration.json'

parser = argparse.ArgumentParser()
parser.add_argument('k', type=int)
args = parser.parse_args()
neighbors = json.loads(model.NEIGHBORS.read_text())
model.calculate(args.k, [r for r in neighbors['results'] if r['p'] in (7, 13)])
