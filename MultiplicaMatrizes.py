def transpor(matriz):
    lin = []
    Bt = []
    for j in range(len(matriz[0])):
        
        for i in range(len(matriz)):
            lin.append(matriz[i][j])

        Bt.append(lin)
        lin = []
    return Bt


#u = [ [1,1], [1,1] ] 2 x 2
#v = [ [2,2,2], [2,2,2] ] 2 x 3
#multiplica(u,v) 2 x 3
def multiplica(A,B):
    Bt = transpor(B)
    AB = []
    linA = []
    linBt = []
    linAB = []
    p = 0

    for i in range(len(A)):
        linA = A[i]
        
        for j in range(len(Bt)):
            linBt = Bt[j]

            for k in range(len(A[i])):
                p += linA[k] * linBt[k]
            linAB.append(p)
            p = 0
        AB.append(linAB)
        linAB = []
    return AB





def prod(a,b):
    S = 0
    for i in range(len(a)):
        S += a[i] * b[i]
    return S
