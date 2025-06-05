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