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
    # Look for all numbers in between the range that can be formed by two identical concatenated numbers
    rangeList = lines[0].split(",")
    res = 0
    
    for line in rangeList:
        start, end = line.split("-")
        startNum = int(start)
        endNum = int(end)

        # Approach:
        # For each number in the range, check if it can be formed by two identical concatenated numbers
        for num in range(startNum, endNum + 1):
            numStr = str(num)
            length = len(numStr)

            # Only consider even length numbers
            if length % 2 != 0:
                continue

            halfLength = length // 2
            firstHalf = numStr[:halfLength]
            secondHalf = numStr[halfLength:]

            if firstHalf == secondHalf:
                res += int(firstHalf+secondHalf)

        # # go through the range of the length of the numbers
        # # For example, if the range is 100-500, we only need to check length 3 as both 100 and 500 have length 3
        # # Since we only have to consider length 3, which is odd, the are no valid numbers

        # # If teh range is 101-4930, we need to check length 3 and length 4
        # # For length 3, there are no valid numbers
        # # For length 4, we can have numbers like 1111, 2222.

        # # When considering numbers, we can go from 1 to 9 for each digit
        # for length in range(len(start), len(end) + 1):
        #     if length % 2 != 0:
        #         continue

        #     halfLength = length // 2
        #     for firstHalf in range(10**(halfLength - 1), 10**halfLength):
        #         candidateStr = str(firstHalf) * 2
        #         candidateNum = int(candidateStr)

        #         if startNum <= candidateNum <= endNum:
        #             res += 1
    
    return res

def part2(lines):
    # Look for all numbers in between the range that can be formed by more than one identical concatenated numbers
    rangeList = lines[0].split(",")
    res = 0
    
    for line in rangeList:
        start, end = line.split("-")
        startNum = int(start)
        endNum = int(end)

        # Approach:
        # For each number in the range, check if it can be formed by more than one identical concatenated numbers
        for num in range(startNum, endNum + 1):
            numStr = str(num)
            length = len(numStr)

            # Check for all possible divisors of the length
            for div in range(2, length + 1):
                if length % div != 0:
                    continue

                partLength = length // div
                part = numStr[:partLength]
                if part * div == numStr:
                    res += int(numStr)
                    break

    return res

if __name__ == "__main__":
    solve()
