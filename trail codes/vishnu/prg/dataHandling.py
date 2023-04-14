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
    
def deleteData(filename):
    with open (filename,"wb")as file:
        lst1=pk.load()
        

# lst = ['Tamil', 'Fav']
# storeData(r'data\Playlist.pkl' ,lst)