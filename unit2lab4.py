"""
Program: Total Weekday and Weekend Visitors calculator
Description: This program calculates the total number of visitors on weekdays and weekends.
Date: 2026-09-30
Name: Oluwatomi Alo

"""
from typing import Final
OIL_PRICE: Final = 1.25
OIL_LITRES_PER_CASE: Final = 12
GAS_PRICE: Final = 1.05
AB_OR_BC_GST: Final = 0.05
ON_GST: Final = 0.13
OTHERS_GST: Final = 0.15


print("Please select the type of purchase:")
print("G: Gas\nO: Oil")
user_choice = input("")

if user_choice.upper() != "G" and user_choice.upper() != "O":
    print("Invalid input, you should enter g/G or o/O")

elif user_choice.upper() == "O":
    num_of_cases = int(input("Enter # of cases of Oil : "))
    if num_of_cases < 0:
        print("Number of oil cases should be > 0")
        exit()
    else:
        if num_of_cases > 6:
            discount_price = OIL_PRICE * 0.9 * OIL_LITRES_PER_CASE
            total_cost = num_of_cases * discount_price
        else:
            discount_price = OIL_PRICE * OIL_LITRES_PER_CASE
            total_cost = num_of_cases * discount_price
        province = input("Please enter the 2 letters province abbreviation: ")
        if province.upper() == "AB" or province.upper() == "BC":
            gst = total_cost * AB_OR_BC_GST
            total_cost += gst
        elif province.upper() == "ON":
            gst = total_cost * ON_GST
            total_cost += gst 
        else:
            gst = total_cost * OTHERS_GST
            total_cost += gst
    print(f"Total cost of Oil purchase is: ${total_cost:.2f}")
    print("Thanks for your business, Good Bye")    

elif user_choice.upper() == "G":
    num_of_litres = int(input("Enter the number of litres of gas : "))
    if num_of_litres < 0:
        print("Number of gas litres should be > 0")
        exit()
    else:
        if num_of_litres > 2000:
            discount_price = GAS_PRICE * 0.9
            total_cost = num_of_litres * discount_price
        else:
            discount_price = GAS_PRICE
            total_cost = num_of_litres * discount_price
        province = input("Please enter the 2 letters province abbreviation: ")
        if province.upper() == "AB" or province.upper() == "BC":
            gst = total_cost * AB_OR_BC_GST
            total_cost += gst
        elif province.upper() == "ON":
            gst = total_cost * ON_GST
            total_cost += gst
        else:
            gst = total_cost * OTHERS_GST
            total_cost += gst   
    print(f"Total cost of Gas purchase is: ${total_cost:.2f}")

    print("Thanks for your business, Good Bye")