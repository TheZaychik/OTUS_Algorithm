def rle_encode(line: str):
    encoded = ''
    prev_c = ''
    count = 1

    for c in line:
        if c != prev_c:
            if prev_c:
                encoded += str(count) + prev_c
            count = 1
            prev_c = c
        else:
            count += 1
    else:
        encoded += str(count) + prev_c
        return encoded


def rle_decode(line: str):
    decode = ''
    count = ''
    for char in line:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


if __name__ == '__main__':
    data = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
    print(data)
    encoded_line = rle_encode(data)
    print(encoded_line)
    decoded_line = rle_decode(encoded_line)
    print(decoded_line)
