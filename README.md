# RPG Ilha do Medo

## Descrição do Problema
O jogo apresenta batalhas em turnos entre um herói(criado pelo usuário) e uma sequência de inimigos. O herói tem a possibilidade de escolher entre atacar ou usar habilidades(ofensivas, defensivas ou de cura). Por outro lado, os inimigos atacam ou usam suas próprias habilidades. Quando derrotado o inimigo, o herói ganha experiência, podendo subir de nível e tornando-se mais forte para os desafios futuros.

## Casos de Uso
1. Início do Jogo
 - Ator Principal: Jogador
 - Objetivo: Criação do personagem.

Fluxo Principal:

 - O jogador inicia o programa.
 - O sistema exibe uma mensagem de boas-vindas.
 - O sistema pede um nome para o herói.
 - O sistema pede que o jogador escolha uma classe para o herói, a qual pode ser Guerreiro, Mago ou Clérigo.
 - O sistema cria e exibe os atributos iniciais do herói.
 - O jogo entra no loop de combate contra o primeiro inimigo.

Fluxos Alternativos:

 - Escolha de Classe Inválida:
    - Caso o jogador escolha uma opção inválida na escolha de classe do herói, o sistema informa que aquela opção não é válida e define o herói como Guerreiro Padrão.
    - Após isso, o fluxo principal continua.
   
2. Combates
 - Ator Principal: Jogador, Sistema(controlando o Inimigo)
 - Objetivo: Simular um confronto por turnos entre o Herói e um Inimigo até que um dos dois seja derrotado.

 - Pré-condições:

  - Um Herói e um Inimigo estão definidos e ativos.
  - Ambos estão vivos.
    
Fluxo Principal (Turno a Turno):

O sistema inicia o combate e exibe a situação inicial (HP do Herói e Inimigo).
Turno do Herói: a. O sistema exibe as opções de ação do Herói (Atacar, Usar Habilidade). b. O jogador escolhe uma ação. c. Se "Atacar": i. O sistema calcula e aplica o dano do Herói no Inimigo. ii. O sistema exibe o resultado do ataque. d. Se "Usar Habilidade": i. O sistema lista as habilidades disponíveis do Herói. ii. O jogador escolhe uma habilidade pelo índice. iii.O sistema executa a habilidade (aplicando dano ao Inimigo, curando o Herói, aplicando escudo, etc.). iv. O sistema exibe o resultado da habilidade.
O sistema verifica se o Inimigo foi derrotado. Se sim, o combate termina (Fluxo Alternativo A2).
Turno do Inimigo: a. O sistema decide a ação do Inimigo (Atacar ou Usar Habilidade), baseando-se em sua IA simples. b. O sistema executa a ação do Inimigo (aplicando dano ao Herói ou usando uma habilidade). c. O sistema exibe o resultado da ação do Inimigo.
O sistema verifica se o Herói foi derrotado. Se sim, o combate termina (Fluxo Alternativo A3).
O combate continua para o próximo turno (volta ao passo 2).
Pós-condições:

Um dos combatentes (Herói ou Inimigo) tem 0 HP ou menos.
Fluxos Alternativos:

A1: Escolha de Ação Inválida do Herói:
No passo 2b, o jogador insere uma escolha inválida.
O sistema informa que a escolha é inválida e o Herói perde o turno.
O fluxo principal continua no passo 3.
A2: Inimigo Derrotado:
No passo 3, o Inimigo tem 0 HP.
O sistema informa que o Inimigo foi derrotado.
O Herói ganha experiência (XP).
O sistema verifica se o Herói subiu de nível (Fluxo de Inclusão UC.3).
O combate termina e o jogo avança para o próximo inimigo ou encerra.
A3: Herói Derrotado:
No passo 5, o Herói tem 0 HP.
O sistema informa que o Herói foi derrotado.
O jogo exibe "GAME OVER!" e encerra.
3. Caso de Uso: Subir de Nível (Incluído em "Participar de Combate")
Ator Principal: Sistema

Objetivo: Aprimorar os atributos do Herói quando ele acumula XP suficiente.

Pré-condições:

O Herói está vivo.
O Herói ganhou XP.
Fluxo Principal:

O sistema verifica se o XP atual do Herói é maior ou igual ao XP necessário para o próximo nível.
Se sim: a. O sistema incrementa o nível do Herói. b. O sistema subtrai o XP necessário do XP atual do Herói. c. O sistema calcula o novo XP necessário para o próximo nível (aumenta progressivamente). d. O sistema aumenta os atributos do Herói (HP máximo, força, defesa). e. O sistema cura totalmente o HP do Herói. f. O sistema exibe uma mensagem de "Subiu de Nível" com os novos atributos. g. O sistema verifica novamente se o XP restante é suficiente para outro nível (para subir múltiplos níveis de uma vez).
Se não: Nenhuma ação é tomada.
Pós-condições:

Os atributos do Herói podem ter sido aprimorados.
O XP necessário para o próximo nível pode ter sido recalculado.
