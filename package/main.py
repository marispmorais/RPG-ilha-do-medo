from game_classes import Heroi, Inimigo, Batalha

def jogar_rpg():
    print("Seja bem-vindo à ilha do medo! Você está pronto para uma aventura?!")
    nome_jogador = input("Digite o nome do seu herói: ")
    heroi = Heroi(nome_jogador)

    print(f"\nVocê escolheu: {heroi.nome} - Nível {heroi.nivel}!")
    print(f"HP: {heroi.vida_atual}/{heroi.vida_maxima}, Força: {heroi.forca}, Defesa: {heroi.defesa}")

    inimigos = [
        Inimigo("Grompe", hp=60, ataque=12, defesa=4, recompensa_xp=30),
        Inimigo("Azuporã", hp=90, ataque=18, defesa=6, recompensa_xp=50),
        Inimigo("Vastilarva", hp=120, ataque=25, defesa=8, recompensa_xp=80),
        Inimigo("Dragão Ancião", hp=200, ataque=35, defesa=15, recompensa_xp=150)
    ]

    for inimigo in inimigos:
        if not heroi.esta_vivo:
            print("\nGAME OVER! Não foi dessa vez...")
            break

        print(f"\n\n=== PRÓXIMA BATALHA: {inimigo.nome.upper()} ===")
        batalha = Batalha(heroi, inimigo)
        batalha.iniciar()

    if heroi.esta_vivo:
        print("\n🏆 Parabéns! Você derrotou todos os inimigos e se tornou um lendário herói!")
    else:
        print("\nObrigado por jogar!")

if __name__ == "__main__":
    jogar_rpg()