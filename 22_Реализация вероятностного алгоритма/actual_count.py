import time
import csv_parser


def count_all_unique_plates(filename, total_entries):
    unique = []

    for plate in csv_parser.get_plates(filename):
        if plate not in unique:
            unique.append(plate)

    return len(unique)


def get_exact_unique_using_set(filename):
    entries = []
    for plate in csv_parser.get_plates(filename):
        entries.append(plate)

    entries = set(entries)

    return len(entries)
