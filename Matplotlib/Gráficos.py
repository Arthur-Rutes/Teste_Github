import numpy as np
import matplotlib.pyplot as plt

# Gráfico De Linha
x = [1,2,3,4,5,6]
y = [2,5,8,9,10,12]

plt.plot(x,y)
plt.title('Exemplo De Linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()

# Gráfico De Barra
categorias = ['A','B','C']
valores = [10,2,30]

plt.bar(categorias,valores)
plt.title('Barras')
plt.show()

# Gráfico De Setores

plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Setores')
plt.show()

# Histograma
dados = np.random.randn(1000)
plt.hist(dados,bins=30)
plt.title('Histograma')
plt.show()

# Dispersão

a = np.random.rand(50)
b = a + np.random.randn(50)*0.1
plt.scatter(a,b)
plt.title('Dispersão')
plt.show()


