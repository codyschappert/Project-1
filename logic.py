from votemenugui import *
from PyQt6.QtWidgets import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def vote_menu():

    #Displays vote menu and gets lowered and stripped input
        print('-'*35)
        print('VOTE MENU')
        print('-'*35)
        print('v: Vote')
        print('x: Exit')
        option = input('Option: ').strip().lower()

    # Returns user's choice
        if option == 'v' or option == 'x':
            return option

    # Logical check to ensure 'v' or 'x' is entered
        else:
            while option != 'x' and option != 'v':
                option = input('Invalid (v/x): ').strip().lower()
                if option == 'v' or option == 'x':
                    return option



    def candidate_menu():

    # Displays candidate menu and gets lowered and stripped input
        print('-' * 35)
        print('CANDIDATE MENU')
        print('-' * 35)
        print('1: John')
        print('2: Jane')
        candidate  = input('Candidate: ').strip().lower()

    # Checks to see which candidate was measured and returns the user's input as a string
        if int(candidate) == 1:
            print('Voted John')
            return candidate
        elif int(candidate) == 2:
            print('Voted Jane')
            return candidate

    # Logical check to ensure '1' or '2' is entered
        else:
            while candidate != 1 and candidate != 2:
                candidate = input('Invalid (1/2): ').strip().lower()
                if int(candidate) == 1:
                    print('Voted John')
                    return candidate
                elif int(candidate) == 2:
                    print('Voted Jane')
                    return candidate
    def main():

    # Declares values for vote counts and runs first iteration
        john = 0
        jane = 0
        option = vote_menu()

    # Loops through menus and iterates vote counts until user exits
        while option != 'x':
            if option == 'v':
                candidate = candidate_menu()

                # Iterates the candidate's votes by checking the string input from candidate_menu()
                if int(candidate) == 1:
                    john += 1
                elif int(candidate) == 2:
                    jane += 1
            option = vote_menu()

    # Displays vote counts when user exits
        if option == 'x':
            print('-' * 35)
            print(f'John - {john}, Jane - {jane}, Total - {john + jane}')
            print('-' * 35)

    main()