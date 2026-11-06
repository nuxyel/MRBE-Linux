# 01 — Arquitetura do MRBE Linux

## Camadas

1. Hardware virtual ou físico.
2. Kernel Linux e drivers.
3. BusyBox init e ferramentas de sistema.
4. Serviços pequenos (rede, entrada e diagnóstico).
5. Launcher de TV.

## Decisões de leveza

A primeira prova de conceito não usa:
- desktop XFCE;
- servidor X;
- compositor Wayland;
- Chromium;
- Electron;
- systemd;
- serviços residentes que não sejam necessários.

O launcher é um processo C que acessa framebuffer e evdev. Isso reduz dependências e torna o caminho de renderização fácil de auditar.

## Observação sobre a interface gráfica

Este kit usa fbdev como primeiro caminho didático. Em Linux moderno, o caminho preferível para um produto embarcado de longo prazo é DRM/KMS direto. O kernel precisa expor `/dev/fb0` para o protótipo atual funcionar. Se isso não ocorrer no QEMU, o sistema ainda poderá iniciar em console; a próxima tarefa será corrigir a configuração gráfica ou migrar o launcher para DRM/KMS.

LVGL poderá ser avaliado depois como biblioteca de UI. A documentação oficial descreve seu driver DRM como renderização direta sem X11/Wayland, com buffers dumb, GBM ou EGL. A escolha final dependerá do orçamento de memória e dos drivers do hardware.
