# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:11:40 2023

@author: user pc
"""

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_merge = merge_and_count_split_inv(left, right)

    return merged, inv_left + inv_right + inv_merge


def merge_and_count_split_inv(left, right):
    merged = []
    inv_count = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count


def read_array_from_file(file_path):
    with open(file_path, 'r') as file:
        array = [int(line.strip()) for line in file]
    return array


def main():
    file_path = r"C:\Users\user pc\Documents\nmber.txt"
    array = read_array_from_file(file_path)

    sorted_array, inversions = count_inversions(array)

    print(f"Number of inversions: {inversions}")


if __name__ == "__main__":
    main()
