from operacoes import calcular_media, verificar_reprovacao, saida_reprovados

# Definindo a estrutura de dados dos alunos e as notas de cada bimestre
alunos = [

    {"nome": "Maria", "matricula": 26, "notas": [8, 7, 5, 9]},
    {"nome": "Ana", "matricula": 101, "notas": [9, 9, 8, 9]},
    {"nome": "João", "matricula": 13, "notas": [6, 5, 5, 5]},
    {"nome": "Ágatha", "matricula": 37, "notas": [8, 6, 7.5, 9]},
    {"nome": "Joaquim", "matricula": 72, "notas": [6, 5.5, 5, 7]},
    {"nome": "Félix", "matricula": 5, "notas": [10, 8, 8, 8]}
]

# Critério de aprovação
media_minima = 6.0

# Identificando matrículas dos alunos reprovados
matriculas_reprovados = [
    aluno["matricula"] 
    for aluno in alunos 
    if verificar_reprovacao(calcular_media(aluno["notas"]))
]

# Gerando a saída dos alunos reprovados
saidas_reprovados = saida_reprovados(alunos, matriculas_reprovados)

# Imprimindo os dados dos alunos reprovados
print("Alunos reprovados:")
for saida in saidas_reprovados:
    print(saida)
