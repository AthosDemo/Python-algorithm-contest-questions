'''
题目
矩阵乘法

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
　　给定一个N阶矩阵A，输出A的M次幂（M是非负整数）
　　例如：
　　A =
　　1 2
　　3 4
　　A的2次幂
　　7 10
　　15 22

输入格式
　　第一行是一个正整数N、M（1<=N<=30, 0<=M<=5），表示矩阵A的阶数和要求的幂数
　　接下来N行，每行N个绝对值不超过10的非负整数，描述矩阵A的值

输出格式
　　输出共N行，每行N个整数，表示A的M次幂所对应的矩阵。相邻的数之间用一个空格隔开

样例输入
2 2
1 2
3 4

样例输出
7 10
15 22
'''



# n = 阶数， m = 幂数

n,m = map(int,input().split())
assert n <= 30 and n >= 1 and m <=5 and m >=0,()

# 将输入的矩阵写入
start = []
for i in range(n):
    start.append(input().split())

# 生成“竖排列表”

def vertical(e):
    o = []
    for j in range(n):
        l = []
        for k in e:
            l.append(k[j])
        o.append(l)
    return o
#矩阵X*Y
#i为X的行，j为Y的每列，列已由vertical函数实现，u为计数下标，n阶就n次

def matrix_multi(x,y):
    q = []
    for i in x:
        p = []
        for j in y :
            a = 0
            for u in range(n):
                a =a +int(i[u]) * int(j[u])
            p.append(a)
        q.append(p)
    return q


def mi(xx,num):
    q2 = matrix_multi(xx,o2)
    if num == 2:
        print_verticl(q2,n)
    else:
        mi(q2,num - 1)


# 程序的开始
#幂为0时，为单位矩阵E

def print_verticl(ver,n):
    for iii in range(n):
        for jjj in range(n):
            print(str(ver[iii][jjj])+" ",end='')
        print()


if m == 0 :
    EE = []
    for ii in range(n):
        E = []
        for jj in range(n):
            if not jj == ii:
                E.insert(jj,0)
            else:
                E.insert(jj,1)
        EE.append(E)
    print_verticl(EE,n)
elif m == 1:
    print_verticl(start,n)
else:
    o2 = vertical(start)
    mi(start,m)

