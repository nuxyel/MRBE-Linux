# 05 — Executar no QEMU

## Perfil do guest

- Máquina: `virt`.
- CPU: Cortex-A53.
- RAM: 1024 MiB.
- CPUs: 2.
- Kernel: `Image` ARM64.
- Disco: `rootfs.ext4` ligado como `/dev/vda`.
- Rede: user-mode networking com VirtIO.
- Gráficos: VirtIO GPU.
- Entrada: VirtIO keyboard/mouse.
- Aceleração: TCG (emulação por software).

## Boot serial

```bash
./scripts/wsl/run-qemu-console.sh
```

Esse modo valida boot, rootfs, init e login serial. A tela gráfica não é exibida.

## Boot gráfico

Com WSLg ativo:

```bash
./scripts/wsl/run-qemu-gui.sh
```

O script usa GTK. Se o QEMU instalado não tiver backend GTK, instale o pacote gráfico QEMU pelo script de dependências ou ajuste `-display gtk` para um backend disponível (`-display help` mostra as opções).

## Linha de comando equivalente

```bash
qemu-system-aarch64 \
  -M virt \
  -cpu cortex-a53 \
  -smp 2 \
  -m 1024 \
  -accel tcg \
  -kernel work/output/images/Image \
  -append "root=/dev/vda rootwait console=ttyAMA0 rw loglevel=4" \
  -drive file=work/output/images/rootfs.ext4,if=none,format=raw,id=hd0 \
  -device virtio-blk-device,drive=hd0 \
  -netdev user,id=net0 \
  -device virtio-net-device,netdev=net0 \
  -device virtio-gpu-pci \
  -device virtio-keyboard-pci \
  -device virtio-mouse-pci \
  -display gtk,gl=off \
  -serial stdio \
  -monitor none
```

Execute a partir da raiz do projeto.

## Sair

- No modo gráfico: feche a janela do QEMU ou interrompa o processo no terminal.
- No modo serial multiplexado: `Ctrl+A`, depois `X`; se necessário, `Ctrl+C`.
