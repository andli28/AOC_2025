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
    # Your solution for part 1 goes here
    # Convert strings to lists for mutability
    lines = [list(line) for line in lines]

    res = 0
    for i in range(len(lines[:-1])):
        for j in range(len(lines[i])):
            if i%2 == 0:
                if lines[i][j] == "S":
                    lines[i+1][j] = "|"
                elif lines[i][j] == "^":
                    if lines[i-1][j] == "|":
                        res += 1
                        lines[i+1][j+1] = "|"
                        lines[i+1][j-1] = "|"
                elif lines[i][j] == "|" and lines[i+1][j] == ".":
                    lines[i+1][j] = "|"
            else:
                if lines[i][j] == "|" and lines[i+1][j] == ".":
                    lines[i+1][j] = "|"

    
    # for line in lines:
    #     print("".join(line))

    return res

def part2(lines):
    lines = [list(line) for line in lines]

    res = 0
    for i in range(len(lines[:-1])):
        for j in range(len(lines[i])):
            if i%2 == 0:
                if lines[i][j] == "S":
                    lines[i+1][j] = "1"
                elif lines[i][j] == "^":
                    if lines[i-1][j] != ".":
                        if lines[i+1][j+1] == ".": 
                            lines[i+1][j+1] = lines[i-1][j]
                        else:
                            lines[i+1][j+1] = str(int(lines[i+1][j+1]) + int(lines[i-1][j]))
                        if lines[i+1][j-1] == ".":
                            lines[i+1][j-1] = lines[i-1][j]
                        else:
                            lines[i+1][j-1] = str(int(lines[i+1][j-1]) + int(lines[i-1][j]))
                elif lines[i][j] != ".":
                    if lines[i+1][j] == ".": 
                        lines[i+1][j] = lines[i][j]
                    else:
                        lines[i+1][j] = str(int(lines[i+1][j]) + int(lines[i][j]))
            else:
                if lines[i][j] != "." and lines[i+1][j] == ".":
                    lines[i+1][j] = lines[i][j]
    
    # for line in lines:
    #     print("".join(line))

    for charac in lines[-1]:
        if charac != ".":
            res += int(charac)

    # for i in range(len(lines)-1, -1, -1):
    #     for j in range(len(lines[i])):
    #         if i%2 == 0:
    #             if lines[i][j] == "^":
    #                 lines[i-1][j] = str(int(lines[i+1][j-1]) + int(lines[i+1][j+1]))
    #             elif lines[i][j] == "S":
    #                 res = lines[i+1][j]
    #                 break
    #             elif lines[i][j] != ".":
    #                 lines[i-1][j] = lines[i][j]
    #         else:
    #             if lines[i][j] == "|":
    #                 lines[i][j] = "1"
    #             if lines[i][j] != ".":
    #                 lines[i-1][j] = lines[i][j]
    #     print("line:", i, lines[i])

    # for line in lines:
    #     print("".join(line))
    
    return res

if __name__ == "__main__":
    solve()
