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
    return "Solution 1"

def part2(lines):
    # Your solution for part 2 goes here
    return "Solution 2"

if __name__ == "__main__":
    solve()
