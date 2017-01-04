# coding=utf-8
# Create by Lingfeng Lin

import numpy as np
import  matplotlib.pyplot as plt

def eig(a2):
    a,b = np.linalg.eig(a2)
    print 'a=',a
    print 'b=',b
def fig1():
    x1 = [0, 0, 0.52, -1.70]
    x2 = [0.52, -0.85, 2.22, -1.89]
    y = [0, 0, 0, 0]
    plt.plot(x1, y, 'bo', label = "w1 category")
    plt.plot(x2, y, 'r*', label = "w2 category")
    plt.title('K-L Transform for One-dimensional category')
    plt.legend()
    plt.show()

def fig2():
    x1 = [0, 0, 0.52, -1.70]
    y1 = [0, 2, 2, 1]
    x2 = [0.52, -0.85, 2.22, -1.89]
    y2 = [0, 0, 0, 1]
    plt.plot(x1, y1, 'bo', label = "w1 category")
    plt.plot(x2, y2, 'r*', label = "w2 category")
    plt.title('K-L Transform for Two-dimensional category')
    plt.legend()
    plt.ylim(-1, 3)
    plt.show()

a2 = np.array([[10/8,3/8,0],[3/8,10/8,-4/8],[0,-4/8,7/8]])
#eig(a2)
#fig1()
fig2()
