'''
题目
闰年判断

资源限制
时间限制：1.0s   内存限制：256.0MB

问题描述
给定一个年份，判断这一年是不是闰年。

当以下情况之一满足时，这一年是闰年：

1. 年份是4的倍数而不是100的倍数；

2. 年份是400的倍数。

其他的年份都不是闰年。

输入格式
输入包含一个整数y，表示当前的年份。

输出格式
输出一行，如果给定的年份是闰年，则输出yes，否则输出no。

样例输入
2016

样例输出
yes

数据规模与约定
1990 <= y <= 2050。

year = eval(input())

if year < 1990 or year > 2050 :
    pass

else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
       print("yes")
    else:
        print("no")
'''
#这里用了断言函数
year = eval(input())

assert( year >= 1990 and year <= 2050),'输入错误'    
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("yes")
else:
    print("no")
