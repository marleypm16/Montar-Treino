import sqlite3
import os
import io
import datetime


class Connect():
    """cria a conexao com o banco de dados"""
    
    def __init__(self):
        try:
            #conectando...
            self.conn = sqlite3.connect('clientes.db')
            self.createTable()
        except sqlite3.Error:
            print('Erro ao abrir o banco de dados')
            return False

    def createTable(self):
      """ Criando a tabela """
      
      c = self.conn.cursor()
      c.execute("""CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
	              nome TEXT,
	              idade INTEGER,
	              cpf	VARCHAR(11) NOT NULL,
	              email TEXT NOT NULL UNIQUE,
	              celular TEXT,
	              criado_em DATETIME NOT NULL
               );""")
      self.conn.commit()
      c.close()
      