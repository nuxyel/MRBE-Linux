#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
exec python3 "$ROOT/scripts/dev/qemu-smoke.py" --root "$ROOT" --qemu "${QEMU:-qemu-system-aarch64}" --timeout "${SMOKE_TIMEOUT:-150}"
