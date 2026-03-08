import secrets
import string

print("=== GERADOR DE SENHAS ===")

# Importamos as bibliotecas "secrets" e "string"
# A biblioteca "secrets" é usada para gerar escolhas aleatórias seguras
# A biblioteca "string" contém conjuntos prontos de caracteres como letras, números e símbolos

quantidade = int(input("Quantas senhas você deseja gerar? "))
tamanho = int(input("Qual o tamanho de cada senha? "))
# Definimos as variáveis "quantidade" e "tamanho" para dar mais flexibilidade ao usuário
# Assim ele pode escolher tanto quantas senhas gerar quanto o tamanho delas

usar_letras = input("Deseja usar letras? (s/n): ").lower() == "s"
usar_numeros = input("Deseja usar números? (s/n): ").lower() == "s"
usar_simbolos = input("Deseja usar símbolos? (s/n): ").lower() == "s"
# Essas variáveis verificam se o usuário quer incluir cada tipo de caractere
# O ".lower()" transforma a resposta em minúscula para evitar erros caso o usuário digite "S" ou "N"

caracteres = ""
# A variável "caracteres" armazenará todos os caracteres possíveis que poderão ser usados na senha

if usar_letras:
    caracteres += string.ascii_letters
# "string.ascii_letters" contém todas as letras do alfabeto, maiúsculas e minúsculas
# Se o usuário escolher usar letras, elas são adicionadas ao conjunto de caracteres possíveis

if usar_numeros:
    caracteres += string.digits
# "string.digits" contém todos os números de 0 a 9

if usar_simbolos:
    caracteres += string.punctuation
# "string.punctuation" contém vários símbolos especiais como !@#$%&*

# Caso o usuário não escolha nenhum tipo de caractere
if caracteres == "":
    print("Erro! Você precisa escolher pelo menos um tipo de caractere.")
# Esse bloco funciona como tratamento de erro para evitar que o programa tente gerar uma senha vazia

else:
    for i in range(quantidade):
        senha = ""
        # A variável "senha" é reiniciada a cada repetição para gerar uma nova senha

        for j in range(tamanho):
            senha += secrets.choice(caracteres)
        # O comando "secrets.choice()" escolhe aleatoriamente um caractere da variável "caracteres"
        # O "for" repete essa operação até que a senha tenha o tamanho desejado

        print(f"Senha {i+1}: {senha}")
        # Esse print mostra cada senha gerada para o usuário

# Projeto simples de gerador de senhas em Python
# Feito por Arthur Costa