import json
import os
import csv


def smallest_area(Data):
    #area of triangle 
    x1,x2,x3 = float(Data[0][0]),float(Data[1][0]),float(Data[2][0])
    y1,y2,y3 = float(Data[0][1]) ,float(Data[1][1]) ,float(Data[2][1])
    area_tri = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if area_tri > 1:
        area_tri = (1/2)*area_tri

    print("%.6f"%area_tri)

if __name__ == "__main__":
    
    #First paste the file in this directory 
    
    file_name,extension = input("Enter the file Name : ").split(".")
    # Opening JSON file
    #In JSON, Keys are pillar numbers 
    file = os.getcwd()+'\\'+file_name+'.'+extension

    #if extension == 'json':
        #with open(file) as f:
        #    Data = json.load(f)
    if extension == 'csv':
        #opening .csv file
        with open(file) as f:
            Data = [row for row in csv.reader(f)]
    elif extension == 'txt':
        #opening .txt file
        with open(file) as f:
            Data =[[_ for _ in row.split(",")] for row in f.readlines()]
    else:
        print("Sorry! This program can't read '.{}' file".format(extension))
    
    smallest_area(Data)

 
