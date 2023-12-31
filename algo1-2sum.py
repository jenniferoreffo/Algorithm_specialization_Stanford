# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 07:40:04 2023

@author: Jennifer Oreffo
"""

def count_2sum_targets(file_path):
    numbers = set()
    target_values = set()

    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())

            # Check for distinct pairs that sum up to target values
            for target in range(-10000, 10001):
                complement = target - num
                if complement in numbers and complement != num:
                    target_values.add(target)

            numbers.add(num)

    return len(target_values)

def main():
    file_path =  
    
    count = count_2sum_targets(file_path)
    
    print(f"Number of distinct target values in the interval [-10000, 10000]: {count}")

if __name__ == "__main__":
    main()
