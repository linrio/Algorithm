#7 Simplex Algorithm
#Please implement simplex algorithm or dual simplex algorithm with your favorate language,
#and make comparison with GLPK or Gurobi or other similar tools.

import numpy as np
def simplex(A, B, C):
    count = 0
    z = 0
    while(True):
        e = np.argmin(C);
        #选出选C中最小的那列中，B/A 最小者的那一行"l"行
        mini = B[0]/A[0][e]
        l=0
        for i in range( A.shape[0] ):
            if A[i][e] == 0:
                continue
            elif B[i] / A[i][e] < 0:
                continue
            elif B[i] / A[i][e] < mini:
                mini = B[i] / A[i][e]
                l = i;
            else:
                continue

        #对A, B的第l行变换
        if A[l][e] ==0:
            B[l] = B[l]
        else:
            B[l] = B[l] / A[l][e]

        for j in range(A.shape[1]):
            if A[l][e] == 0:
                A[l][j] = A[l][j]
            else:
                A[l][j] = A[l][j] / A[l][e];

        #对B及A剩下的行做变换
        for i in range(A.shape[0]):
            if i == l:
                continue;
            else:
                B[i] = B[i] - A[i][e]*B[l];
                for j in range(A.shape[1]):
                    A[i][j] = A[i][j] - A[i][e]*A[l][j];

        #求目标函数
        z = z - B[l]*C[e];
        for j in range(A.shape[1]):
            C[j] = C[j] - C[e]*A[l][j];

        #设置一个计数器，当C的没有负值时即找到最优解。
        for j in range(A.shape[1]):
            if C[j] >= 0:
                count+=1
            else:
                continue
        if count == A.shape[1]:
            break
        else:
            count = 0
    return A, B, C, z



#原参数矩阵
Q = np.array([[1,1,1],
              [1,0,0],
              [0,0,1],
              [0,3,1]]);

#增加松弛变量后的参数矩阵
A = np.array([[1,1,1,1,0,0,0],
              [1,0,0,0,1,0,0],
              [0,0,1,0,0,1,0],
              [0,3,1,0,0,0,1]]);
B = [4,2,3,6];
C = [-1,-14,-6,0,0,0,0];
D = simplex(A, B, C);
print D
