# MRBE TV OS 0.7.0

## Qualidade, estabilidade e APIs

### Evidências de 06/11/2026

Testes de API no Ubuntu:

- 13 executados;
- 12 aprovados;
- 1 ignorado pela ausência de BusyBox.

Testes gerais:

- 33 executados;
- 32 aprovados;
- 1 ignorado.

### Componentes avaliados

- Código C;
- Scripts Bash;
- Interface gráfica local;
- Navegação;
- Assets;
- HTTP e HTTPS simulados;
- Validação TLS;
- Respostas JSON.

### Pendências

- Compilação ARM64 concluída;
- Inicialização da versão atualizada no QEMU;
- API HTTPS externa dentro do QEMU;
- Estabilidade de 300 segundos;
- Verificação de consumo de memória.

### Critérios de homologação

A versão deve:

1. Compilar sem erros.
2. Inicializar a interface no QEMU.
3. Reconhecer teclado e mouse.
4. Comunicar-se por HTTPS.
5. Validar corretamente certificados TLS.
6. Manter o launcher funcionando.
7. Concluir o monitoramento de estabilidade.

Os testes locais não substituem
a homologação no QEMU ou no hardware físico.
