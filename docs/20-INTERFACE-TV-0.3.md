# MRBE Linux TV 0.3.0 — Interface de TV

## O que foi implementado

O launcher leve em C foi reescrito com interface de navegação para televisão:

- **Home:** barra de categorias, destaque principal com arte procedural, dois botões, catálogos horizontais e marca MRBE TV.
- **Apps:** grade de dez cartões de demonstracao, responsivos às setas e Enter.
- **Configurações:** oito seções navegáveis com painéis informativos e ações perigosas desativadas.
- **Barra superior:** Pesquisar, Para você, Filmes, Séries, Apps e Biblioteca. Algumas abas são demonstrativas.
- **Navegação:** setas, Enter, Esc/Backspace; atalhos H (Home), A (Apps), S (Configurações).
- **UI sem navegador:** desenho pelo framebuffer Linux `/dev/fb0`, sem bibliotecas gráficas extras, sem assets proprietários e sem serviços do Google.

## Diferença do Google TV

O design é **inspirado no padrão de interface usado em smart TVs**. Não é uma cópia do Google TV, não executa Android e não inclui Play Store, aplicativos reais ou reprodução de streaming protegida. A interface e o conteúdo demonstrativo são originais do MRBE Linux.

## Atualizar a instalação 0.2.0 do WSL

**Pré-condição:** o projeto 0.2.0 já está instalado em `~/MRBE-Linux` e você já compilou o sistema uma vez.

1. Copie `MRBE_Linux_0_3_0.zip` para `/home/renan` usando `explorer.exe .` (no terminal do Ubuntu).
2. Execute no Ubuntu:

```bash
cd ~
unzip -o MRBE_Linux_0_3_0.zip -d ~
cd ~/MRBE-Linux
chmod +x scripts/wsl/*.sh scripts/dev/*.sh
make test
JOBS=2 make ui-rebuild
make check
make smoke
make gui
```

O ZIP não inclui a pasta `work/`, portanto conserva a toolchain, o kernel e os downloads previamente compilados. O comando `make ui-rebuild` invalida **somente o pacote de launcher**, reutilizando a base existente e reconstruindo as imagens necessárias para incorporar o novo binário. Na primeira compilação, se não houver Buildroot instalado, os arquivos faltantes serão baixados e compilados.

Os scripts `build.sh` normalizam o `PATH` para evitar caminhos do Windows com espaços no WSL e dão preferência ao GNU `install` quando a distribuição apresenta o problema conhecido do `uutils install`.

## Teste de navegação

- Abrir `make gui` após `make smoke`.
- Na Home: `↓` entra no destaque, outro `↓` seleciona a primeira fileira. `←`/`→` escolhem cartões. `↓` percorre fileiras.
- `Enter` exibe aviso demonstrativo. Na terceira fileira, `Enter` abre o catálogo de Apps.
- `A` abre a grade Apps. `S` abre Configurações. `H` volta à Home. `Esc` volta ou coloca foco no menu superior.
- Botões Reiniciar/Desligar **não executam ações** nesta versão.

## Testes e prévia

```bash
make test
make preview
```

Arquivos: `docs/preview-mrbe-tv.png`, `docs/preview-mrbe-apps.png` e `docs/preview-mrbe-settings.png` (quando Pillow estiver instalado).

## Limitações conhecidas

A tipografia é bitmap 5x7, sem fontes externas, para simplicidade. A arte é procedural, não inclui pôsteres licenciados. O layout é desenhado na área de referência 1280×720 e escalado de acordo com o framebuffer informado por `/dev/fb0`; resoluções muito baixas podem reduzir a legibilidade. Entrada via `evdev` do kernel; não há busca real nem instalação de apps. O QEMU ARM64 deve ser executado no computador do usuário para validar boot e interface gráfica 0.3.0.

## Como obter logs se algo falhar

```bash
tail -n 80 ~/MRBE-Linux/work/build.log
cat ~/MRBE-Linux/logs/testes/qemu-smoke-latest.json
tail -n 80 ~/MRBE-Linux/logs/testes/qemu-boot-latest.log
```
