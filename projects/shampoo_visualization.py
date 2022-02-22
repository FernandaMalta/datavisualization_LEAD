#!/usr/bin/env python
# coding: utf-8

# # Oficina 3.3

# ##### Este código foi escrito pela aluna Fernanda Malta para a avaliação do tópico 3.3 do curso de Visualização de dados.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="darkgrid")


# In[3]:


uri = 'https://d11s0xq1vqg039.cloudfront.net/videos_conteudo/visual/micro07/oficina/arquivos/dadosoficina07.txt'
shampoo = pd.read_csv(uri)
shampoo.head(10)


# In[9]:


plt.figure(figsize=(20,7))
plt.title('Vendas de Shampoo ao longo dos meses')
sns.lineplot(x="Month", y="Sales", data=shampoo)
plt.show()


# Com estes dados é possível observar uma tendência crescente na venda de shampoo ao longo dos meses.  
