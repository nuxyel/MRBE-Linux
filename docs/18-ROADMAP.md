# Roadmap tecnico de releases

## v0.2.0 — baseline de desenvolvimento (este pacote)
- [x] Arvore Buildroot externa, kernel config, init e launcher.
- [x] Scripts QEMU, compilacao, check, smoke, preview e testes estaticos.
- [x] Docs para usuario iniciante, desempenho e boot seguro.
- [ ] Compilacao completa executada em host Ubuntu com rede.
- [ ] Boot + GUI validados em QEMU por logs/screenshot.

## v0.3.0 — boot e multimidia basicos
- [ ] Validar artefatos T03–T08 e corrigir falhas efetivamente observadas.
- [ ] File browser e reproducao offline de MP4/H264 com GStreamer ou mpv
      (avaliacao de memoria, licencas de codecs, desempenho).
- [ ] Melhorar interacao, foco, fontes, e eventual HDMI-CEC via drivers.

## v0.4.0 — hardware MXQ Pro
- [ ] Identificar SoC/PCB/DTB/boot chain e procedimento de recuperacao.
- [ ] Kernel, DTB, rede, GPU, som, HDMI e controle apropriados.
- [ ] Inicializacao nao destrutiva e testes no modelo exato.

## v0.5.0 — boot por firmware virtual
- [ ] Integrar imagem GPT/ESP + GRUB AA64 + AAVMF e testes UEFI.
- [ ] Testes automatizados de boot UEFI distintos do QEMU direct kernel.

## v1.0 — apenas apos verificacao
- [ ] Matriz hardware clara, politica de updates, endurecimento de seguranca,
      build reproduzivel comprovado, release com hash e evidencias.


## v0.4.0 — identidade visual MRBE
- Brasao RGBA, paleta carvao/esmeralda/ouro/prata e aplicacao nas telas.
- Atualizacao do launcher framebuffer sem substituir o caminho de boot existente.

## v0.5.0 — migracao LVGL
- LVGL 9.x com renderizacao parcial para reduzir memoria.
- Backend fbdev no target inicial; avaliar DRM/KMS quando o hardware for identificado.
- Simulador SDL2 no computador de desenvolvimento.
- Tipografia Noto Sans e catalogo de imagens redimensionadas/cacheadas.
- Medir RSS, uso de CPU e memoria de framebuffer em QEMU com 1 GiB.
