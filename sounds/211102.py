# '''读取数据'''
import numpy
import numpy as np
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合
from openpyxl import load_workbook
import pandas as pd
import operator

# 获取Excel数据
wb = load_workbook('C:/Users/zhangming/Desktop/采集卡1210/1102数据/噪音/噪音2.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

# 获取第一列所有数据
col1 = []
for col in sheet1['A'][0:200000]:
    col1.append(col.value)
col2 = []
for col in sheet1['B'][0:200000]:
    col2.append(col.value)
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col9 = []

# 读取音频文件
y = col2
x = col1  # 时间刻度
# 绘制图形
plt.plot(x, y)
plt.xlabel('times')  # x轴时间
plt.ylabel('amplitude')  # y轴振幅
plt.title('zujian.wav', fontsize=12, color='black')  # 标题名称、字体大小、颜色
plt.ylim(-10, 10)
plt.show()
sum = 0


for j in range(len(col2)):  # 循环逐行打印
    m = col2[j]  # 获取第2列的数字
    n = abs(m)   # 绝对值
    sum += n

Umean = sum / len(col2)  # 计算平均能量
print(Umean)

Upeak = Umean * 3.2  # 计算脉冲峰值阈值
Ustart = Umean * 1.2  # 计算脉冲开始阈值
Uend = Umean * 1.1  # 计算脉冲结束阈值

print("平均能量：" + '%.6f' % Umean)
print("脉冲峰值阈值："+ '%.6f' % Upeak)      # 脉冲峰值阈值
print("脉冲开始阈值："+ '%.6f' % Ustart)  # 脉冲开始阈值
print()

tss = []  # 脉冲开始时间数组 col2.append(col.value)
ss = len(col2)
sa = 0
ge = 0
jg1 = 50
jg2 = 25
tend = 0
# 打印脉冲时间
for a in range(0, ss, jg1):  # 循环逐行
    if a > sa:  # 保证下一个脉冲从是一个脉冲结束时间之后找
        if col2[a] >= Upeak:
            Tmax1 = col1[a]    # 峰值时间
            Tu = col2[a]       # 峰值
            print("峰值时间：" + '%.6f' % Tmax1+"峰值："+ '%.6f' % Tu)
            for q in range(a, sa, -jg2):  # 往前找开始脉冲时间
                if 0 <= col2[q] <= Ustart:
                    Tstart = col1[q]
                    Z1 = q
                    print("开始时间：" + '%.6f' % Tstart)
                    tss.append(Tstart)
                    break
            for p in range(a, ss, jg2):  # 往后找结束脉冲时间
                if 0 <= col2[p] <= Uend:
                    Tend = col1[p]
                    Z2 = p
                    print("结束时间：" + '%.6f' % Tend)
                    sa = p
                    break
            # for max in range(Z1, Z2, 1):  # 找最大值
            #     col8.append( col1[max] )
            #     max_index, max_number = max(enumerate(col8), key=operator.itemgetter(1))
            #     Tmax2 = col1[max_index]
            print("脉冲持续时间：" + '%.6f' % (Tend - Tstart))
            #print((Tmax2 - Tstart) / (Tend - Tstart))
            ge += 1
            col4.append(Z1)
            col5.append(Z2)
            col6.append(Tend - Tstart)
            # col7.append(((Tmax2 - Tstart) / (Tend - Tstart)))
            col9.append(col1[q])
# ——————————————————————找完脉冲之后，提取脉冲特征——————————————————
for max1 in range(0, len(col4), 1):  # 循环逐行
    col8 = []
    for max2 in range(col4[max1], col5[max1], 1):  # 循环逐行
        col8.append( col2[max2] )
    max_index, max_number = max(enumerate(col8), key=operator.itemgetter(1))
    Tmax2 = col1[max_index+ col4[max1]]
    # col7.append(((Tmax2 - col1[col4[max1]]) / (col1[col5[max1]] - col1[col4[max1]])))
    col7.append(((Tmax2 - col1[col4[max1]]) / (col1[col5[max1]] - Tmax2)))

print(col4)
print(col5)
print(col6)
print(col7)
# print(col8)
# print(max_number)
# print(max_index)
# print(Tmax2)
# print(col1[1250])
# print(col1[2000])
# print(((Tmax2 - col1[1250]) / (col1[2000] - col1[1250])))
#  max_index, max_number = max(enumerate(col4), key=operator.itemgetter(1))
#  print(max_index, max_number)

tezh = numpy.vstack((col6, col7)).T  #  两个时域特征合并到一起

data = pd.DataFrame(tezh)
writer2 = pd.ExcelWriter('C:/Users/zhangming/Desktop/采集卡1210/1102数据/噪音/test2.xlsx')
# header参数表示列的名称，index表示行的标签
data.to_excel(writer2, 'sheet_1', float_format='%.6f', header=False, index=False)
writer2.save()
writer2.close()




#  ————————————————————————把脉冲数据写入数组,然后写入Excel——————————————————————————————————————————————————
tstart = 0
for m2 in range(0, len(col4), 1):  # 循环逐行

    for m1 in range(tstart, col5[m2], 1):  # 循环逐行
            if col4[m2] <= m1 <= col5[m2]:
                    col3.append(col2[m1])
            else:
                    col3.append(0)
            tstart = col5[m2]


data = pd.DataFrame(col3)
writer = pd.ExcelWriter('C:/Users/zhangming/Desktop/采集卡1210/1102数据/噪音/test.xlsx')
# header参数表示列的名称，index表示行的标签
data.to_excel(writer, 'sheet_1', float_format='%.6f', header=False, index=False)
writer.save()
writer.close()
# —————————————————————把脉冲数据写入数组,然后写入Excel——————————————————————————————————————————————————

print("提取脉冲得个数为："+ '%.2f' % ge)

            #Z3 = 0
            # 计算过零率函数
            #for Z in range(Z1, Z2, 1):
                #if col2[Z]*col2[Z-1] < 0:
                    #Z3 += 1
            #print(Z3)
            #print()

# 脉冲间隔方差  反映脉冲的周期性
fc1 = 0
for i in range(0, len(col9)-1, 1):  # 循环逐行
    fc1 += (col9[i+1] - col9[i])

fc2 = 0
for j in range(0, len(col9)-1, 1):  # 循环逐行
    fc2 += ( (col9[i+1] - col9[i]) - fc1 )**2
s = (fc2 / ( len(col9) - 1 ))**0.5
print( )
print(s)
arr_var = np.var(col9)
print(col9)
print("方差为：%f" % arr_var)
