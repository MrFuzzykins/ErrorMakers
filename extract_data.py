#!/usr/bin/python

import csv, webbrowser, re

def get_coord(data, index):
    x_coords = []

    for line in data:
        x_coords.append(line[index])

    return x_coords

def formatted_data(datafilename):
    data_arr = [['Lat', 'Long', 'Name', 'Marker']]

    file_data = csv.reader(open(datafilename, "r"))
    x_coord = get_coord(file_data, 8)

    file_data = csv.reader(open(datafilename, "r"))
    y_coord = get_coord(file_data, 7)

    file_data = csv.reader(open(datafilename, "r"))
    name_arr = get_coord(file_data, 2)

    file_data = csv.reader(open(datafilename, "r"))
    bubbler_type = get_coord(file_data, 6)

    for i in range(1, len(name_arr)):
        new_arr = []
        new_arr.append(float(x_coord[i]))
        new_arr.append(float(y_coord[i]))
        new_arr.append(name_arr[i].title())
        
        # types are:
        # regular - 1666
        # disabled - 34
        # with dog bowl - 243
        # anti vandal tap/ maintainence tap - 11
        # relocation & unit attached to seat and bin (i.e. not working)
        check = bubbler_type[i]
        if re.search(r"RELOCATION|UNIT", check) != None:
            new_arr = []
        elif re.search(r"VANDAL|MAINTENANCE", check):
            new_arr.append("vandal")
        elif re.search(r"BOWL", check):
            new_arr.append("dog")
        elif re.search(r"DI[S]*ABLED|ACCESSIBLE", check) != None:
            new_arr.append("disabled")
        else:
            new_arr.append("regular")

        if len(new_arr) == 4:
            data_arr.append(new_arr)
    
    return data_arr

def main():
    datafilename = "data.csv"
    htmlfilename = "display_map.html"
    final = formatted_data(datafilename)

    for line in final:
        print(line)

    # open the html file data
    # replace all of the lines after google.visualization.arrayToDataTable([
    # to ]);
    # 

    # view html file on web browser
    #webbrowser.open(htmlfilename)

if __name__ == "__main__":
    main()