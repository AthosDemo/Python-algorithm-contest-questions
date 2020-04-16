'''
题目
	01字串

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：

00000

00001

00010

00011

00100

请按从小到大的顺序输出这32种01串。

输出格式
输出32行，按从小到大的顺序每行一个长度为5的01串。

样例输出
00000
00001
00010
00011
<以下部分省略>



'''


num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0



for i in range(32):
    if num1 == 0:
        if num2 == 0:
            if num3 == 0:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 1
                    
            else:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 0
                        num2 = 1
        else:
            if num3 == 0:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 1
                    
            else:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 0
                        num2 = 0
                        num1 = 1
    else:
        if num2 == 0:
            if num3 == 0:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 1
                    
            else:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 0
                        num2 = 1
        else:
            if num3 == 0:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 1
                    
            else:
                if num4 == 0:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 1
                else:
                    if num5 ==0:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 1
                    else:
                        print(str(num1)+str(num2)+str(num3)+str(num4)+str(num5))
                        num5 = 0
                        num4 = 0
                        num3 = 0
                        num2 = 0
                        num1 = 1
    



