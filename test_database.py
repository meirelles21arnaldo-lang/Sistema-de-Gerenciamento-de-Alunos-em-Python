import unittest
import sqlite3 as sql
import os
import database as db

class TestCadastroAluno(unittest.TestCase):

    def setUp(self):
        #cria uma variavel que guarda o nome banco_teste.db
        self.banco_teste = "banco_teste.db"
        #chama o criar tabela e passa o nome banco teste
        db.criar_tabela(nome_banco = self.banco_teste)

    def tearDown(self):
        if os.path.exists(self.banco_teste):
        #se no caminho do programa que me chamou, tme um banco_teste.db existe:
            os.remove(self.banco_teste)

    def test_cadastrar_aluno_com_sucesso(self):
            db.cadastro_aluno("Lohan Victor" , 17 , 1.5 , self.banco_teste)

            conn = sql.connect(self.banco_teste)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alunos WHERE nome = 'Lohan Victor'")
            aluno_salvo = cursor.fetchone()
            conn.close()

            self.assertIsNotNone(aluno_salvo,"O Aluno deveria ter sido cadastrado")
            self.assertEqual(aluno_salvo[1], "Lohan Victor")
            self.assertEqual(aluno_salvo[2], 17)

    def test_cadastrar_aluno_com_mais_de_22(self):

        resultado = db.cadastro_aluno("Lohan Victor" , 25 , 1.5 , self.banco_teste)

        self.assertEqual(resultado , "Idade acima de 22 anos.")

    def test_cadastrar_nota_com_mais_de_10(self):
        aluno_salvo = db.cadastro_aluno("Lohan Victor" , 17 , 11 , self.banco_teste)

        self.assertEqual(aluno_salvo, "Nota não pode ser maior que 10 e/ou menor que 0")

class TestGetAluno(unittest.TestCase):

    def setUp(self):
        self.banco_teste = "banco_teste.db"
        db.criar_tabela(nome_banco = self.banco_teste)

    def tearDown(self):
        if os.path.exists(self.banco_teste):
            os.remove(self.banco_teste)

    def test_pega_aluno_sucesso(self):
        db.cadastro_aluno("Lohan Victor", 17, 8.5, self.banco_teste)
        db.cadastro_aluno("Maria Victória", 18, 9.0, self.banco_teste)

        lista_alunos = db.getAlunos(self.banco_teste)

        self.assertEqual(len(lista_alunos) , 2)
        self.assertEqual(lista_alunos[0][1] , "Lohan Victor")
        self.assertEqual(lista_alunos[1][1] , "Maria Victória")

    def test_pega_aluno_vazio(self):
        lista_alunos = db.getAlunos(self.banco_teste)

        self.assertEqual(lista_alunos , [])

class TestDeletarAluno(unittest.TestCase):

    def setUp(self):
        #cria uma variavel que guarda o nome banco_teste.db
        self.banco_teste = "banco_teste.db"
        #chama o criar tabela e passa o nome banco teste
        db.criar_tabela(nome_banco = self.banco_teste)

    def tearDown(self):
        if os.path.exists(self.banco_teste):
        #se no caminho do programa que me chamou, tme um banco_teste.db existe:
            os.remove(self.banco_teste)

    def test_deletar_aluno_com_sucesso(self):
        db.cadastro_aluno("Lohan Victor" , 17 , 1.5 , self.banco_teste)

        conn = sql.connect(self.banco_teste)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM alunos WHERE nome = 'Lohan Victor'")
        aluno_salvo = cursor.fetchone()

        db.deletar_aluno(aluno_salvo[0] , self.banco_teste)
        
        cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_salvo[0],))
        aluno_deletado = cursor.fetchone()
        conn.close()

        self.assertIsNone(aluno_deletado, "O aluno deveria ter sido deletado do banco de dados")

    def testar_deletar_id_invalido(self):
        resultado = db.deletar_aluno(0 , self.banco_teste)

        self.assertEqual(resultado , "ID inserido é invalido")

    def testar_deletar_id_inexistente(self):
        resultado = db.deletar_aluno(400 , self.banco_teste)

        self.assertEqual(resultado , "ID inserido é invalido")

class TestUpdateAluno(unittest.TestCase):

    def setUp(self):
        #cria uma variavel que guarda o nome banco_teste.db
        self.banco_teste = "banco_teste.db"
        #chama o criar tabela e passa o nome banco teste
        db.criar_tabela(nome_banco = self.banco_teste)

    def tearDown(self):
        if os.path.exists(self.banco_teste):
        #se no caminho do programa que me chamou, tme um banco_teste.db existe:
            os.remove(self.banco_teste)

    def test_update_aluno_com_sucesso(self):

        db.cadastro_aluno("Lohan Victor" , 17 , 1.5 , self.banco_teste)
        
        conn = sql.connect(self.banco_teste)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM alunos WHERE nome = 'Lohan Victor'")
        aluno_salvo = cursor.fetchone()

        db.update_idade_aluno(aluno_salvo[0] , 18 , self.banco_teste)

        cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_salvo[0],))
        aluno_atualizado = cursor.fetchone()
        conn.close()

        self.assertEqual(aluno_atualizado[2] , 18)

    def test_update_aluno_maior_de_22(self):

        db.cadastro_aluno("Lohan Victor" , 17 , 1.5 , self.banco_teste)
                
        conn = sql.connect(self.banco_teste)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM alunos WHERE nome = 'Lohan Victor'")
        aluno_salvo = cursor.fetchone()

        resultado = db.update_idade_aluno(aluno_salvo[0] , 26 , self.banco_teste)

        self.assertEqual(resultado , "Idade acima de 22 anos não é permitida!")
        conn.close()

if __name__ == "__main__":
    unittest.main()
