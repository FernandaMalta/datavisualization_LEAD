#!/usr/bin/env python
# coding: utf-8

# # Oficina 4.1

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 4.1 do curso de Visualização de dados.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="darkgrid")


# In[18]:


titanic = sns.load_dataset("titanic")
titanic.head(10)


# In[20]:


plt.figure(figsize=(10,6))
plt.title('Distribuição do valor da passagem de acordo com a cidade na qual o passageiro embarcou')
sns.stripplot(x="embark_town", y="fare", data=titanic)
plt.show()


# In[25]:


sns.catplot(x="embark_town", y="fare", hue = 'sex', col = 'survived', kind = 'swarm', data=titanic)


# É possível verificar nesse conjunto de dados, que a maioria dos passageiros que sobreviveram foram mulheres. Além disso, nota-se que os passageiros que pagaram valores maiores que 500 na passagem sobreviveram, indepente do gênero. 
