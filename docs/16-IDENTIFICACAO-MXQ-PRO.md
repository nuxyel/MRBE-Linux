# Fase E — Identificar o MXQ Pro com seguranca

**MXQ Pro nao identifica um hardware unico.** Existem multiplas revisoes.
Precisamos de identificacao antes de kernel, DTB, U-Boot e drivers reais.

## Sem abrir TV Box, com Android funcionando
Se tiver ADB habilitado de forma legitima, por USB ou rede local autorizada:

```sh
adb devices
adb shell getprop ro.product.board
adb shell getprop ro.hardware
adb shell getprop ro.board.platform
adb shell cat /proc/cpuinfo
adb shell cat /proc/meminfo
adb shell ls /proc/device-tree
```

`adb` deve ser executado no computador e autorizado no proprio TV Box.
Se nao houver ADB, anote informacoes das configuracoes de Android/CPU-Z
caso o aplicativo esteja disponivel. Nao habilite acesso remoto publico.

## Informacoes necessarias
- Etiqueta: MXQ Pro e especificacao impressa (geralmente pouco confiavel).
- SoC real (`/proc/cpuinfo`, `ro.hardware`, DT model/compatible).
- Arquitetura: ARMv7, ARM64, outra; 1/2/4/8 GiB RAM real.
- Fotos da **placa inteira dos dois lados** (somente se souber abrir sem riscos).
- Codigo impresso no PCB (ex.: Vxx), chip de flash (eMMC ou NAND), Wi-Fi e ethernet.
- Particionamento e modo boot externo, backup e procedimento de recuperacao.

## Nao fazer ainda
Nao execute `dd` no armazenamento interno, `fastboot flash`, comandos
U-Boot `saveenv`, `erase`, `nand write` ou arquivo `update.img` aleatorio.
Nao use uma imagem de um modelo MXQ Pro em outro apenas pelo nome.

## Marco de aceite
Hardware identificado -> avaliar suporte linux SoC -> selecionar DTB e
bootloader corretos -> teste nao destrutivo -> trilha de recuperacao.
