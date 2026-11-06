# MRBE Linux TV 0.4.0 — Identidade visual e atualizacao

## Objetivo
Aplicar o brasao MRBE como identidade visual do sistema, preservando a base Buildroot + Linux ARM64 + QEMU que ja foi iniciada pelo usuario. Esta versao atualiza o launcher framebuffer; nao e ainda a migracao para LVGL.

## Elementos da marca
- Brasao: escudo metalico, coroa, monitor com simbolo de reproducao, mascote Linux e ramos de louro.
- Carvao: fundo principal e paineis.
- Verde-esmeralda: superficies e acentos de sistema.
- Ouro: foco, selecao, divisores e detalhes da marca.
- Prata: texto secundario e detalhes metalicos.

## Arquivos de identidade
- `arte/identidade-visual/brasao-mrbe-original.png`: imagem original gerada.
- `arte/identidade-visual/brasao-mrbe-transparente.png`: versao com fundo removido.
- `arte/identidade-visual/brasao-mrbe-256.png`: versao otimizada para uso em interface.
- `package/mrbe-launcher/src/assets/brasao-256.rgba`: RGBA8888 cru, 256 x 256, usado pelo launcher sem dependencia PNG.

## Como o logo entra no sistema
O pacote `mrbe-launcher` instala o asset em `/usr/share/mrbe/brand/brasao-256.rgba`. O launcher carrega 256 x 256 pixels RGBA e o reduz por software para o cabecalho, hero e painel Sobre. Se o asset nao estiver disponivel, usa um emblema vetorial de fallback.

## Atualizar uma instalacao 0.3.0 sem perder o Buildroot
1. Baixe `MRBE_Linux_0_4_0.zip` e copie para a pasta pessoal do Ubuntu/WSL.
2. No Ubuntu, execute:

```bash
cd ~
unzip -o MRBE_Linux_0_4_0.zip -d ~
cd ~/MRBE-Linux
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
make test
JOBS=2 make ui-rebuild
make check
make smoke
make gui
```

Nao apague `work/`: ela contem o Buildroot, downloads, toolchain e compilacao anterior. O script detecta a alteracao em `src/` (incluindo o RGBA) e invalida apenas o pacote `mrbe-launcher`, preservando kernel e toolchain.

## O que deve ser observado no QEMU
- Brasao pequeno no canto superior esquerdo.
- Nome MRBE e selo TV ao lado do brasao.
- Paleta carvao/esmeralda/ouro/prata nas tres telas.
- Brasao em tamanho maior no painel de destaque e em Configuracoes.
- Navegacao por setas, Enter, Esc e atalhos H/A/S continua igual.

## Validacao e limitacoes
- `make test` valida sintaxe, maquina de estados, instalacao do asset e previsualizacoes host.
- `make smoke` valida o boot da imagem real no QEMU; precisa ser executado no computador do usuario.
- `make gui` valida a janela e a aparencia no QEMU; precisa de WSLg ou servidor grafico funcional.
- O launcher ainda usa fonte bitmap 5x7 e desenhos procedurais. A migracao para LVGL e a etapa 0.5, com fonte Noto Sans, imagens de catalogo e backend fbdev no equipamento; SDL2 sera usado apenas no simulador de desenvolvimento.
- Os cartoes e aplicativos continuam demonstrativos. Nao ha Netflix, Play Store, DRM ou streaming implementados.
- O QEMU `virt` ARM64 nao emula a ROM/bootloader da placa MXQ Pro.

## Referencias tecnicas
- LVGL Linux framebuffer: https://lvgl.io/docs/open/9.1/integration/driver/display/fbdev
- LVGL Linux ports (SDL2, fbdev, DRM/KMS): https://github.com/lvgl/lv_port_linux
