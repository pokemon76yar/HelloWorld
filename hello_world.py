import random

def pl(t):
    for i in t:
        print(*i)

def creatArray():
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    a = []
    for i in range(x):
        a.append([])
        for j in range(y):
            a[i].append(random.randint(0,10))
    return a

def plus(m1,m2):
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        print('Матрицы разной размерности нельзя складывать!')
    else:
        s=0
        res = []
        for i in range(len(m1)):
            res.append([])
            for j in range(len(m1[i])):
                res[i].append(m1[i][j]+m2[i][j])
        print('Результат сложения 2 матриц:')
        return pl(res)

matrix1=creatArray()
matrix2=creatArray()
print('Матрица 1: ')
pl(matrix1)
print('Матрица 2: ')
pl(matrix2)
res=plus(matrix1,matrix2)

