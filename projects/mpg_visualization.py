#!/usr/bin/env python
# coding: utf-8

# # Oficina 4.2

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 4.2 do curso de Visualização de dados.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="darkgrid")


# In[2]:


carros = sns.load_dataset("mpg")
carros.head()


# In[3]:


sns.pairplot(carros, hue='origin')


# É possível verificar uma forte correlação entre as variáveis mpg e peso; cilindrada e peso; cavalos de potência e peso e cavalos de potência e aceleração.

# In[4]:


sns.pairplot(carros, kind = 'reg')


# Apesar da diferenciação ser resultada através das cores diferentes dos países de origem, no gráfico de distribuição de uma variável, em basicamente todos os casos as curvas se sobrepõe, dificultanto a percepção destas. Entretanto, os gráficos de distribuição conjunta permitem maior distinção entre os países de origem, assim como a interpretação dos dados.  

# In[10]:


sns.jointplot(x="weight", y="horsepower", kind = 'reg', data=carros)

