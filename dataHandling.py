import pickle as pk

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

def addTraction():
    with open('transactions.pkl', 'ab') as file:
        data = pk.load(file)
        pk.dump(data, file)
        print('Transaction added')
        
lst = []
data = ('Fuel added', 20, )