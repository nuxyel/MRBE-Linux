# Seguranca e compliance do prototipo

## Riscos conhecidos
- Console root sem senha no perfil de desenvolvimento. Nao conectar em redes
  nao confiaveis nem habilitar SSH/telnet inadvertidamente.
- QEMU `-netdev user` usa NAT de usuario; nao ha encaminhamento de portas.
- Boot `-kernel` nao valida firmware assinado, secure boot nem BIOS MXQ Pro.
- Buildroot inclui dependencias com licencas e notices distintos; para
  redistribuir binarios, forneca fontes e avisos correspondentes e acompanhe
  CVEs. Gere a lista com `make legal-info` no Buildroot apos compilacao.
- OTA, armazenamento criptografado, autenticacao, sandbox de app e atualizacao
  de seguranca NAO estao implementados.

## Limites de marca e DRM
Google TV e Netflix sao nomes de terceiros. O launcher MRBE nao e certificado,
nao roda Android APK e nao inclui Widevine, Play Services ou bibliotecas de DRM.

## Operacoes proibidas no projeto sem validacao especifica
Nao flashar ROM, bootloader ou eMMC de MXQ Pro indeterminado; nao coletar
firmware de terceiros para publicar. Preservar backup privado e plano recovery.
