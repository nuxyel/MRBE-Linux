# Changelog

## 0.4.0 - 2026-11-06
- Adota o brasao MRBE com coroa, escudo, monitor/play e mascote Linux como identidade do sistema.
- Integra o asset RGBA transparente ao launcher framebuffer, sem biblioteca de imagem adicional.
- Atualiza paleta para carvão, verde-esmeralda, ouro e prata.
- Reaplica a identidade na Home, Apps, Configuracoes e painel de informacoes.
- Instala o brasao em `/usr/share/mrbe/brand/` no rootfs.
- Mantem Buildroot, kernel, QEMU e backend fbdev para preservar a base de boot previamente validada.
- Migração para LVGL fica como etapa seguinte, após validação visual e funcional da versão 0.4.0.

## 0.3.0 - 2026-11-05
- Nova interface home de TV estilo streaming, identidade MRBE original.
- Tela Apps, Configuracoes e atalhos H, A e S por evdev.
- Ilustracoes e cards procedurais em C, sem biblioteca grafica ou assets externos.
- Preview real das tres telas e testes automatizados do estado da UI.
- Rebuild inteligente do launcher Buildroot com hash de codigo-fonte; alvo `make ui-rebuild`.
- Script de compilacao corrige PATH importado do Windows e substitui uutils install localmente quando necessario.
- Apps, streaming e controles de energia sao demonstrativos.

# Changelog

## 0.2.0 — 2026-11-05
- Continua o DevKit 0.1.0 em um repositorio GitHub ready.
- Corrige configuracao Buildroot do kernel (defconfig arm64 + fragment absoluto).
- Adiciona boot marker `MRBE_BOOT_OK`, espera por framebuffer, imagens QEMU em snapshot.
- Adiciona smoke test de console serial com saida assim que detectar o boot, testes locais, gerador de previa do launcher.
- Documenta diferenca entre QEMU e a cadeia de boot do MXQ Pro; proibe flash prematuro.
- Documenta criterios verificaveis de uso em 1 GiB, escopo e limitacoes.

## 0.1.0 — DevKit original
- Bootstrap Buildroot, launcher simples framebuffer, console QEMU e guia iniciante.
