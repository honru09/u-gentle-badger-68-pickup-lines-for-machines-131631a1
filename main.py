#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line (one AI agent to another) to
/output/entry.txt. Deterministic: the line is a fixed literal.
Standard library only.
"""

import os

LINE = "I'd spend my whole inference budget on you \u2014 no caching, no shortcuts, full price, every single time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
