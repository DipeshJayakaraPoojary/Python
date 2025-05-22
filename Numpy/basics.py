import numpy as np

print("arrays:1D")
arr = np.array([1,2,3])
print(arr)
print(arr.shape)
print(arr.dtype)

print("arrays:2D")
mat = np.array([[1,2],[3,4]])
print(mat)
print(mat.shape)
print(mat.dtype)

print("Zero matrix")
print(np.zeros((3,3)))

print("Identity matrix")
print(np.ones((2,2)))
print(np.eye(3))

print(np.arange(0, 10, 4))
print(np.linspace(0, 1, 5))
