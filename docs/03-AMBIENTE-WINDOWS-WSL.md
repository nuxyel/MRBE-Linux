# 03 — Ambiente de desenvolvimento Windows + WSL2

## Requisitos recomendados

- Windows 10 atualizado ou Windows 11 com suporte a WSL2.
- WSL2.
- Ubuntu 24.04 LTS.
- 20 GB livres para fontes, cache e compilação.
- Internet.
- 8 GB de RAM no computador hospedeiro como mínimo prático; 16 GB ou mais é confortável.
- QEMU ARM system emulado no Ubuntu.
- WSLg para janela gráfica. Sem WSLg, use o modo serial.

## Por que WSL?

Buildroot é um sistema de compilação Linux. O WSL fornece um ambiente Linux integrado ao Windows sem exigir uma máquina virtual Ubuntu completa.

## Instalação pelo PowerShell administrativo

```powershell
wsl --install -d Ubuntu-24.04
wsl --set-default-version 2
```

Reinicie se o Windows solicitar. Abra Ubuntu 24.04 e crie usuário e senha.

## Conferir WSL

No PowerShell:

```powershell
wsl --status
wsl -l -v
```

A coluna VERSION deve indicar `2` para Ubuntu.

## Instalar dependências

Dentro do Ubuntu:

```bash
cd ~/MRBE-Linux
chmod +x scripts/wsl/*.sh
./scripts/wsl/install-dev-tools.sh
```

## Conferir QEMU

```bash
qemu-system-aarch64 --version
qemu-system-aarch64 -machine help | grep -w virt
```

## WSLg

```bash
printf 'DISPLAY=%s\nWAYLAND_DISPLAY=%s\n' "$DISPLAY" "$WAYLAND_DISPLAY"
```

Se ambas estiverem vazias, a janela gráfica provavelmente não está disponível nessa sessão. O boot serial continua possível.
