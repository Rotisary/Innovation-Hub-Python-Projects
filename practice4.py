def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


number = int(input('enter a number: '))
if number < 0:
    print('you no fit put negative number baba!')
else:
    result = factorial(number)
    print(f'the factorial of {number} is {result}')



