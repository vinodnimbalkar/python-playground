import os
import csv

basedir = os.path.abspath(os.path.dirname(__file__))
path = basedir + "/CallRecorders/"
lst = os.listdir(path)
with open("call_data.csv","w") as new_file:
    fieldnames = ['Mobile No', 'Year', 'Month', 'Date', 'Hour', 'Minute', 'Second', 'Call Type', 'Audio']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
    csv_writer.writeheader()
    for i in lst:
        filelink = '=HYPERLINK("'+path+i+'")'
        csv_writer.writerow({fieldnames[0]:i.split('_')[0],fieldnames[1]:i.split('_')[1],fieldnames[2]:i.split('_')[2],\
        fieldnames[3]:i.split('_')[3],fieldnames[4]:i.split('_')[4],fieldnames[5]:i.split('_')[5],fieldnames[6]:i.split('_')[6],\
        fieldnames[7]:i.split('_')[7],fieldnames[8]:filelink})