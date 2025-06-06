import random
from abc import ABC, abstractmethod

class HabilidadeCuraMixin:
    def curar(self, alvo, quantidade):
        alvo.receber_cura(quantidade)
        print(f"{self.nome} curou {alvo.nome} em {quantidade} de HP!")

class Habilidade(ABC):
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @abstractmethod
    def usar(self, atacante, alvo):
        pass

class HabilidadeOfensiva(Habilidade):
    def __init__(self, nome, dano_base):
        super().__init__(nome)
        self._dano_base = dano_base

    def usar(self, atacante, alvo):
        dano_total = self._dano_base + (atacante.forca * 0.5)
        dano_total = max(1, int(dano_total))
        alvo.receber_dano(dano_total)
        print(f"{atacante.nome} usou {self.nome} em {alvo.nome} e causou {dano_total} de dano!")

class HabilidadeDefensiva(Habilidade):
    def __init__(self, nome, escudo):
        super().__init__(nome)
        self._escudo = escudo

    def usar(self, defensor, alvo=None): 
        defensor.aplicar_escudo(self._escudo)
        print(f"{defensor.nome} usou {self.nome} e ganhou {self._escudo} de escudo!")

class HabilidadeCurativa(Habilidade):
    def __init__(self, nome, cura_base):
        super().__init__(nome)
        self._cura_base = cura_base

    def usar(self, curador, alvo):
        cura_total = self._cura_base + (curador.forca * 0.2)
        cura_total = max(1, int(cura_total))
        alvo.receber_cura(cura_total)
        print(f"{curador.nome} usou {self.nome} em {alvo.nome} e curou {cura_total} de HP!")

class Personagem(ABC):
    def __init__(self, nome, vida_maxima, forca, defesa):
        self._nome = nome
        self._vida_maxima = vida_maxima
        self._vida_atual = vida_maxima
        self._forca = forca
        self._defesa = defesa
        self._habilidades = []
        self._escudo_atual = 0 

    @property
    def nome(self):
        return self._nome

    @property
    def vida_atual(self):
        return self._vida_atual

    @vida_atual.setter
    def vida_atual(self, valor):
        self._vida_atual = max(0, min(valor, self._vida_maxima))

    @property
    def vida_maxima(self):
        return self._vida_maxima

    @property
    def forca(self):
        return self._forca

    @forca.setter
    def forca(self, valor):
        self._forca = valor

    @property
    def defesa(self):
        return self._defesa

    @defesa.setter
    def defesa(self, valor):
        self._defesa = valor

    @property
    def esta_vivo(self):
        return self.vida_atual > 0

    @property
    def habilidades(self):
        return self._habilidades

    def receber_dano(self, dano):
        dano_real = dano
        if self._escudo_atual > 0:
            if dano >= self._escudo_atual:
                dano_real = dano - self._escudo_atual
                self._escudo_atual = 0
            else:
                self._escudo_atual -= dano
                dano_real = 0 
        
        if dano_real > 0:
            self.vida_atual -= dano_real
            print(f"{self.nome} sofreu {dano_real} de dano. HP atual: {self.vida_atual}/{self.vida_maxima}")
        else:
            print(f"{self.nome} bloqueou o dano com o escudo!")

        if self.vida_atual == 0:
            print(f"{self.nome} foi derrotado!")

    def receber_cura(self, cura):
        self.vida_atual += cura
        print(f"{self.nome} foi curado em {cura} HP. HP atual: {self.vida_atual}/{self.vida_maxima}")

    def aplicar_escudo(self, quantidade):
        self._escudo_atual += quantidade
        print(f"{self.nome} ganhou {quantidade} de escudo. Escudo atual: {self._escudo_atual}")

    def remover_escudo(self):
         if self._escudo_atual > 0:
            print(f"{self.nome} perdeu o escudo de {self._escudo_atual} pontos.")
            self._escudo_atual = 0

    @abstractmethod
    def atacar(self, inimigo):
        pass

    def usar_habilidade(self, alvo, habilidade_idx):
        if 0 <= habilidade_idx < len(self._habilidades):
            habilidade = self._habilidades[habilidade_idx]
            habilidade.usar(self, alvo) 
        else:
            print("Habilidade inválida!")
            return False
        return True

class Heroi(Personagem, HabilidadeCuraMixin):
    def __init__(self, nome):
        super().__init__(nome, vida_maxima=100, forca=20, defesa=10)
        self._nivel = 1
        self._xp = 0
        self._xp_para_prox_nivel = 100
        self._habilidades = [
            HabilidadeOfensiva("Golpe Poderoso", 25),
            HabilidadeCurativa("Cura Rápida", 20),
            HabilidadeDefensiva("Escudo Divino", 15)
        ]

    @property
    def nivel(self):
        return self._nivel

    @property
    def xp(self):
        return self._xp

    def ganhar_xp(self, quantidade):
        self._xp += quantidade
        print(f"{self.nome} ganhou {quantidade} XP! (Total: {self.xp}/{self._xp_para_prox_nivel})")
        while self._xp >= self._xp_para_prox_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self._nivel += 1
        self._xp -= self._xp_para_prox_nivel
        self._xp_para_prox_nivel = int(self._xp_para_prox_nivel * 1.5)
        self.vida_maxima += 20
        self.vida_atual = self.vida_maxima 
        self.forca += 5
        self.defesa += 3
        print(f"\n⭐ {self.nome} subiu para o nível {self.nivel}!")
        print(f"HP máximo: {self.vida_maxima}, Força: {self.forca}, Defesa: {self.defesa}")

    def atacar(self, inimigo):
        dano_base = self.forca - inimigo.defesa
        dano = max(1, dano_base + random.randint(-2, 2))
        inimigo.receber_dano(dano)
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, hp=80, ataque=15, defesa=5, recompensa_xp=50):
        super().__init__(nome, hp, ataque, defesa)
        self._recompensa_xp = recompensa_xp
        self._habilidades = [
            HabilidadeOfensiva("Mordida Venenosa", 10),
            HabilidadeOfensiva("Investida Brutal", 15)
        ]

    @property
    def recompensa_xp(self):
        return self._recompensa_xp

    def atacar(self, heroi):
        dano_base = self.forca - heroi.defesa // 2
        dano = max(1, dano_base + random.randint(-1, 1))
        heroi.receber_dano(dano)
        print(f"{self.nome} atacou {heroi.nome} e causou {dano} de dano!")

    def escolher_acao(self, heroi):
        if random.random() < 0.7 or not self.habilidades:
            return "atacar", None
        else:
            habilidades_ofensivas = [i for i, h in enumerate(self.habilidades) if isinstance(h, HabilidadeOfensiva)]
            if habilidades_ofensivas: 
                return "habilidade", random.choice(habilidades_ofensivas)
            else:
                return "atacar", None

class Batalha:
    def __init__(self, heroi, inimigo):
        self._heroi = heroi
        self._inimigo = inimigo

    def iniciar(self):
        print("\n--- INÍCIO DO COMBATE ---")
        print(f"{self._heroi.nome} vs. {self._inimigo.nome}")

        turno = 0
        while self._heroi.esta_vivo and self._inimigo.esta_vivo:

            print(f"\n=== Turno {turno + 1} ===")
            print(f"{self._heroi.nome} (Nível {self._heroi.nivel}): HP {self._heroi.vida_atual}/{self._heroi.vida_maxima} (Escudo: {self._heroi._escudo_atual})")
            print(f"{self._inimigo.nome}: HP {self._inimigo.vida_atual}/{self._inimigo.vida_maxima} (Escudo: {self._inimigo._escudo_atual})")
            
            self._turno_heroi()
            if not self._inimigo.esta_vivo: 
                break 

            print(f"\n{self._inimigo.nome} está agindo...")
            acao, index = self._inimigo.escolher_acao(self._heroi)
            
            if acao == "atacar":
                self._inimigo.atacar(self._heroi)
            elif acao == "habilidade":
                habilidade_selecionada = self._inimigo.habilidades[index]
                if isinstance(habilidade_selecionada, (HabilidadeCurativa, HabilidadeDefensiva)):
                     self._inimigo.usar_habilidade(self._inimigo, index)
                else:
                     self._inimigo.usar_habilidade(self._heroi, index)
            
            if not self._heroi.esta_vivo:
                break 

            if self._heroi._escudo_atual > 0:
                self._heroi.remover_escudo() 
            if self._inimigo._escudo_atual > 0:
                self._inimigo.remover_escudo() 
            
            turno += 1

        self._verificar_vencedor()
        
    def _turno_heroi(self):
        print(f"\n{self._heroi.nome}, escolha sua ação:")
        print("1. Atacar")
        print("2. Usar Habilidade")
        
        escolha = input("Sua escolha: ")
        if escolha == "1":
            self._heroi.atacar(self._inimigo)
        elif escolha == "2":
            if not self._heroi.habilidades:
                print("Você não possui habilidades para usar!")
                return
            print("Habilidades:")
            for i, hab in enumerate(self._heroi.habilidades):
                print(f"[{i}] {hab.nome}")
            try:
                habilidade_idx = int(input("Escolha uma habilidade: "))
                if not (0 <= habilidade_idx < len(self._heroi.habilidades)):
                    print("Habilidade inválida! Tente novamente.")
                    return
                
                habilidade_selecionada = self._heroi.habilidades[habilidade_idx]

                if isinstance(habilidade_selecionada, (HabilidadeCurativa, HabilidadeDefensiva)):
                    self._heroi.usar_habilidade(self._heroi, habilidade_idx)
                else:
                    self._heroi.usar_habilidade(self._inimigo, habilidade_idx)

            except ValueError:
                print("Entrada inválida. Digite um número.")
        else:
            print("Escolha inválida. Você perdeu seu turno!")

    def _verificar_vencedor(self):
        print("\n--- FIM DO COMBATE ---")
        if self._heroi.esta_vivo:
            self._heroi.ganhar_xp(self._inimigo.recompensa_xp)
            print(f"\n🎉 {self._heroi.nome} venceu a batalha e ganhou {self._inimigo.recompensa_xp} XP!")
        else:
            print(f"\n💀 {self._inimigo.nome} venceu a batalha!")