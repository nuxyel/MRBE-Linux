# Fase F — Publicar MRBE Linux no GitHub

## Preparar e revisar
O ZIP contem fontes, **nao** `work/output`, dumps de ROM, chaves ou flash.
Verifique `git status`, licenca e segredos antes de enviar arquivos publicamente.

## Criar repositorio no GitHub
Na interface web: New repository -> `MRBE-Linux` -> Public -> Create.
Nao adicione README remoto (ja existe local).

## Terminal Ubuntu na pasta do projeto

```bash
git init
git switch -c main
git add .
git status
git commit -m "feat: MRBE Linux TV 0.2.0 ARM64 QEMU DevKit"
git remote add origin https://github.com/SEU-USUARIO/MRBE-Linux.git
git push -u origin main
```

O GitHub nao aceita senha de conta em `git push` por HTTPS: use fluxo de
credenciais do GitHub CLI (`gh auth login`) ou token de acesso com escopo minimo.
Nunca coloque token, senha ou dump de firmware no repositorio.

## Release
Marque apenas o codigo-fonte: `git tag v0.2.0; git push origin v0.2.0`.
**Nao** chame de imagem bootavel homologada antes dos testes T03–T08.

## Licenciamento
MIT para o codigo launcher e docs originais deste pacote; kernel Linux,
BusyBox e outros componentes ficam sob licencas proprias. Consulte
`docs/19-SEGURANCA-E-LICENCAS.md`.
