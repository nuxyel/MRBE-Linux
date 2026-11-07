# MRBE TV OS 0.7.0

## Configuração Buildroot

### Problema identificado

Durante a compilação ARM64 foi observado:

```text
Makefile.legacy:9:
You have legacy configuration in your .config!
```

Uma das causas identificadas foi:

```text
BR2_PACKAGE_CURL=y
```

Para Buildroot 2025.02.19, a opção do
cliente curl é:

```text
BR2_PACKAGE_LIBCURL_CURL=y
```

### Procedimento de diagnóstico

Fazer backup:

```bash
cp work/output/.config \
  work/output/.config.backup
```

Executar migração:

```bash
./scripts/wsl/ensure-api-config.sh \
  work/output/.config
```

Atualizar configuração:

```bash
make -C work/buildroot-2025.02.19 \
  O="$PWD/work/output" \
  BR2_DL_DIR="$PWD/work/dl" \
  BR2_EXTERNAL="$PWD" \
  olddefconfig
```

Verificar opções legadas:

```bash
grep '^BR2_LEGACY=y' \
  work/output/.config
```

Se BR2_LEGACY continuar ativo,
não prossiga sem investigar os símbolos
obsoletos e os avisos do configurador.

### Cuidados

Não apagar work/.

Não executar make clean como primeira
tentativa de correção.

A atualização da configuração não comprova
que a compilação ARM64 terminou.
