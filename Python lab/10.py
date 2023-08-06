# matrix multiplication
import numpy as np

# Two dimensional arrays
print("Two dimensional arrays")
m1 = np.array([[1,2,3],[4,5,5]])
print(f'Elements of matrix a ::\n {m1}')
m2 = np.array([[7,8],[4,10],[5,3]])
print(f'Elements of matrix  ::\n {m2}')
m3 = np.dot(m1,m2) 
print(f'Multiplication of two matrix is::\n {m3}')
  

