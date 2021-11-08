# Program to peform basic arthematic operations

print('This is a calculator program using python')
print('The operations :')
print('')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Greater than')
print('6. Table of any number')
print('')

choice = int(input('Enter Your Choice : '))
print('')

if (choice == 1):
    choice1 = int(input('Enter first number : '))
    choice2 = int(input('Enter second number : '))
    sum1 = choice1 + choice2
    print('The sum is : ' , sum1)

elif(choice == 2):
    choice1 = int(input('Enter first number : '))
    choice2 = int(input('Enter second number : '))
    difference = choice1 - choice2
    print('The difference is : ' , difference)

elif(choice == 3):
    choice1 = int(input('Enter first number : '))
    choice2 = int(input('Enter second number : '))
    product = choice1 * choice2
    print('The product is : ' , product)

elif(choice == 4):
    choice1 = int(input('Enter first number : '))
    choice2 = int(input('Enter second number : '))
    quotient = choice1 / choice2
    print('The quotient is : ' , quotient)

elif(choice == 5):
    choice1 = int(input('Enter first number : '))
    choice2 = int(input('Enter second number : '))
    if choice1 > choice2:
        print(choice1,'is greater')
    elif choice2 > choice1:
        print(choice2 ,'is greater')
    else:
        print('Both are equal')

elif(choice == 6):
    numbers = int(input('Enter the number : '))

    for val in range(1,11):
        print(numbers , ' x ' , val , ' = ' , numbers*val)

else:
    print('Invalid choice')



    

