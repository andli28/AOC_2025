import fileinput
import sys
import math

def solve():
    # Read input data into a list of lines, stripping newlines
    # Use [int(line.strip()) for line in fileinput.input()] for integer input
    lines1 = [line.strip() for line in fileinput.input()]
    lines2 = [line for line in fileinput.input()]
    

    # --- Part 1 ---
    result_part1 = part1(lines1)
    print(f"Part One: {result_part1}")

    # --- Part 2 ---
    result_part2 = part2(lines2)
    print(f"Part Two: {result_part2}")

def part1(lines):
    # or [0] * len(lines[0].split(" ")))
    resVec = [] 
    opVec = lines[-1].split(" ")
    opVec = [s for s in opVec if s != ""]
    # print(opVec)

    firstNums = lines[0].split(" ")
    firstNums = [s for s in firstNums if s != ""]
    # print(firstNums)
    for num in firstNums:
        resVec.append(int(num))

    for line in lines[1:-1]:
        numVec = line.split(" ")
        numVec = [s for s in numVec if s != ""]
        for i in range(len(numVec)):
            if opVec[i] == "*":
                resVec[i] *= int(numVec[i])
            else:
                resVec[i] += int(numVec[i])

    return sum(resVec)

def part2(lines):
    res = 0

    resVecStr = []
    resVecNum = []
    opVec = []
    opPositions = set()
    lastLine = lines[-1]

    for i in range(len(lastLine)):
        if lastLine[i] != " ":
            opVec.append(lastLine[i])
            opPositions.add(i)
    
    
    opNum = 0
    colIndex = 0
    for j in range(len(lines[0])):
        for i in range(len(lines[:-1])):
            # print((i,j))
            # print(lines[i])
            # print(lines[i][j])
            if j+1 in opPositions or j == len(lines[0])-1:
                # print(resVecStr)
                for num in resVecStr:
                    resVecNum.append(int(num))

                if opVec[opNum] == "*": res += math.prod(resVecNum)
                else: res += sum(resVecNum)
                opNum += 1
                resVecStr = []
                resVecNum = []
                colIndex = -1

                break
            if lines[i][j] != " ":
                # print(j, len(resVecStr), colIndex)
                if len(resVecStr) <= colIndex:
                    resVecStr.append(lines[i][j])
                else:
                    resVecStr[colIndex] += lines[i][j]
        # print("next col")
        colIndex += 1


    return res

if __name__ == "__main__":
    solve()
