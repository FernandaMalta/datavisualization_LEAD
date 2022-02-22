#!/usr/bin/env python
# coding: utf-8

# # Oficina 2.2

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 2.2 do curso de Visualização de dados

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


games = pd.read_csv('dadosoficina04.txt')
games.head(10)


# In[43]:


nintendo = games[games['Publisher'] == 'Nintendo']
nintendo


# In[44]:


genero = nintendo.groupby(by='Genre').sum()
genero


# In[48]:


plt.style.use('seaborn-muted')
plt.pie(x=genero['Global_Sales'], labels = genero.index, autopct='%1.1f%%',startangle=90, pctdistance=0.90)
my_circle=plt.Circle((0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title('Proporção de vendas global entre gêneros de jogos')
plt.show()


# In[47]:


genero = genero.sort_values(by='Global_Sales', ascending=False)
porcentagens = genero['Global_Sales']*100.0/genero['Global_Sales'].sum()
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(16,5))
plt.bar(genero.index,porcentagens)
plt.title('Proporção de vendas global entre gêneros de jogos')
plt.show()


# In[4]:


ano = games[games['Year'] >= 2015]
ano.head(10)


# In[5]:


plataforma = ano.groupby(by='Platform').sum()
plataforma


# In[6]:


plataforma = plataforma.sort_values(by='Year', ascending=False)
porcentagens = plataforma['Year']*100.0/plataforma['Year'].sum()
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(16,5))
plt.bar(plataforma.index,porcentagens)
plt.title('Proporção da quantidade de jogos por plataforma')
plt.show()

