# '''读取数据'''
import numpy
import numpy as np
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合
from openpyxl import load_workbook
import pandas as pd
import operator

def duqu(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def tiqu(A, B):
    col1 = A
    col2 = B
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col9 = []
    for j in range(len(col2)):  # 循环逐行打印
        m = col2[j]  # 获取第2列的数字
        n = abs(m)  # 绝对值
        sum += n

    Umean = sum / len(col2)  # 计算平均能量
    print(Umean)

    Upeak = Umean * 4  # 计算脉冲峰值阈值
    Ustart = Umean * 1.2  # 计算脉冲开始阈值
    Uend = Umean * 1.1  # 计算脉冲结束阈值

    print("平均能量：" + '%.6f' % Umean)
    print("脉冲峰值阈值：" + '%.6f' % Upeak)  # 脉冲峰值阈值
    print("脉冲开始阈值：" + '%.6f' % Ustart)  # 脉冲开始阈值
    print()

    tss = []  # 脉冲开始时间数组 col2.append(col.value)
    ss = len(col2)
    sa = 0
    ge = 0
    jg1 = 20
    jg2 = 10
    tend = 0
    # 打印脉冲时间
    for a in range(0, ss, jg1):  # 循环逐行
        if a > sa:  # 保证下一个脉冲从是一个脉冲结束时间之后找
            if col2[a] >= Upeak:
                Tmax1 = col1[a]  # 峰值时间
                Tu = col2[a]  # 峰值
                print("峰值时间：" + '%.6f' % Tmax1 + "峰值：" + '%.6f' % Tu)
                for q in range(a, sa, -jg2):  # 往前找开始脉冲时间
                    if 0 < col2[q] <= Ustart:
                        Tstart = col1[q]
                        Z1 = q
                        print("开始时间：" + '%.6f' % Tstart)
                        tss.append(Tstart)
                        break
                for p in range(a, ss, jg2):  # 往后找结束脉冲时间
                    if 0 < col2[p] <= Uend:
                        Tend = col1[p]
                        Z2 = p
                        print("结束时间：" + '%.6f' % Tend)
                        sa = p
                        break
                print("脉冲持续时间：" + '%.6f' % (Tend - Tstart))
                # print((Tmax1 - Tstart) / (Tend - Tstart))
                ge += 1
                col4.append(q)
                col5.append(p)
                col6.append(Tend - Tstart)
                col9.append(col1[q])
                # col7.append(((Tmax1 - Tstart) / (Tend - Tstart)))
    #  ————————————————————————把脉冲数据写入数组,然后写入Excel，命名为时间——————————————————————————————————————————————————
    tstart = 0
    for m2 in range(0, len(col4), 1):  # 循环逐行

        for m1 in range(tstart, col5[m2], 1):  # 循环逐行
            if col4[m2] <= m1 <= col5[m2]:
                col3.append(col2[m1])
            else:
                col3.append(0)
            tstart = col5[m2]
        data = pd.DataFrame(col3)

    writer = pd.ExcelWriter('C:/Users/zhangming/Desktop/采集卡1210/1102数据/组件+多余物/test31.xlsx')
    # header参数表示列的名称，index表示行的标签
    data.to_excel(writer, 'sheet_1', float_format='%.6f', header=False, index=False)
    writer.save()
    writer.close()

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
    writer = pd.ExcelWriter('C:/Users/zhangming/Desktop/采集卡1210/1102数据/组件+多余物/test31.xlsx')
    # header参数表示列的名称，index表示行的标签
    data.to_excel(writer, 'sheet_1', float_format='%.6f', header=False, index=False)
    writer.save()
    writer.close()
    # —————————————————————把脉冲数据写入数组,然后写入Excel——————————————————————————————————————————————————

    print("提取脉冲得个数为：" + '%.2f' % ge)


    # 脉冲开始时间间隔的方差  反映脉冲的周期性

    fc1 = 0
    for i in range(0, len(col9) - 1, 1):  # 循环逐行
        fc1 += (col9[i + 1] - col9[i])

    fc2 = 0
    for j in range(0, len(col9) - 1, 1):  # 循环逐行
        fc2 += ((col9[i + 1] - col9[i]) - fc1) ** 2
    s = (fc2 / (len(col9) - 1)) ** 0.5
    print()
    print(s)

    arr_var = np.var(col9)
    print(col9)
    print("方差为：%f" % arr_var)


def tezh(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

