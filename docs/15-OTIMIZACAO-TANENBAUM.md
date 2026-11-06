# Fase D — Performance e conceitos de Tanenbaum (alvo 1 GiB)

Referencial: Andrew S. Tanenbaum, *Modern Operating Systems* e *Structured
Computer Organization*. Uso aplicado de conceitos, sem reproduzir trechos do livro.

1. **Camadas e modularidade**: BootROM/firmware, kernel, init, aplicacao separados.
   Trocar launcher nao exige recompilar o kernel (seja no QEMU ou na placa).
2. **Politica versus mecanismo**: kernel cuida de escalonamento, MMU, E/S;
   launcher aplica foco e navegacao, nao cria servidor grafico completo.
3. **Espaco de memoria**: eliminar processos residentes desnecessarios; musl +
   BusyBox + C nativo em framebuffer, sem Electron, Chromium, GNOME ou XFCE.
4. **I/O**: framebuffer e evdev; desenho so quando muda selecao, nao 60 FPS.
5. **Concorrencia**: um processo de interface em primeiro plano; SysV Init simples.
6. **Medicao**: RAM QEMU -m 1024 e configuracao; sucesso real exige `free`,
   RSS, boot time, resposta do teclado e observacao de OOM em uso prolongado.
7. **Tradeoff**: usar `-Os` ajuda tamanho binario, nao garante latencia baixa.
8. **Capacidade**: video por software e streaming DRM normalmente precisam
   mais CPU, drivers e memoria; por enquanto fora do escopo.

## Metas propostas, ainda nao comprovadas
- Guest 1 GiB executa sem swap e sem OOM em idle.
- Launcher responde ao teclado em menos de 200 ms em condicoes de teste.
- Runtime estavel por 30 minutos de interacao.
- Comparar 512, 768 e 1024 MiB apenas **depois** de passar em 1024 MiB.

## Registrar desempenho
`free -m`, `cat /proc/meminfo`, `ps`, `dmesg | grep -i oom`.
Para latencia, registrar timestamps de entrada/evento e frame concluido;
ainda nao ha instrumentacao pronta. Nao inventar valores.
