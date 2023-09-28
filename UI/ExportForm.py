import tkinter as tk
from Controllers.CustomerController import *
from Controllers.AppointmentController import *
from Helpers.CalendarFormatter import *
from Validators.ValidateExport import *

class ExportForm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.config(bg="white")

        self.CustomerController = CustomerController()
        self.AppointmentController = AppointmentController()
        self.ValidateExport = ValidateExport()
        self.controller = controller

        tk.Label(self, text="Εξαγωγή Ραντεβού", font=("Lucida", "16", "bold"),
                 fg='#335BA3', bg='white').grid(row=0, column=1, columnspan=2, pady=(10, 10))

        self.date = MyCalendar(self, allowed_weekdays=(
            calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY),
                               weekendbackground='red', weekendforeground='red',
                               othermonthbackground='gray95', othermonthwebackground='gray95',
                               othermonthforeground='black', othermonthweforeground='black',
                               font="Lusida", selectmode='day',
                               cursor="hand1", date_pattern='yyyy-mm-dd',
                               selectforeground='green', locale='el')

        self.date.grid(row=3, column=1, columnspan=2)
        self.date_label = tk.Label(self, text="Επιλογή Ημέρας", font=("Lucida", "12", "bold"), fg='#335BA3',
                                   bg='#C0C0C0').grid(row=3, column=0, padx=5)

        tk.Button(self, text="<<Επιστροφή στο Αρχικό Μενού", font=("Lucida", "10", "bold"), fg='white', bg='#335BA3',
                  command=lambda: (controller.show_frame("Menu"), self.date.selection_set(datetime.today()))).grid(
            row=1, column=1,
            padx=(10, 0), pady=(0, 10))
        self.label_comment = tk.Label(self, text="""Επιλέγοντας την ημέρα στο ημερολόγιο, μπορείτε να εξάγετε
        σε αρχείο Excel τα στοιχεία των ραντεβού της ημέρας εκείνης""",
                                      font=("Lucida", "10", "italic"), fg='#335BA3', bg='white').grid(row=2, column=1,
                                                                                                      pady=(0, 10))
        self.xlsx_button = tk.Button(self, text="Εξαγωγή σε αρχείο Excel", font=("Lucida", "10",
                                                                                 "bold"), fg='#335BA3', bg='#DAE3F3',
                                     command=lambda: (self.export_xlsx()))
        self.xlsx_button.grid(row=10, column=1, pady=(10, 0))

    def export_xlsx(self):
        exists = self.ValidateExport.validate_date(self.date.get_date())

        if exists is not None:
            self.AppointmentController.export_xlsx(self.date.get_date())
        else:
            messagebox.showerror("Κάτι πήγε λάθος.",
                                 "Η μέρα που επέλεξες δεν έχει ραντεβού.Επέλεξε μια νέα μέρα και προσπάθησε ξανά.")
