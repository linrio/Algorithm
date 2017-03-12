# coding=utf-8
# Create by Lingfeng Lin

import numpy as np
import  matplotlib.pyplot as plt

def bayesplot():
    x1 = np.arange(0, 10, 7)
    x2 = -x1 + 6
    x = [0,2,2,0]
    y = [0,0,2,2]
    w1 = [4,6,6,4]
    w2 = [4,4,6,6]
    plot1 =  plt.plot(x,y,'ro')
    plot2 =  plt.plot(w1,w2,'bo')
    plot3 =  plt.plot(x1, x2)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.ylim(0,7)
    plt.title('Bayesian discriminant interface for two models')
    #plt.show()

def BayesianClassification(w1,w2):
    m1 = sum(w1)/len(w1)
    m2 = sum(w2)/len(w2)
    M = m1 - m2
    for i in range(len(w1)):
        w1[i] = w1[i] - m1
        w2[i] = w2[i] - m2
    C1 = np.dot(w1.T,w1)/len(w1)
    C2 = np.dot(w2.T,w2)/len(w2)
    C = C1
    d = M * C
    dd = m1.T * C * m1
    cc = m2.T * C * m2
    ee = -0.5 * (dd[0][0]+dd[1][1]) + 0.5 * (cc[0][0] + cc[1][1])
    print '两类正态分布模式的贝叶斯分类面：'
    print d[0][0],'* x1 + ',d[1][1],'* x2 + ',ee,' = 0'
#画出贝叶斯分类面
bayesplot()
w1 = np.array([[0,0],[2,0],[2,2],[0,2]])
w2 = np.array([[4,4],[6,4],[6,6],[4,6]])

#两类正态分布模式的贝叶斯分类程序
BayesianClassification(w1,w2)