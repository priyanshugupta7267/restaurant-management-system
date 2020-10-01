# -management-system
# run this file 
best for restaurants 

'''
 Management System
'''

# modules 
import random


# defs 





# main

name=str(input(" > Enter your name. \n You > "))
print("Hello", name)

phone=int(input(" > Enter your phone number. \n You > "))
print("ok thanks!")

=random.randint(1, 9999)

rupees=0

choose=input(" > Hello, do you want to continue. Answer in y/n. \n You > ")
while True:
    if choose=='y':
        print("Ok thanks!")
        food=input(" > What do you want \n 1) Pizza \n 2) Burger \n 3)  \n 4)  \n Or type t to exit \n User > ")
        if food=='1':
            quantity_1=int(input(" > How many pizzas do you want? \n User > "))
            print("ok you need", quantity_1 , "pizza/pizzas.")
            rupees += 100*quantity_1
            print(" is now ", rupees , ".")

        elif food=='2':
            quantity_2=int(input(" > How many burgers do you want? \n User > "))
            print("ok you need", quantity_2 , "burger/burgers.")
            rupees += 25*quantity_2
            print(" is now ", rupees , ".")

        elif food=='3':
            quantity_3=int(input(" > How many sandwiches do you want? \n User > "))
            print("ok you need", quantity_3 , "/sandwiches.")
            rupees += 75*quantity_3
            print(" is now ", rupees , ".")

        elif food=='4':
            quantity_4=int(input(" > How many plates do you want? \n You > "))
            print("ok you need", quantity_4 , "plate/plates.")
            rupees += 50*quantity_4
            print(" is now ", rupees , ".")

        elif food=='t':
            exit()
        
      # billing
    print(" > Now its time to . \n You > ")
    print("Your  is", rupees)
    pay=str(input("Do you want to continue. Answer in y/n."))
    if pay=='y':
        print("-------------------------------------------------------------")
        print("Thanks for paying")

    elif pay=='n':
        exit()

    else:
        exit()

    stars=input(" > Please give us stars. \n You > ")
    if '1' in stars:
        print("Thanks for giving us stars.")
        print("Your  is printed.")
        print('''                                            HOTEL
                                                          
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
           Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '2' in stars:
        print("Thanks for giving us stars.")
        print("Your  is printed.")
        print('''                                            HOTEL
                                                          
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
           Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '3' in stars:
        print("Thanks for giving us stars.")
        print("Your  is printed.")
        print('''                                            HOTEL
                                                          
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
           Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()
    
    elif '4' in stars:
        print("Thanks for giving us stars.")
        print("Your  is printed.")
        print('''                                            HOTEL
                                                          
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, '''
          -------------------------------------------------------------------------------------------------------
           Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    elif '5' in stars:
        print("Thanks for giving us stars.")
        print("-----------------------------------------------------------------------------------------------------")
        print("Your  is printed.")
        print('''                                            HOTEL
                                                          
          ------------------------------------------------------------------------------------------------------
          Name=''', name ,'''Phone number=''', phone, ''' no.=''', , '''
          -------------------------------------------------------------------------------------------------------
           Amount=''', rupees, '''
          thanks for buying 
          _____________________________________________________________________________________________________''')

        exit()

    else:
        exit()



        


