from unidecode import unidecode

with open("texto.txt", "r") as texto:
    conteudo = texto.read()

conteudo_limpo = unidecode(conteudo)

print(conteudo_limpo)

palavras = conteudo_limpo.split()

palavrass = []
quantidade = []

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
    

print(palavrass)
print(quantidade)


while True:
    pergunta = input("Qual palavra você deseja saber a quantidade de vezes que aparece no texto: ")
    
    if not pergunta:
        print("Saindo do programa...")
        break

    if pergunta in palavrass:
        print(f"A palavra {pergunta} apareceu {quantidade[palavrass.index(pergunta)]} vezes no texto")
    else:
        input(f"A palavra {pergunta} não está no texto, digite outra palavra")


palavra_mais_frequente = max(frequencia)
palavra_menos_frequente = min(frequencia)

print(palavra_mais_frequente)

