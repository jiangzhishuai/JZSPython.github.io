from openpyxl import load_workbook
import numpy as np

wb = load_workbook('C:/Users/zhangming/Desktop/采集卡1210/1021数据/zujian1.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet
print(sheets)

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

sum = 0
# 获取第一列所有数据
col1 = []
for col in sheet1['A']:
    col1.append(col.value)

# 获取第二列所有数据
col2 = []
for col in sheet1['B']:
    col2.append(col.value)
a = col2[1]
print(a)
# 第2列数据求和
for j in range(len(col2)):  # 循环逐行打印
    m = col2[j]  # 获取第2列的数字
    n = abs(m)
    sum += n

Umean = sum / len(col2)  # 计算平均能量
Upeak = Umean * 10  # 计算脉冲峰值阈值
Ustart = Umean * 1.2  # 计算脉冲开始阈值
Uend = Umean * 1.2  # 计算脉冲结束阈值

print(Umean)
print(Upeak)  # 脉冲峰值阈值
print(Ustart)  # 脉冲开始阈值
print()

tss = []  # 脉冲开始时间数组 col2.append(col.value)
ss = len(col2)
sa = 0
# 打印脉冲时间
for a in range(0, ss, 6):  # 循环逐行
    if a > sa:  # 保证下一个脉冲从是一个脉冲结束时间之后找
        if col2[a] >= Upeak:
            Tmax1 = col1[a]
            Tu = col2[a]
            print("峰值时间：" + '%.3f' % Tmax1+"峰值："+ '%.3f' % Tu)
            for q in range(a, 0, -5):  # 往前找开始脉冲时间
                if col2[q] <= Ustart:
                    Tstart = col1[q]
                    Z1 = q
                    print("开始时间：" + '%.3f' % Tstart)
                    tss.append(Tstart)
                    break
            for p in range(a, ss, 5):  # 往后找结束脉冲时间
                if col2[p] <= Uend:
                    Tend = col1[p]
                    Z2 = p
                    print("结束时间：" + '%.3f' % Tend)
                    sa = p
                    break
            print((Tmax1 - Tstart) / (Tend - Tstart))
            Z3 = 0


# 脉冲开始时间的方差  反映脉冲的周期性
arr_var = np.var(tss)
print("方差为：%f" % arr_var)
