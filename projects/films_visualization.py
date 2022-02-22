#!/usr/bin/env python
# coding: utf-8

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 2.1 do curso de Visualização de dados

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


filmes_uri = 'https://d11s0xq1vqg039.cloudfront.net/videos_conteudo/visual/micro03/oficina/arquivos/dadosoficina03.txt'
filmes = pd.read_json(filmes_uri)
filmes.head()


# In[19]:


sns.set(style="darkgrid")
plt.figure(figsize=(12,7))
plt.title('Visualização dos filmes de acordo com o orçamento')
sns.barplot(x="Budget_M", y="Film", color='r', ci = 'sd', data=filmes)
plt.show()


# De acordo com a visualização, podemos verificar que o filme com o maior orçamento foi Pirates of the Caribbean: At World's End e o filme com menor orçamento foi The Twilight Saga: New Moon.

# In[18]:


plt.figure(figsize=(10,7))
plt.title('Categorização dos filmes por bilheteria')
sns.barplot(x="Worldwide_Gross_M", y="Film", color = 'g', ci = 'sd', data=filmes)
plt.show()


# Conforme o gráfico descreve, o filme com maior bilheteria foi Avatar e de menor bilheteria foi Ratatouille.

# In[20]:


plt.figure(figsize=(15,8))
plt.title('Quantidade de filmes por gênero em cada ano')
sns.countplot(x="Year", hue= 'Genre', palette ="Set2", edgecolor="0.6", data=filmes)
plt.show()


# Nos anos 2007 e 2010 foram produzidos menos filmes de ação. Enquanto isso, foram feitos menos filmes de animação nos anos 2008 e 2011. 

# In[22]:


plt.figure(figsize=(15,8))
plt.title('Média do orçamento de filmes por gênero em cada ano')

#aqui usando barplot() ao invés de countplot()
sns.barplot(x="Year", y = 'Budget_M' , ci = None, hue= 'Genre', data=filmes)
plt.show()


# Os filmes de ação tiveram maior média de orçamento nos anos 2007 e 2011.  Já os filmes de animação tiveram a maior média de orçamento nos anos 2008 e 2010. 
