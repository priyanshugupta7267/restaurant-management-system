# -management-system
best for restaurants 

'''
Restaurant Management System
'''

# modules 
import random


# defs 





# main

name=str(input("Restaurant > Enter your name. \n You > "))
print("Hello", name)

phone=int(input("Restaurant > Enter your phone number. \n You > "))
print("ok thanks!")

bill=random.randint(1, 9999)

rupees=0

choose=input("Restaurant > Hello, do you want to continue. Answer in y/n. \n You > ")
while True:
    if choose=='y':
        print("Ok thanks!")
        food=input("Restaurant > What do you want \n 1) Pizza \n 2) Burger \n 3) Sandwich \n 4) Noodles \n Or type t to exit \n User > ")
        if food=='1':
            quantity_1=int(input("Restaurant > How many pizzas do you want? \n User > "))
            print("ok you need", quantity_1 , "pizza/pizzas.")
            rupees += 100*quantity_1
            print("Bill is now ", rupees , ".")

        elif food=='2':
            quantity_2=int(input("Restaurant > How many burgers do you want? \n User > "))
            print("ok you need", quantity_2 , "burger/burgers.")
            rupees += 25*quantity_2
            print("Bill is now ", rupees , ".")

        elif food=='3':
            quantity_3=int(input("Restaurant > How many sandwiches do you want? \n User > "))
            print("ok you need", quantity_3 , "sandwich/sandwiches.")
            rupees += 75*quantity_3
            print("Bill is now ", rupees , ".")

        elif food=='4':
            quantity_4=int(input("Restaurant > How many plates do you want? \n You > "))
            print("ok you need", quantity_4 , "plate/plates.")
            rupees += 50*quantity_4
            print("Bill is now ", rupees , ".")

        elif food=='t':
            exit()
        
      # billing
    print("Restaurant > Now its time to bill. \n You > ")
    print("Your bill is", rupees)
    pay=str(input("Do you want to continue. Answer in y/n."))
    if pay=='y':
        print("-------------------------------------------------------------")
        print("Thanks for paying")

    elif pay=='n':
        exit()

    else:
        exit()

    stars=input("Restaurant > Please give us stars. \n You > ")
    if '1' in stars:
        print("Thanks for giving us stars.")
        print("Your bill is printed.")
        print('''                                            HOTEL
                                                          Bill
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
          Bill Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '2' in stars:
        print("Thanks for giving us stars.")
        print("Your bill is printed.")
        print('''                                            HOTEL
                                                          Bill
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
          Bill Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '3' in stars:
        print("Thanks for giving us stars.")
        print("Your bill is printed.")
        print('''                                            HOTEL
                                                          Bill
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
          Bill Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()
    
    elif '4' in stars:
        print("Thanks for giving us stars.")
        print("Your bill is printed.")
        print('''                                            HOTEL
                                                          Bill
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
          Bill Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '5' in stars:
        print("Thanks for giving us stars.")
        print("-----------------------------------------------------------------------------------------------------")
        print("Your bill is printed.")
        print('''                                            HOTEL
                                                          Bill
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''Bill no.=''', bill, '''
          -------------------------------------------------------------------------------------------------------
          Bill Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    else:
        exit()



        


