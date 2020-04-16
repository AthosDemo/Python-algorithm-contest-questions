'''
题目
矩形面积交

资源限制
时间限制：1.0s   内存限制：512.0MB

问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。
对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。

输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。

输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。

样例输入
1 1 3 3
2 2 4 4

样例输出
1.00
'''
while True:
    try:
        s1 = list(map(float, input().split()))
        s2 = list(map(float, input().split()))
        if s1[0] > s1[2]:
            s1[0],s1[2] = s1[2],s1[0]
        if s1[1] > s1[3]:
            s1[1], s1[3] = s1[3], s1[1]
        if s2[0] > s2[2]:
            s2[0],s2[2] = s2[2],s2[0]
        if s2[1] > s2[3]:
            s2[1],s2[3] = s2[3],s2[1]
        temp_x1 = max(s1[0],s2[0])
        temp_x2 = min(s1[2],s2[2])
        temp_y1 = max(s1[1],s2[1])
        temp_y2 = min(s1[3],s2[3])
        if temp_x2-temp_x1<0 or temp_y2-temp_y1<0:
            res = 0
        else:
            res = (temp_y2-temp_y1)*(temp_x2-temp_x1)
        print("{:.2f}".format(res))
    except:
        break
    
