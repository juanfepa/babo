# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:01:06 2021

@author: Student
"""
""" File Name: Mattress.py.;
 Date: February 15, 2021
 Description: the purpose of this program is to createe a POS prototype for an online mattress retailer
 Honesty Statement: I abide by this statement that I have completed this work individually"""
 
print("Welcome!")

Mattress_Brand= (input("Please select the mattress brand(1-Sealy, 2- Simmons): ")

if Mattress_Brand == 1: 
    print("Sealy")
if Mattress_Brand == 2: 
    print("Simmons")

Mattress_Size= {3, 4, 5}
Mattress_Size= input("Please select the Mattress Size (3-King, 4-Queen, 5-Twin): ")

if Mattress_Size == 3: 
    print("King")
    
elif Mattress_Size == 4: 
    print("Queen")
elif Mattress_Size == 5:
    print("Twin")
else: 
    print(" Please try K for King, Q for Queen, or T for Twin")
    
Mattress_Comfort= input("Please select the mattress Comfort Level (6-Medium, 7-Firm, 8- Extra Firm): ")
if Mattress_Comfort == 6: 
    print("Medium")
elif Mattress_Comfort == 7: 
    print("Firm")
elif Mattress_Comfort == 8:
    print("Extra Firm")
else: 
    print(" Please try 6 for Medium, 7 for Firm, or 8 for Extra Firm")
    
Box_Spring= input("Do you like box springs?( 9- Yes, 10- No)): ")
if Box_Spring == 9:
    print("Yes")
elif Mattress_Comfort == 10:
    print("No")
else: 
    print(" Please try 9 for Yes and 10 for No")
    
Shipping_Mode= input("Which Shipping mode do you like? (11-Standard, 12- Next Day): ")
Shipping_Mode= 11, 12
if Shipping_Mode == 11: 
    print("Standard")
elif Shipping_Mode == 12: 
    print("Next Day")
else: 
    print(" Please try Sd for Standard or Nd for Next Day")
    
Mattress_Price = {

    "sealy": {

        'medium': {

            'king': 1800,

            'queen': 1400,

            'twin': 900

        },

        'firm': {

            'king': 2200,

            'queen': 1800,

            'twin': 1300

        },

        'extra firm': {

            'king': 2400,

            'queen': 2000,

            'twin': 1500

        }

    },

    "simmons": {

        'medium': {

            'king': 2000,

            'queen': 1400,

            'full': 1000,

        },

        'firm': {

            'king': 2500,

            'queen': 1900,

            'full': 1500,

        },

        'extra firm': {

            'king': 3000,

            'queen': 2400,

            'full': 2000,

        }

    }

}

Box_Price = {

    'king': 400,

    'queen': 300,

    'full': 200,

    'twin': 100

}

if __name__ == "__main__":
    while True:
    
        Shipping_Price = [100, 300]

Brand=Mattress_Brand

Size= Mattress_Size(Mattress_Brand)

Comfort= Mattress_Comfort()
    
Bill= Mattress_Price[Brand][Comfort][Size]

is_box_spring = input('Would you like to add a box spring? (yes or no): ')
if is_box_spring[0] in ['y', 'Y']:

    Bill += Box_Price[Size]



 

    

