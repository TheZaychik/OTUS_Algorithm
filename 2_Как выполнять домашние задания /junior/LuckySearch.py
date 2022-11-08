count = 0

for a1 in range(0, 10):
    for a2 in range(0, 10):
        for a3 in range(0, 10):
            sumA = a1 + a2 + a3
            for b1 in range(0, 10):
                for b2 in range(0, 10):
                    if 0 <= (sumA - b2 - b1) <= 9:
                        count += 1

print(count)
