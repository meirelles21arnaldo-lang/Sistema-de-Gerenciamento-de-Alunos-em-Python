import sqlite3

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

#o nome_banco = escola e o valor padrao, logo se eu nao passar nada, e o escola.db, se eu passar, vira outro  
def criar_tabela(nome_banco = "escola.db"):

    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL)
    """)

    conn.commit()
    conn.close()

def cadastro_aluno(nome: str, idade, nota ,nome_banco = "escola.db"):

    if nome.strip() == "":
        return "Nome do aluno não pode ficar em branco."
    
    elif idade > 22:
        return "Idade acima de 22 anos."
    
    else:
        conn = conectar(nome_banco)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota))  

        conn.commit()
        conn.close()

        return "Aluno cadastrado com sucesso!"

#deletar aluno
def deletar_aluno(id , nome_banco = "escola.db"):
    if id > 0:
            
        conn = conectar(nome_banco)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM alunos WHERE id = ?" , (id,))

        conn.commit()
        conn.close()

        return f"O aluno de ID {id}, foi deletado"

    else:
        return "ID inserido é invalido"


#mudar aluno
def update_idade_aluno(id_aluno, idade , nome_banco = "escola.db"):   #mas no update o cliente pode quebrar a regra de ngc da idade máx, ent tem q validar isso

#quebra de regra de ngc
    if idade > 22:
        return "Idade acima de 22 anos não é permitida!"

    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?" , (idade , id_aluno))
    rows_affected = cursor.rowcount #atributo n encapsulado

#caso de glória :) "happy path"
    if rows_affected > 0:
        conn.commit()
        conn.close()

        return rows_affected

    #aluno inexistente
    else:
        return f"Aluno com ID = {id}, não encontrado"


def getAlunos(nome_banco = "escola.db"):
    conn = conectar(nome_banco)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados_alunos = cursor.fetchall()

    conn.close()
    return dados_alunos

#encapsulamento é publico ou privado - modificadores de acesso
#tupla(tipo do retorno de dados)
# insert, delete, update, select
# fet - pega o retorno do select
