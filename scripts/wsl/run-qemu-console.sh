#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/work/output/images"
QEMU="${QEMU:-qemu-system-aarch64}"
RAM_MB="${RAM_MB:-1024}"
for f in "$OUT/Image" "$OUT/rootfs.ext4"; do [ -s "$f" ] || { echo "[ERRO] $f ausente; execute make build"; exit 2; }; done
command -v "$QEMU" >/dev/null || { echo 'Instale qemu-system-arm'; exit 2; }
case "$RAM_MB" in 512|768|1024|2048) ;; *) echo 'RAM_MB suportado: 512, 768, 1024 ou 2048'; exit 2;; esac
echo "MRBE Linux QEMU console: RAM ${RAM_MB} MiB. Para sair: Ctrl+A, X."
exec "$QEMU"   -M virt -cpu cortex-a53 -smp 2 -m "$RAM_MB" -accel tcg   -kernel "$OUT/Image"   -append 'root=/dev/vda rootwait console=ttyAMA0 rw loglevel=4'   -drive "file=$OUT/rootfs.ext4,if=none,format=raw,id=hd0,snapshot=on"   -device virtio-blk-device,drive=hd0   -netdev user,id=net0 -device virtio-net-device,netdev=net0   -display none -serial mon:stdio
