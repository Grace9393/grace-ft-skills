#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract everything a contract reviewer needs from a .docx:
body text, Word comments, tracked changes, placeholder scan, headers/footers,
and any files embedded in the document.

Parsing is delegated to the shared engine in the `deep-extract` skill, so this
tool inherits its handling of damaged containers, tables, and embedded objects.

Usage:
    python contract_extract.py "path/to/contract.docx" [-o outdir]

Writes to outdir (default: alongside the docx, suffix _extracted):
    contract_text.txt   - body text, one paragraph or table row per line
    comments.md         - reviewer comments with author/date (if any)
    review_flags.md     - placeholders, tracked changes, headers/footers,
                          embedded attachments, and container damage
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _engine

PLACEHOLDER_PATTERNS = [
    (re.compile(r"\[[^\]\n]{0,80}\]"), "square-bracket placeholder"),
    (re.compile(r"X{3,}"), "XXX placeholder"),
    (re.compile(r"_{4,}"), "blank underscore line"),
    (re.compile(r"\bTBD\b|\bTBC\b|\bto be (agreed|confirmed|determined)\b", re.I),
     "TBD/TBC"),
]

EMBED_MARK = re.compile(r"⟦EMBEDDED OBJECT progid=(\S+) -> (\S+?)⟧")


def extract(docx_path: Path, outdir: Path):
    dx = _engine.load()
    outdir.mkdir(parents=True, exist_ok=True)

    with open(dx.long_path(str(docx_path)), "rb") as fh:
        raw = fh.read()

    entries, warns = dx.read_zip_entries(raw)
    parts = {n: b for n, b, _ in entries if b is not None}
    if "word/document.xml" not in parts:
        sys.exit("Not a readable .docx: word/document.xml missing. "
                 "Warnings: %s" % ("; ".join(warns) or "none"))

    sections = dx.docx_text(parts)
    body = next((txt for title, txt in sections if title == "Body"), "")
    comments = dx.comments_map(parts)

    # --- body text -------------------------------------------------------
    lines = [ln.rstrip() for ln in body.splitlines()]
    (outdir / "contract_text.txt").write_text("\n".join(lines), encoding="utf-8")

    # --- comments --------------------------------------------------------
    comment_lines = []
    for cid in sorted(comments, key=lambda x: int(x) if x.isdigit() else 0):
        c = comments[cid]
        comment_lines.append("- **%s** (%s): %s"
                             % (c["author"], c["date"],
                                re.sub(r"\s+", " ", c["text"]).strip()))
    (outdir / "comments.md").write_text(
        "# Reviewer comments\n\n" + ("\n".join(comment_lines) or "None found."),
        encoding="utf-8")

    # --- review flags ----------------------------------------------------
    flags = []

    if warns:
        flags.append("- **Container damage** - the file did not open cleanly. "
                     "Do not treat the extraction as complete:")
        for w in warns:
            flags.append("    - %s" % w)

    n_ins = len(re.findall(r"\{\+", body))
    n_del = len(re.findall(r"\{-", body))
    if n_ins or n_del:
        flags.append("- **Unaccepted tracked changes**: %d insertion(s), %d "
                     "deletion(s) still in the document. They are marked "
                     "`{+inserted+}` / `{-deleted-}` in contract_text.txt."
                     % (n_ins, n_del))
    if comment_lines:
        flags.append("- **Unresolved comments**: %d comment(s) still attached "
                     "(see comments.md). Resolve or strip before signature."
                     % len(comment_lines))

    embeds = EMBED_MARK.findall(body)
    if embeds:
        flags.append("- **Embedded attachments**: %d file(s) are embedded in "
                     "this contract. They are part of what you would be "
                     "signing and are NOT included in contract_text.txt - open "
                     "them separately (the deep-extract skill will unpack them "
                     "recursively):" % len(embeds))
        for progid, target in embeds:
            flags.append("    - `%s` (%s)" % (target.split("/")[-1], progid))

    declared, present, missing = dx.embedding_reconciliation(parts)
    if missing:
        flags.append("- **Missing attachments**: the document references %d "
                     "embedded file(s) that are absent from it. Whatever they "
                     "say is unavailable and cannot be reviewed:" % len(missing))
        for t in missing:
            flags.append("    - `%s`" % t)

    for i, txt in enumerate(lines, 1):
        for pat, label in PLACEHOLDER_PATTERNS:
            for m in pat.finditer(txt):
                flags.append("- **%s** at line %d: `%s` in “%s”"
                             % (label, i, m.group(0)[:40], txt.strip()[:100]))

    for title, txt in sections:
        if re.match(r"word/(header|footer)\d*\.xml$", title):
            flat = re.sub(r"\s+", " ", txt).strip()
            if flat:
                flags.append("- header/footer `%s`: “%s”"
                             % (title, flat[:120]))

    (outdir / "review_flags.md").write_text(
        "# Pre-signature hygiene flags\n\n" + ("\n".join(flags) or "None found."),
        encoding="utf-8")

    print("Extracted %d lines, %d comments, %d embedded attachment(s), "
          "%d flags -> %s" % (len(lines), len(comment_lines), len(embeds),
                              len(flags), outdir))
    if warns:
        print("WARNING: container did not open cleanly - see review_flags.md")
        return 2
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("-o", "--outdir")
    args = ap.parse_args()
    src = Path(args.docx)
    if not src.exists():
        sys.exit("Not found: %s" % src)
    outdir = Path(args.outdir) if args.outdir else \
        src.parent / (src.stem + "_extracted")
    return extract(src, outdir)


if __name__ == "__main__":
    sys.exit(main() or 0)
