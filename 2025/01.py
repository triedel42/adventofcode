from pprint import pprint
from functools import reduce


def part_one():
    rot = ((-1 + 2 * (s[0] == "R")) * int(s[1:-1]) for s in open("inputs/01"))
    dial = 50
    cnt = 0
    for r in rot:
        dial = (dial + r + 100) % 100
        cnt += dial == 0
        # print(r, dial, cnt)
    return cnt


def part_two():
    rot = ((-1 + 2 * (s[0] == "R")) * int(s[1:-1]) for s in open("inputs/01"))
    dial = 50
    cnt = 0
    for r in rot:
        while r != 0:
            sign = 1 if r > 0 else -1
            dial = (dial + 100 + sign) % 100
            r -= sign
            cnt += dial == 0
    return cnt


print("Part One: ", part_one())
print("Part Two: ", part_two())
