-- esquema para geração da tabela

CREATE TABLE alunos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	idade INTEGER,
	cpf	VARCHAR(11) NOT NULL,
	email TEXT NOT NULL UNIQUE,
	celular TEXT,
	criado_em DATETIME NOT NULL
);