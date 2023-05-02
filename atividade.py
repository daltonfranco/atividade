from unidecode import unidecode

with open("texto.txt", "r") as texto:
    conteudo = texto.read()

print(f'''O texto é: 

{conteudo}
''')

palavrass = []
quantidade = []
lista_menores_valores = []
lista_maiores_valores = []
numeros = []

texto_limpo = False

pergunta_global = 1

while pergunta_global != '0':


    pergunta_p = input('''

                
                [1] - limpar os acentos desse texto
                [2] - Realizar a contagem das palavras e mostrar a quantidade das palavras em ordem decrescente
                [3] - Mostrar a quantidade de alguma palavra
                [4] - Mostrar as palavras que menos apareceram no texto
                [5] - Mostrar as palavras que mais apareceram no texto
                [0] - Sair do programa

        Qual você quer --> '''
    )


    if (pergunta_p == '2' or pergunta_p == '3'or pergunta_p == '4' or pergunta_p == '5') and not texto_limpo:

        input("Não é possivel escolher essa opção agora, tente outra")


    elif pergunta_p == '1':

        conteudo_limpo = unidecode(conteudo)

        print(conteudo_limpo)
        
        texto_limpo = True

    elif pergunta_p == '2':

        palavras = conteudo_limpo.split()

        #palavrass = []
        #quantidade = []

        # Conta a frequência de cada palavra usando um dicionário
        frequencia = {}
        for palavra in palavras:
            if palavra in frequencia:
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1

        # Ordena as palavras por frequência em ordem decrescente
        palavras_ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)

        # Imprime o resultado
        print("O texto tem", len(palavras), "palavras.")
        print("Palavras por frequência:")
        for palavra in palavras_ordenadas:
            print(palavra, ":", frequencia[palavra])
            palavrass.append(palavra)
            quantidade.append(frequencia[palavra])
            
        #print(palavrass)
        #print(quantidade)
    
    elif pergunta_p == '3':

        while True:
            pergunta = input("Qual palavra você deseja saber a quantidade de vezes que aparece no texto: ")
            
            if not pergunta:
                print("Saindo do programa...")
                break

            if pergunta in palavrass:
                print(f"A palavra {pergunta} apareceu {quantidade[palavrass.index(pergunta)]} vezes no texto")
            else:
                input(f"A palavra {pergunta} não está no texto, digite outra palavra")

    #numeros = []

    #lista_menores_valores = []
    #lista_maiores_valores = []

    elif pergunta_p == '4':

        numero_menos_frequente = min(quantidade)
        

        for i, numero in enumerate(quantidade):
            if numero == numero_menos_frequente:
                numeros.append(i)

        ''''''

        for x in numeros:
            lista_menores_valores.append(palavrass[x])

        print("Lista das palavras que menos aparecem: ")
        print(lista_menores_valores)


    elif pergunta_p == '5':
        numero_mais_frequente = max(quantidade)

        for i, numeross in enumerate(quantidade):
            if numeross == numero_mais_frequente:
                numeros.append(i)

        print("Lista das palavras que mais aparecem: ")
        print(lista_maiores_valores)

    elif pergunta_p == '0':
        pergunta_global = '0'
    
    else:
        input("Esse não é um numero disponível, tente outro... ")

