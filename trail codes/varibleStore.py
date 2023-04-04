import pickle as pk

def storeQty(Pqty):
    with open('petrolQty.pkl', 'wb') as file:
        pk.dump(Pqty, file)
        print('storing Successful..')
        
def getQty():
    with open('petrolQty.pkl', 'rb') as file:
        qty = pk.load(file)
        return qty

def main():
    # i = int(input('Enter Available Qty : '))
    # storeQty(i)
    # h = 10
    # print(f'h = {h}')
    h = getQty()
    print(f'Qty : {h}')

main()