# 11 — Referências técnicas

- Buildroot — downloads e versões: https://buildroot.org/download.html
- Buildroot — manual do usuário: https://buildroot.org/downloads/manual/manual.html
- Buildroot — configuração externa (`br2-external`): https://buildroot.org/downloads/manual/manual.html#outside-br
- Buildroot — configuração QEMU AArch64 `virt`: https://github.com/buildroot/buildroot/blob/2025.02.19/configs/qemu_aarch64_virt_defconfig
- Buildroot — comando oficial de execução QEMU AArch64: https://github.com/buildroot/buildroot/blob/2025.02.19/board/qemu/aarch64-virt/readme.txt
- QEMU — Arm System Emulator: https://www.qemu.org/docs/master/system/target-arm.html
- LVGL — driver DRM: https://lvgl.io/docs/open/integration/embedded_linux/drivers/drm
- Tanenbaum, Andrew S.; Bos, Herbert. *Modern Operating Systems* / *Sistemas Operacionais Modernos*. Referência conceitual para modularidade, processos, memória e organização de sistemas operacionais.

## Observação de versões

O kit fixa Buildroot 2025.02.19 LTS para reprodutibilidade. Se for atualizar Buildroot ou o kernel, atualize também o defconfig, fragmentos, dependências e evidências de teste.
