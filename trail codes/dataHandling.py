import pickle as pk

def storeData(filename, data):
    with open(filename, 'wb') as file:
        pk.dump(data, file)
        print('Value Updated...')


def getData(filename):
    with open(filename, 'rb') as file:
        val = pk.load(file)
        print('Getting Values...')
        return val


