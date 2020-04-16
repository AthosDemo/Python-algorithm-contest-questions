'''

数列排序

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
　　给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200

输入格式
　　第一行为一个整数n。
　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。

输出格式
　　输出一行，按从小到大的顺序输出排序后的数列。

样例输入
5
8 3 6 4 9

样例输出
3 4 6 8 9
'''



n =int(input())
assert n>=1 and n<=200,()
seq=input().split()
seq =list(map(int,seq))
'''
#快速排序  通过42%
import random

def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left =[elem for elem in seq[1:] if int(elem) < int(base)]
        right = [elem for elem in seq[1:] if int(elem) > int(base)]
        return quicksort(left) + [base] + quicksort(right)

random.shuffle(seq)

new_seq = quicksort(seq)
'''





'''
#冒泡排序  通过100


def bouble_sort(sequence):
    seq = sequence[:]
    length = len(seq) - 1
    i = j = 0
    flag = 1
    while i <length:
        j = 0
        while j <length - i:
            if int(seq[j]) > int(seq[j + 1]):
                seq[j],seq[j + 1] = seq[j + 1],seq[j]
                flag = 0
            j += 1
        if flag:
            break
        i +=1
    return seq

new_seq = bouble_sort(seq)

'''

'''
#选择排序

def find_minimal_index(seq):
    min_elem = seq[0]
    count = 0
    min_elem_index = count

    for elem in seq[1:]:
        count += 1
        if int(elem) < int(min_elem):
            elem, min_elem = min_elem, elem
            min_elem_index =count
    return min_elem_index

def select_sort(sequence):
    seq = sequence[:]
    length = len(seq)
    for i in range(length):
        index = find_minimal_index(seq[i:])
        seq[index + i],seq[i] = seq[i], seq[index + i]
    return seq


new_seq =select_sort(seq)

'''
'''

#插入排序
def insert_sort(seq):
    count = len(seq)
    for i in range(1,count):
        key = seq[i]
        j = i - 1
        while j >=0:
            if int(seq[j]) > int(key):
                seq[j + 1] =seq[j]
                seq[j] = key
            j -= 1
    return seq



new_seq = insert_sort(seq)
for i in range(len(new_seq)):
    print(new_seq[i],end=" ")

'''

#sort()函数  本质是归并排序

seq =list(map(int,seq))
seq.sort()

print(" ".join(map(str,seq)))






    
