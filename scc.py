# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 22:47:05 2023

@author: user pc
"""

import sys
sys.setrecursionlimit(10**6)  # Set recursion limit to avoid RecursionError

def read_graph(file_path):
    graph = {}
    reverse_graph = {}

    with open(file_path, 'r') as file:
        for line in file:
            tail, head = map(int, line.strip().split())
            graph.setdefault(tail, []).append(head)
            reverse_graph.setdefault(head, []).append(tail)

    return graph, reverse_graph

def kosaraju(graph, reverse_graph):
    def dfs_first_pass(graph, node, visited, stack):
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_first_pass(graph, neighbor, visited, stack)
        stack.append(node)

    def dfs_second_pass(reverse_graph, node, visited, scc):
        visited.add(node)
        scc.add(node)
        if node in reverse_graph:
            for neighbor in reverse_graph[node]:
                if neighbor not in visited:
                    dfs_second_pass(reverse_graph, neighbor, visited, scc)

    def get_scc_sizes(graph, reverse_graph):
        visited = set()
        stack = []

        for node in graph:
            if node not in visited:
                dfs_first_pass(graph, node, visited, stack)

        visited.clear()
        scc_sizes = []

        while stack:
            node = stack.pop()
            if node not in visited:
                scc = set()
                dfs_second_pass(reverse_graph, node, visited, scc)
                scc_sizes.append(len(scc))

        return sorted(scc_sizes, reverse=True)

    return get_scc_sizes(graph, reverse_graph)

def main():
    file_path = r"C:\Users\user pc\Documents\scc.txt"
    
    try:
        graph, reverse_graph = read_graph(file_path)
        scc_sizes = kosaraju(graph, reverse_graph)
        
        # Output the sizes of the 5 largest SCCs
        print(','.join(map(str, scc_sizes[:5])))
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Invalid file format. Make sure each line has two integers.")
    except RecursionError:
        print("Recursion limit exceeded. Try increasing the recursion limit.")

if __name__ == "__main__":
    main()
