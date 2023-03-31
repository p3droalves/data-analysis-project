#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=share_link

# In[18]:


# Passo a passo.
# Passo 1: Importar a base de dados.
import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")
display(tabela) 


# In[19]:


# Passo 2: Visualizar a base de dados.
    # -> Entender as informações disponibilizadas.
    # -> Procurar erros na base de dados.
    # -> Deletar a coluna inútil.
import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

    # -> Deletar a coluna inútil.
    # -> axis= 0 (tratamos linhas), axis= 1 (tratamos colunas) 
tabela = tabela.drop("Unnamed: 8", axis=1)
display(tabela) 


# In[20]:


# Passo 3: Tratamento de dados.

    # -> Acertar informações reconhecidas de forma errada.
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

    # -> Corrigir colunas vazias.
tabela = tabela.dropna()
print(tabela.info())

    # -> Tratar salário que está sendo reconhecido como texto.


# In[24]:


# Passo 4: Análise inicial -> Entender notas e requisitos dos clientes.
display(tabela.describe())

import plotly.express as px

# Criar gráfico
for coluna in tabela.columns:
    gráfico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc= "avg", text_auto=True, )
    # Exibir gráfico
    gráfico.show()




# In[22]:


# Perfil ideal:
# Acima de 15 anos
# Faixa salarial não é relevante
# Áreas de trabalho : Entretenimento e artistas, evitar contrução
# Experiência de 10 a 15 anos
# Com famílias até no máximo 6 pessoas
  


# In[23]:


# Passo 5: Análise completa -> Entender cada característica específica dos clientes.



