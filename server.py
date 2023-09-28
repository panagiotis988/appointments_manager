import tkinter as tk
from tkinter import font as tkfont
import UI.Register as Register
import UI.Menu as Menu
import UI.AppointmentAppearance as AppointmentAppearance
import UI.ExportForm as ExportForm
import UI.CustomerDisplay as CustomerDisplay
import UI.AppointmentReminder as AppointmentReminder
from Helpers.ExitQuestionHelper import ExitQuestionHelper
from Migrations.TableCreation import sql_table
from database import conDatabase


class server(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        sql_table(conDatabase)

        self.attributes("-fullscreen", True)
        self.bind("<F11>", lambda event: self.attributes("-fullscreen",
                                                         not self.attributes("-fullscreen")))
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))

        container = tk.Frame(self)
        container.pack(padx=10, pady=20,expand=True)

        self.frames = {
            "Register": Register.Register(parent=container, controller=self),
            "Menu": Menu.Menu(parent=container, controller=self),
            "AppointmentAppearance": AppointmentAppearance.AppointmentAppearance(parent=container, controller=self),
            "ExportAppointments": ExportForm.ExportForm(parent=container, controller=self),
            "CustomerDisplay": CustomerDisplay.CustomerDisplay(parent=container, controller=self),
            "AppointmentReminder": AppointmentReminder.AppointmentReminder(parent=container, controller=self)
        }

        self.frames["Menu"].grid(row=0, column=0, sticky="nsew")
        self.frames["Register"].grid(row=0, column=0, sticky="nsew")
        self.frames["AppointmentAppearance"].grid(row=0, column=0, sticky="nsew")
        self.frames["CustomerDisplay"].grid(row=0, column=0, sticky="nsew")
        self.frames["ExportAppointments"].grid(row=0, column=0, sticky="nsew")
        self.frames["AppointmentReminder"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = server()
    app.title("Appointment Management")
    app.protocol("WM_DELETE_WINDOW", ExitQuestionHelper.on_close)
    app.mainloop()
