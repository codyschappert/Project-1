from badidgui import Ui_Dialog
from votemenugui import *
from PyQt6.QtWidgets import *
from alreadyvotederrorgui import *

ID_list = []

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vote_button.clicked.connect(lambda: self.submit())
        self.error_label.setText(' ')
        self.error = Error()

    def submit(self):
        user_id = self.ID_input.text()
        if self.confirm_id(user_id):
            print(ID_list)
        elif not self.confirm_id(user_id):
            pass

    def confirm_id(self, id_num) -> bool | None:
        try:
            id_num = int(id_num)
            if id_num not in ID_list:
                ID_list.append(id_num)
                return True
            elif id_num in ID_list:
                raise TypeError("Invalid ID")
        except ValueError:
            self.error_label.setText('Please enter a valid numerical ID.')
            self.error.show()
        except TypeError:
            self.error.show()
            self.error_label.setText('This ID already has a registered vote.')
            self.ID_input.clear()

class Error(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.close_error.clicked.connect(lambda: self.close_popup())

    def close_popup(self):
        self.error.hide()

