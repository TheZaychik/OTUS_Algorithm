# https://data.cityofnewyork.us/api/views/faiq-9dfq/rows.csv?accessType=DOWNLOAD

import os.path
import statistics
import sys
import csv_parser
import hyper_log_log
import actual_count

filename = "Parking_Violations_Issued_-_Fiscal_Year_2019.csv"

ex_buckets = 8

loops_to_run = 8

plate_hashes = []
if os.path.exists("hashes.csv"):
    print("Loading plate hashes from file..")
    plate_hashes = csv_parser.load_hashes()
else:
    print("Creating plate hashes.. (this may take a moment)")
    plate_hashes = csv_parser.create_hashes(filename)
print(str(len(plate_hashes)) + " plate hashes loaded.\n")

exact_unique = actual_count.get_exact_unique_using_set(filename)
print("There are exactly " + str(exact_unique) + " unique plates..\n")

hll = []
for i in range(0, loops_to_run):
    sys.stdout.write("Running test " + str(i + 1) + " of " + str(loops_to_run) + ".. (this may take a moment)")
    sys.stdout.flush()

    hashes = []
    for hash in plate_hashes:
        hash = '{:256b}'.format(int(hash, 16)).replace(' ', '0')
        off = i * 32
        temp = hash[len(hash) - (32 + off) + 1:len(hash) - off]
        hashes.append(temp)

    hll.append(hyper_log_log.HyperLogLog(hashes, ex_buckets))

    sys.stdout.write('\r')


def printTest(label, expected, actual):
    print('*' * 50)
    print('{s:{c}^{n}}'.format(s=f' {label} ', n=50, c='*'))
    print('*' * 50)
    print()

    print('{s:{c}^{n}}'.format(s=' Expected result ', n=50, c='-'))
    print(expected)
    print('{s:{c}^{n}}'.format(s=' Actual results ', n=50, c='-'))
    print("\n".join("{0:.0f}".format(x) for x in actual))
    print('{s:{c}^{n}}'.format(s=' Mean result ', n=50, c='-'))
    print("{0:.0f}".format(statistics.mean(actual)))
    print()

    print('{s:{c}^{n}}'.format(s=' Difference ', n=50, c='-'))
    print("{0:.0f}".format(expected - statistics.mean(actual)))
    print('{s:{c}^{n}}'.format(s=' Percent Error ', n=50, c='-'))
    print("{0:.2%}".format(abs(expected - statistics.mean(actual)) / expected))
    print('{s:{c}^{n}}'.format(s=' Standard Deviation ', n=50, c='-'))
    print("{0:.0f}".format(statistics.pstdev(actual)))
    print()
    print()


printTest("HyperLogLog", exact_unique, hll)
