import fileinput
import sys
# https://adventofcode.com/2025/day/1

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
    # Goal: Count how many times n mod 100 == 0

    # Keep track of the n mod 100
    # We start at n mod 50

    # Inputs will be in the form of R[Number] or L[Number]
    # If R, we add the number to n mod 100
    # If L, we subtract the number from n mod 100

    res = 0
    currMod = 50

    for line in lines:
        direction = line[0]
        number = int(line[1:])

        if direction == 'R':
            currMod = (currMod + number) % 100
        elif direction == 'L':
            currMod = (currMod - number) % 100

        if currMod == 0:
            res += 1

    return res

def part2(lines):
    # Goal: Count how many times n mod 100 == 0
    # But now, we need to track every intermediate step

    res = 0
    currMod = 50

    for line in lines:
        direction = line[0]
        number = int(line[1:])

        for _ in range(number):
            if direction == 'R':
                currMod = (currMod + 1) % 100
            elif direction == 'L':
                currMod = (currMod - 1) % 100

            if currMod == 0:
                res += 1


    return res

if __name__ == "__main__":
    solve()
