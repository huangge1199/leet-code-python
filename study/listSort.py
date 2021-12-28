#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/12/28
# @file listSort.py
if __name__ == "__main__":
    nums = [2, 3, 5, 1, 6]
    print("原列表：", nums)
    print("------sorted-------")
    newNums = sorted(nums)
    print("原变量：", nums)
    print("赋值变量：", newNums)
    print("------sort-------")
    nums.sort()
    print("原变量：", nums)
