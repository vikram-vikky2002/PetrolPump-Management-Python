import ast
file_name = 'petrol.txt'

def saveData(updateQty, filename):
    with open(filename, 'w') as f:
        f.write(updateQty)
        
def loadPetrol(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read

def fill_Petrol(qty, rate, avPetrol):
    if(avPetrol >= qty):
        print('Filling...')
        avPetrol = avPetrol - qty
        price = qty*rate
    else:
        print('Fuel Not there...')


try:
    values = ast.literal_eval(loadPetrol(file_name))
    print('Loaded Value : ', values)
except:
    print('Creating a new File...')
    values = {}
    
while True:
    addingQty = int(input('Enter the quantity added into the storage : '))
    saveData(str(values), file_name)
    print(values['updateQty'])