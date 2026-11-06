#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SRC="$ROOT/package/mrbe-launcher/src"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
CC="${CC:-cc}"
"$CC" -std=c11 -Os -Wall -Wextra -Werror \
    -DMRBE_LOGO_PATH=\"$SRC/assets/brasao-256.rgba\" \
    -o "$TMP/mrbe-preview" "$SRC/preview.c" "$SRC/ui.c" "$SRC/fb.c" "$SRC/font.c"
for view in home apps settings; do
    if [ "$view" = home ]; then
        "$TMP/mrbe-preview" "$TMP/preview-home.ppm"
        name="preview-mrbe-tv"
    else
        "$TMP/mrbe-preview" "$TMP/preview-${view}.ppm" "$view"
        name="preview-mrbe-${view}"
    fi
    if python3 -c 'from PIL import Image' >/dev/null 2>&1; then
        python3 - "$TMP/preview-${view}.ppm" "$ROOT/docs/${name}.png" <<'PYTHON'
import sys
from PIL import Image
Image.open(sys.argv[1]).save(sys.argv[2], optimize=True)
print('Previa PNG:',sys.argv[2])
PYTHON
    else
        cp "$TMP/preview-${view}.ppm" "$ROOT/docs/${name}.ppm"
        echo "Previa PPM: docs/${name}.ppm (python3-pil para PNG)"
    fi
done
