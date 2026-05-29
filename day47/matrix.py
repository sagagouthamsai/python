matrix1=[
    [1,2],
    [3,4]]

matrix2=[
    [1,2],
    [3,4]
]

mat3=[]

for i in range(len(matrix1)):
    row=[]
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j]+matrix2[i][j])
    print(row)
    mat3.append(row)

print("\n",mat3)


