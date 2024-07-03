# x = int(input("Enter the first number "))

# y = int(input("Enter the second number "))
# z= x+y
# print(f" the sum is {z} and 2*z is {2*z} ")
# print(" The sum is {} and 2*z is {}" .format(z, 2*z))



# name = input("Enter your name ")

# if name != "Lucie":
#     print("You are not Lucie")
# else:
#     if not name == "Mohamed" and not name == "Lucie":
#         print("You're neither Lucie nor Mohamed")
#     else:
#         print(f"Hello {name} ") 

# if not name == "Lucie":
#     print("You are not Lucie")
# elif not name == "Mohamed" and not name == "Lucie":
#     print("You are also not Mohamed")
# else:
#     print(f"Welcome {name}")
# for n in range (1,11):
#     print(name)

# forbiddenNums = [401,403,404]

# a = int(input("Enter a new number "))
# if a in forbiddenNums:
#     print("forbidden number")
# else:
#     print(a)

# for a in forbiddenNums:
#     print(a)

# name = "Lucie"
# len(name)
# n= 1
# while n <= 10:
#     print(f"numbers are {n}")
#     n+=1

# def palindromeChecker(letters) :
#     i = 0
#     j =len(letters) - 1
#     while letters[i] == letters[j] and i < j:
#         i+=1 
#         j-=1
        
#     if i >= j :
#         return True
#     else:
#         return False
    
def checker(name):
    return name == name[::-1]

print(checker("mom"))




