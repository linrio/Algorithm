#include <iostream>
#include "BinaryTree.h"

using namespace std;

//author: Lingfeng Lin
//time:   26.Feb 2017
int main()
{
    BinaryTree<char> tree;
    TreeNode<char> add, jian, mul, chu,a,b,c,d,e;
    add.data = '+';
    jian.data = '-';
    mul.data = '*';
    chu.data = '/';
    a.data = 'A';
    b.data = 'B';
    c.data = 'C';
    d.data = 'D';
    e.data = 'E';

    tree.root = &add;
    add.leftChild = &jian;
    add.rightChild = &e;
    jian.leftChild = &mul;
    jian.rightChild = &d;
    mul.leftChild = &chu;
    mul.rightChild = &c;
    chu.leftChild = &a;
    chu.rightChild = &b;

    cout << "���������";
    tree.InOrder();
    cout << endl;

    cout <<"���������";
    tree.PreOrder();
    cout <<endl;

    cout << "���������";
    tree.PostOrder();
    cout <<endl;

    cout << "���������";
    tree.LevelOrder();
    cout << endl;

    cout << "Hello world!" << endl;
    return 0;
}
