def fill_Petrol(qty, rate, avPetrol):
    if(avPetrol >= qty):
        print('Filling...')
        avPetrol = avPetrol - qty
        price = qty*rate
    else:
        print('Fuel Not there...')
        