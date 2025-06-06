import numpy as np
# np.array Converte Tuplas E Listas Em Array (Arranjo)
arr1d = np.array([90,77,1,37,12])

arr2d = np.array([[9.8,7.2,1.2],[7.7,6.6,5.5]])

print(f"Numero Total De Elementos Do Array 1D: {arr1d.size}\nDimensões: {arr1d.ndim}\nShape Do arr1d: {arr1d.shape}\nDtype Da Array1: {arr1d.dtype}\nItemsize Do arr1d: {arr1d.itemsize}")
print("")
print(f"Numero Total De Elementos Do Array 2D: {arr2d.size}\nDimensões: {arr2d.ndim}\nShape Do arr2d: {arr2d.shape}\nDtype Da Array2: {arr2d.dtype}\nItemsize Do arr2d: {arr2d.itemsize}")
