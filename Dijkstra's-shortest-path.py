# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:56:44 2023

@author: user pc
"""

import heapq

def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            node = int(parts[0])
            edges = [tuple(map(int, pair.split(','))) for pair in parts[1:]]
            graph[node] = edges
    return graph

def dijkstra(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, edge_length in graph[current_vertex]:
            new_distance = distances[current_vertex] + edge_length

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

def main():
    file_path =  r"C:\Users\user pc\Documents\dijkstraData.txt"
    graph = read_graph(file_path)

    source_vertex = 1
    distances = dijkstra(graph, source_vertex)

    target_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    result = [str(distances[vertex] if distances[vertex] != float('inf') else 1000000) for vertex in target_vertices]

    print(','.join(result))

if __name__ == "__main__":
    main()
