# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:48:10 2023

@author: Jennifer Oreffo
"""

import heapq

def read_array(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def median_maintenance(arr):
    min_heap = []  # for the larger half
    max_heap = []  # for the smaller half

    result = []
    for num in arr:
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Get the current median
        if len(max_heap) == len(min_heap):
            median = -max_heap[0]
        else:
            median = -max_heap[0]

        result.append(median)

    return result

def main():
    file_path = r"C:\Users\user pc\Documents\Median.txt"
    array = read_array(file_path)

    medians = median_maintenance(array)

    # Print the sum of medians modulo 10000
    print(f"Sum of medians modulo 10000: {sum(medians) % 10000}")

if __name__ == "__main__":
    main()
