'''
A+B 问题

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
输入A、B，输出A+B。

输入格式
输入的第一行包括两个整数，由空格分隔，分别表示A、B。

输出格式
输出一行，包括一个整数，表示A+B的值。

样例输入
12 45

样例输出
57

数据规模与约定
-10000 <= A, B <= 10000。
'''

#不满足测试的代码一
# a = eval(input("Enter the first numbers"))
# if a < -10000:
#     print("The first input is not in a valid range")
# else:
#     b = eval(input("Enter the second numbers"))
#     if b > 10000:
#         print("The second input is not in a valid range")
#     else:
#         print("The value of two inputs are",a,"and",b)
#         print("The sum of the two inputs is",a+b)

#不满足测试的代码二
# a = eval(input())
# b = eval(input())
# print(a,b)
# print(a+b)
'''
模拟题中输入的数据格式是 0 451 中间是一个空格，需要转化一下输入的内容
'''
a,b,=map(int,input().split())
print(a+b)
