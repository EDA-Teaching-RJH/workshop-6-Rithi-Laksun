#Your code goes here. 

import math

#def main():
    #print(safe_divide(10, 2))
    #print(safe_divide(10, 0))
    #print(process_list([1, '2', 3, 'four', 5]))    
    #print(nested_operations(16, 4))
    #print(nested_operations(10, 0))
    #print(nested_operations('a', 5))
    #process_input()

#main() 

def safe_divide(a, b):
    print("Give two numbers to divide!")
    try:
        a = int(input("What's the first number? "))
        b = int(input("What's the second number? "))
        c = a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(c)


def process_list(input_list):
    process_list = []
    try:
        input_list = input("Write the numbers you want to add to the list with spaces: ")
        string_list =input_list.split()
        process_list = [int(no) for no in string_list]
    except(TypeError, ValueError):
        #processnew_list = ([no for no in string_list if isinstance(no, int)])
        processnew_list = []
        for no in process_list:
            if isinstance(no, int):
                processnew_list.append(no)
        print(processnew_list)
    else:
        print(process_list)


def nested_operations():
    try:
        a = input("What's your first value: ")
        b = input("What's your second value: ")
        try:
            a = int(a)
            b = int(b)
            c = a/b
            d = math.sqrt(c)
        except ValueError:
            print("Not able to convert to integer")
        else:
            print("The two values divided then squared rooted is ", d)
    except ZeroDivisionError:
        print("You cannot divide by 0")

def process_input():
    number = input("Enter a number: ")
    try:
        number = float(number)
        n2 = number*number
    except ValueError:
        print("Input is not valid number")
    else:
        print("The number squared is ",n2)
    finally:
        print("Processing complete")
#process_input()
#nested_operations()
process_list(input_list= 1000000)
#safe_divide(100000,100000)

