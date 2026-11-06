# Fase A — Guia de desenvolvimento completo (iniciante)

## Requisitos de hardware do **computador de desenvolvimento**
Windows 11 com virtualizacao/WSL2 (ou Ubuntu Linux); pelo menos 8 GiB RAM,
preferencialmente 16 GiB; 25–40 GiB de disco livre (compilacao varia). O **convidado**
QEMU recebe apenas 1 GiB de memoria; a compilacao exige mais RAM e disco.

## Passo 1: WSL2
No PowerShell como administrador execute `wsl --install -d Ubuntu` e `wsl --update`.
Reinicie quando solicitado. Abra Ubuntu pelo menu Iniciar, crie usuario e senha;
sua senha nao aparece ao digitar, o que e normal.

## Passo 2: fontes
Descompacte o ZIP no Ubuntu, em `~/MRBE-Linux` (nao trabalhe em `/mnt/c`).
Abra Terminal Ubuntu e execute `cd ~/MRBE-Linux` e `pwd` para confirmar.

## Passo 3: dependencias
Execute `chmod +x scripts/wsl/*.sh scripts/dev/*.sh` e `make setup`.
O Ubuntu pede sua senha para instalar pacotes. Verifique com:
`qemu-system-aarch64 --version`, `make --version` e `gcc --version`.

## Passo 4: teste estatico e preview
Execute `make test`. Deve mostrar `[APROVADO]`. Caso exista python3-pil,
`docs/preview-mrbe-tv.png` sera gerado. Esse teste **nao liga Linux no QEMU**.

## Passo 5: compilacao Buildroot
Execute `JOBS=4 make build`. Primeiro download de Buildroot e suas dependencias;
compilar kernel+toolchain pode demorar bastante e gerar muitos GB em `work/`.
Nao interrompa no meio. Em falha, abra `work/build.log` e `docs/10-SOLUCAO-DE-PROBLEMAS.md`.

## Passo 6: verificar artefatos
`make check`. Devem existir `work/output/images/Image` e `rootfs.ext4`.
Nao renomeie nem converta `rootfs.ext4` para imagem do MXQ Pro.

## Passo 7: QEMU serial, primeiro
`make smoke`. Resultado esperado `[APROVADO] MRBE_BOOT_OK ...`.
Se falhar, leia `logs/testes/qemu-boot-latest.log`.
Execute `make console`; na linha de comando do Linux convidado digite
`mrbe-info`, `free -m`, `dmesg | tail`. Saia com `Ctrl+A`, depois `X`.

## Passo 8: QEMU TV GUI
No Windows 11, WSLg deve estar ativo (ver `echo $DISPLAY`). Execute
`make gui`. Use teclado com setas, Enter e Esc. A tela tem quatro tiles.
Se `fb0` nao estiver disponivel, GUI nao aparecera; consulte log da
serial e `/var/log/mrbe-launcher.log` no convidado.

## Passo 9: medir consumo
No convidado: `free -m; cat /proc/meminfo | head -n 5; ps w`.
Registre uma captura, a versao, o instante e RSS do launcher. Nao afirme
que o produto atende ao alvo de 1 GiB apenas por configurar `-m 1024`.

## Passo 10: documentar evidencias
Guarde data, host, kernel, hashes das imagens, log boot e screenshot GUI.
Use `docs/14-TESTES-E-EVIDENCIAS.md`.
