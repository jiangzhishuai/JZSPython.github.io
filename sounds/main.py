# utf-8
import os
import sys

path_0 = r"C:\Users\zhangming\Desktop\1114下午\焊锡"

path_1 = r"C:\Users\zhangming\Desktop\1114下午\引脚" + '\\'
sys.path.append(path_1)

# print(sys.path)

# list current all files

files = os.listdir(path_0)

print('files', files)

for filename in files:

    portion = os.path.splitext(filename)

    if portion[1] == ".dat":
        # recombine file name
        newname = portion[0] + ".txt"
        filenamedir = path_1 + filename
        newnamedir = path_1 + newname

        # os.rename(filename, newname)
        os.rename(filenamedir, newnamedir)