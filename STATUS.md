# MRBE Linux TV 0.4.0 — Estado do projeto

## Entregue nesta versão
- Brasão oficial MRBE integrado ao launcher como asset RGBA, com fallback vetorial.
- Paleta de identidade: carvão, verde-esmeralda, ouro e prata.
- Home, Apps e Configurações atualizadas com a identidade visual.
- Asset instalado em `/usr/share/mrbe/brand/brasao-256.rgba`.
- Renderizador framebuffer preservado para não quebrar o boot já validado na versão anterior.
- Testes locais e prévias host devem ser executados com `make test`.

## Validação pendente no computador do usuário
- `JOBS=2 make ui-rebuild` para atualizar apenas o launcher e regenerar as imagens.
- `make smoke` para confirmar o boot da imagem 0.4.0 no QEMU.
- `make gui` para conferir o brasão e a interface na janela QEMU.

## Limites conhecidos
- QEMU `virt` ARM64 é plataforma virtual, não firmware/BIOS do MXQ Pro.
- Catálogo, apps, streaming, áudio e ações de energia continuam demonstrativos.
- A imagem do brasão foi gerada para o projeto; confirme a licença escolhida para os assets antes de publicar o repositório.
- Migração para LVGL está planejada como etapa seguinte, mantendo fbdev como backend de baixo consumo.
