import numpy as np
import lattice as it

# v = np.array([0,1,2,3,4,5,6,7])
# mod_vec = v % 3
# print(f"Vector: {mod_vec}")
# print(f"Number of elemtns: {v.size}")
# print(f"Dimesion: {v.ndim}")

# print("\n--------------------------------\n")

# matrix = np.array([
#         [0,1,2,3],
#         [4,5,6,7]])
# print(f"Matrix: {matrix}")
# print(f"Number of elements: {matrix.size}")
# print(f"Dimension: {matrix.ndim}")

# print("\n--------------------------------\n")


#Random Number Generator

# np.random.seed(6)
# vector = np.random.randint(low=-10, high=11, size=5)
# print(f"Vector: {vector}")
# matrix = np.random.randint(low=-10, high=11, size=(3,3))
# print(f"Matrix: {matrix}")



# #Ex.1
# def ex1(seed, dim, mod):
#     np.random.seed(seed)
#     vector = np.random.randint(low=-mod+1, high=mod, size=dim)
#     print(f"Vector: {vector}")
#     matrix = np.random.randint(low=-mod+1, high=mod, size=(dim,dim))
#     print(f"Matrix: {matrix}")
#     c = np.dot(matrix, vector) % mod
#     print(f"\nc:{c}")
     
# #Func call
# ex1(6,3,11)

# print("\n--------------------------------\n")

#Lattice - Good and Bad Bases
L = np.array([[2,0,0],[1,1,0],[0,0,3]])
#print(f"Hamadamard's Ratio for L: {it.hamdamard_ratio(L)}")

U = it.rand_unimod(3)
B = np.matmul(L,U)
#print(f"Hamadamard's Ratio for B: {it.hamdamard_ratio(B)}")


#Ex.2
def distance_lattice_vector(basis, v):
    b = it.babai(basis, v)
    dist = np.linalg.norm(np.abs(v - b))
    return dist

#Func call
v1 = [-5,1,0]
v2 = [-10,1,13]

# #For v1
# print(distance_lattice_vector(B, v1))
# print(distance_lattice_vector(U, v1))

# #For v2
# print(distance_lattice_vector(B, v2))
# print(distance_lattice_vector(U, v2))



def func(basis1, basis2, v):
    dist_basis1_v = distance_lattice_vector(basis1, v)
    dist_bassis2_v = distance_lattice_vector(basis2, v)

    if (dist_basis1_v < dist_bassis2_v):
        print(-1)
    elif (dist_basis1_v == dist_bassis2_v):
        print(0)
    else:
        print(1)

func(U,B,v1)
func(U,B,v2)