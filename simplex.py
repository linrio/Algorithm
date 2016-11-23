#7 Simplex Algorithm
#Please implement simplex algorithm or dual simplex algorithm with your favorate language,
#and make comparison with GLPK or Gurobi or other similar tools.
# Author: Lin Lingfeng  ID:201628017729008
#Attention: Please test and verify by ipython

import numpy as np
def simplex(A, B, C):
    count = 0
    z = 0
    e = 0
    L = [4,5,6,7]
    while(True):
        
        #选出C中的负数的最大值cmax，以及最大负数对应的列e。
        cmax = min(C)
        c_i = np.argmin(C)
        e = c_i
        for i in range(A.shape[1]):
            if i ==c_i:
                continue
            elif C[i] >= 0:
                continue
            elif C[i] >= cmax:
                cmax = C[i]
                e = i
            else:
                continue
        
        #先判断C的最小值是否非负，若非负数则表明最优解已经找到。
        #选出e那列的B/A的值最小的那一行，记为l行
        if  min(C)== 0:
            print "break in min[C] == 0"
            break
        else:
            mini = 100
            #mini = B[0]/A[0][e]
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
            #注意这里要把A[i][e]存到一个临时变量a_ie，因为A{i}[e]在更新A[i][j]的时候会被更改。
            for i in range(A.shape[0]):
                if i == l:
                    continue;
                else:
                    B[i] = B[i] - A[i][e]*B[l];
                    a_ie=A[i][e]
                    for j in range(A.shape[1]):
                        A[i][j] = A[i][j] - a_ie*A[l][j];
            
            #对目标函数z,目标函数的参数C做变换(第一行作变换)
            #注意此时也要把C[e]存到一个临时变量c_e，因为C[e]在更新C[j]的时候会被更改。
            z = z - B[l]*C[e];
            c_e = C[e]
            for j in range(A.shape[1]):
                C[j] = C[j] - c_e*A[l][j];
            
            #B的解，L向量代表最优解在B中的位置
            L[l] = e
            
            
            #对C的非负数的个数计数，如果非负数的个数为7，表明所有的C均大于等于0，意味着找到了最优解。
            for j in range(A.shape[1]):
                if C[j] >= 0:
                    count+=1
                else:
                    continue
            if count == A.shape[1]:
                #print "break in count == A.shape[1]"
                break
            else:
                count = 0
    
    #While循环结束，构造一下最优解X的表达式，L向量代表最优解在B中的位置
    x2 = [0,0,0]
    L = L + x2
    X = [0]*7
    for j in range(A.shape[0]): 
        X[L[j]]=B[j]
    return A, B, C, X,z



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
print "A=",D[0]
print "B=",D[1]
print "C=",D[2]
print "X=",D[3]
print "z=",D[4]
