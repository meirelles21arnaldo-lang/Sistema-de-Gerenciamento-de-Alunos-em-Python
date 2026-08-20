import streamlit as st
import database as db

#roda o criar tabela
db.criar_tabela()

#front-end
st.title("Sistema de Gerenciamento da Escola", text_alignment="center")
st.subheader("Cadastro, busca, atualização e remoção de alunos", text_alignment="center")

resp = st.selectbox("Ação Desejada:" , ["Cadastrar Aluno" , "Buscar Aluno" , "Deletar Aluno" , "Atualizar Aluno"])

#switch case para diferentes telas
match resp:

        #Cadastra o aluno com formulário
        case "Cadastrar Aluno":
                with st.form("nome_do_formulario"):
                        #formulario do site
                        pega_nome = st.text_input("Nome")
                        pega_idade = st.number_input("Idade", value = 10 , min_value= 10 , max_value= 100)
                        pega_nota = st.number_input("Nota", value=0.0, step=0.5, min_value=0.0, max_value=10.0)

                        btn_form = st.form_submit_button("Enviar")

                if btn_form:
                        db.cadastrar_aluno(pega_nome , pega_idade , pega_nota)

        #Busca um aluno e exibe uma lista
        case "Buscar Aluno":
                st.text("Realizar busca do aluno por:")
                busca = st.selectbox("ID ou Nome" , ["ID" , "Nome"])

                #Busca por ID
                if busca == "ID":
                        pega_id = st.number_input("Digite o ID do Aluno:", min_value=1 , step=1)
                        btn = st.button("Buscar")

                        if btn:
                                aluno = db.buscar_aluno_id(pega_id)

                                if aluno:
                                        for item in aluno:
                                                aluno_id , aluno_nome , aluno_idade , aluno_nota = item

                                                with st.container():
                                                        st.text(f"Id: {aluno_id}")
                                                        st.text(f"Nome: {aluno_nome}")
                                                        st.text(f"Idade: {aluno_idade}")
                                                        st.text(f"Nota: {aluno_nota}")
                                                        st.text("--------------------")

                                else:
                                        st.warning("Nenhum aluno encontrado.")

                #Busca por Nome
                elif busca == "Nome":
                        pega_nome = st.text_input("Digite o Nome do Aluno:")
                        btn = st.button("Buscar")

                        if btn:
                                aluno = db.buscar_aluno_nome(pega_nome)

                                if aluno:
                                        for item in aluno:
                                                aluno_id , aluno_nome , aluno_idade , aluno_nota = item

                                                with st.container():
                                                        st.text(f"Id: {aluno_id}")
                                                        st.text(f"Nome: {aluno_nome}")
                                                        st.text(f"Idade: {aluno_idade}")
                                                        st.text(f"Nota: {aluno_nota}")
                                                        st.text("--------------------")

                                else:
                                        st.warning("Nenhum aluno encontrado.")
                        



        #muda o nome, idade e nota de um aluno por id
        case "Atualizar Aluno":
                with st.form("nome_do_formulario"):
                        #formulario do site
                        id_aluno = st.number_input ("Insira o ID do aluno:", value=0)
                        novo_nome = st.text_input("Novo Nome")
                        nova_idade = st.number_input("Nova Idade", value = 10 , min_value= 10 , max_value= 100)
                        nova_nota = st.number_input("Nova Nota", value=0.0, step=0.5, min_value=0.0, max_value=10.0)

                        btn_form = st.form_submit_button("Enviar")

                if btn_form:
                        db.atualizar_aluno(novo_nome , nova_idade , nova_nota, id_aluno)


        #deleta o aluno por id
        case "Deletar Aluno":
                with st.form("formulario deletar"):
                        id_aluno = st.number_input("Insira o ID do aluno a ser excluído", step=0)
                        btn_form = st.form_submit_button("Enviar")

                if btn_form:
                        db.deletar_aluno(id_aluno)
