import math

selec = 0
x = 0
y = 0
print()
print('Welcome to my Calculator!')

def selection(select):
    if select == 0:
        addition()
    if select == 1:
        subtraction()
    if select == 2:
        multiplication()
    if select == 3:
        division()
    if select == 4:
        sqrt()

def formatEquation():
    global selec
    if selec == 0:
        print('\nAddition format: x + y')
    if selec == 1:
        print('\nSubtraction format: x - y')
    if selec == 2:
        print('\nMultiplication format: x * y')
    if selec == 3:
        print('\nDivision format: x / y')
    if selec == 4:
        print('\nSquare root format: x')



def basicEquation():
    global select
    global x
    global y
    if selec > 3:
        x = int(input('Input x: '))
    else:
        x = int(input('Input x: '))
        y = int(input('Input y: '))
def answer():
    global selec
    if selec == 0:
        print(f'\nThe answer is {x + y}')
    if selec == 1:
        print(f'\nThe answer is {x - y}')
    if selec == 2:
        print(f'\nThe answer is {x * y}')
    if selec == 3:
        print(f'\nThe answer is {x / y}')
    if selec == 4:
        print(f'\nThe answer is {math.sqrt(x)}')



def addition():
    formatEquation()
    basicEquation()
    answer()
    welcome()
def subtraction():
    formatEquation()
    basicEquation()
    answer()
    welcome()
def multiplication():
    formatEquation()
    basicEquation()
    answer()
    welcome()
def division():
    formatEquation()
    basicEquation()
    answer()
    welcome()
def sqrt():
    formatEquation()
    basicEquation()
    answer()
    welcome()


def welcome():
    print()
    print('Type the corresponding number in the category to select',
          'what calucation you want to do today.\n')
    print('Number\tCalculation')
    print('===================')
    print('0\tAddition')
    print('1\tSubtraction')
    print('2\tMultiplication')
    print('3\tDivision')
    print('4\tSquare Root')
    print('Number: ', end='')
    inp = int(input())
    user_input(inp)

def user_input(inp):
    global selec
    if inp < 0:
        print(f"\n{inp} isn't a valid option.")
        welcome()
    elif inp >= 5:
        print(f"\n{inp} isn't a valid option.")
        welcome()
    else:
        selec = inp
        selection(inp)
welcome()
    
