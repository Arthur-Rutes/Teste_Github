import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

# Usando Metodo De Seno Do Numpy

y_line = np.sin(x)

categorias = ['Ação','Comédia','Drama','Terror']

valores = [50,60,15,20]

# Dados Por Gráfico De Dispersão

x_scatter = np.random.rand(50)

y_scatter = x_scatter + np.random.rand(50)*0.1

# Histograma
hist_data = np.random.randn(1000)

fig, axs = plt.subplots(2,2, figsize=(10,8))

axs[0,0].plot(x,y_line, color='red', linestyle='--', label='sin(x)')
axs[0,0].set_title('Grafico De Linha')
axs[0,0].legend()

axs[0,1].bar (categorias, valores, color=['lime','indigo','yellow','purple'])
axs[0,1].set_title('Gráfico De Barras | Colunas')

axs[1,0].scatter(x_scatter,y_scatter, alpha=0.6,color='crimson')
axs[1,0].set_title('Gráfico De Dispersão')

axs[1,1].hist(hist_data,bins=30, color='pink',edgecolor='violet')
axs[1,1].set_title('Histograma')

fig.tight_layout()

plt.show()