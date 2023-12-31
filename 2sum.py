# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 08:30:56 2023

@author: user pc
"""



from bisect import bisect_left, bisect_right


if __name__ == "__main__":
    

    txt_file = r"C:\Users\user pc\Documents\algo1-2sum.txt"

    numberSet = set()

    with open(txt_file, 'r') as f:
        for line in f.readlines():
            numberSet.add(int(line))
    
    dist_num = 0

    numberSet = sorted(numberSet)

    numberTarget = set()

    for num in numberSet:
        low = bisect_left(numberSet, -10000-num)
        high = bisect_right(numberSet, 10000-num)

        yRange = numberSet[low:high]

        for y in yRange:
            if y!=num:
                numberTarget.add(num + y)
    
    print("num is {}".format(len(numberTarget)))