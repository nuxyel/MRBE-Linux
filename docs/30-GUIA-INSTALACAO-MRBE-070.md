# MRBE TV OS 0.7.0

## Guia de instalação em outra máquina

### Objetivo

Instalar o ambiente de desenvolvimento,
compilar o MRBE TV OS e executar no QEMU ARM64.

### Ambiente recomendado

- Windows 11
- WSL2
- Ubuntu 24.04 LTS
- Git
- GCC e Make
- Python 3
- QEMU ARM64
- Buildroot 2025.02.19

O Ubuntu 26.04 ainda requer validação
adicional com o Buildroot utilizado.

### Instalar WSL

No PowerShell como administrador:

```powershell
wsl --install -d Ubuntu-24.04
wsl --update
```

### Clonar a versão publicada

No terminal Ubuntu:

```bash
cd ~

git clone \
  --branch fix/mrbe-0.7.0-20261106-185934 \
  --single-branch \
  https://github.com/renanassuncao/MRBE-Linux.git

cd MRBE-Linux
```

### Instalar dependências

```bash
chmod +x scripts/wsl/*.sh
chmod +x scripts/dev/*.sh

make setup
```

### Executar testes

```bash
make api-test
make test
```

### Compilar o sistema

```bash
JOBS=2 make ui-rebuild
```

### Verificar a imagem

```bash
make check
make smoke
```

### Executar a interface gráfica

```bash
make gui
```

### Diagnóstico dentro do QEMU

```sh
mrbe-healthcheck
mrbe-api-test
```

### Estabilidade

```sh
MRBE_STABILITY_DURATION=300 \
MRBE_STABILITY_API_INTERVAL=60 \
mrbe-stability-test
```

Consultar relatório:

```sh
cat /var/log/mrbe-stability.log
```

### Limitações

A imagem QEMU virt ARM64 não é firmware
para a TV Box Amlogic S905X3.

Os aplicativos de streaming apresentados
na interface ainda não possuem integração
oficial de reprodução e DRM.

A pasta work/ não deve ser enviada ao GitHub.
