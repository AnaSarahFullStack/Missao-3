# Criação do dicionário inicial
meu_dicionario = {
    "codigo1": "Python",
    "codigo2": "Java",
    "codigo3": "PHP"
}

# Impressão do conteúdo do dicionário
print("Conteúdo do dicionário:", meu_dicionario)

# Impressão do tipo de dados do dicionário
print("Tipo de dados do dicionário:", type(meu_dicionario))

# Utilização do método get para obter o valor da chave 'linguagem'
# Como a chave é código, vamos pegar 'codigo1', 'codigo2' e 'codigo3'
print("Valor da chave 'codigo1':", meu_dicionario.get("codigo1"))

# Impressão do tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))

# Criação de um novo dicionário aninhado
dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}

# Impressão do valor das chaves "nome" e "tipo" da chave 1
print("Chave 1 - Nome:", dicionario_frutas[1]["nome"], ", Tipo:", dicionario_frutas[1]["tipo"])

# Impressão do valor das chaves "nome" e "tipo" da chave 2
print("Chave 2 - Nome:", dicionario_frutas[2]["nome"], ", Tipo:", dicionario_frutas[2]["tipo"])

# Iteração no dicionário dicionario_frutas e impressão dos valores de todas as chaves "nome" e "tipo"
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")