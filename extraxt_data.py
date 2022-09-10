#!/usr/bin/env python

import csv

import matplotlib.pyplot as plt


def get_coord(data, index):
    x_coords = []

    for line in data:
        x = line[index]
        x_coords.append(x)

    return x_coords


def main():
    file_data = csv.reader(open("data.csv"))
    x_coord = get_coord(file_data, 7)
    
    file_data = csv.reader(open("data.csv"))
    y_coord = get_coord(file_data, 8)

    for i in range(0,len(x_coord)):
        print(f"x: {x_coord[i]}, y: {y_coord[i]}")
    
    plt.plot()

if __name__ == "__main__":
    main()
