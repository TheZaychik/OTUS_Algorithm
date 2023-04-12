import csv
import hashlib

row_limit = -1


def count_lines(filename):
    with open(filename, "r") as csvfile:
        return sum(1 for row in csvfile) - 1


def get_plates(filename):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile)
        count = -1
        for row in datareader:
            if (count == -1):
                # ignore the header row
                count += 1
            elif (row_limit == -1 or count < row_limit):
                yield row[1]
                count += 1
            else:
                return


def create_hashes(filename):
    hashes = []
    with open('hashes.csv', 'w') as file:
        for plate in get_plates(filename):
            hash = hashlib.sha256(str(plate).encode('utf-8'))
            hashes.append(hash.hexdigest())
            file.write(hash.hexdigest() + "\n")
    return hashes


def load_hashes():
    f = open("hashes.csv", "r")
    if (row_limit > 0):
        return f.readlines(row_limit * 65)
    else:
        return f.readlines()
