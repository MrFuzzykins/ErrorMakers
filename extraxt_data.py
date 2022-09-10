#!/usr/bin/env python

import csv

def get_x(data):
    x_coords = []

    for line in data:
        x = line[7]
        x_coords.append(x)

    return x_coords

def get_y(data):
    y_coords = []

    for line in data:
        y = line[8]
        y_coords.append(y)

    return y_coords


def main():
    file_data = csv.reader(open("data.csv"))

    print(get_x(file_data))
    print(get_y(file_data))

if __name__ == "__main__":
    main()
