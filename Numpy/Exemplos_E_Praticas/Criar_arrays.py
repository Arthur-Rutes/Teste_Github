import numpy as np

# Variavel Que Representa O Método default_rng.
rng = np.random.default_rng()

# Criar Array Apartir De Listas.
lista_py = [1,2,3,4,5,6,7,8,9,10]
print(lista_py)
array_1d = np.array(lista_py)
print(array_1d)
print("")
lista_py2 = [[1,2,3,4],[5,6,7,8]]
array_2d = np.array(lista_py2)
print(array_2d)
print("")

# np.zeros.
# Cria Um Array Preenchido Por Zeros.
# Cria Por Base Em Floats.
zero_array = np.zeros((3,3),int)
print(f"Array De Zeros:\n {zero_array}")
print("")

# np.ones.
# Cria Um Array Preenchido Por Uns.
one_array = np.ones((4,4),int)
print(f"Array De Uns:\n {one_array}")
print("")

# np.full.
# Cria Um Array Preenchido Com Números Especificos.
full_array = np.full((5,5),6.6)
print(f"Array Completo Pedido:\n {full_array}")
print("")

# np.arange.
alcance_fracional = np.arange(0.0,5.0,1.25)
alcance = np.arange(0,80,8)
print(f"Contagens Pedidas:\n {alcance}\n{alcance_fracional}")
print("")

# Array Aleatório.
# random e interger.
aleatoriedades = rng.random((2,2))
aleatoriedades2 = rng.integers(0, 500, size=15)
print(f"Array Aleatoriamente Preenchido:\n{aleatoriedades}")
print(f"Array Definido:\n{aleatoriedades2}")
print("")

# Indices Em Numpy.
# Indice Vetor.
array_indice = np.array([1,2,4,7,9])
print(f"Elemento 0: {array_indice[0]}")
print(f"Elemento 3: {array_indice[3]}")
print("")

# Indice Matriz.
array_indice2 = np.array([[1,2,4,6,7],[0,3,5,8,9]])
print(f"Elemento Na Linha 0, Coluna 3:\n {array_indice2[0,2]}")
print("")

# Slicing.
print("Slicing")
arr2d = np.array([[1, 2, 3, 4], #0
                  [5, 6, 12, 13], #1
                  [14, 7, 9, 22]]) #2
fatia2d_a = +arr2d[:3, 1:3]
print(fatia2d_a)
print("")

# Operações Matemáticas.
array_a = np.array([3,4,7,8])
array_b = np.array([1,5,6,9])

# Adição.
soma = array_a + array_b
print(soma)
print("")

# Subtração.
menos = array_a - array_b
print(menos)
print("")

# Multiplicação.
vezes = array_a * array_b
print(vezes)
print("")

# Divisão.
divisao = array_a / array_b
print(divisao)
print("")

# Copy E View.
# Copy Copia E Cria Um Novo Arquivo, Diferentemente Do View Que Só Espelha Tal Arquivo.
precos = np.array([150.00,10.99,20.50])
print(f"Preços {precos}")

PrecoAjustado = precos
print(precos[0] * 2)
print("")

PrecoAjustado2 = precos.copy()
print(PrecoAjustado2)
print("")

# Iteração
array_inter = np.array([1,2,3,4,5,6,25,78,99,105,133,666,1332,1998])

for n in array_inter:
    print(f"Valor{n}")
print("")

# Sum E Mean

o_array = np.array([15,25,84,62,11,3])
soma = np.sum(o_array)
media = np.mean(o_array)