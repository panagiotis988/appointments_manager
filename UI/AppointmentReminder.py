import tkinter as tk
from Controllers.AppointmentController import *
from Helpers.CalendarFormatter import *
import Helpers.EmailNotifications as EmailNotifications

class AppointmentReminder(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.config(bg="white")

        self.appointmentController = AppointmentController()
        self.controller = controller

        tk.Label(self, text="Αποστολή Υπενθύμισης σε Πελάτη", font=("Lucida", "16", "bold"),
                 fg='#335BA3', bg='white').grid(row=0, column=1,pady=10)
        date_today = datetime.now()

        self.date = MyCalendar(self, allowed_weekdays=(
            calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY),
                               weekendbackground='red', weekendforeground='red',
                               othermonthbackground='gray95', othermonthwebackground='gray95',
                               othermonthforeground='black', othermonthweforeground='black',
                               font="Lucida 10", selectmode='day',
                               cursor="hand1", date_pattern='yyyy-mm-dd',
                               selectforeground='green',mindate=date_today,locale='el')
        self.date.grid(row=3, column=1)

        self.date_label = tk.Label(self, text="Επιλογή Ημέρας", font=("Lucida", "12", "bold"), fg='#335BA3',
                                   bg='#C0C0C0').grid(row=3, column=0, pady=10)

        tk.Button(self, text="<<Επιστροφή στο Αρχικό Μενού", font=("Lucida", "10", "bold"),
            fg='white', bg='#335BA3',command=lambda: (controller.show_frame("Menu"),
                                    self._delete_entry())).grid(row=1, column=1, pady=10)
        self.label_comment = tk.Label(self, text="""Επιλέγοντας την ημέρα στο ημερολόγιο, θα σταλεί αυτόματη ειδοποίηση
        υπενθύμισης σε όλους τους πελάτες που έχουν ραντεβού την ημέρα εκείνη""",
                                 font=("Lucida", "10", "italic"), fg='#335BA3', bg='white').grid(row=2, column=1,
                                                                                                 pady=(0,10))
        tk.Button(self, text="Αποστολή ειδοποίησης", font=("Lucida", "10","bold"), fg='#335BA3', bg='#DAE3F3',
                  command=lambda: (self.notify())).grid(row=11, column=1, pady=(10,10))

    def notify(self):
        appointments = self.appointmentController.getAllAppointmentsByDay(self.date.get_date())

        EmailNotifications.EmailNotifications.sendEmail(appointments, 'Υπενθύμιση ραντεβού', 'EmailNotification')

        messagebox.showinfo("Επιτυχής αποστολή email.", "'Ολες οι ειδοποιήσεις στάλθηκαν με επιτυχία.")

    def _delete_entry(self):
        self.date.selection_set(datetime.today())
