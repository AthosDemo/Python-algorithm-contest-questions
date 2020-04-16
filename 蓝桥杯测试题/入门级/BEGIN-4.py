'''
Fibonacci数列    斐波纳契（一种整数数列）

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。

当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。

输入格式
输入包含一个整数n。

输出格式
输出一行，包含一个整数，表示Fn除以10007的余数。

样例输入
10

样例输出
55

样例输入
22

样例输出
7704

数据规模与约定
1 <= n <= 1,000,000。
'''

'''

递归法
输入55就会超时，输入
输入9999 最大递归深度在比较中超过，产生递归错误


def fib_recur(n):
    assert n >= 0, "n > 0"
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recur( n - 1 ) % 10007 + fib_recur( n - 2 ) % 10007



n = eval(input())

print(fib_recur(n))

写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O（1.618^n）,而且最深度1000

'''

'''
递推法
在输入999999超时
def fib_loop(n):
  a,b = 0,1
  for i in range(n):
    a, b = b, a + b
  return a % 10007
n = eval(input())
print(fib_loop(n))

'''

'''
生成器
也超时
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a 
n = eval(input())


for i in fib_loop_while(n):
    num = i % 10007

print(num)

'''
'''
类实现内部魔法方法
也超时

class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self

n = eval(input())
if __name__ == '__main__':
    fib = Fibonacci(n)
    for num in fib:
        num1 = num % 10007

print(num1)
'''


'''
矩阵快速幂
唯一不超时 但是可能没有numpy这个包
import numpy as np

def pow(n):
    a = np.array([[1,0],[0,1]])
    b = np.array([[1,1],[1,0]])
    n -= 1
    while(n > 0):
        if (n % 2 == 1):
            a = np.dot(b, a)
        b = np.dot(b, b)
        n >>= 1
    return a[0][0]

n = eval(input())

print(pow(n)%10007)

'''


'''
但是还是不够快

首先看一下之前的迭代版本的Fibonacci函数，很容易可以发现存在一个变换：y->x, x+y->y。换一个角度，
就是[x,y]->[y,x+y]。
在这里，我声明一个二元向量[x,y]T，它通过一个变换得到[y,x+y]T，可以很容易得到变换矩阵是[[1,0],[1,1]]，
也就是说：[[1,0],[1,1]]*[x,y]T=[y,x+y]T
令二元矩阵A=[[1,0],[1,1]]，二元向量x=[0,1]T，容易知道Ax的结果就是下一个Fibonacci数值，即：
Ax=[fib(1),fib(2)]T
亦有：
Ax=[fib(2),fib(3)]T
………………
以此类推，可以得到：
Aⁿx=[fib(n),fib(n-1)]T
也就是说可以通过对二元向量[0,1]T进行n次A变换，从而得到[fib(n),fib(n+1)]T，从而得到fib(n)。
在这里定义了一个二元矩阵的相乘函数m1，以及一个在二元向量上的变换m2，
然后利用reduce操作完成一个连乘操作得到Aⁿx，最后得到fib(n）

from functools import reduce
def fib(n):
     def m1(a,b):
         m=[[],[]]
         m[0].append(a[0][0]*b[0][0]+a[0][1]*b[1][0])
         m[0].append(a[0][0]*b[0][1]+a[0][1]*b[1][1])
         m[1].append(a[1][0]*b[0][0]+a[1][1]*b[1][0])
         m[1].append(a[1][0]*b[1][0]+a[1][1]*b[1][1])
         return m
     def m2(a,b):
         m=[]
         m.append(a[0][0]*b[0][0]+a[0][1]*b[1][0])
         m.append(a[1][0]*b[0][0]+a[1][1]*b[1][0])
         return m
     return m2(reduce(m1,[[[0,1],[1,1]] for i in range(n)]),[[0],[1]])[0]

n = eval(input())

print(fib(n)%10007)

'''

'''
利用斐波纳契数列的一系列恒等式
F(1)+F(3)+。。。+F(2n - 1) = F(2 n)

F(2)+F(4)+。。。+F(2n) = F(2 n + 1) - 1

def fib_loop(n):
  a,b = 0,1
  for i in range(n):
    a, b = b, a + b
  return a 

def fib(n):
    if n % 2 == 1:
       if n == 1:
           return 1
       else:
           fib_n = 0
           for i in range(n):
               fib_n += fib_loop( i * 2 - 1)
    else:
        if n == 2:
            return 1
        else:
            fib_n = 1
            for i in range(n):
                fib_n += fib_loop(2 * i)
                

n = eval(input())

print(fib_loop(n)%10007)   

'''

'''

用通项公式算，但是会数据溢出

n = eval(input())

num = 5 ** (1/2)
Fib_n1 = ( ( 1 + num ) / 2 )** n
Fib_n2 = ( ( 1 - num ) / 2 )** n
Fib_n =  1 / num  * ( Fib_n1 - Fib_n2 )

put_number = int(Fib_n % 10007)
print(put_number)                      


'''



'''
唯一通过的方法
 
'''

n=int(input())
a=[]
a.append(1)
a.append(1)
for i in range(2,n):
    a.append( (a[i-1]+a[i-2]) % 10007 )
print(a[n-1])  
 
