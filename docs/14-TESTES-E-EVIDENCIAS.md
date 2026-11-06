# Fase C — Matriz de teste e criterios de aceite

| ID | Tipo | Comando | Resultado esperado | Estado inicial |
|----|------|---------|--------------------|----------------|
| T01 | shell | `make test` | Sintaxe e C sem erros | executar |
| T02 | tela offline | `make preview` | PNG/PPM 1280x720 | executar |
| T03 | Buildroot | `JOBS=4 make build` | Image e rootfs.ext4 | pendente |
| T04 | artefatos | `make check` | sem ERRO | pendente |
| T05 | boot QEMU 1 GiB | `make smoke` | `MRBE_BOOT_OK` | pendente |
| T06 | TV GUI | `make gui` | tela e quatro tiles | pendente |
| T07 | controle remoto | setas/Enter/Esc | seleciona tile/estado | pendente |
| T08 | uso memoria | `free -m` no guest | sem OOM, responsivo | pendente |
| T09 | detecao MXQ Pro | `docs/16-IDENTIFICACAO-MXQ-PRO.md` | SoC e placa comprovados | bloqueado |

## Log estruturado manual
Data/hora: _______  Tester: _______  Host/WSL: _______
Commit Git: _______  Buildroot: 2025.02.19  RAM QEMU: 1024 MiB
Comando: _______  Exit code: _______  Result: PASS/FAIL/BLOCKED
Evidencia: caminho arquivo ou imagem _______

## Como calcular hash dos artefatos
No Ubuntu: `sha256sum work/output/images/Image work/output/images/rootfs.ext4`.
Anote os hashes junto ao log, sem publicar segredos do computador.

## Notas
`MRBE_BOOT_OK` comprova somente execucao da rotina de init, **nao**
comprova framebuffer, input, desempenho, media player ou boot no MXQ Pro.
Para cada uma dessas capacidades ha teste separado.
