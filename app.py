import pandas as pd
import streamlit as st
#from pycaret.regression import *
import joblib 

# loading the trained model.
model = joblib.load('model/modelo-amanda.pkl')

# carregando uma amostra dos dados.
dataset = pd.read_csv('StudentsPerformance.csv') 
#classifier = pickle.load(pickle_in)


# título
st.title("Data App - Predição de Notas de Matematica")

# subtítulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de predição de Notas de Matematica.")



st.sidebar.subheader("Defina os atributos do aluno para predição da nota de matematica")


# mapeando dados do usuário para cada atributo
leitura = st.sidebar.number_input("Nota de Leitura")
escrita = st.sidebar.number_input("Nota de Escrita")


genero = st.sidebar.selectbox("Gênero do Aluno",("Feminino","Masculino"))
raca = st.sidebar.selectbox("Raça/Etinia",("A","B","C","D","E"))
educacao = st.sidebar.selectbox("Grau de Escolaridade",("BD","SC","MD","AD","HS", "SHS"))
teste = st.sidebar.selectbox("Curso Preparatório para Teste",("Nenhum","Completo"))
almoco = st.sidebar.selectbox("Tipo de Almoço",("Gratuito/Reduzido","Padrão"))

# transformando o dado de entrada em valor binário
genero_female = 1 if genero == "Feminino" else 0
genero_male = 1 if genero == "Masculino" else 0

raca_A = 1 if raca == "A" else 0
raca_B = 1 if raca == "B" else 0
raca_C = 1 if raca == "C" else 0
raca_D = 1 if raca == "D" else 0
raca_E = 1 if raca == "E" else 0

educacao_AD = 1 if educacao == "AD" else 0
educacao_BD = 1 if educacao == "BD" else 0
educacao_HS = 1 if educacao == "HS" else 0
educacao_MD = 1 if educacao == "MD" else 0
educacao_SC = 1 if educacao == "SC" else 0
educacao_SHS = 1 if educacao == "SHS" else 0


teste_completed = 1 if teste == "Completo" else 0
teste_none = 1 if teste == "Nenhum" else 0

almoco_FR = 1 if almoco == "Gratuito/Reduzido" else 0
almoco_S = 1 if almoco == "Padrão" else 0


# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    data_teste = pd.DataFrame()

    data_teste["leitura"] =	[leitura]
    data_teste["escrita"] =	[escrita]    
    data_teste["genero_female"] = [genero_female]
    data_teste["genero_male"] = [genero_male]	
    data_teste["raca_A"] = [raca_A]
    data_teste["raca_B"] = [raca_B]
    data_teste["raca_C"] = [raca_C]
    data_teste["raca_D"] =	[raca_D]
    data_teste["raca_E"] =	[raca_E]
    data_teste["educacao_AD"] = [educacao_AD]
    data_teste["educacao_BD"] = [educacao_BD]
    data_teste["educacao_HS"] = [educacao_HS]
    data_teste["educacao_MD"] = [educacao_MD]
    data_teste["educacao_SC"] = [educacao_SC]
    data_teste["educacao_SHS"] = [educacao_SHS]
    data_teste["almoco_FR"] = [almoco_FR]
    data_teste["almoco_S"] = [almoco_S]
    data_teste["teste_completed"] = [teste_completed]
    data_teste["teste_none"] = [teste_none]


    #imprime os dados de teste    
    print(data_teste)

    #realiza a predição
    result = model.predict(data_teste)
    
    st.subheader("A nota final de matematica para o aluno é:")
    result = (round(result[0],2))
    
    st.write(result)


