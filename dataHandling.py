'''
    This file is used to store and retrieve data from the file
    It will store the data in the file in the form of pickle
    It will retrieve the data from the file in the form of pickle
    It will also add the data to the transactions.csv file

'''

import pickle as pk
import csv

def storeData(filename, data):
    with open(filename, 'wb') as file:
        pk.dump(data, file)
        print('Value Updated...')


def getData(filename):
    with open(filename, 'rb') as file:
        val = pk.load(file)
        print('Getting Values...')
        print(val)
        return val

def addTraction(data):
    with open(r'data\transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print('Data Added...')
        