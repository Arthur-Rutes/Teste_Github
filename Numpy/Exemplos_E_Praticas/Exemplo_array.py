import numpy as np

# Saída O Array E As Dimensões Pelo Método (ndim)
arr1d = np.array([1,2,3])
print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}")

arr2d = np.array([[1,2,3,4,5],[5,6,8,9,7]])
print(f"Array 2D: {arr2d}, Dimensões: {arr2d.ndim}")

arr3d = np.array([[[0,5,7],[9,7,2]],[[6,4,7],[5,2,3]]])
print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}")

# Shape.
# Indica O Tamanho Do Array. 
print(f"Shape Do arr1d: {arr1d.shape}")
print(f"Shape Do arr2d: {arr2d.shape}")
print(f"Shape Do arr3d: {arr3d.shape}")


# Dtype.
# Indica Qual O Tipo De Dado Da Array.
array_float = np.array([1.5, 1.8, 6.3])
print(f"O Dtype Dessa Array É: {array_float.dtype}")
print(f"O Dtype Da arr1d É: {arr1d.dtype}")


# Itemsize
# Retorna O Comprimento De Cada Elemento Da Matriz Em Bytes.
print(f"O Itemsize Do arr1d É: {arr1d.itemsize}")
print(f"O Itemsize Do arr3d É: {arr3d.itemsize}")
print(f"O Itemsize Do array_float É: {array_float.itemsize}")


