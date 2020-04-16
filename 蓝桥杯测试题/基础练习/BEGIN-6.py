'''
题目
 杨辉三角形

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)^i的展开式的系数。

　　
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。

　　
下面给出了杨辉三角形的前4行：

　　
   1

　　
  1 1

　　
 1 2 1

　　
1 3 3 1

　　
给出n，输出它的前n行。

输入格式
输入包含一个数n。

输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。

样例输入
4

样例输出
1
1 1
1 2 1
1 3 3 1

数据规模与约定
1 <= n <= 34。

'''


n = int(input())
assert n <=34 and n >= 1,("")



def yanghui(max):
    L = [1]
    count = 0
    while count < max:
        for j in range(len(L)):
            print(L[j],end=" ")
            if j == len(L)-1:
                print()
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
        
        count += 1

yanghui(n)







    
