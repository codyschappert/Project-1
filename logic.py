from gui import *
from PyQt6.QtWidgets import *
import csv

user_votes = {}
csv_file = 'votes.csv'

def load_previous_votes() -> None:
    """Loads previously submitted votes from csv file into user_votes dictionary."""
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue
                elif row[0].startswith('Total'):
                    continue
                else:
                    try:
                        user_id = int(row[0])
                        user_votes[user_id] = row[1]
                    except ValueError:
                        pass

    except FileNotFoundError:
        pass # No file means no previous votes which is fine

def save_votes() -> None:
    """Saves all votes and user ID's from user_votes dictionary into csv file. """
    john_count = 0
    jane_count = 0

    for vote in user_votes.values():
        if vote == 'John':
            john_count += 1
        elif vote == 'Jane':
            jane_count += 1

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        for user_id, vote in user_votes.items():
            writer.writerow([user_id, vote])

        writer.writerow([]) # Blank row separator for total counts

        writer.writerow(["Total for John", john_count])
        writer.writerow(["Total for Jane", jane_count])


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self: Logic) -> None:
        """Initializes the main window."""
        super().__init__()
        self.setupUi(self)

        load_previous_votes()

        self.vote_button.clicked.connect(lambda: self.submit())
        self.bad_id = BadID()
        self.already_voted = AlreadyVoted()
        self.no_candidate = NoCandidate()
        self.voted = VoteSubmitted()

    def submit(self: Logic) -> None:
        """Checks for numerical ID and adds the user's ID and vote to the user_votes dictionary."""
        user_id = self.ID_input.text().strip()

        try:
            if self.vote_john.isChecked():
                vote = 'John'
            elif self.vote_jane.isChecked():
                vote = 'Jane'
            else:
                raise KeyError

            id_num = int(user_id)
            if id_num not in user_votes:
                user_votes[id_num] = vote
                save_votes()
            else:
                raise TypeError

            self.voted.show()
            self.reset_window()

        except ValueError:
            self.bad_id.show()

        except TypeError:
            self.already_voted.show()
            self.ID_input.clear()

        except KeyError:
            self.no_candidate.show()

    def reset_window(self: Logic) -> None:
        self.ID_input.clear()

        self.vote_john.setAutoExclusive(False)
        self.vote_jane.setAutoExclusive(False)

        self.vote_john.setChecked(False)
        self.vote_jane.setChecked(False)

        self.vote_john.setAutoExclusive(True)
        self.vote_jane.setAutoExclusive(True)

class BadID(QDialog, Ui_BadID):
    def __init__(self: BadID) -> None:
        """Initializes the 'Bad ID' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close())

class AlreadyVoted(QDialog, Ui_AlreadyVoted):
    def __init__(self: AlreadyVoted) -> None:
        """Initializes the 'Already Voted' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close())

class VoteSubmitted(QDialog, Ui_VoteSubmitted):
    def __init__(self: VoteSubmitted) -> None:
        """Initializes the 'Vote submitted' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close())

class NoCandidate(QDialog, Ui_NoCandidate):
    def __init__(self: NoCandidate) -> None:
        """Initializes the 'No Candidate' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close())
