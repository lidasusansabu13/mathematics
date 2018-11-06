#Program to find the inverse of a matrix
import numpy as np
n=input("enter the size of the matrix")
mat=np.zeros((n,n)) #initializing with zeros
for i in range(n):
    mat[i]=input().split(" ")
matt=mat.I 
print(matt)
