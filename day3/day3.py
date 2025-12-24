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
    # For each line, find the largest number in len(line) - 1
    # Then, find the largest number to the right of it.
    
    res = 0

    for line in lines:
        maxSoFar = 0
        maxIndexSoFar = 0
        maxSoFar2 = 0

        for i in range(len(line) - 1):
            if int(line[i]) > maxSoFar:
                maxSoFar = int(line[i])
                maxIndexSoFar = i
        
        for i in range(maxIndexSoFar + 1, len(line)):
            if int(line[i]) > maxSoFar2:
                maxSoFar2 = int(line[i])
    
        res += maxSoFar * 10 + maxSoFar2
        # print(maxSoFar * 10 + maxSoFar2)

    return res


def part2(lines):
    # First, find the largest number in len(line) - 12
    # Then, find the largest number to the right of it.

    res = 0
    temp = ""

    for line in lines:
        start = 0
        temp = ""

        for i in range(11, -1, -1):
            maxNum = "0"

            for j in range(start, len(line) - i):
                if int(line[j]) > int(maxNum):
                    maxNum = line[j]
                    start = j + 1
            
            temp += maxNum
        # print(temp)
        res += int(temp)
    

    return int(res)

if __name__ == "__main__":
    solve()
