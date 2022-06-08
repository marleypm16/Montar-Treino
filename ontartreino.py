class Personal():
    """build the personal trainer profile"""
    def __init__(self, nome, sobrenome):
        """initialize the class"""

        self.nome = nome
        self.sobrenome = sobrenome
        self.superior = []
        self.inferior = []

    def personal(self):
        """greet the user and start to create the trainning plan"""

        nome_completo = self.nome + " " + self.sobrenome
        print("\n" + f"Bem vindo {nome_completo.title()} ")
        print("Vamos montar o treino do aluno!")

        self.quantidadeSuperior = int(input("Quantos exercicios de superior : ").strip())
        self.quantidadeInferior = int(input("Quantos exercicios de Inferior : ").strip())

        print("-" * 30)

    def treino(self):
        """build the training plan"""

        print("Treino Superior :")

        for c in range(1, self.quantidadeSuperior + 1):
            montar_superior = input(
                f"{c} Exercício de Superior do aluno : ").lower().strip()
            print("-" * 30)
            self.superior.append(montar_superior)

        print("Treino Inferior :")

        for i in range(1, self.quantidadeInferior + 1):
            montar_inferior = input(
                f"{i} Exercício de Inferior do aluno : ").lower().strip()
            print("-" * 30)
            self.inferior.append(montar_inferior)

    def mostrar_treino(self):
        """show the trainning plan and save in a file"""

        question = input("Exibir Treino? [Sim/Não]: ").lower().strip()
        if question == 'sim':

            print("-" * 30 + "\nSuperior:\n")
            for treino_superior in self.superior:
                print(treino_superior)

            print("-" * 30 + "\nInferior:\n")
            for treino_inferior in self.inferior:
                print(treino_inferior)
            print("-" * 30)


class Aluno():
    """create the costumer profile"""
    def __init__(self, name, age):
        """initialize the class"""

        self.name = name
        self.age = age

    def treino_do_aluno(self):
        """build the profile"""

        print("\n" + f'Aluno: {self.name.title()}')
        print(f'Idade: {self.age}')