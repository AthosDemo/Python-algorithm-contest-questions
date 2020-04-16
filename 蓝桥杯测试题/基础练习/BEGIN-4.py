'''
题目
数列特征

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
给出n个数，找出这n个数的最大值，最小值，和。

输入格式
第一行为整数n，表示数的个数。

第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。

输出格式
输出三行，每行一个整数。第一行表示这些数中的最大值，第二行表示这些数中的最小值，第三行表示这些数的和。

样例输入
5
1 3 -2 4 5

样例输出
5
-2
11

数据规模与约定
1 <= n <= 10000。

'''

n=eval(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])
sum=0
max=arr[0]
min=arr[0]
for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
    sum+=i
print(max)
print(min)
print(sum)



'''
def input_number(count):
   
    
    number_list =list(map(int,input().split()))
    for k in range(count):

        for L in range(len(number_list) - 1):
            for m in range(len(number_list) - L - 1):
                if number_list[m] > number_list[m+1]:
                    number_list[m],number_list[m+1] = number_list[m+1],number_list[m]
    
    print(number_list[0])

    print(number_list[count-1])
    
    sum = 0
    for j in range(count):
    
        sum += number_list[j]

    print(sum)
    
    



count = eval(input())

input_number(count)
'''
