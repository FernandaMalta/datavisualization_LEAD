#!/usr/bin/env python
# coding: utf-8

# # Oficina Aula 3.1

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 3.1 do curso de Visualização de dados.

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


df = pd.read_csv('dadosoficina05.txt')
df.head(10)


# In[15]:


plt.figure(figsize=(10, 5))
plt.style.use('seaborn-darkgrid')
plt.title('Distribuição dos valores de aluguel')
plt.hist(df['rent amount (R$)'], bins=25)
plt.show()


# A faixa de valores de aluguel mais comuns estão estão aproximadamente entre *1000* e *2500* reais.

# In[14]:


plt.figure(figsize=(10, 5))
plt.title('Distribuição de áreas dos imóveis')
sns.distplot(df['fire insurance (R$)'])
plt.show()


# Os valores a partir de 150 reais para o seguro contra incêndio aparentam ser incomuns.
