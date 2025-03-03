with open('input.txt') as f:
    lines = f.readlines()

left = []
right = []

for line in lines:
    parts = line.strip().split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left_sorted = sorted(left)
right_sorted = sorted(right)

total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

print(total_distance)
