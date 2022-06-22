# Write a program to find if a number is prime or not

number = int(input("Enter the number: "))

if number > 1:


    for i in range(2, number):

        if number % i == 0: # % is Modulo Operator: returns the remainder of the division. Raises ZeroDivisionError like the / operator 
            print("The number is composite")
            break # breaks and comes out of the loop

else:
    print("The number is prime")
