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
    # Read in ranges, merge where necessary.
    # set of (start, end) tuples
    ranges = set()
    index = 0

    while index < len(lines):
        if lines[index] == "":
            index += 1
            break
        merged = False
        start, end = lines[index].split("-")

        start = int(start)
        end = int(end)
        for s, e in ranges:
            if start > e or end < s:
                # cannot merge with this tuple
                continue
            else:
                # merge
                ranges.remove((s, e))

                realStart = min(start, s)
                realEnd = max(end, e)

                ranges.add((realStart, realEnd))

                merged = True
        
        # if not merged with any tuple
        if not merged:
            ranges.add((start, end))
        index += 1
    
    res = 0
    while index < len(lines):
        ingID = int(lines[index])
        for s, e in ranges:
            if ingID >= s and ingID <= e:
                res += 1
                break
        
        index += 1


    # Read in the ingredients, add where necessary.
    return res

def part2(lines):
    # read in ranges
    ranges = set()
    index = 0

    while index < len(lines):
        if lines[index] == "":
            index += 1
            break
        merged = False
        start, end = lines[index].split("-")

        start = int(start)
        end = int(end)
        for s, e in ranges:
            if start > e or end < s:
                # cannot merge with this tuple
                continue
            else:
                # merge
                ranges.remove((s, e))

                start = min(start, s)
                end = max(end, e)

                merged = True
                break
        
        ranges.add((start, end))
        
        while merged:
            for s, e in ranges:
                if start > e or end < s:
                    # cannot merge with this tuple
                    merged = False
                    continue
                elif start == s and end == e:
                    merged = False
                    continue
                else:
                    # merge
                    ranges.remove((s, e))

                    start = min(start, s)
                    end = max(end, e)

                    ranges.add((start, end))

                    merged = True
                    break

        index += 1

    # loop through ranges, add the end - start + 1
    res = 0
    for s, e in ranges:
        # print(s, e)
        res += (e - s) + 1

    return res

if __name__ == "__main__":
    solve()
