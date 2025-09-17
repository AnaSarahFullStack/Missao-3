# Criação da lista com os valores iniciais
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Impressão do conteúdo da lista
print("Conteúdo da lista inicial:", lista_mesclada)

# Adição de um novo elemento usando o método append
lista_mesclada.append(["Lista aninhada"])

# Impressão do conteúdo da lista após adição
print("Conteúdo da lista após append:", lista_mesclada)

# Inserção de um novo elemento na posição 4 usando o método insert
lista_mesclada.insert(4, 5)

# Impressão do conteúdo da lista após inserção
print("Conteúdo da lista após insert:", lista_mesclada)

# Impressão do tamanho atual da lista
print("Tamanho atual da lista:", len(lista_mesclada))

# Remoção do item na posição 1
lista_mesclada.pop(1)

# Impressão do conteúdo da lista após remoção
print("Conteúdo da lista após remoção:", lista_mesclada)

# Criação da nova lista com os itens até a posição 4 da lista anterior
nova_lista_mesclada = lista_mesclada[:4]

# Impressão do conteúdo da nova lista
print("Conteúdo da nova lista:", nova_lista_mesclada)
