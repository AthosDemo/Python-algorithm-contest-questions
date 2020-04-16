'''
序列求和

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
求1+2+3+...+n的值。

输入格式
输入包括一个整数n。

输出格式
输出一行，包括一个整数，表示1+2+3+...+n的值。

样例输入
4

样例输出
10

样例输入
100

样例输出
5050

数据规模与约定
1 <= n <= 1,000,000,000。
'''

#这里用了递归的算法,但是输入1000会导致最大递归深度在比较中超过
'''
def cumulative(n):
    if 0 == n:
        return 0
    elif n >1000000000:
        print("Date overflow")
    else:
        return n + cumulative( n - 1 )

while True:
    n = input()
    if n.isdigit():
        n = eval(n)
        print(cumulative(int(n)))
    else:
        break

'''


'''
这里在值为100000000的测试时，超时，运算时间过长
sum = 0
n = eval(input())

if n <= 1 :
    print(n)
elif n > 1000000000:
    pass
else:
    for n in range(n,0,-1):
        sum += n
    print(sum)

'''


#这里直接用了高斯算法
n = eval(input())
sum_n = ( n + 1) * n / 2
print(int(sum_n))

    
