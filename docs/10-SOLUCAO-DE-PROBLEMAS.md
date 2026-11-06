# 10 — Solução de problemas

## `qemu-system-aarch64: command not found`

Execute:

```bash
./scripts/wsl/install-dev-tools.sh
```

## Buildroot falha por dependência ausente

Copie as últimas linhas do erro. Não instale pacotes aleatórios; compare com os requisitos do manual Buildroot e com a mensagem exata.

## Download interrompido

Execute novamente:

```bash
./scripts/wsl/build.sh
```

O `wget -c` tenta continuar o download.

## `Image` ou `rootfs.ext4` ausente

A compilação não terminou ou a configuração não foi aplicada. Execute `build.sh` e guarde a saída completa.

## QEMU não encontra `/dev/vda`

Confira:
- `-drive file=...rootfs.ext4`;
- `-device virtio-blk-device,drive=hd0`;
- argumento `root=/dev/vda`;
- driver VirtIO block no kernel.

## `No bootable device`

Este kit carrega o kernel diretamente com `-kernel`; não depende de UEFI/OVMF/AAVMF. Confira se o caminho `Image` está correto. Se estiver usando outro comando com firmware, volte ao script fornecido.

## Tela preta no modo gráfico

No modo serial:
```sh
mrbe-diagnostico
dmesg | grep -Ei 'drm|virtio|fb'
cat /var/log/mrbe-launcher.log
```

Se `/dev/fb0` não existir, o launcher não tem dispositivo para desenhar. O sistema pode ter iniciado corretamente em console.

## Teclado não funciona no launcher

Confira:
```sh
ls -l /dev/input/event*
dmesg | grep -i input
```
Verifique se QEMU recebeu `-device virtio-keyboard-pci` e se o kernel habilitou `CONFIG_VIRTIO_INPUT` e `CONFIG_INPUT_EVDEV`.

## Janela GTK não abre no WSL

Confira:
```bash
echo "$DISPLAY"
echo "$WAYLAND_DISPLAY"
qemu-system-aarch64 -display help
```
Se WSLg não estiver disponível, use o boot serial. Não confunda ausência de janela com falha do kernel.
