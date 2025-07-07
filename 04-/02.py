notas = []


quantidade = int(input("Quantos alunos deseja registrar? "))


for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)


soma = sum(notas)
media = soma / len(notas)


print(f"\nNotas registradas: {notas}")
print(f"Média da turma: {media:.2f}")
