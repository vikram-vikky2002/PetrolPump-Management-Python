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
        