#!/usr/bin/env bash
# Regenerates every HTML page. Only needed if you change shared markup —
# the nav, the footer, or the record cards. OVERWRITES your content edits.
set -e
cd "$(dirname "$0")/.."
python3 _source/build_a.py         # index.html, work.html
python3 _source/build_projects.py  # soundexchange, bearcheck, lipor, chillzu
python3 _source/build_d.py         # teaching, about, in-rotation
echo "Rebuilt."
