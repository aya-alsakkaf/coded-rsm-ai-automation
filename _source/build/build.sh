#!/usr/bin/env bash
# Build the whole workshop from the kit, then validate. Lives in _source/build/ (the engine); the kit is in _source/kit/.
#   bash _source/build/build.sh            (any folder; WK_KIT=/path/to/kit to use another kit folder)
#   bash _source/build/build.sh --no-validate
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
KIT="${WK_KIT:-$(cd ../kit && pwd)}"; export WK_KIT="$KIT"
ROOT="$(cd "$KIT/../.." && pwd)"
rm -rf "$ROOT/public"; mkdir -p "$ROOT/public/staff"
python3 "$KIT/gen_files.py" "$KIT/../files"          # the kit's sample files (names never change once published)
python3 deck.py "$ROOT/public"                       # decks: public (no notes) + /staff copy (notes on N) + _source/kit-pages records
python3 pages.py "$ROOT/public"                      # hub, day pages, sheets, labs, cheat sheet, card page, guide, 404, index, robots.txt
python3 staff.py "$ROOT/public"                      # trainer pages under /staff
python3 config.py "$ROOT"                            # vercel.json, package.json, middleware.js, .gitignore, .vercelignore
python3 surveys.py "$KIT/../surveys"                 # portal survey payloads (skipped when the kit has no SURVEY)
if [ "${1:-}" != "--no-validate" ]; then python3 validate_site.py "$ROOT/public"; fi
