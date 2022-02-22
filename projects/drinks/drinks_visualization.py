#!/usr/bin/env python
# coding: utf-8

# # Oficina Aula 1.1

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 1.1 do curso de Visualização de dados

# In[2]:


import pandas as pd
df = pd.read_csv('drinks.txt')


# In[63]:


print('1. A média e desvio padrão do consumo de cerveja, licor, vinho e total de álcool são respectivamente:')

df.mean(), df.std()


# In[64]:


print('2. O consumo de licor na França é: ')

df.iloc[[61], [0, 2]]


# In[65]:


print('3. Os 5 países nos quais se consome mais vinho são:')


df.sort_values(by='wine_servings', ascending = False).head()


# In[66]:


print('4. Os países nos quais o consumo de cerveja está acima da média são:')


df[df['beer_servings'] > 106.160622]


# In[67]:


print('5. Os países nos quais o consumo total de álcool está acima do Brasil, em ordem do menor para o maior são:')


df[df['total_litres_of_pure_alcohol'] > 7.2].sort_values(by = 'total_litres_of_pure_alcohol', ascending = True)

