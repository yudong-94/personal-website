#!/usr/bin/env python3
"""
Batch-update Weekly Viz posts:
- If title == "Weekly Viz YYYY-MM-DD", set:
    title   := first heading in the body (#, ##, or ###), markdown stripped
    excerpt := "Weekly Viz YYYY-MM-DD"
Usage:
  python update_weekly_viz.py _posts/projects/data_viz --dry-run
"""

import argparse, re, sys, pathlib
from typing import Optional


try:
    import yaml  # pip install pyyaml
except ImportError:
    print("This script needs PyYAML. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

WEEKLY_TITLE_RE = re.compile(r"^Weekly Viz (\d{4}-\d{2}-\d{2})$")

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

def split_front_matter(text: str):
    """Return (yaml_str, body_str) given a Jekyll-style file."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, text
    yaml_block = parts[0][3:]  # drop leading ---
    body = parts[1]
    # drop single leading newline in body if present
    if body.startswith("\n"): body = body[1:]
    return yaml_block, body

def first_heading_from_body(body: str) -> Optional[str]:
    for line in body.splitlines():
        m = HEADING_RE.match(line.strip())
        if m:
            heading = m.group(2)
            # strip common inline markdown: emphasis, code, links
            heading = re.sub(r"\*\*?(.*?)\*\*?", r"\1", heading)  # *em* or **em**
            heading = re.sub(r"`([^`]+)`", r"\1", heading)        # `code`
            heading = re.sub(r"$begin:math:display$(.*?)$end:math:display$$begin:math:text$[^)]+$end:math:text$", r"\1", heading) # [text](url)
            heading = heading.strip(" _*-–—")
            return heading.strip()
    return None

def process_file(path: pathlib.Path, dry_run=False):
    src = path.read_text(encoding="utf-8")
    yml_str, body = split_front_matter(src)
    if yml_str is None:
        return (path, "skip: no front matter")

    data = yaml.safe_load(yml_str) or {}
    title = str(data.get("title", "")).strip()
    m = WEEKLY_TITLE_RE.match(title)
    if not m:
        return (path, "skip: title not Weekly Viz YYYY-MM-DD")

    date_in_title = m.group(1)  # YYYY-MM-DD
    # Prefer the first heading in the body
    new_title = first_heading_from_body(body)
    if not new_title:
        return (path, "skip: no heading found")

    changed = False
    if data.get("title") != new_title:
        data["title"] = new_title
        changed = True

    desired_excerpt = f"Weekly Viz {date_in_title}"
    if data.get("excerpt") != desired_excerpt:
        data["excerpt"] = desired_excerpt
        changed = True

    if not changed:
        return (path, "no change")

    # Rebuild file
    new_front = "---\n" + yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True
    ) + "---\n"
    new_content = new_front + body

    if dry_run:
        return (path, f"would update → title: {new_title!r}, excerpt: {desired_excerpt!r}")

    # backup then write
    path.with_suffix(path.suffix + ".bak").write_text(src, encoding="utf-8")
    path.write_text(new_content, encoding="utf-8")
    return (path, f"updated → title: {new_title!r}, excerpt: {desired_excerpt!r}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("root", help="directory containing Weekly Viz markdown files")
    p.add_argument("--dry-run", action="store_true", help="print changes only")
    args = p.parse_args()

    root = pathlib.Path(args.root)
    if not root.exists():
        print(f"Directory not found: {root}", file=sys.stderr); sys.exit(1)

    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        print("No .md files found.")
        return

    for f in md_files:
        path, msg = process_file(f, dry_run=args.dry_run)
        print(f"{path}: {msg}")

if __name__ == "__main__":
    main()