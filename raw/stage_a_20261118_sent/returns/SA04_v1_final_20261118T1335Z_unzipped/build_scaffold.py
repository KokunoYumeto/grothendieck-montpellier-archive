#!/usr/bin/env python3
"""Rebuild the SA04 preservation scaffold from the supplied ZIPs.
This script intentionally does not claim mathematical adjudication."""
import zipfile, re, csv, json, pathlib, pandas as pd
