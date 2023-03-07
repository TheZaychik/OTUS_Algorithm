import argparse


def rle_encode(file: str):
    encoded = ''
    prev_c = ''
    count = 1
    data = open(file, 'rb').read()
    for c in data:
        if c != prev_c:
            if prev_c:
                encoded += f'{str(count)}%{prev_c}$'
            count = 1
            prev_c = c
        else:
            count += 1
    else:
        encoded += f'{str(count)}%{prev_c}$'
        open(file + '.arc', 'wb').write(bytearray(encoded.encode()))
        return encoded


def rle_decode(file: str):
    decode = ''
    data = open(file, 'rb').read().decode()
    for code in data.split('$'):
        if len(code) == 0:
            break
        count, prev_c = code.split('%')
        decode += int(count) * str(prev_c)
    open(file + '.decoded', 'wb').write(bytearray(decode.encode()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сжимает/распаковывает файлы используя RLE алгоритм')
    parser.add_argument('filedir', metavar='/var/file', type=str, help='путь до файла')
    parser.add_argument('--arc', action='store_true', help='сжать файл')
    parser.add_argument('--dearc', action='store_true', help='распаковать файл (.arc -> .arc.decoded)')
    args = parser.parse_args()
    if args.arc:
        rle_encode(args.filedir)
    elif args.dearc:
        rle_decode(args.filedir)
