import numpy as np

#Matriz 3x3.
{ 4a - 3b + c = -10 }
{ 2a +  b + 3c = 0  }
{ -a + 2b -  c = 17 }


A = np.array([
        [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
    ], dtype=np.dtype(float))

#Seus valores independentes.
b = np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

np.shape(A)
np.shape(b)

#Solução do sistema. Aqui usaremos uma função de NUMPY "np.linalg.solve(A, b)" que
#resolve uma equação de matriz linear, ou sistema de equações escalares lineares.

x = np.linalg.solve(A, b)
print(f"Solução: {x}")


#Determinante
d = np.linalg.det(A)

print(f"Determinante da matriz: {d:.2f}")

#Exemplo de um sistema que possui várias soluções, ou seja, D=0, singular.
A_2= np.array([
        [1, 1, 1],
        [0, 1, -3],
        [2, 1, 5]
    ], dtype=np.dtype(float))

b_2 = np.array([2, 1, 0], dtype=np.dtype(float))


try:
    d_2 = np.linalg.det(A_2)
    x_2 = np.linalg.solve(A_2, b_2)
except np.linalg.LinAlgError as err:
    print(f"O determinante é {d_2:.2f}, logo uma {err}")

#A resposta será o valor do determinante  e se a matriz é singular ou não singular.
