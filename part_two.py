from collections import Counter

with open('input.txt') as f:
    left = []
    right = []
    for line in f:
        parts = line.strip().split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

right_counts = Counter(right)

similarity_score = 0
for num in left:
    similarity_score += num * right_counts.get(num, 0)

print(similarity_score)
