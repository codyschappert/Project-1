from badidgui import *
from votemenugui import *
from votesubmittedgui import *
from nocandidategui import *
from PyQt6.QtWidgets import *
from alreadyvotederrorgui import Already_Voted

user_votes = {}

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Initializes the main window."""
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.submit())
        self.bad_id = BadID()
        self.already_voted = AlreadyVoted()
        self.no_candidate = NoCandidate()
        self.voted = VoteSubmitted()

    def submit(self) -> None:
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
            elif id_num in user_votes:
                raise TypeError

            self.voted.show()

        except ValueError:
            self.bad_id.show()

        except TypeError:
            self.already_voted.show()
            self.ID_input.clear()

        except KeyError:
            self.no_candidate.show()


class Popup(QDialog):
    def close_popup(self) -> None:
        """Inherited class method for closing the popup."""
        self.close()

class BadID(QDialog, BadID, Popup):
    def __init__(self) -> None:
        """Initializes the 'Bad ID' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())


class AlreadyVoted(QDialog, Already_Voted, Popup):
    def __init__(self):
        """Initializes the 'Already Voted' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())

class VoteSubmitted(QDialog, VoteSubmitted, Popup):
    def __init__(self) -> None:
        """Initializes the 'Vote submitted' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close_popup())

class NoCandidate(QDialog, NoCandidate, Popup):
    def __init__(self) -> None:
        """Initializes the 'No Candidate' pop up."""
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())
