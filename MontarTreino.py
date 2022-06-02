
superior=[]
inferior=[]

class Personal:
    def __init__(self,nome) :
        self.nome=nome
    def personal(self):
        print(f"Bem vindo {self.nome} ")
        print("Vamos montar o treino do aluno!")
        self.quantidade= int(input("Quantos exericios : ").strip())
        print("-"*30)
    def Treino(self):
            print("Treino Superior :")
            for c in range(1, self.quantidade + 1):
                MontarSuperior=input(f"{c} Exercício de Superior do aluno : ").lower().strip()
                print("-"*30)
                superior.append(MontarSuperior)
            print("Treino Inferior :")
            for i in range(1,self.quantidade + 1):
                MontarInferior=input(f"{i} Exercício de Inferior do aluno : ").lower().strip()
                print("-"*30)
                inferior.append(MontarInferior)
                
               


    def MostrarTreino(self):
        question=input("Exibir Treino? [Sim/Não]").lower().strip()
        if question == 'sim':
            print("-"*30)
            print("Superior:")
            print('')
            for treinosuperior in superior:
                print(treinosuperior)
            print("-"*30)
            print('')
            print("Inferior:")
            print("")
            for treinoinferior in inferior:
                print(treinoinferior)
            print("-"*30)
            

class Aluno:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def TreinoDoAluno(self):
        print(f'Aluno: {self.name}')
        print(f'Idade: {self.age}')
        breno.MostrarTreino()

programarodando=True

breno=Personal('Breno Amorim')
marley=Aluno("Marley",'18')

breno.personal()
breno.Treino()
marley.TreinoDoAluno()


#Criar arquivo com os treinos
arquivo= 'treino.txt'
for item in superior:
    a=item
for treino in inferior:
    b= treino
with open(arquivo,'a') as arq:
    arq.write(a)
    arq.write(b)
        
