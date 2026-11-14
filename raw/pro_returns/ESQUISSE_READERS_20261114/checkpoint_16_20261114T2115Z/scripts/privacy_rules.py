#!/usr/bin/env python3
"""Shared checks and explicit redaction of documentary path/email strings."""
from __future__ import annotations

import hashlib
import re

LOCAL_PATH = re.compile(r"/(?:workspace|home|mnt|tmp|usr|opt|var)/[^\s<>\"'\)\}]+")
EMAIL = re.compile(r"(?<![\w@])[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,}")


def findings(text, relative_name):
    result = []
    for pattern, kind in [(LOCAL_PATH, "local path"), (EMAIL, "email address")]:
        for match in pattern.finditer(text):
            interpreter = "/".join(["", "usr", "bin", "env"])
            line_start = text.rfind("\n", 0, match.start()) + 1
            prefix = text[line_start:match.start()]
            portable_directive = (relative_name.endswith(".py") and text.startswith("#!") and match.start() == 2)
            historical_directive = relative_name.endswith(".diff.txt") and prefix in {"#!", "+#!", "-#!", " #!"}
            if match.group() == interpreter and (portable_directive or historical_directive):
                continue
            result.append({
                "start": match.start(), "end": match.end(), "kind": kind,
                "line": text[:match.start()].count("\n") + 1,
                "column": match.start() - line_start + 1,
                "removed_sha256": hashlib.sha256(match.group().encode()).hexdigest(),
            })
    return sorted(result, key=lambda item: item["start"])


def redact_history(text, relative_name):
    records = findings(text, relative_name)
    redacted = text
    for item in reversed(records):
        marker = "[redacted " + item["kind"] + "; sha256=" + item["removed_sha256"] + "]"
        redacted = redacted[:item["start"]] + marker + redacted[item["end"]:]
    return redacted, records
