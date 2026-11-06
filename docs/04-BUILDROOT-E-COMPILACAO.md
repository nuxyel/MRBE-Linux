# 04 — Buildroot e compilação

## Versão fixada

O kit utiliza Buildroot 2025.02.19, uma versão da série LTS, para tornar os resultados mais reproduzíveis e evitar seguir automaticamente a versão de desenvolvimento.

## O que o Buildroot faz

O Buildroot prepara uma toolchain, compila o kernel e pacotes selecionados e gera o root filesystem. O kit mantém customizações no `br2-external` MRBE, separadas da árvore principal do Buildroot.

## Estrutura externa

- `external.desc`: identifica o projeto externo.
- `Config.in`: registra opções Kconfig do MRBE.
- `external.mk`: inclui receitas de pacotes.
- `configs/mrbe_qemu_aarch64_defconfig`: configuração da plataforma.
- `package/mrbe-launcher`: pacote C do launcher.
- `board/qemu-aarch64`: overlay e fragmento de kernel.

## Compilar

```bash
./scripts/wsl/build.sh
```

O script:
1. baixa Buildroot se ainda não existir;
2. cria a configuração MRBE;
3. compila toolchain, kernel, rootfs e launcher;
4. verifica os artefatos básicos.

## Saídas esperadas

```text
work/output/images/Image
work/output/images/rootfs.ext4
```

## Recompilar após alterar o código do launcher

A primeira forma simples é executar:

```bash
./scripts/wsl/build.sh
```

Se Buildroot não perceber uma alteração no pacote local, use no Ubuntu:

```bash
make -C work/buildroot-2025.02.19 \
  O="$PWD/work/output" \
  BR2_EXTERNAL="$PWD" \
  mrbe-launcher-dirclean

./scripts/wsl/build.sh
```

Se o nome do alvo não for reconhecido na versão usada, confira os alvos disponíveis em `make help` e envie a saída para diagnóstico.

## Limpar

`make clean` remove somente `work/output`. Isso força nova configuração/compilação, mas preserva o cache de downloads e a fonte Buildroot.
