# print("Hello World")
# x = "3.32"
# print(f"this is a {x} number")
# x = float(x)
# print(type(x))
# a, b, c = 1 , 2 , 3
# print(a,b,c)
# name = input()
# print(f"Hello, {name}")
# x , y , z = map(int,input().split())
# map function map(function,array)
# print(x+y+z)
# print(4 in list1)         membership operations
# return function 


# Exercise 1
# name= input("Enter your name: ")
# p1,p2,p3 = map(float, input("Enter the 3 prices: ").split())
# total_price = (p1 + p2 + p3)*(10/100)
# print(f"hey {name}, the price after discount is {total_price}")
# List vs array
# indentation
# x , y = 3 , 4 
# if(y>=x):
#     print(True)
# print("Hello")
# in range(start,end,step) for loop
# def func(x=1, y=2):
#     print(x,y)
# func(x=2, y=1)
# enumerate function >> index + item
# len() function
# Nested foor loops

prices = map(float, input("Enter the prices: ").split())
for item in prices:
    if(item > 0 and item <50):
        print(f"{item} is cheap")
    elif(item >= 50 and item <=100):
        print(f"{item} is Mid")
    else:
        print(f"{item} is Expensive")


# Taking many inputs 
# items_list = []
# n = int(input("How many items do you want to add? "))

# for i in range(n):
#     item = input(f"Enter item {i+1}: ")
#     items_list.append(item)

# print(items_list)
