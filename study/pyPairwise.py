#!/usr/bin/env python3
# @Time : 2022/9/5 20:23
# @Author : 轩辕龙儿
# @File : pyPairwise.py 
# @Software: PyCharm
from itertools import pairwise

if __name__ == "__main__":
    arrs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("传入数据：0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
    for arr in pairwise(arrs):
        print(str(arr[0]) + "," + str(arr[1]))
    print("------------------------------------")
    print("传入数据：1")
    for arr in pairwise([1]):
        print(str(arr[0]) + "," + str(arr[1]))
