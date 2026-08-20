import sqlite3 as sql
#importa o sql

#cria uma funcao para se conectar ao banco de dados
def conectar():
    conn = sql.connect("escola.db")
    return conn


#cria funcao para criar tabela
def criar_tabela():

    conn = conectar()
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

#cadastra um novo aluno
#o : str é pra tipar o nome e poder dar o strip()
def cadastrar_aluno(nome: str , idade , nota):

    #strip retira os whitespaces e joga um valor default pra dentro (None) se tiver nulo
    if nome.strip() == "":
        return "Nome do aluno não pode estar vazio"

    elif idade > 22:
        return "Idade acima de 22 anos"

    else:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (? , ? , ?)" , (nome , idade , nota))

    conn.commit()
    conn.close()
    return "Aluno cadastrado com sucesso!"


#busca um aluno por nome
def buscar_aluno_nome(busca_nome):

    conn = conectar()
    cursor = conn.cursor()

    #a vírgula é pq é uma tupla de 1
    cursor.execute("SELECT * FROM alunos WHERE nome = ?" , (busca_nome,))

    #pega a lista e guarda em alunos
    alunos = cursor.fetchall()

    #sem commit já que não altera o banco de dados
    conn.close()

    return alunos

#busca um aluno por ID
def buscar_aluno_id(busca_id):

    conn = conectar()
    cursor = conn.cursor()

    #a vírgula é pq é uma tupla de 1
    cursor.execute("SELECT * FROM alunos WHERE id = ?" , (busca_id,))

    #pega a lista e guarda em alunos
    alunos = cursor.fetchall()

    #sem commit já que não altera o banco de dados
    conn.close()

    return alunos

#mudar aluno
def atualizar_aluno(nome , idade , nota , id):

    #if tudo nao nulo:

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE alunos SET nome = ? , idade = ? , nota = ? WHERE id = ?" , (nome , idade , nota , id))
    
    conn.commit()
    conn.close()
    return "Aluno atualizado!"

#deletar aluno
def deletar_aluno(id):
    if id > 0:
            
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM alunos WHERE id = ?" , (id,))

        conn.commit()
        conn.close()

        return f"O aluno de ID {id}, foi deletado"

    else:
        return "ID inserido é invalido"
