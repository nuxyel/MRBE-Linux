# 00 — Primeiros passos (leia antes de executar)

Este guia foi escrito para quem nunca compilou um Linux embarcado.

## O que será criado

O Buildroot será baixado e compilado dentro do Ubuntu no WSL. O resultado será:
- `work/output/images/Image`: kernel ARM64.
- `work/output/images/rootfs.ext4`: sistema de arquivos raiz.
- `work/output/.config`: configuração aplicada.
- `work/dl/`: cache de fontes baixadas.

O computador Windows é o hospedeiro. O Linux ARM64 é o convidado simulado pelo QEMU.

## Etapa A — Instalar WSL 2

1. Abra o menu Iniciar.
2. Digite PowerShell.
3. Clique com o botão direito e escolha “Executar como administrador”.
4. Entre na pasta do kit no Windows ou execute o script:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\windows\Install-WSL.ps1
```

5. Se solicitado, reinicie o Windows.
6. Abra “Ubuntu 24.04” pelo menu Iniciar.
7. Na primeira abertura, crie um nome de usuário Linux e uma senha. Ao digitar a senha, nada aparece na tela; isso é normal.

Se o comando `wsl --install` informar que o WSL já existe, não remova sua distribuição atual. Confira `wsl -l -v` e adapte o nome da distribuição nos comandos posteriores.

## Etapa B — Colocar o projeto no disco Linux do WSL

É importante compilar no sistema de arquivos Linux do WSL, e não em `/mnt/c`, porque o Buildroot cria muitos arquivos pequenos e a compilação em NTFS pode ficar muito lenta.

No Ubuntu:

```bash
cd ~
explorer.exe .
```

O Explorador de Arquivos abrirá a pasta pessoal do Ubuntu. Copie para ela a pasta `MRBE-Linux` extraída do ZIP. O resultado deve ser `\home\seu_usuario\MRBE-Linux` dentro do Ubuntu (não crie outra pasta MRBE-Linux dentro dela).

Volte ao Ubuntu:

```bash
cd ~/MRBE-Linux
ls
```

Você deve ver `README.md`, `PRD.md`, `configs`, `docs`, `package` e `scripts`.

## Etapa C — Instalar o ambiente de desenvolvimento

```bash
cd ~/MRBE-Linux
chmod +x scripts/wsl/*.sh
./scripts/wsl/install-dev-tools.sh
```

O script instala compilador, Make, ferramentas exigidas pelo Buildroot e QEMU ARM64 com backend gráfico.

## Etapa D — Compilar

```bash
./scripts/wsl/build.sh
```

A primeira compilação baixa o Buildroot, kernel e pacotes. Precisa de internet e pode levar bastante tempo. Não feche o Ubuntu durante a compilação.

Para reduzir a carga do computador:

```bash
JOBS=2 ./scripts/wsl/build.sh
```

Para usar mais núcleos, por exemplo:

```bash
JOBS=6 ./scripts/wsl/build.sh
```

Não use um número maior que a quantidade de núcleos lógicos disponíveis sem necessidade.

## Etapa E — Verificar o resultado

```bash
./scripts/wsl/check-build.sh
```

Devem existir:
- `work/output/images/Image`
- `work/output/images/rootfs.ext4`

## Etapa F — Primeiro boot em console

```bash
./scripts/wsl/run-qemu-console.sh
```

O login aparecerá no terminal serial. O console serve para confirmar kernel, montagem do rootfs e init. Entre como `root` se o sistema não tiver sido configurado com senha.

Comandos úteis no guest:

```sh
uname -a
cat /proc/meminfo
free
mrbe-diagnostico
```

Para encerrar o QEMU, use `Ctrl+A` e depois `X` se o console estiver multiplexado. Se isso não funcionar, use `Ctrl+C` no terminal que iniciou o QEMU.

## Etapa G — Abrir a janela gráfica

Se seu Windows/WSL oferece WSLg, no Ubuntu:

```bash
echo "$DISPLAY"
echo "$WAYLAND_DISPLAY"
```

Se pelo menos uma variável estiver preenchida:

```bash
./scripts/wsl/run-qemu-gui.sh
```

A janela deve abrir. O launcher aparecerá somente se o kernel criar `/dev/fb0` e o dispositivo de entrada virtual for detectado.

## Se algo der errado

Não execute `make clean` imediatamente. Copie:
- o comando que executou;
- as últimas 50 a 100 linhas do erro;
- saída de `wsl -l -v`;
- saída de `qemu-system-aarch64 --version`.

Envie isso para análise. Não tente gravar a imagem no MXQ Pro.
