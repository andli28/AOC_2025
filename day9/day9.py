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
    # Find the largest rectangle formed by two opposite corners
    # naive way is to calculate nC2 pairs and take the max. This is O(N^2) complexity

    coords = []
    res = 0
    for line in lines:
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        for cX, cY in coords:
            rectArea = (abs(cX - x) + 1) * (abs(cY - y) + 1)
            if rectArea > res:
                res = rectArea
        coords.append((x,y))
    
    return res

def part2(lines):
    # Find the largest rectangle formed by two opposite corners, 
    # but it also must be entirely contained by the entire shape formed by all corners.

    includedPoints = set()
    corners = []

    x, y = lines[0].split(",")
    x = int(x)
    y = int(y)
    includedPoints.add((x,y))
    lastPoint = (x,y)

    for i in range(1, len(lines)):
        x, y = lines[i].split(",")
        x = int(x)
        y = int(y)
        corners.append((x,y))
        includedPoints.add((x,y))
        if lastPoint[0] != x:
            # x coords are diff
            for p in range(min(lastPoint[0],x) + 1, max(lastPoint[0],x)):
                includedPoints.add((p,y))
        else: 
            # y coords must be diff
            for p in range(min(lastPoint[1],y) + 1, max(lastPoint[1],y)):
                includedPoints.add((x,p))
        
        lastPoint = (x,y)

    # Have to account for last point to first point
    x1 = corners[-1][0]
    x2 = corners[0][0]
    y1 = corners[-1][1]
    y2 = corners[0][1]

    if x1 != x2:
        # x coords are diff
        for p in range(min(x1,x2) + 1, max(x1,x2)):
            includedPoints.add((p, y1))
    else:
        # y coords must be diff
        for p in range(min(y1,y2) + 1, max(y1,y2)):
            includedPoints.add((x1, p))
    
    
    # outer floodfill to fill in the exterior of this shape.
    # Then take the inverse
    # First bound by 1 more than minimum and max x,y values.

    min_x = min(x for x, y in corners)
    max_x = max(x for x, y in corners)
    min_y = min(y for x, y in corners)
    max_y = max(y for x, y in corners)

    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1

    # floodfill from (min_x, min_y)
    # this is iterative instead of recursive to avoid the limit.
    outsidePoints = set()

    stack = [(min_x, min_y)]
    while stack:
        r, c = stack.pop()
        
        if r < min_x or r > max_x or c < min_y or c > max_y or ((r, c) in includedPoints) or ((r, c) in outsidePoints):
            continue
        
        outsidePoints.add((r, c))
        
        stack.append((r - 1, c))
        stack.append((r + 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

    # now, check pairwise sizes
    # If all of the boundary? points are not in outside points, we are good.
    res = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):     
            fail = False

            x1 = corners[i][0]
            y1 = corners[i][1]
            x2 = corners[j][0]
            y2 = corners[j][1]

            # check all <= four boundaries.
            for x in range(min(x1,x2) + 1, max(x1,x2)):
                if (x, y1) in outsidePoints or (x, y2) in outsidePoints:
                    fail = True
                    break
            if fail: break

            for y in range(min(y1,y2) + 1, max(y1,y2)):
                if (x1, y) in outsidePoints or (x2, y) in outsidePoints:
                    fail = True
                    break
            if fail: break

            res = max(res, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

    return res

if __name__ == "__main__":
    solve()
