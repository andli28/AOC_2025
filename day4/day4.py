import fileinput
import sys

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
    # First, pad outside with zeroes
    # Then, iterate and look for @'s.
    # If there are less than 4 @'s around, add 1 to the result.

    graph = []
    graph.append("0" * (len(lines[0]) + 2))
    for line in lines:
        graph.append("0" + line + "0")
    graph.append("0" * (len(lines[0]) + 2))

    res = 0
    for i in range(1, len(graph) - 1):
        for j in range(1, len(graph) - 1):
            temp = 0

            if graph[i][j] == '@':
                if graph[i-1][j-1] == '@': temp += 1
                if graph[i-1][j] == '@': temp += 1
                if graph[i-1][j+1] == '@': temp += 1
                if graph[i][j-1] == '@': temp += 1
                if graph[i][j+1] == '@': temp += 1
                if graph[i+1][j-1] == '@': temp += 1
                if graph[i+1][j] == '@': temp += 1
                if graph[i+1][j+1] == '@': temp += 1

                if temp < 4:
                    res += 1
    
    return res

def part2(lines):
    
    graph = []
    graph.append("0" * (len(lines[0]) + 2))
    for line in lines:
        graph.append("0" + line + "0")
    graph.append("0" * (len(lines[0]) + 2))

    res = 0
    while True:        
        tempRes = 0
        for i in range(1, len(graph) - 1):
            for j in range(1, len(graph) - 1):
                temp = 0

                if graph[i][j] == '@':
                    if graph[i-1][j-1] == '@': temp += 1
                    if graph[i-1][j] == '@': temp += 1
                    if graph[i-1][j+1] == '@': temp += 1
                    if graph[i][j-1] == '@': temp += 1
                    if graph[i][j+1] == '@': temp += 1
                    if graph[i+1][j-1] == '@': temp += 1
                    if graph[i+1][j] == '@': temp += 1
                    if graph[i+1][j+1] == '@': temp += 1

                    if temp < 4:
                        tempRes += 1
                        graph[i] = graph[i][:j] + '#' + graph[i][j+1:]

        if tempRes == 0:
            break
        res += tempRes

    return res

if __name__ == "__main__":
    solve()
