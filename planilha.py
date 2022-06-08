
#run the program

from ontartreino import Personal, Aluno

treino = True

professores = {}
alunos = {}

while treino:
    prof = input("Insira seu nome e sobrenome: ").split()

    for i in prof:
        professores[prof[0]] = prof[1]

    for key, value in professores.items():
        prof = Personal(key, value)
        prof.personal()
        prof.treino()

    aluno = input("\nInsira o Nome e a Idade do Aluno: ").split()

    for i in aluno:
        alunos[aluno[0]] = aluno[1]

    for key, value in alunos.items():
        nome = Aluno(key, value)
        nome.treino_do_aluno()

        prof.mostrar_treino()

    treino = False