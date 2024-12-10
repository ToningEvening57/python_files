import sys

system_data = []
print()
print(f'Welcome to my cool list program!')

def your_list():
    print()
    print('This is your cool list ==', system_data)
    print()


def system_input():
    for bruh in input().split():
        system_data.append(bruh)
    menu()

def system_delete():
    for bruh2 in system_data:
        for bruh in input().split():
            if bruh2 == bruh:
                system_data.remove(bruh)
            else:
                print()
                print(f"You don't have {bruh} in your list")
            menu()

def user_select(selection):
    if selection < 0:
        print()
        print(f"{selection} isn't an option")
        menu()
    if selection > 2:
        print()
        print(f"{selection} isn't an option")
        menu()
    if selection == 0:
        sys.exit('Thank you for using my program! Goodbye!')
    if selection == 1:
        system_input()
    if selection == 2:
        system_delete()

def selection_menu():
    print('Select which option you want to do today.')
    print('================')
    print('0: Quit')
    print('1: Edit your list')
    print('2: Delete something in your list')
def menu():
    your_list()
    selection_menu()
    user_input = int(input('Input Number: '))
    user_select(user_input)
    

menu()
print(system_data)


