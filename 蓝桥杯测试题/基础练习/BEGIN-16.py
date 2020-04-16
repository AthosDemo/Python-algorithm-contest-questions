'''
题目
分解质因数

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
　　求出区间[a,b]中所有整数的质因数分解。

输入格式
　　输入两个整数a，b。

输出格式
　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)(具体可看样例)

样例输入
3 10

样例输出
3=3
4=2*2
5=5
6=2*3
7=7
8=2*2*2
9=3*3
10=2*5

提示
　　先筛出所有素数，然后再分解。

数据规模和约定
　　2<=a<=b<=10000
'''


#判断质数
'''
def is_prime(number):
        if number == 2:
            return True
        if number % 2 == 0 and number != 2:
            return False
        current = 3
        for current in range(3,number+1) :
            if number % current == 0 :
                return False            
            elif number % current == 0 and number == current:
                return True

'''
def is_prime(a,b):
    import math
    for n in range(a,b+1):
        flag=1
        if n % 2 == 0 and 2 <n:
            flag = 0
            factorization(n)
        else:
            for i in range(3,int(math.sqrt(n)+1),2):
                if n %i ==0:
                    flag = 0
                    factorization(n)
                    break
        if flag == 1:
            print(str(n)+'='+str(n))
                

def factorization(number):
    i = 2
    c = number
    ls = []
    outstr =''
    while number != 1:
        if number % i == 0:
            if number // i !=1:
                  outstr +=(str(i)+'*')
            else:
                outstr +=(str(i))

            number //= i
            i = 2
        else:
            i = i + 1
    print(str(c)+'='+outstr)

    
a,b = map(int,input().split())



assert a >= 2 and a <= b and b <= 10000,()

is_prime(a,b)
   
        

