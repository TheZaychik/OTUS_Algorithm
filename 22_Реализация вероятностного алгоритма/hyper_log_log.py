import math


def HyperLogLog(hashes, k):
    m = 2 ** k
    buckets = [0] * m

    for i in range(0, len(hashes)):
        j = str(hashes[i])[:k]
        j = int(j, 2)

        data = hashes[i][k:]
        rank = 1
        for c in reversed(data):
            if c == "0":
                rank += 1
            else:
                break

        buckets[j] = max(buckets[j], rank)

    total = 0
    for bucket in buckets:
        total += 2 ** (-1 * bucket)
    mean = total ** -1
    estimate = (m ** 2) * mean

    if k <= 4:
        BIAS = 0.673
    elif k == 5:
        BIAS = 0.697
    else:
        BIAS = 0.7213 / (1 + (1.079 / m))

    estimate = BIAS * estimate

    if estimate < ((5 / 2) * m):
        zeros = 0
        for i in buckets:
            if buckets[i] == 0:
                zeros += 1
        if not zeros == 0:
            estimate = m * math.log(estimate, 2)

    elif estimate > ((2 ** 32) / 30):
        estimate = -1 * (2 ** 32) * math.log(1 - (estimate / (2 ** 32)))

    return estimate
