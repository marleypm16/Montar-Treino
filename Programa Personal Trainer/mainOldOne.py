from tkinter import *
from refatorar import *
from dbconfig import *

# inicia o App e outras funcionalidades
root = Tk()
root.title("Personal Trainer App")
root.geometry('320x200')
cadastro = Frame(root)
treino = Frame(root)

def cadastroAluno():
  """Aba para cadastro dos Clientes/Alunos"""

  cadastro.grid()
  e1 = Label(cadastro, text="Nome:").grid(row=0)
  e2 = Label(cadastro, text="Idade:").grid(row=1)
  e3 = Label(cadastro, text="Cpf:").grid(row=2)
  e4 = Label(cadastro, text="E-mail:").grid(row=3)
  e5 = Label(cadastro, text="Celular:").grid(row=4)

  e1 = Entry(cadastro)
  e2 = Entry(cadastro)
  e3 = Entry(cadastro)
  e4 = Entry(cadastro)
  e5 = Entry(cadastro)

  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)
  e3.grid(row=2, column=1)
  e4.grid(row=3, column=1)
  e5.grid(row=4, column=1)
  treino.grid_forget()
  
def clicked():
  """Funcao para cadastrar os dados"""
  
  banco = Connect()
  
  c = banco.conn.cursor()
  c.execute("""
            INSERT INTO alunos VALUES(
            :nome, 
            :idade, 
            :cpf, 
            :email, 
            :celular)
            """,
            {
              'nome': e1.get(),
              'idade': e2.get(),
              'cpf': e3.get(),
              'email': e4.get(),
              'celular': e5.get()
            })
          
  banco.conn.commit()
  c.close()
  
  
  e1.delete(0,"end")
  e2.delete(0,"end")
  e3.delete(0,"end")
  e4.delete(0,"end")
  e5.delete(0,"end")

btn = Button(cadastro, text="Cadastrar", command=clicked)
btn.grid(column=1, row=5)


def montarTreino():
  """Aba para montagem do treino"""
  
  treino.grid()
  f1 = Label(treino, text="Superior:").grid(row=0)
  f2 = Label(treino, text="Inferior:").grid(row=1)


  f1 = Entry(treino)
  f2 = Entry(treino)


  f1.grid(row=0, column=1)
  f2.grid(row=1, column=1)
  cadastro.grid_forget()

# cria o menu para acesso ao sistema de cadastro ou
# montagem do treino

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Novo Cadastro', command=cadastroAluno)
filemenu.add_separator()
filemenu.add_command(label='Montar Treino', command=montarTreino)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

root.mainloop()
