import fileinput
import sys

import numpy as np
from scipy.spatial.distance import cdist

from io import StringIO

def solve():
    # Read input data into a list of lines, stripping newlines
    # Use [int(line.strip()) for line in fileinput.input()] for integer input
    lines = [line.strip() for line in fileinput.input()]

    # --- Part 1 ---
    result_part1 = part1(lines)
    print(f"Part One: {result_part1}")

    # --- Part 2 ---
    result_part2 = part2(lines)
    print(f"Part Two: {result_part2}")


def part1(lines):
    
    points = []
    for line in lines:
        points.append([int(x) for x in line.split(",")])

    n = len(points)
    
    # 2. Pre-calculate all pairwise distances
    # Distance: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            # Storing dist_sq is faster than calculating sqrt
            edges.append((dist_sq, i, j))

    # 3. Sort edges to get the closest pairs
    edges.sort()

    # 4. Disjoint Set Union (DSU) to track circuits
    parent = list(range(n))
    size = [1] * n

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by size
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    # 5. Process the first 1000 closest connections
    for k in range(min(1000, len(edges))):
        _, u, v = edges[k]
        union(u, v)

    # 6. Extract circuit sizes
    # We find the root of every point to get the final components
    final_sizes = {}
    for i in range(n):
        root = find(i)
        if root not in final_sizes:
            final_sizes[root] = size[root]
    
    sizes = sorted(final_sizes.values(), reverse=True)
    
    # 7. Result: Multiply the 3 largest
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
        # print(f"Sizes: {sizes[:3]}")
        # print(f"Result: {result}")

    return result

def part2(lines):

    points = []
    for line in lines:
        points.append([int(x) for x in line.split(",")])

    n = len(points)
    
    # 2. Pre-calculate all pairwise distances
    # Distance: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            # Storing dist_sq is faster than calculating sqrt
            edges.append((dist_sq, i, j))

    # 3. Sort edges to get the closest pairs
    edges.sort()

    # 4. Disjoint Set Union (DSU) to track circuits
    parent = list(range(n))
    size = [1] * n

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by size
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    # 5. Process connections until all points are connected
    k = 0
    while True:
        _, u, v = edges[k]
        union(u, v)
        k += 1

        if size[find(u)] == n:
            result = points[u][0] * points[v][0]
            break
        
    return result

if __name__ == "__main__":
    solve()
