'''
our goal is to create a menu driven system

screen s0 has two options s00 and so1, each of these screens
has two options s000, s001 for s00 and s010, s011 for s01



                                 s0

                    s00                              s01

            s000         s001               s010          s011

we want to go to the right choice, unless the user enters return instead of selecting
a valid choice. In that case we want to go to the previous menu. Unless we are in the 
top screen , s0, and then we want to exit the program.

Let's start by first defining display_menu(items) where the input parameter items
is a list of valid choices
'''


def display_menu(items):
    # print out the menu
    for idx, item in enumerate(items, start = 1):
        print(f'{idx}) {item}')

    print('\n\n')

    txt = "Please enter your choice (ret to go back): "
    while True:
        # get raw input, trapping for return
        choice = input(txt)

        #if return is entered, '' is returned, which is False. So, not choice is True when choice is False
        # when choice is False we return None
        if not choice: return None
        
        #try except block trying top convert text to int
        try:
            choice = int(choice)
        except ValueError:
            txt = 'Enter an integer: '
        else:
            if choice < 1 or choice > len(items):
                txt = f'Enter an integer between 1 and {len(items)}: '
            else:
                return choice
#Notice that we either return None or we return a valid choice.
# return statements break us out of the function.


def simple():
    items = ['go to s00', 'go to s01']
    choice = display_menu(items)
    print(choice)

simple()

def second_level():
   
    while True:
        items = ['go to s00', 'go to s01']
        choice = display_menu(items)
        
        #if we are on the top menu and user hits return we exit the program
        if not choice: exit()

        # if choice selected from s0 is 1 we want to display menu with s000 and s001
        elif choice == 1:            
            while True:
                items = ['go to s000', 'go to s001']
                choice = display_menu(items)

                # if the user entered return ('') we break out of this while loop
                # and go back to the top while loop
                if not choice: break 

                elif choice == 1:

                    # user entered 1 we keep printing till user enters return
                    while True:
                        print("output for s000")
                        choice = input('Enter return to go back: ')                      
                        
                        # if return entered ('') we break out of this while loop and go to the 
                        # previous while loop.
                        if not choice: break 
                
                elif choice == 2:

                    # user entered 2 we keep printing till user enters return
                    while True:
                        print("output for s001")
                        choice = input('Enter return to go back: ')    

                        # if return entered ('') we break out of this while loop and go to the 
                        # previous while loop.
                        if not choice: break 
                
                        
                else:
                    print('FATAL ERROR: We should never get here 0')


        # if choice selected from s0 is 2 we want to display menu with s010 and s011
        elif choice == 2:
            
            while True:
                items = ['go to s010', 'go to s011']
                choice = display_menu(items)

                # if the user entered return ('') we break out of this while loop
                # and go back to the top while loop
                if not choice: break 

                elif choice == 1:
                    
                    while True:
                        print("output for s010")
                        choice = input('Enter return to go back: ')                      

                        if not choice: break 

                elif choice == 2:
                    
                    while True:
                        print("output for s011")
                        choice = input('Enter return to go back: ')    

                        if not choice: break                 
                        
                else:
                    print('FATAL ERROR: We should never get here 0')

second_level()