"""
Note on nested while statements:

cnt = 0
while True:
    print('hello')    
    cnt += 1
    if cnt == 3: break

#the break statement will get us out of the while loop when cnt == 5

cnt = 0
while True:
    print('hello')
    cnt += 1
    if cnt == 3: break

    sec_cnt = 0
    while True:
        print('goodbye')
        sec_cnt += 1
        if sec_cnt == 2: break
    

# see if you ca figure out what this will print out before you run the code





Menu System Example
-------------------

Goal:
    Build a menu-driven system with hierarchical screens.

Structure:
    The root menu (s0) has two choices:
        - s00
            - s000
            - s001
        - s01
            - s010
            - s011

Navigation rules:
    - The user selects options by entering numbers.
    - Pressing <return> (empty input) means "go back":
        * From a submenu -> return to the parent menu
        * From the root menu -> exit the program
"""

def display_menu(items):
    """
    Display a numbered menu and return the user’s choice.

    Parameters:
        items (list of str): A list of choices to show.

    Returns:
        int   -> The index (1-based) of the chosen item
        None  -> If the user pressed <return> to go back
    """
    # Print out menu options in numbered form
    for idx, item in enumerate(items, start=1):
        print(f"{idx}) {item}")

    print("\n")  # add some spacing

    txt = "Please enter your choice (<return> to go back): "
    while True:
        choice = input(txt)

        # If the user presses return (''), choice is empty -> return None
        if not choice:
            return None

        # Try to convert the input to an integer
        try:
            choice = int(choice)
        except ValueError:
            # User didn’t enter a number
            txt = "Enter an integer: "
        else:
            # Check if number is within menu range
            if choice < 1 or choice > len(items):
                txt = f"Enter an integer between 1 and {len(items)}: "
            else:
                # Return a valid choice
                return choice


def simple():
    """
    A simple example:
    Just show the root menu once and print the result.
    """
    items = ['go to s00', 'go to s01']
    choice = display_menu(items)
    print("You selected:", choice)


def second_level():
    """
    Main program:
    Implements the nested menu navigation system with 'go back' logic.
    """
    while True:
        # Top-level menu s0
        items = ['go to s00', 'go to s01']
        choice = display_menu(items)

        # If user pressed return at top level -> exit the program
        if not choice:
            exit()

        # If user selected "s00"
        elif choice == 1:
            while True:
                items = ['go to s000', 'go to s001']
                choice = display_menu(items)

                # Return -> go back to top-level
                if not choice:
                    break

                elif choice == 1:
                    # Stay in s000 until return is pressed
                    while True:
                        print("output for s000")
                        choice = input("Enter <return> to go back: ")
                        if not choice:  # return pressed, break out of this loop
                            break

                elif choice == 2:
                    # Stay in s001 until return is pressed
                    while True:
                        print("output for s001")
                        choice = input("Enter <return> to go back: ")
                        if not choice: # return pressed, break out of this loop
                            break

                else:
                    print("FATAL ERROR: Invalid state in s00 menu")

        # If user selected "s01"
        elif choice == 2:
            while True:
                items = ['go to s010', 'go to s011']
                choice = display_menu(items)

                # Return -> go back to top-level
                if not choice:
                    break

                elif choice == 1:
                     # Stay in s010 until return is pressed
                    while True:
                        print("output for s010")
                        choice = input("Enter <return> to go back: ")
                        if not choice:
                            break

                elif choice == 2:
                    # Stay in s011 until return is pressed
                    while True:
                        print("output for s011")
                        choice = input("Enter <return> to go back: ")
                        if not choice:
                            break

                else:
                    print("FATAL ERROR: Invalid state in s01 menu")


# Run demos
# simple()
#second_level()


cnt = 0
while True:
    print('hello')
    cnt += 1
    if cnt == 3: break

    sec_cnt = 0
    while True:
        print('goodbye')
        sec_cnt += 1
        if sec_cnt == 2: break
