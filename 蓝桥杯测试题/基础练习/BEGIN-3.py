'''
题目
字母图形

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
利用字母可以组成一些美丽的图形，下面给出了一个例子：

ABCDEFG

BABCDEF

CBABCDE

DCBABCD

EDCBABC

这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。

输入格式
输入一行，包含两个整数n和m，分别表示你要输出的图形的行数的列数。

输出格式
输出n行，每个m个字符，为你的图形

样例输入
5 7

样例输出
ABCDEFG
BABCDEF
CBABCDE
DCBABCD
EDCBABC

据规模与约定
1 <= n, m <= 26。



'''


def beautiful_shape(n,m):
    assert (1<= n and m <= 26),"输入错误"
    
    num1 = ord('A')

    for i in range(n):
        num2 = num1
        count = num1
        for j in range(m):
            
            if  count != ord('A')  and num2 != ord('A'):
                #print('*',end="")
                print(chr(num2),end="")
                num2 -=1
                count -=1
                
            else:
                #print('&',end="")
                print(chr(num2),end="")
                num2 +=1
        num1 += 1
        print()
    
n,m =map(int,input().split())

beautiful_shape(n,m)
