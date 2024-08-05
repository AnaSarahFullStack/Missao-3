# Criação do set com os valores iniciais
set_inicial = {11, 12, 13, 14}

# Impressão do conteúdo do set
print("Conteúdo do set inicial:", set_inicial)

# Adição de um novo elemento usando o método add
set_inicial.add(15)

# Impressão do conteúdo do set após adição
print("Conteúdo do set após add:", set_inicial)

# Atualização do set com novos elementos usando o método update
set_inicial.update([1, 2, 3, 4, 5])

# Impressão do conteúdo do set após update
print("Conteúdo do set após update:", set_inicial)

# Remoção do elemento 13 usando o método discard
set_inicial.discard(13)

# Impressão do conteúdo do set após remoção
print("Conteúdo do set após discard:", set_inicial)

# Criação de um novo set com os elementos especificados
novo_set = set([20, 21, 23, 1, 2])

# Impressão do conteúdo do novo set
print("Conteúdo do novo set:", novo_set)

# União dos dois sets
uniao = set_inicial.union(novo_set)
print("Resultado da união entre os dois sets:", uniao)

# Interseção dos dois sets
intersecao = set_inicial.intersection(novo_set)
print("Resultado da interseção entre os dois sets:", intersecao)

# Diferença entre os dois sets
diferenca = set_inicial.difference(novo_set)
print("Resultado da diferença entre os dois sets:", diferenca)

# Diferença simétrica entre os dois sets
diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print("Resultado da diferença simétrica entre os dois sets:", diferenca_simetrica)