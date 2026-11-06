#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/work/output"
fail=0
for f in "$OUT/.config" "$OUT/images/Image" "$OUT/images/rootfs.ext4"; do
    if [ -s "$f" ]; then ls -lh "$f"; else echo "[ERRO] Artefato ausente: $f"; fail=1; fi
done
if [ -s "$OUT/.config" ]; then
    for key in 'BR2_aarch64=y' 'BR2_TOOLCHAIN_BUILDROOT_MUSL=y' 'BR2_PACKAGE_MRBE_LAUNCHER=y'; do
        grep -q -F "$key" "$OUT/.config" || { echo "[ERRO] Opcao Buildroot: $key"; fail=1; }
    done
fi
if [ "$fail" -ne 0 ]; then exit 1; fi
echo '[MRBE] Artefatos presentes. Isso NAO comprova o boot: execute make smoke.'
