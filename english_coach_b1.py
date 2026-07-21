import random

palavras_b1 = [
    {
        "palavra": "improve",
        "traducao": "melhorar",
        "exemplo": "I want to improve my English."
    },
    {
        "palavra": "schedule",
        "traducao": "agenda / cronograma",
        "exemplo": "My schedule is busy today."
    },
    {
        "palavra": "challenge",
        "traducao": "desafio",
        "exemplo": "Learning English is a good challenge."
    },
    {
        "palavra": "explain",
        "traducao": "explicar",
        "exemplo": "Can you explain this sentence?"
    }
]

perguntas = [
    "What did you do today?",
    "What are your plans for the weekend?",
    "Tell me about a movie you like.",
    "Why do you want to improve your English?",
    "What kind of stories do you enjoy?"
]

erros_comuns = {
    "techter": "teacher",
    "tetcher": "teacher",
    "studing": "studying",
    "becouse": "because",
    "freind": "friend",
    "languege": "language",
    "englis": "english",
    "inglish": "english",
    "speek": "speak",
    "lerning": "learning",
    "everydays": "every day"
}


def limpar_espacos(frase):
    frase = frase.strip()
    palavras = frase.split()
    frase_limpa = " ".join(palavras)

    return frase_limpa


def corrigir_frase(frase):
    frase_original = frase
    frase_corrigida = limpar_espacos(frase)

    frase_corrigida = frase_corrigida.replace("wanna", "want to")
    frase_corrigida = frase_corrigida.replace("gonna", "going to")
    frase_corrigida = frase_corrigida.replace("gotta", "have to")

    for erro, correcao in erros_comuns.items():
        frase_corrigida = frase_corrigida.replace(erro, correcao)

    if frase_corrigida != "":
        frase_corrigida = frase_corrigida[0].upper() + frase_corrigida[1:]

        if frase_corrigida[-1] not in ".!?":
            frase_corrigida = frase_corrigida + "."

    print("\nFrase original:")
    print(frase_original)

    print("\nSugestao de correcao:")
    print(frase_corrigida)

    print("\nExplicacao:")

    encontrou_explicacao = False

    if "wanna" in frase_original:
        print("- 'Wanna' e informal. Em uma frase mais padrao, use 'want to'.")
        encontrou_explicacao = True

    if "gonna" in frase_original:
        print("- 'Gonna' e informal. Em uma frase mais padrao, use 'going to'.")
        encontrou_explicacao = True

    if "gotta" in frase_original:
        print("- 'Gotta' e informal. Em uma frase mais padrao, use 'have to'.")
        encontrou_explicacao = True

    for erro, correcao in erros_comuns.items():
        if erro in frase_original:
            print("- Possivel erro de escrita:", erro, "->", correcao)
            encontrou_explicacao = True

    if frase_original != frase_original.strip():
        print("- A frase tinha espacos no inicio ou no fim.")
        encontrou_explicacao = True

    if "  " in frase_original:
        print("- A frase tinha espacos extras entre palavras.")
        encontrou_explicacao = True

    if encontrou_explicacao == False:
        print("- Nao encontrei erros especificos nas regras cadastradas.")

    print("- Lembre de comecar frases com letra maiuscula e terminar com pontuacao.")


def mostrar_palavra_do_dia():
    palavra = random.choice(palavras_b1)

    print("\nPalavra:", palavra["palavra"])
    print("Traducao:", palavra["traducao"])
    print("Exemplo:", palavra["exemplo"])


def praticar_conversa():
    print("\nModo conversa iniciado.")
    print("Digite 'voltar' quando quiser retornar ao menu.")

    perguntas_disponiveis = perguntas.copy()
    continuar = True

    while continuar == True:
        if len(perguntas_disponiveis) == 0:
            perguntas_disponiveis = perguntas.copy()

        pergunta = random.choice(perguntas_disponiveis)
        perguntas_disponiveis.remove(pergunta)

        print("\nResponda em ingles:")
        print(pergunta)
        print("(Digite 'voltar' para retornar ao menu)")

        resposta = input("Sua resposta: ")

        if resposta.lower().strip() == "voltar":
            continuar = False
            print("Voltando ao menu...")

        elif resposta.strip() == "":
            print("Voce nao digitou uma resposta. Tente responder ou digite 'voltar'.")

        else:
            print("\nVamos revisar sua resposta:")
            corrigir_frase(resposta)

            print("\nContinue praticando!")


opcao = ""

while opcao != "4":
    print("\nEnglish Coach B1")
    print("1 - Palavra do dia")
    print("2 - Corrigir frase")
    print("3 - Praticar conversa")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        mostrar_palavra_do_dia()

    elif opcao == "2":
        frase = input("\nDigite uma frase em ingles: ")
        corrigir_frase(frase)

    elif opcao == "3":
        praticar_conversa()

    elif opcao == "4":
        print("See you next time!")

    else:
        print("Opcao invalida. Tente novamente.")
