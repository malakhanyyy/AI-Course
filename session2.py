# Slicing >> sequence[start:stop:step] >> we don't take the last number
# Reversing (-1,-2,-3)
# string built in functions in python >> strip() >> removes spaces and * from begin and end >> replace(,) >> replaces chars in string
# Conc >> adding many strings >> equals to join()
# printing using formatting or %s then calling it or .format

# Ex 1
# myString = input("Enter a string: ") 
# length = len(myString)
# list=[]

# for i in range(length):
#     if(i%2==0):
#         list.append(myString[i])
# word = "".join(list)
# print(f"Without reversing : {word}")
# halfLength= int(len(word)/2)
# reversed = word[-1:halfLength-1:-1]
# nonReversed = word[:halfLength:]
# FinalWord = nonReversed + reversed
# print(f"Final after reversing half is : {FinalWord}")
# FinalWord= FinalWord.upper()
# print(f"Final is: " + FinalWord[-1]+  FinalWord[1:-1:]+ FinalWord[0])



# TOP


# set (removes duplicates) && tuple
# Lists >> Mutable & Ordered
# Lists have dynamic size
# append & Insert
# list is a stack >> pop() >> remove() >> insert(index,value) >> extend() adding a list to another list >> remove()  for value >>  del list1[i]
# 2d arrays 




# matrix = []
# row , col = 2 , 3
# for i in range(row):
#     new_row = []
#     for j in range(col):
#         x = int(input())
#         new_row.append(x)
#     matrix.append(new_row)

# print(matrix)


# matrix = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(3):
#         matrix[i][i] = 1
#         matrix[i][2-i]=2
# matrix[1][1]=3
# for row in matrix:
#         print(row)        
        

# Immutable data types cannot be changed
# dictionary       key & value       new = {key: value1 , key: value}
# sets >> add >> remove >> discard             calling by value          operations like union & intersections

# lambda 

# list = []
# for i in range(5):
#     num = input()
#     list.append(num)
# list = map(int, list)
# list2 = []

# for i in list:
#     for j in range(5):
#         if(j%2==0):
#             list2.append(i*i)

            



# print(list2)
    

# nums = input("Enter numbers: ").split()
# length = len(nums)
# list = []
# for i in range(length):
#     if(i%2==0):
#         list.append(int(nums[i])**2)

# print(list)


# Vowel Example
# sentence = input("Enter a sentence: ")
# vowels= ['a','e','i','o','u']
# for char in sentence:
#     if char in vowels:
#         sentence= sentence.replace(char,'')

# print(sentence)


# numpy
import numpy as np





    
    




