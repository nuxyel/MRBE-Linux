# 02 — Princípios de projeto inspirados em Tanenbaum

Referência conceitual: Andrew S. Tanenbaum e Herbert Bos, *Modern Operating Systems* / *Sistemas Operacionais Modernos*.

Este projeto não implementa um kernel novo nem afirma ser um microkernel. Ele usa o kernel Linux e aplica princípios de projeto de sistemas operacionais.

## Modularidade

Cada subsistema possui responsabilidade definida:
- `fb.c`: acesso ao framebuffer;
- `input.c`: leitura de eventos;
- `font.c`: fonte bitmap;
- `ui.c`: composição da tela;
- `main.c`: ciclo principal e coordenação.

## Separação de mecanismos e políticas

O kernel fornece mecanismos (memória virtual, processos, drivers, arquivos e entrada). O launcher decide a política da interface (qual cartão está selecionado e o que mostrar).

## Separação de responsabilidades

O launcher não configura diretamente rede, monta discos ou administra o kernel. Serviços de sistema cuidam dessas tarefas. Uma falha de interface não deve exigir alterações no kernel.

## Simplicidade e auditabilidade

Menos dependências significam menos componentes para atualizar, menos serviços residentes e uma superfície menor de falhas. Isso não substitui atualizações de segurança.

## Gerenciamento de memória

- Evitar caches ilimitados.
- Alocar buffers gráficos de forma previsível.
- Não manter múltiplas cópias de imagens grandes.
- Medir RSS e memória disponível no guest.
- Tratar 1 GiB como orçamento total, não como memória disponível para o launcher.

## Não confundir meta com medição

O orçamento de memória será registrado em testes. Não se declara “consumo de 300 MiB” antes de medir a imagem real.
