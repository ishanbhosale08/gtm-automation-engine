#!/usr/bin/env python3
"""Load and summarize synthetic demo leads from sample_contacts.csv."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

LEADS_DIR = Path(__file__).resolve().parent
SAMPLE_CSV = LEADS_DIR / "sample_contacts.csv"


def load_contacts(path: Path = SAMPLE_CSV) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Sample leads file not found: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def summarize(contacts: list[dict[str, str]]) -> None:
    counts = Counter(row.get("status", "UNKNOWN") for row in contacts)
    print(f"Loaded {len(contacts)} contacts from {SAMPLE_CSV.name}")
    for status, total in sorted(counts.items()):
        print(f"  {status}: {total}")
    print("\nWorkable queue preview:")
    for row in contacts:
        if row.get("status") == "WORKABLE":
            print(
                f"  - {row['name']} ({row['title']}) @ {row['company']} <{row['email']}>"
            )


def main() -> None:
    contacts = load_contacts()
    summarize(contacts)


if __name__ == "__main__":
    main()
