import streamlit as st
import database as db

db.criar_tabela()

st.title("Painel de Gestão de Alunos", text_alignment="center")

st.markdown("#### --- Cadastro Alunos ---", text_alignment="center")
with st.form("cadastro_aluno"):

    nome = st.text_input("Preecha com o NOME COMPLETO do aluno")#nome do aluno 
    idade = st.number_input("Preecha com a IDADE do aluno", value=50)#idade do aluno, e o step é o valor para pularde 1 em 1
    nota = st.number_input("Preecha com a NOTA do aluno", min_value=0.0, max_value=10.0, step=0.5)
    data = st.date_input("Data de Nascimento", value="today")

    btn_from= st.form_submit_button("Enviar")

if btn_from:
    msg = db.criar_aluno(nome, idade, nota)
    st.warning(msg)

st.markdown("#### --- Exclusão de Aluno ---", text_alignment="center")
with st.form("deletar_aluno"):
    id_aluno = st.number_input("ID do Aluno", value=0, step=1, min_value=0)

    btn_delete_aluno = st.form_submit_button("Deletar", 
    help= "Ao clicar aqui você deleta um aluno")
# help= "Ao clicar aqui você deleta um aluno" é a mensagem que aparece quando o mouse fica em cima do botãos
if btn_delete_aluno:
        msg = db.deletar_aluno(id_aluno)
        st.success(msg)

#muda o nome, idade e nota de um aluno por id
st.markdown("--- Alteração de cadastro de alunos ---", text_alignment="center")
with st.form("form_update_aluno"):
        id_aluno = st.number_input("ID do aluno", value=0, step=1, min_value=0)          
        idade = st.number_input("Idade", value=0)

        btn_update_aluno = st.form_submit_button("Alterar")

if btn_update_aluno:
        msg = db.update_idade_aluno(id_aluno, idade) 

        if msg == 1:
                st.success("Aluno alterado com glória!") 
        else:
                st.error(msg)

st.markdown("#### --- Lista de Alunos Cadastrados ---" , text_alignment="center")

listaAlunos = db.getAlunos()

if listaAlunos == None:
        st.warning("Não há alunos cadastrados!")
else:
        dataAlunos = [{"ID" : aluno[0], "Nome": aluno [1] , "Idade": aluno[2] , 
                        "Nota": aluno[3] } for aluno in listaAlunos]

        st.dataframe(dataAlunos, width="stretch")
