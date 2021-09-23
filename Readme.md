# Agente Iago 

## Grupo

| Nome                       | Matrícula | Turma |
|----------------------------|-----------|-------|
| Garrenlus de Souza         |  00315521 |     A |
| Júlia Pelayo Rodrigues     |  00315868 |     A |
| Leonardo Rodrigues Pedroso |  00265001 |     A | 

## Função de avaliação 

Para a função de avaliação consideramos que o jogo tem 3 etapas: o ínicio (primeiras 20 jogadas), o meio (próximas 20 jogadas) e o final (demais jogadas até o fim). No ínicio e no final do jogo buscamos maximizar o número de peças do jogador e minimizar o número de peças do oponente (utilidade() = # peças do jogador/# peças do oponente), já no meio do jogo buscamos maximizar a mobilidade do jogador (utilidade() = # movimentos possiveis do jogador/# movimentos possíveis do oponente).

## Estratégia de parada

Usamos uma estratégia de profundidade fixa e também há um teste de tempo para verificar se a escolha do movimento está próxima do tempo limite e então encerrar a busca. 

## Dificuldades encontradas

Após a implementação do teste do tempo restante de decisão houve uma tentativa de aumentar significativamente a profundidade máxima de busca, mas isto não apresentou resultados bons para o desempenho (este novo agente perdeu para o anterior). Houve também uma tentativa de implementar uma estratégia de parada com profundidade iterativa, mas devido às dificuldades de implementação encontradas, e como também não sabíamos se isto ia aumentar significativamente o desempenho do agente, julgamos desnecessário a implementação desta estratégia.

## Bibliografia 

- [1] Materiais da disciplina 
- [2] D. E. Moriarty and R. Miikkulainen, “Discovering Complex Othello Strategies through Evolutionary Neural Networks,” Connection Sc., vol. 7, no. 3, pp. 195–210, Jan. 1995, doi: 10.1080/09540099550039228.
- [3] “Computer Othello” Wikipedia. Jun. 12, 2021. Accessed: Sep. 22, 2021. [Online]. Available: https://en.wikipedia.org/w/index.php?title=Computer_Othello&oldid=1028246377
- [4] B. Rose, Othello: A Minute to Learn... A Lifetime to Master. 

