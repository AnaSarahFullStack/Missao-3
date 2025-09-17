def calcular_media(notas):
    """Calcula a média das notas dos 4 bimestres de um aluno."""
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """Verifica se o aluno foi reprovado com base na média."""
    return media < 6

def saida_reprovados(alunos, matriculas_reprovados):
    """Gera a saída dos alunos reprovados com seus nomes, matrículas e médias finais."""
    saidas = []
    for aluno in alunos:
        if aluno["matricula"] in matriculas_reprovados:
            media = calcular_media(aluno["notas"])
            saida = f"Aluno Reprovado: {aluno['nome']} – Matrícula: {aluno['matricula']} – Média Final: {media:.2f}"
            saidas.append(saida)
    return saidas
