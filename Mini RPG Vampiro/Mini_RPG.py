# Definindo o herói e o monstro
import random
print("="*40)
print("     🩸 REINO DOS VAMPIROS 🩸     ")
print("="*40)

# 1. Escolha do Nome
nome_vampiro = input("✨ Como você é chamado nas sombras? ").capitalize()

# 2. Definição das Classes com Fé e Sorte
# Atributos: Vida 💖 | Força 💪 | Res 🛡️ | Agi ⚡ | Sangue 🍷 | Fé ⛪ | Sorte 🍀
classes = {
    "1": {"nome": "Caminhante da Noite", "vida": 100, "força": 15, "res": 10, "agi": 10, "sangue": 10, "fé": 5,  "sorte": 5},
    "2": {"nome": "Lorde Sanguinário",  "vida": 120, "força": 22, "res": 15, "agi": 5,  "sangue": 5,  "fé": 2,  "sorte": 3},
    "3": {"nome": "Sombra Veloz",       "vida": 85,  "força": 12, "res": 5,  "agi": 25, "sangue": 10, "fé": 4,  "sorte": 12},
    "4": {"nome": "Feiticeiro de Sangue","vida": 75,  "força": 7,  "res": 5,  "agi": 10, "sangue": 35, "fé": 15, "sorte": 8},
    "5": {"nome": "Gárgula Imortal",    "vida": 160, "força": 18, "res": 30, "agi": 2,  "sangue": 2,  "fé": 10, "sorte": 1},
    "6": {"nome": "Rejeitado",    "vida": 90, "força": 10, "res": 7, "agi": 4,  "sangue": 8,  "fé": 5, "sorte": 2}
}

print("\n📜 Escolha sua linhagem vampírica:")
print("Atributos: Vida 💖 | Força 💪 | Agi ⚡ | Fé ⛪ | Sorte 🍀")
for num, info in classes.items():
    print(f"{num}. {info['nome']} \n   (💖 {info['vida']} | 💪 {info['força']} | ⚡ {info['agi']} | ⛪ {info['fé']} | 🍀 {info['sorte']})")

escolha = input("\n👉 Digite o número da sua classe: ")

# Validação simples
if escolha not in classes:
    print("\n⚠️  Linhagem desconhecida... Você renasceu como um Rejeitado.")
    escolha = "6"

# 3. Criando o Jogador
classe_sel = classes[escolha]

jogador = {
    "nome": nome_vampiro,
    "classe": classe_sel["nome"],
    "vida": classe_sel["vida"],
    "vida_max": classe_sel["vida"],
    "força": classe_sel["força"],
    "resistencia": classe_sel["res"],
    "agilidade": classe_sel["agi"],
    "sangue": classe_sel["sangue"],
    "fé": classe_sel["fé"],
    "sorte": classe_sel["sorte"],
    "exp": 0,          
    "nivel": 1,
    "poderes": [],
    "escolhas_feitas": [] # <--- AQUI: Para salvar o histórico da história
}


print("\n" + "—"*30)
print(f"🧛 FICHA DO VAMPIRO")
print(f"👤 Nome: {jogador['nome']}")
print(f"🩸 Linhagem: {jogador['classe']}")
print(f"💖 Vida: {jogador['vida']}")
print(f"💪 Força: {jogador['força']}")
print(f"🛡️ Resitência: {jogador['resistencia']}")
print(f"⚡ Agilidade: {jogador['agilidade']}")
print(f"🍷 Sangue: {jogador['sangue']}")
print(f"⛪ Fé: {jogador['fé']}")
print(f"🍀 Sorte: {jogador['sorte']}")

# --- INTRODUÇÕES POR CLASSE ---
introducoes = {
    "Caminhante da Noite": "🌃 Você desperta em um beco úmido de Londres. O som das carruagens ecoa, e a sede aperta.",
    "Lorde Sanguinário": "🏰 Você abre os olhos em seu caixão de carvalho em um castelo em ruínas. Séculos de sono te deixaram faminto por poder.",
    "Sombra Veloz": "⚡ Você está pendurado no telhado de uma catedral, observando a guarda da cidade passar. Seus reflexos estão tinindo.",
    "Feiticeiro de Sangue": "🍷 O cheiro de incenso e sangue seco preenche seu laboratório oculto. As vozes do além sussurram seu nome.",
    "Gárgula Imortal": "🗿 O líquen se desprende de sua pele de pedra enquanto você se desprende da estátua da igreja. Você é pesado e eterno.",
    "Rejeitado": "🏚️ Você acorda em uma vala comum, sem memórias, sentindo uma dor terrível e uma fome que não consegue explicar."
}

# Exibe a introdução baseada na classe do jogador
print("\n" + "—"*50)
print(f"📖 {introducoes[jogador['classe']]}")
print("—"*50)


import time
import random

# --- DEFINIÇÃO DAS MISSÕES ÚNICAS POR LINHAGEM ---
detalhes_missoes = {
    "Caminhante da Noite": {
        "1": {"msg": "🌃 Seguir rastro de sangue", "inimigo": "Guarda Noturno", "v": 40, "f": 10, "A": "Libertar Prisioneiros", "B": "Roubar Tesouro"},
        "2": {"msg": "🕵️ Espionar a Mansão", "inimigo": "Cão de Guarda", "v": 30, "f": 12, "A": "Envenenar poço", "B": "Roubar chaves"}
    },
    "Lorde Sanguinário": {
        "1": {"msg": "🏰 Cobrar tributos", "inimigo": "Aldeão Rebelde", "v": 35, "f": 8, "A": "Escravizar", "B": "Executar"},
        "2": {"msg": "⚔️ Desafiar Cavaleiro", "inimigo": "Cavaleiro de Prata", "v": 60, "f": 15, "A": "Beber sangue nobre", "B": "Transformá-lo"}
    },
    "Sombra Veloz": {
        "1": {"msg": "⚡ Invadir mansão", "inimigo": "Mordomo Armado", "v": 30, "f": 10, "A": "Sabotar carruagem", "B": "Saquear joias"},
        "2": {"msg": "🗡️ Emboscar Mensageiro", "inimigo": "Batedor Real", "v": 45, "f": 12, "A": "Ler carta secreta", "B": "Roubar cavalo"}
    },
    "Feiticeiro de Sangue": {
        "1": {"msg": "🍷 Ritual no Cemitério", "inimigo": "Coveiro", "v": 40, "f": 9, "A": "Invocar sombra", "B": "Profanar túmulo"},
        "2": {"msg": "🔮 Ler aura da vidente", "inimigo": "Aprendiz de Mago", "v": 50, "f": 14, "A": "Roubar grimório", "B": "Drenar mana"}
    },
    "Gárgula Imortal": {
        "1": {"msg": "🗿 Proteger Portal", "inimigo": "Fanático Religioso", "v": 45, "f": 10, "A": "Esmagar crânio", "B": "Petrificar"},
        "2": {"msg": "🤜 Expulsar Vândalos", "inimigo": "Líder de Gangue", "v": 55, "f": 13, "A": "Arremessar do teto", "B": "Exigir adoração"}
    },
    "Rejeitado": {
        "1": {"msg": "🏚️ Vasculhar lixo", "inimigo": "Rato Gigante", "v": 25, "f": 7, "A": "Comer restos", "B": "Fugir com trapos"},
        "2": {"msg": "🐀 Caçar nos esgotos", "inimigo": "Vagabundo Armado", "v": 35, "f": 10, "A": "Roubar comida", "B": "Pedir clemência"}
    }
}

# --- 3. SISTEMA DE LUTA REFORMULADO ---
def iniciar_luta(jogador, nome_inimigo, vida_inimigo, força_inimigo):
    # Todo o resto do código que você mandou entra aqui, indentado...
    print(f"\n⚠️ UM {nome_inimigo.upper()} APARECEU! ⚔️")
    vida_max_inimigo = vida_inimigo
    
    while vida_inimigo > 0 and jogador["vida"] > 0:
        print(f"\n❤️ Vida: {jogador['vida']} | 🍷 Sangue: {jogador['sangue']} | 🖤 {nome_inimigo}: {vida_inimigo}")
        opcoes = "1. 🗡️ Atacar | 2. 🍷 Usar Sangue (-10 🍷)"
        if jogador["nivel"] >= 1:
            opcoes += " | 3. 🔥 PODER ESPECIAL (-20 🍷)"
        print(opcoes)
        
        opc = input("👉 Ação: ")
        
        # --- TURNO DO JOGADOR ---
        if opc == "1":
            critico = 2 if random.randint(1, 20) <= jogador["sorte"] else 1
            dano = random.randint(5, jogador["força"]) * critico
            vida_inimigo -= dano
            print(f"💥 Você causou {dano} de dano!" + (" ✨ CRÍTICO!" if critico > 1 else ""))
            
        elif opc == "2":
            if jogador["sangue"] >= 10:
                jogador["vida"] = min(jogador["vida_max"], jogador["vida"] + 20)
                jogador["sangue"] -= 10
                print("🍷 Cura rápida! +20 de vida.")
            else:
                print("❌ Sangue insuficiente!")

        elif opc == "3": 
            if jogador["sangue"] >= 20:
                # Dicionário de nomes de poderes
                poderes = {
                    "Caminhante da Noite": "Névoa Asfixiante",
                    "Lorde Sanguinário": "Esmagar Coração",
                    "Sombra Veloz": "Mil Cortes de Prata",
                    "Feiticeiro de Sangue": "Explosão de Hemoglobina",
                    "Gárgula Imortal": "Impacto de Meteoro",
                    "Rejeitado": "Fúria dos Esquecidos"
                }
                nome_poder = poderes.get(jogador["classe"], "Poder Oculto")
                
                dano_especial = jogador["força"] * 3
                vida_inimigo -= dano_especial
                jogador["sangue"] -= 20
                print(f"🔥 {nome_poder.upper()}!")
                print(f"💥 Dano devastador de {dano_especial}!")
            else:
                print("❌ Sangue insuficiente!")

        # --- VEZ DO INIMIGO (COM AGILIDADE E FÉ) ---
        if vida_inimigo > 0:
            chance_esquiva = random.randint(1, 100)
            if chance_esquiva <= jogador["agilidade"]:
                print(f"⚡ ESQUIVA! Você foi rápido demais para o {nome_inimigo}!")
            else:
                # O dano do inimigo é reduzido pela sua Resistência
                dano_recebido = max(1, força_inimigo - (jogador["resistencia"] // 2))
                jogador["vida"] -= dano_recebido
                print(f"🩸 {nome_inimigo} te golpeou! -{dano_recebido} HP.")

                # --- SISTEMA DE SOBREVIVÊNCIA POR FÉ ---
                if jogador["vida"] <= 0:
                    if random.randint(1, 100) <= jogador["fé"]:
                        jogador["vida"] = 1 # O "Milagre" trava a vida em 1
                        print(f"\n✨ MILAGRE! Sua fé de {jogador['fé']}% te manteve de pé com 1 HP!")
                    else:
                        print("\n💀 Sua fé fraquejou... a escuridão te levou.")

    # --- PÓS-LUTA (VITÓRIA OU MORTE) ---
    if jogador["vida"] > 0:
        # Se for o Boss Final, dá muito XP, se for caçador, dá pouco
        xp_ganho = vida_max_inimigo // 2 
        jogador["exp"] += xp_ganho
        print(f"\n🏆 Vitória! +{xp_ganho} XP.")
        
        # Aumentamos o XP necessário: Nível 1 -> 2 (50 XP) | Nível 2 -> 3 (100 XP)
        xp_proximo_nivel = 50 if jogador["nivel"] == 1 else 100
        
        if jogador["exp"] >= xp_proximo_nivel:
            jogador["nivel"] += 1
            jogador["exp"] = 0 # Reseta o XP para o novo nível
            jogador["força"] += 5
            jogador["vida_max"] += 20
            jogador["vida"] = jogador["vida_max"]
            print(f"🌟 LEVEL UP! Nível {jogador['nivel']}! Suas trevas se intensificam!")
            
            # Mensagem especial se chegar no nível do Boss
            if jogador["nivel"] == 3:
                print("🚨 Você sente uma presença divina se aproximando... O Inquisidor está perto!")
                
        return True
    return False

# --- 4. INTRODUÇÃO E MISSÕES ---
introducoes = {
    "Caminhante da Noite": "🌃 Becos de Londres...",
    "Lorde Sanguinário": "🏰 Castelo em ruínas...",
    "Sombra Veloz": "⚡ Telhados da catedral...",
    "Feiticeiro de Sangue": "🍷 Laboratório oculto...",
    "Gárgula Imortal": "🗿 Estátua da igreja...",
    "Rejeitado": "🏚️ Vala comum..."
}

missoes_linhagem = {
    "Caminhante da Noite": ["🌃 Seguir um rastro de sangue no beco", "🕵️ Espionar a guarda noturna"],
    "Lorde Sanguinário":   ["🏰 Reivindicar tributo dos aldeões", "⚔️ Desafiar um cavaleiro errante"],
    "Sombra Veloz":        ["⚡ Invadir a mansão pelo telhado", "🗡️ Emboscar o mensageiro do Rei"],
    "Feiticeiro de Sangue":["🍷 Realizar um ritual no cemitério", "🔮 Ler a aura da vidente local"],
    "Gárgula Imortal":     ["🗿 Defender o portal da catedral", "🤜 Esmagar os vândalos da praça"],
    "Rejeitado":           ["🏚️ Vasculhar o lixo por restos", "🐀 Caçar ratos nos esgotos"]
}

print(f"\n📖 {introducoes[jogador['classe']]}")
time.sleep(1)

while jogador["vida"] > 0:
    # 1. Checagem do Boss Final
    if jogador["nivel"] >= 3:
        print("\n" + "☠️" * 20)
        print("🚨 O CÉU SE TORNA VERMELHO SANGUE... O INQUISIDOR MAGNUS CHEGOU! 🚨")
        print("☠️" * 20)
        time.sleep(2)
        
        if iniciar_luta(jogador, "Inquisidor Magnus", 150, 25):
            print("\n" + "✨" * 30)
            print(f"✨ VITÓRIA ETERNA, {jogador['nome'].upper()}! ✨")
            print("O corpo do Inquisidor Magnus se desfaz em cinzas sagradas.")
            print("O Reino dos Vampiros agora tem um novo soberano.")
            print("—" * 30)
            time.sleep(2)
            
            print("\n📖 O SEU EPÍLOGO:")
            
            # Final por Classe
            if jogador["classe"] == "Rejeitado":
                print("🌑 De uma vala comum ao trono: Você provou que o sangue mais fraco pode se tornar o mais puro.")
            elif jogador["classe"] == "Lorde Sanguinário":
                print("🏰 Seu castelo foi reconstruído. Os humanos tremem ao ouvir o bater de asas nas proximidades.")
            elif jogador["classe"] == "Feiticeiro de Sangue":
                print("🍷 Você desvendou os segredos da imortalidade total, tornando-se uma entidade do além.")
            else:
                print(f"🦇 Como um {jogador['classe']}, você marcou seu nome na história da noite.")

            # --- FINAL POR CONDUTA REFORMULADO ---
            escolhas_A = sum(1 for e in jogador["escolhas_feitas"] if "_A" in e)
            escolhas_B = sum(1 for e in jogador["escolhas_feitas"] if "_B" in e)
            total_escolhas = escolhas_A + escolhas_B

            print("\n👑 ESTILO DE REINADO:")
            
            if escolhas_A > escolhas_B:
                if escolhas_A >= 4: # Se ele foi MUITO agressivo
                    print(f"⚔️ Seu reinado é de PURO SANGUE. Você não apenas governa, você devora. As nações vizinhas tremem diante de {jogador['nome']}.")
                else:
                    print("⚔️ Seu reinado é de FERRO. Você é um tirano implacável que não aceita desobediência.")
            
            elif escolhas_B > escolhas_A:
                if escolhas_B >= 4: # Se ele foi MUITO sutil
                    print(f"🎭 Seu reinado é de NÉVOA. Você controla o mundo das sombras, transformando reis e papas em suas marionetes.")
                else:
                    print("🎭 Seu reinado é de SOMBRAS. Você governa através da diplomacia e do medo sutil.")
            
            else:
                print("⚖️ Seu reinado é de EQUILÍBRIO. Você é um governante justo para os monstros, mas implacável para os homens.")

            # --- INSIRA AQUI O NOVO FINAL POR FÉ ---
            print("\n✨ DESTINO DA ALMA:")
            if jogador["fé"] >= 20:
                print("🌟 Sua Fé é tão alta que você não é apenas um monstro, mas um Messias das Sombras.")
            elif jogador["fé"] <= 5:
                print("🌑 Você abandonou qualquer traço de humanidade ou crença. Você é o puro vazio.")
            else:
                print("🌓 Você caminha no crepúsculo, equilibrando sua natureza herética com o que restou de sua alma.")

            # Eventos específicos (Rebelde_A, Prisioneiros_A, etc)
            # ... (resto do seu código) ...
            # Eventos específicos
            if any("Rebelde_A" in e for e in jogador["escolhas_feitas"]):
                print("⛓️ Os vilarejos vizinhos tornaram-se suas fazendas de sangue particulares.")
            if any("Prisioneiros_A" in e for e in jogador["escolhas_feitas"]):
                print("🩸 Os renegados que você libertou agora formam sua guarda de elite pessoal.")

            print("\n--- FIM DE JOGO ---")
            print("✨" * 30)
            break # <--- IMPORTANTE: Encerra o jogo aqui!
        else:
            print("\n💀 Magnus foi forte demais. Seu legado termina em cinzas.")
            break

    # 2. Puxa as missões da classe do jogador
    m_hoje = detalhes_missoes[jogador["classe"]]
    
    print(f"\n--- MENU NÍVEL {jogador['nivel']} | SANGUE: {jogador['sangue']} ---")
    print(f"1. {m_hoje['1']['msg']}")
    print(f"2. {m_hoje['2']['msg']}")
    print(f"3. 🩸 Caçar")
    print(f"4. ⚰️ Descansar")
    print(f"5. 📊 Status")
    print(f"6. 🚪 Sair")
    
    esc = input("\n👉 Escolha: ")

    if esc in ["1", "2"]:
        missao = m_hoje[esc]
        if iniciar_luta(jogador, missao["inimigo"], missao["v"], missao["f"]):
            print(f"\n🔱 DECISÃO DE LINHAGEM:")
            print(f"A) {missao['A']} | B) {missao['B']}")
            sub = input("👉 Sua escolha: ").upper()
            
            # Salva no histórico para o final do jogo
            jogador["escolhas_feitas"].append(f"{missao['inimigo']}_{sub}")
            
            # --- CONSEQUÊNCIAS ÚNICAS POR CLASSE ---
            if sub == "A":
                # Geralmente uma escolha AGRESSIVA/SANGUINÁRIA
                jogador["sangue"] += 25
                jogador["força"] += 2
                print(f"🩸 {missao['A']} concluído. Sua sede de sangue aumenta sua força! (+25 🍷 | +2 💪)")
            
            elif sub == "B":
                # Geralmente uma escolha ESTRATÉGICA/SUTIL
                jogador["sorte"] += 2
                jogador["agilidade"] += 2
                print(f"🍀 {missao['B']} concluído. Você se torna mais astuto e veloz! (+2 🍀 | +2 ⚡)")
            
            # Bônus Específicos de Fé (Se a escolha for 'Pia')
            if "Ritual" in missao["msg"] or "Catedral" in missao["msg"]:
                jogador["fé"] += 3
                print("⛪ Sua conexão com o oculto/sagrado aumentou sua Fé! (+3 ⛪)")

    elif esc == "3":
        print("\n🦇 Você sai pelas sombras em busca de presas...")
        time.sleep(1)
        
        # Sorteia um evento: 1 a 100
        evento_caca = random.randint(1, 100)

        if evento_caca <= 20:
            # 20% de chance de encontrar um Caçador (LUTA!)
            print("🚨 CUIDADO! Um Caçador de Vampiros sentiu seu cheiro e te emboscou!")
            time.sleep(1)
            iniciar_luta(jogador, "Caçador de Aluguel", 45, 15)
            
        elif evento_caca <= 40:
            # 20% de chance de se ferir na caça (PERDA DE VIDA)
            dano_caca = random.randint(5, 15)
            jogador["vida"] -= dano_caca
            print(f"😫 A caçada foi difícil! Você se machucou ao lutar com a presa. (-{dano_caca} ❤️)")
            if jogador["vida"] <= 0:
                print("💀 Você estava tão fraco que não sobreviveu à caçada...")
                break # Encerra o jogo se morrer caçando

        else:
            # 60% de chance de SUCESSO (GANHO DE SANGUE)
            ganho = random.randint(15, 35)
            jogador["sangue"] += ganho
            print(f"🍷 Sucesso! Você encontrou uma vítima isolada. (+{ganho} 🍷)")

    elif esc == "4":
        jogador["vida"] = min(jogador["vida_max"], jogador["vida"] + 30)
        print(f"⚰️ Você descansou. Vida: {jogador['vida']}/{jogador['vida_max']}")

    elif esc == "5":
        print(f"\n📊 STATUS DE {jogador['nome']}")
        print(f"Lvl: {jogador['nivel']} | Força: {jogador['força']} | Sorte: {jogador['sorte']}")
        print(f"Histórico: {jogador['escolhas_feitas']}")
        input("\n[Enter para voltar]")

    elif esc == "6":
        print("🌙 Saindo para as sombras...")
        break

# --- MENSAGEM FINAL DE DERROTA ---
if jogador["vida"] <= 0:
    print("\n" + "💀" * 20)
    print(f"  O VAMPIRO {jogador['nome'].upper()} FOI DESTRUIDO!")
    print("  SUAS CINZAS FORAM SOPRADAS PELO VENTO...")
    print("💀" * 20)
    input("\n[Pressione Enter para fechar]")