import random
from junior import Sort


def gen_file() -> None:
    with open('nums.bin', 'wb') as f:
        for _ in range(10 ** 9):
            f.write(random.randint(0, 65536).to_bytes(3, byteorder='big'))


def read_file() -> None:
    with open('nums.bin', 'rb') as f:
        while True:
            data = f.read(3)
            if data == "":
                break
            print(int.from_bytes(data, byteorder='big'))


if __name__ == '__main__':
    mas = []
    for _ in range(10 ** 9):
        mas.append(random.randint(0, 65536))
    read_file()
