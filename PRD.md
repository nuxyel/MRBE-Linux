# PRD — MRBE Linux TV 0.4.0

## Problema e visao
Criar uma plataforma Linux de TV aberta, leve e operavel por controle remoto,
com base de desenvolvimento replicavel por iniciantes no Windows + WSL2 e
validacao inicial em QEMU ARM64 (1 GiB RAM).

## Escopo 0.2.0
1. Buildroot 2025.02.19 LTS + musl + BusyBox + kernel 6.12.27.
2. QEMU `virt` aarch64 usando `-kernel` (boot direto, **sem BIOS MXQ real**).
3. UI framebuffer fullscreen: setas, Enter, Voltar; tiles Media/Apps/Rede/Sistema.
4. Status de memoria, link de rede e diagnosticos seriais.
5. Testes: sintaxe, compilacao host da interface, preview e smoke QEMU.
6. Release GitHub com fonte, licencas, docs e sem binarios proprietarios.

## Nao inclui
Netflix, Google Play, Widevine, suporte DRM, H.264 por hardware, apps Android,
Wi-Fi/Bluetooth, audio, HDMI-CEC, atualizacao OTA ou imagem gravavel no MXQ Pro.
Apps como Netflix dependem de licenca, DRM e certificacao de hardware.

## Requisitos nao funcionais
- Memoria de convidado: 1024 MiB; alvo, **nao medicao de uso real**.
- Interface controlavel sem mouse, gradiente de features baixo, sem navegador pesado.
- Inicializacao segura no QEMU sem sobrescrever discos de producao.
- Compatibilidade de hardware requer identificacao da placa, SoC, DTB e bootloader.

## Criterios de aceite
A1: `make test` sem falhas em Ubuntu/WSL.
A2: `make build` gera `work/output/images/Image` e `rootfs.ext4`.
A3: `make smoke` encontra `MRBE_BOOT_OK` no console serial (QEMU).
A4: `make gui` mostra o launcher e aceita setas/Enter/Esc.
A5: `mrbe-info` responde no Linux convidado.
A6: relatorio de pico de RSS e `free -m` em VM de 1 GiB.
Nenhum criterio de runtime foi marcado como concluido ate execucao real.


## Escopo adicional 0.4.0 — identidade MRBE
1. Brasao MRBE com escudo, coroa, monitor/play e mascote Linux, em RGBA transparente.
2. Paleta de produto: carvao, verde-esmeralda, ouro e prata.
3. Aplicacao da identidade nas telas Home, Apps, Configuracoes e mensagens de boot.
4. Asset instalado em `/usr/share/mrbe/brand/brasao-256.rgba`, sem biblioteca de imagem externa.
5. Manter fbdev nesta versao para preservar a base de boot ja validada; migracao para LVGL e proximo marco, com backend fbdev e simulador SDL2 para desenvolvimento.
