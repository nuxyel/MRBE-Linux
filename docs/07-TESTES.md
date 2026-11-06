# 07 — Plano de testes

## T01 — Artefatos

Executar:

```bash
./scripts/wsl/check-build.sh
```

Aprovação: `Image` e `rootfs.ext4` existem e não estão vazios.

## T02 — Boot serial

Executar `run-qemu-console.sh`.

Aprovação:
- kernel inicia;
- rootfs é montado;
- BusyBox init inicia;
- aparece login serial.

## T03 — Memória do guest

No guest:

```sh
grep -E 'MemTotal|MemAvailable|SwapTotal|SwapFree' /proc/meminfo
free
```

Aprovação: o guest detecta aproximadamente 1 GiB de memória (o valor exato pode ser menor por reservas do kernel/dispositivos).

## T04 — Dispositivos

```sh
ls -l /dev/fb0
ls -l /dev/input/event*
dmesg | grep -Ei 'virtio|drm|framebuffer|input'
```

Aprovação: framebuffer e dispositivo de entrada aparecem para o launcher gráfico.

## T05 — Launcher

Abrir QEMU gráfico e navegar por todos os cartões.

Aprovação: foco muda com setas; Enter mostra status; Esc volta.

## T06 — Rede

```sh
ip link
cat /sys/class/net/eth0/operstate
```

Aprovação: interface VirtIO existe. DHCP pode levar alguns segundos.

## T07 — Estabilidade

Deixar a VM ligada por 2 horas, navegar periodicamente e verificar:
- memória disponível;
- erros no `dmesg`;
- travamentos;
- reinício inesperado do launcher.

## Modelo de registro

| Campo | Valor |
|---|---|
| Data/hora | |
| Commit/versão | |
| QEMU version | |
| RAM guest | 1024 MiB |
| Teste | |
| Resultado | PASS/FAIL |
| Evidência/log | |
| Observações | |

Não marque nenhum teste como PASS antes de executá-lo.
