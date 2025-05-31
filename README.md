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
 - Para ocorrer um combate, o herói e o inimigo precisam estar definidos e vivos.
    
Fluxo Principal(Turno a Turno):
 - O sistema inicia o combate e exibe a situação inicial (HP do Herói e do Inimigo).
 - Vez do Herói:
    - O sistema exibe as opções de ação do Herói (Atacar, Usar Habilidade).
    - Atacar:
      - O sistema calcula e aplica o dano do Herói no Inimigo, exibindo o resultado do ataque.
    - Usar Habilidade:
      - O sistema lista as habilidades disponíveis do Herói.
      - O jogador escolhe uma habilidade pelo índice.
      - O sistema executa a habilidade (aplicando dano ao Inimigo, curando o Herói, aplicando escudo, etc.) e exibe o resultado da ação.
 - O sistema verifica se o Inimigo foi derrotado. Se sim, o combate termina (Fluxo Alternativo 2).
 - Vez do Inimigo:
    - O sistema escolhe a ação do Inimigo (Atacar ou Usar Habilidade).
    - O sistema executa a ação do Inimigo (aplicando dano ao Herói ou usando uma habilidade) e exibe o resultado da ação.
 - O sistema verifica se o Herói foi derrotado. Se sim, o combate termina (Fluxo Alternativo 3).
 - O combate continua para o próximo turno (passo 2 reinicia).

Fluxos Alternativos:

 - 1: Escolha de Ação Inválida do Herói:
   - Na hora de escolher entre atacar ou usar habilidade, caso o jogador insira uma escolha inválida o sistema informará e o Herói perderá o turno.
   - O fluxo principal continua após isso.
 - 2: Inimigo Derrotado:
   - Quando o inimigo tiver 0 HP, O sistema informará que o Inimigo foi derrotado.
   - O Herói ganha experiência (XP).
   - O sistema verifica se o Herói subiu de nível (Fluxo de Inclusão 3).
   - O combate termina e o jogo avança para o próximo inimigo ou encerra.
 - 3: Herói Derrotado:
   - Quando o herói tiver 0 HP, O sistema informará que o herói foi derrotado.
   - O jogo exibe "GAME OVER!" e encerra.
  
3. Subir de Nível (Incluído em "Participar de Combate")
 - Ator Principal: Sistema
 - Objetivo: Aprimorar os atributos do Herói quando ele acumula XP suficiente.

 - Para ser possível subir de nível:
  - O Herói tem que estar vivo.
  - O Herói tem que ganhar XP.

Fluxo Principal:

 - O sistema verifica se o XP atual do Herói é maior ou igual ao XP necessário para o próximo nível.
 - Se sim:
   - O sistema incrementa o nível do Herói. Tendo feito isso, subtrai o XP necessário do XP atual do herói.
   - O sistema calcula o novo XP necessário para o próximo nível.
   - O sistema aumenta os atributos do Herói (HP máximo, força, defesa) e cura totalmente o HP do herói.
   - O sistema exibe uma mensagem de "Subiu de Nível" com os novos atributos.
   - O sistema verifica mais uma vez se o XP restante é suficiente para outro nível.
 - Se não:
   - Nada é feito.

## Diagrama de Classes  
![Diagrama de Classes](diagramadecl![diagramadeclasse](https://github.com/user-attachments/assets/5dc5c34f-6a61-4af1-b79e-0d4504ef5750)
asse.png)
