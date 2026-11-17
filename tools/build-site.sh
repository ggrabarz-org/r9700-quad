#!/usr/bin/env bash
# Build the docs site. ram-board.html lives at the repo root because the RAM
# sweeper writes it there; the site needs it inside docs_dir for relative links.
set -euo pipefail
cd "$(dirname "$0")/.."
cp ram-board.html site-src/docs/ram-board.html
MKDOCS=.venv-docs/bin/mkdocs
command -v "$MKDOCS" >/dev/null 2>&1 || MKDOCS=mkdocs
exec "$MKDOCS" build --strict "$@"
