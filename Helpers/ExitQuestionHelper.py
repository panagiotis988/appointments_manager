from sys import exit
from tkinter import messagebox


class ExitQuestionHelper:
    @staticmethod
    def on_close():
        if messagebox.askokcancel("Εξοδος", "Είστε σίγουρος;"):
            exit()
