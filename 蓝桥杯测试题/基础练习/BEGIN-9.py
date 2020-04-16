'''
题目
特殊回文数

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。

输入格式
　　　输入一行，包含一个正整数n。

输出格式
　　　按从小到大的顺序输出满足条件的整数，每个整数占一行。

样例输入
52

样例输出
899998
989989
998899

数据规模和约定
　　1<=n<=54。
'''
n=int(input())
assert n<=54 and n >=1,()
for i in range(10000,1000000):


    if i <100000:
         num1 = i %  10
         num2 = i // 10 % 10
         num3 = i // 100 % 10
         num4 = i // 1000 %10
         num5 = i // 10000
         if num1+num2+num3+num4+num5 == n and num1==num5 and num2==num4:
             print(i)
    else:
         num1 = i %  10
         num2 = i // 10 % 10
         num3 = i // 100 % 10
         num4 = i // 1000 %10
         num5 = i // 10000 %10
         num6 = i // 100000
         if num1+num2+num3+num4+num5+num6 == n and num1==num6 and num2==num5 and num3==num4:
             print(i)
