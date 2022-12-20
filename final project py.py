


stock = {'running shoes': 300, 'lifestyle shoes': 300, 'trainer shoes': 100,'basketball shoes': 225,'soccer shoes': 100}
alreadypurchase = ['John']





def menu():
    print("Press 1: To add stock")
    print("Press 2: To check stock")
    print("Press 3: To enter purchase")
    print("Press g: to input more stock")
    print("Press p: to close program")
    return input ("Please make selection ")

run = menu()

#to add new type of stock (e.g snow shoes)
while True:
    if run == '1':
        addstock = input('New shoe to be added to stock? ')
        amount = input('Quantity of shoe to be added to stock?')
        stock[addstock] = amount
        run = menu()
 
 #to check stock
    elif run == '2':
        for key, value in stock.items():
            print("{}: {}".format(key, value))
        run = menu()

#to add more stock to current inventory
    elif run == 'g':
         shoe = input('What shoe needs more stock? ')
         if shoe in stock:
             if stock[shoe] >= 0:
                 stock[shoe] += 10
                 run = menu()
# to purchase shoe
    elif run == '3':
        shoe = input('What shoe was purchased? ')
        customer =  input('Who bought the shoes? ')
        if shoe in stock:
            if customer in alreadypurchase:
                print('{} cannot buy again'.format(customer))
                run = menu()
            else:
                if stock[shoe] > 0:
                    stock[shoe] -= 1
                    alreadypurchase.append(customer)
                    print("{} bought {}".format(customer, shoe))
                    run = menu()
                else:
                    print('{} could not buy because we are out of {}'.format(person, shoe))
                    run = menu()
        else:
                print('{} is out of stock'.format(shoe))
                run=menu()
    elif run =='p':
        break
print("end program")
               
    