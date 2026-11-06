# 09 — Limitações e futuro MXQ Pro

## QEMU não é o MXQ Pro

A máquina `virt` do QEMU é uma placa ARM virtual genérica. Ela testa o sistema e a arquitetura ARM64, mas não valida:
- SoC específico do MXQ Pro;
- GPU e driver proprietários;
- decodificador de vídeo;
- Wi-Fi/Bluetooth da placa;
- controle infravermelho;
- HDMI-CEC;
- bootloader original;
- Device Tree do fabricante;
- DRM/Widevine e certificações de streaming.

## Antes de testar em hardware

Identificar:
1. SoC exato;
2. revisão da placa;
3. arquitetura e RAM real;
4. GPU;
5. bootloader e método de recuperação;
6. DTB correspondente;
7. suporte do kernel mainline aos periféricos.

Não grave a imagem QEMU em eMMC/SD do TV Box. A imagem `virt` não é uma imagem para MXQ Pro.

## Netflix e streaming

O protótipo não inclui Netflix. A execução de serviços de streaming em Linux embarcado pode depender de DRM, Widevine, certificação do dispositivo, navegador/app compatível e suporte do fabricante. Não é possível prometer reprodução 4K ou Netflix somente porque o Linux inicializa.
