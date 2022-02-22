#!/usr/bin/env python
# coding: utf-8

# # Oficina 3.2

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 3.2 do curso de Visualização de dados.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="darkgrid")


# In[2]:


mpg = sns.load_dataset("mpg")
mpg.head()


# In[8]:


sns.relplot(x="acceleration", y="mpg", col = 'origin', data=mpg)


# A forma como os dados estão muito espalhados de forma aleatória pelo gráfico demonstram que principalmente para a origem do japão e europa não há uma correlação entre os dados. Entretando, para o USA, apresenta certa correlação não linear. 

# In[10]:


plt.figure(figsize=(8,5))
plt.title('Relação entre a aceleração, consumo de combustível  e ano do modelo')
sns.scatterplot(x="acceleration", y="mpg", hue = 'model_year', data=mpg)
plt.show()


# Essas três variáveis aparentam ter correlação, visto que a maiorida dos dados, conforme a aceleração aumenta, o combustível também. Além disso, é visível que os valores numéricos dos anos do modelo vão aumentando progressivamente conforme aumentam os anos. 
