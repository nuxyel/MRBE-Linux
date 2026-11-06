# Manifesto de entrega 0.4.0

Incluidos: fontes C do launcher framebuffer, brasao MRBE e assets RGBA/PNG, scripts Bash, configuracao Buildroot, overlay do rootfs, testes locais, smoke test QEMU, previews das telas, PRD, STATUS, status.json, licenca do codigo e documentacao de atualizacao.

Excluidos: binarios Buildroot compilados, kernel `Image` pronto, disco `rootfs.ext4`, ISO, firmware MXQ Pro, ROM/bootloader do fabricante, APKs, codecs proprietarios e servicos comerciais.

**Validacao nesta entrega:** 12 testes locais passaram e o renderizador host gerou previews. A compilacao ARM64 e o boot QEMU da versao 0.4.0 ainda precisam ser executados no WSL do usuario.

**Evidencias esperadas apos build:** `work/build.log`, `logs/testes/qemu-boot-latest.log` e captura da janela QEMU.
