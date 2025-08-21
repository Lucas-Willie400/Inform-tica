# QUESTÃO 1

# # QUESTÃO 2

# QUESTÃO 5
nota_turma = 0
aluno =int(input("Digite a quantidade de alunos:"))
alunoQntInicial = aluno
while True:
    nota=int(input("Digite a nota do aluno:"))
    aluno -=1
    nota_turma += nota
    if aluno == 0:
        break
media = nota_turma/alunoQntInicial
print(f"A média da turma é: {media}")

# QUESTÃO 6
# import random

# numero_aleatorio = random.randint(1, 20)
# numero_usuário = int(input("Digite um número entre 1 e 20: "))

# if numero_usuário == numero_aleatorio:
#     print("Parabéns! Você acertou!")
# elif numero_usuário < numero_aleatorio:
#     print("O número aleatório é maior.")
# else:
#     print("O número aleatório é menor.")