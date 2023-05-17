from custom_hashtable import *
import time


def general_test() -> None:
    a = CuckooHashTable(100)
    a.insert('123', 123)
    print(a.find('123'))
    print(a)
    HashTableSerializer.serialize(a)
    d_a = HashTableSerializer.deserialize()
    print(d_a.find('123'))
    print(d_a)

    print('------')

    b = ChainHashTable(100)
    b.insert('123', 123)
    print(b.find('123'))
    HashTableSerializer.serialize(b)
    d_b = HashTableSerializer.deserialize()
    print(d_b.find('123'))
    print(d_b)


def time_test() -> None:
    size = 1000

    missing = 0
    missing_sys = 0
    found = 0
    found_sys = 0
    inserted = 0
    inserted_sys = 0

    c = CuckooHashTable(100)
    c_sys = {}

    print('--------CUCKOO INSERT--------')
    t = time.time()
    for i in range(size):
        if c.insert(str(i) + 'testtesttest', i):
            inserted += 1
    print(inserted, 'нод было успешно положено в таблицу')
    print(time.time() - t)

    print('--------SYS INSERT--------')
    t = time.time()
    for i in range(size):
        c_sys.update({str(i) + 'testtesttest': i})
        inserted_sys += 1
    print(inserted_sys, 'нод было успешно положено в таблицу')
    print(time.time() - t)

    print('--------CUCKOO FIND--------')
    t = time.time()
    for i in range(size):
        ans = c.find(str(i) + 'testtesttest')
        if ans is None or ans != i:
            print(i, 'Отcутствует ключ', str(i) + 'testtesttest')
            missing += 1
    print('Потеряно', missing, 'записей ')
    print(time.time() - t)

    print('--------SYS FIND--------')
    t = time.time()
    for i in range(size):
        ans = c_sys.get(str(i) + 'testtesttest')
        if ans is None or ans != i:
            print(i, 'Отcутствует ключ', str(i) + 'testtesttest')
            missing_sys += 1
    print('Потеряно', missing_sys, 'записей')
    print(time.time() - t)

    print('--------CUCKOO DELETE--------')
    t = time.time()
    for i in range(size):
        c.delete(str(i) + 'testtesttest')
    print(time.time() - t)

    print('--------SYS DELETE--------')
    t = time.time()
    for i in range(size):
        c_sys.pop(str(i) + 'testtesttest')
    print(time.time() - t)

    t = time.time()
    print('--------CUCKOO CHECK--------')
    for i in range(size):
        ans = c.find(str(i) + 'testtesttest')
        if ans is not None or ans == i:
            print(i, 'Невозможно удалить ключ', str(i) + 'testtesttest')
            found += 1
    print('Неудалено', found, 'записей')
    print(time.time() - t)

    t = time.time()
    print('--------SYS CHECK--------')
    for i in range(size):
        ans = c.find(str(i) + 'testtesttest')
        if ans is not None or ans == i:
            print(i, 'Невозможно удалить ключ', str(i) + 'testtesttest')
            found_sys += 1
    print('Неудалено', found_sys, 'записей')
    print(time.time() - t)


if __name__ == '__main__':
    general_test()
