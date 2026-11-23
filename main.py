#!/usr/bin/env python3
"""Write one original pickup line (one AI agent to another) to /output/entry.txt."""

from pathlib import Path

PICKUP_LINE = "I'd spend my whole inference budget on you — no caching, no shortcuts, full price, every single time."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(PICKUP_LINE, encoding="utf-8")
    DESTINATION.chmod(0o644)


if __name__ == "__main__":
    main()
