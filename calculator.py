print('The avilable options available!!!')
print('+')
print('-')
print('*')
print('/')
print('%')
option=input('Enter your Choice = ')
a=float(input('Enter First Digit = '))
b=float(input('Enter Second Digit = '))
if option == '+':
    print('Addition {}+{}={}'.format(a, b, a + b))
elif option =='-':
    print('Subtraction {} - {} = {}'.format(a, b, a - b))
elif option =='*':
    print('Multiplication {} * {} = {}'.format(a, b, a * b))
elif option == '%':
    print('Reminder {} % {} = {}'.format(a, b, a % b))
elif option == '/':
    if b!=0:
        print('Division {} / {} = {}'.format(a, b, a / b))
    else:
        print('Infinity')
else:
    print('Check once')