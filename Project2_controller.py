from PyQt5.QtWidgets import *
from project2_view import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_mainWindow):
    """
    Class representing controls for hangman game.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor to create initial state of hangman game.
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.blank_word = []
        self.wrong_guesses = []
        self.chances = 7
        self.word = ''

        with open('wordlist', 'r') as f:
            words = f.readlines()
        self.word = random.choice(words)[:-1]

        self.pushButton_word.clicked.connect(lambda: self.word_setup())  # enables new word button to function
        self.pushButton_submit.clicked.connect(lambda: self.set_guess())
        self.label_instructions.setText("Click New Word to Start Game")
        self.pushButton_submit.setEnabled(False)

    def word_setup(self):
        """
        Method to set up blank word for hangman game.
        :return: None
        """
        self.blank_word.clear()
        self.wrong_guesses.clear()
        self.label_instructions.setText("")
        self.chances = 7
        self.pushButton_submit.setEnabled(True)
        self.label_head.setVisible(False)
        self.label_face.setVisible(False)
        self.label_rightarm.setVisible(False)
        self.label_rightleg.setVisible(False)
        self.label_leftarm.setVisible(False)
        self.label_leftleg.setVisible(False)
        self.line_body.setVisible(False)

        with open('wordlist', 'r') as f:
            words = f.readlines()
        self.word = random.choice(words)[:-1]
        for char in self.word:
            self.blank_word.append("_")
        self.label_word.setText(' '.join(self.blank_word))  # str of dashes with spaces in-between
        self.textEdit_chances.setText('')
        self.textEdit_wrong_guesses.setText('')

    def set_guess(self):
        """
        Method to analyze user's guess and update word, chances, incorrect guesses, and hangman figure.
        :return:
        """
        guess = self.lineEdit_guess.text()
        found_guess = False
        print(guess)

        for i, letter in enumerate(self.word):
            if guess == letter:
                self.blank_word[i] = guess
                found_guess = True
            if "_" not in self.blank_word:
                self.label_instructions.setText("YOU WIN! PLAY AGAIN")
                self.pushButton_submit.setEnabled(False)

        if found_guess == False:
            self.chances -= 1

            if self.chances == 6:
                self.label_head.setVisible(True)
            if self.chances == 5:
                self.line_body.setVisible(True)
            if self.chances == 4:
                self.label_rightarm.setVisible(True)
            if self.chances == 3:
                self.label_leftarm.setVisible(True)
            if self.chances == 2:
                self.label_rightleg.setVisible(True)
            if self.chances == 1:
                self.label_leftleg.setVisible(True)

            if self.chances == 0:
                self.label_face.setVisible(True)
                self.label_instructions.setText("YOU LOSE! PLAY AGAIN")
                self.pushButton_submit.setEnabled(False)
            if guess in self.wrong_guesses:
                self.label_instructions.setText("Already used letter, guess a new one")
                self.lineEdit_guess.setText('')
            else:
                self.wrong_guesses.append(guess)

        print(self.word)
        print(self.blank_word)

        self.label_word.setText(str(' '.join(self.blank_word)))  # str of dashes and letters

        self.textEdit_chances.setText(f'{self.chances} / 7')  # integer / 7
        self.textEdit_wrong_guesses.setText(' '.join(self.wrong_guesses))  # str of letters
        self.lineEdit_guess.setText('')
