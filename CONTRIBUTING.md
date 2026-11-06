# Como contribuir
1. Abra issue incluindo QEMU/WSL/Ubuntu, arquitetura, comando e log de erro.
2. Crie branch, adicione testes e documente a alteracao.
3. Rode `make test`; se tiver Buildroot compilado, rode `make smoke` e anexe log.
4. Proponha PR com reproduzir, resultado esperado e obtido; indique se teste de boot foi executado.
5. Nao inclua BIOS/ROM/DTB de terceiro, chaves privadas, APKs comerciais, tokens ou imagem proprietaria.
6. Codigo C deve compilar com `-Wall -Wextra -Werror`; scripts shell devem passar `bash -n`.
7. Uso de marcas de plataformas de terceiros apenas descritivo; o MRBE e independente.
