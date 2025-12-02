from badidgui import *
from votemenugui import *
from votesubmittedgui import *
from nocandidategui import *
from PyQt6.QtWidgets import *
from alreadyvotederrorgui import *

ID_list = []

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.submit())
        self.bad_id = BadID()
        self.already_voted = AlreadyVoted()

    def submit(self):
        user_id = self.ID_input.text()
        if self.vote_john.isChecked():
            vote = 'John'
        elif self.vote_jane.isChecked():
            vote = 'Jane'
        else:
            raise TypeError("No candidate")
        try:
            id_num = int(user_id)
            if id_num not in ID_list:
                ID_list.append(id_num)
            elif id_num in ID_list:
                raise TypeError("Invalid ID")
        except ValueError:
            self.bad_id.show()
        except TypeError("Invalid ID"):
            self.already_voted.show()
            self.ID_input.clear()
        except TypeError("No candidate"):
            pass
class BadID(QDialog, BadID):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())

    def close_popup(self):
        self.close()

class AlreadyVoted(QDialog, AlreadyVoted):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())

    def close_popup(self):
        self.close()

class VoteSubmitted(QDialog, VoteSubmitted):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close_popup(self):
        self.close()

class NoCandidate(QDialog, NoCandidate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close_popup(self):
        self.close()