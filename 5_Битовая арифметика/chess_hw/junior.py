def get_horse_moves(pos: int) -> int:
    k = 1 << pos
    no_a = 0xfefefefefefefefe
    no_ab = 0xfcfcfcfcfcfcfcfc
    no_h = 0x7f7f7f7f7f7f7f7f
    no_gh = 0x3f3f3f3f3f3f3f3f
    k_a = k & no_a
    k_h = k & no_h
    mask = no_gh & (k << 6 | k >> 10) \
           | no_h & (k << 15 | k >> 17) \
           | no_a & (k << 17 | k >> 15) \
           | no_ab & (k << 10 | k >> 6)
    return mask


def get_king_moves(pos: int) -> int:
    k = 1 << pos
    no_a = 0xfefefefefefefefe
    no_h = 0x7f7f7f7f7f7f7f7f
    k_a = k & no_a
    k_h = k & no_h
    mask = (k_a << 7) | (k << 8) | (k_h << 9) | \
           (k_a >> 1) | (k_h << 1) | \
           (k_a >> 9) | (k >> 8) | (k_h >> 7)
    return mask


def popcnt1(mask: int) -> int:
    cnt = 0
    while mask > 0:
        if (mask & 1) == 1:
            cnt += 1
        mask >>= 1
    return cnt


def popcnt2(mask: int) -> int:
    cnt = 0
    while mask > 0:
        cnt += 1
        mask &= mask - 1
    return cnt


if __name__ == '__main__':
    king = get_king_moves(1)
    horse = get_horse_moves(1)
    print(king)
    print(popcnt1(king))
    print(horse)
    print(popcnt2(horse))
