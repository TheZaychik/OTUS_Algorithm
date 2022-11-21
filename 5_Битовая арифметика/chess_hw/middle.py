from junior import popcnt1, get_king_moves

bits = []
for i in range(256):
    bits.append(popcnt1(i))


def popcnt3(mask):
    cnt = 0
    while mask > 0:
        cnt += bits[mask & 255]
        mask >>= 8
    return cnt


def get_rook_moves(pos: int) -> int:
    line_a = 72340172838076673
    line_1 = 255
    pos_x, pos_y = 0, 0

    buff = pos
    while buff >= 7:
        buff -= 8
        pos_y += 1

    buff = pos
    while buff % 8 != 0:
        buff -= 1
        pos_x += 1

    for _ in range(pos_x):
        line_a <<= 1
    for _ in range(pos_y):
        line_1 <<= 8

    return line_1 ^ line_a


if __name__ == '__main__':
    rook = get_rook_moves(37)
    print(popcnt3(rook))
    print(rook)
