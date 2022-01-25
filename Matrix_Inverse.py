print("YOU CAN FIND THE INVERSE OF A 2X2 MATRIX:")
print("ENTER THE ELEMENTS OF ROW 1 FIRST AND THEN THE ELEMENTS OF ROW 2.")
a = 2
b = 2
matrix = [[int(input("enter the element:"))for j in range(a)]for i in range(b)] #TO ENTER THE ELEMENTS OF THE MATRIX.

#To print the matrix:
for i in range(a):
    for j in range(b):
         print(matrix[i][j], end=" ")
    print()
#To calculate the determinant of the matrix:
def determinant(m):
    h=m[0][0]
    i=m[0][1]
    j=m[1][0]
    k=m[1][1]
    det = (h*k)-(i*j)
    return det

# To find the cofactors of the matrix:
def cofactor(k):
    A11= k[1][1]
    A12 =(-1)* k[1][0]
    A21 = (-1)*k[0][1]
    A22 = k[0][0]
    CFM = [[A11,A12],[A21,A22]]
    return CFM

d= determinant(matrix)
print("Determinant of the matrix is:",d)
if d==0:
    print("INVERSE OF THE MATRIX DOES NOT EXIST")
else:
    CM = cofactor(matrix) #cofactor() is being called here.
    print("The cofactor matrix is:")
    for i in range(a):
        for j in range(b):
             print(CM[i][j], end=" ")
        print()
    print()
    print("The adjoint of the matix is:")
    for j in range(a):
        for i in range(b):
             print(CM[i][j], end=" ")
        print()
    print()
    # Inverse of a matrix exists only if its determinant is not equal to 0. Inverse = (1/det(A))*adj(A) for any matrix A

    print("The inverse of matrix is:")
    for j in range(a):
        for i in range(b):
             print((1/d)*(CM[i][j]) , end=" ")
        print()
