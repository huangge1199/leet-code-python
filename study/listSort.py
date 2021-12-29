#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/12/28
# @file listSort.py
if __name__ == "__main__":
    nums = [2, 3, 5, 1, 6]
    print("原列表：", nums)
    print("------sorted-------")

    nums = [2, 3, 5, 1, 6]
    newNums = sorted(nums)
    print(nums)  # [2, 3, 5, 1, 6]
    print(newNums)  # [1, 2, 3, 5, 6]

    print("------sort-------")
    nums.sort()
    print(nums)  # [1, 2, 3, 5, 6]
    nums.sort(key=None, reverse=True)
    print(nums)  # [6, 5, 3, 2, 1]

    students = [('john', 'C', 15), ('jane', 'A', 12), ('dave', 'B', 10)]
    students.sort(key=lambda x: x[2])  # 按照列表中第三个元素排序
    print(students)  # [('dave', 'B', 10), ('jane', 'A', 12), ('john', 'C', 15)]

    students = [('john', 'C', 15), ('jane', 'A', 12), ('dave', 'B', 10)]
    newStudents = sorted(students, key=lambda x: x[1])
    print(students)  # [('john', 'C', 15), ('jane', 'A', 12), ('dave', 'B', 10)]
    print(newStudents)  # [('jane', 'A', 12), ('dave', 'B', 10), ('john', 'C', 15)]
