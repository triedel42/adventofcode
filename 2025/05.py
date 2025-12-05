from pprint import pprint


def read_ranges(fname):
    ranges = []
    for l in open(fname):
        l = l[:-1]
        if not l:
            break
        a, b = l.split("-")
        ranges.append([int(a), int(b)])
    return ranges


ranges = read_ranges("input")
# ranges = read_ranges('input_test')
ranges.sort()

merged_ranges = ranges[:1]
for c, d in ranges[1:]:
    if c in range(merged_ranges[-1][0], merged_ranges[-1][1] + 2):
        merged_ranges[-1][1] = max(d, merged_ranges[-1][1])
    else:
        merged_ranges.append([c, d])

pprint(merged_ranges)
s = 0
for rng in merged_ranges:
    c = rng[1] - rng[0] + 1
    print(rng, f"counts for {c}")
    s += c

print(s)
