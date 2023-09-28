import tkinter as tk
from Controllers.CustomerController import *
from Controllers.AppointmentController import *
from Helpers.CalendarFormatter import *
from Validators.ValidateRegisterForm import *
from datetime import datetime


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.customerController = CustomerController()
        self.appointmentController = AppointmentController()
        self.controller = controller
        self.validateRegister = ValidateRegisterForm()
        self.config(bg="white")

        self.option_menu_init = tk.StringVar(value='Eπέλεξε ραντεβού')
        self.duration_time_init = tk.StringVar(value="20")
        self.duration_time = [10, 20, 30, 40, 50, 60]

        self.start_time_value = []

        tk.Label(self, text="Εισαγωγή Νέας Εγγραφής", font=("Lucida", "16", "bold"),
                 fg='#335BA3', bg='white').grid(row=0, column=1, pady=10)

        self.fname = tk.Entry(self, width=30)
        self.fname.grid(row=2, column=1)
        self.fname.config(validate='focusout',
                          validatecommand=(self.register(self.on_valid), '%P', 'firstname'),
                          invalidcommand=(self.register(self.on_invalid), 'firstname'))
        self.lname = tk.Entry(self, width=30)
        self.lname.grid(row=3, column=1)
        self.lname.config(validate='focusout', validatecommand=(self.register(self.on_valid), '%P', 'lastname'),
                          invalidcommand=(self.register(self.on_invalid), 'lastname'))
        self.mobile = tk.Entry(self, width=30)
        self.mobile.grid(row=4, column=1)
        self.mobile.config(validate='focusout', validatecommand=(self.register(self.on_valid), '%P', 'mobile'),
                           invalidcommand=(self.register(self.on_invalid), 'mobile'))
        self.city = tk.Entry(self, width=30)
        self.city.grid(row=5, column=1)
        self.city.config(validate='focusout', validatecommand=(self.register(self.on_valid), '%P', 'city'),
                         invalidcommand=(self.register(self.on_invalid), 'city'))
        self.email = tk.Entry(self, width=30)
        self.email.grid(row=6, column=1)
        self.email.config(validate='focusout', validatecommand=(self.register(self.on_valid), '%P', 'email'),
                          invalidcommand=(self.register(self.on_invalid), 'email'))
        date_today = datetime.now()
        self.date = MyCalendar(self, allowed_weekdays=(
            calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY),
                               weekendbackground='red', weekendforeground='red',
                               othermonthbackground='gray95', othermonthwebackground='gray95',
                               othermonthforeground='black', othermonthweforeground='black',
                               font="Lucida 10", selectmode='day',
                               cursor="hand1", date_pattern='yyyy-mm-dd',
                               selectforeground='green', mindate=date_today, locale='el')
        self.date.bind("<<CalendarSelected>>", self.clear_dropdowns)
        self.date.grid(row=7, column=1)

        self.duration = tk.OptionMenu(self, self.duration_time_init, *self.duration_time)
        self.duration.config(font=("Lucida", "10",
                                   "bold"), fg='white', bg='#335BA3')
        self.duration.grid(row=8, column=1, sticky="news")
        self.duration.bind('<Button-1>', self.reset_dropdown_time_range)

        self.start_time = tk.OptionMenu(self, self.option_menu_init, self.start_time_value)
        self.start_time.config(font=("Lucida", "10",
                                     "bold"), fg='white', bg='#335BA3')
        self.start_time.grid(row=9, column=1, sticky='news')
        self.start_time['direction'] = 'flush'
        self.start_time.bind('<Button-1>', self._callback)

        self.fname_label = tk.Label(self, text="Όνομα", font=("Lucida", "10", "bold"), fg='#335BA3',
                                    bg='white').grid(row=2, column=0, padx=5, pady=5)
        self.lastName_label = tk.Label(self, text="Επώνυμο", font=("Lucida", "10", "bold"), fg='#335BA3',
                                       bg='white').grid(row=3, column=0, padx=5, pady=5)
        self.mobile_label = tk.Label(self, text="Κινητό", font=("Lucida", "10", "bold"), fg='#335BA3',
                                     bg='white').grid(row=4, column=0, padx=5, pady=5)
        self.city_label = tk.Label(self, text="Πόλη", font=("Lucida", "10", "bold"), fg='#335BA3',
                                   bg='white').grid(row=5, column=0, padx=5, pady=5)
        self.email_label = tk.Label(self, text="e-mail", font=("Lucida", "10", "bold"), fg='#335BA3',
                                    bg='white').grid(row=6, column=0, padx=5, pady=5)
        self.date_label = tk.Label(self, text="Ημερομηνία", font=("Lucida", "10", "bold"), fg='#335BA3',
                                   bg='white').grid(row=7, column=0, padx=5, pady=5)
        self.duration_label = tk.Label(self, text="Διάρκεια ραντεβού", font=("Lucida", "10", "bold"), fg='#335BA3',
                                       bg='white').grid(row=8, column=0, padx=5, pady=5)
        self.start_time_label = tk.Label(self, text="Ώρα έναρξης", font=("Lucida", "10", "bold"), fg='#335BA3',
                                         bg='white').grid(row=9, column=0, padx=5, pady=5)

        tk.Button(self, text="<<Επιστροφή στο Αρχικό Μενού", font=("Lucida", "10",
                                                                   "bold"), fg='white', bg='#335BA3',
                  command=lambda: (controller.show_frame("Menu"), self._delete_entry())).grid(row=1, column=1)
        self.submit_button = tk.Button(self, text="Αποθήκευση", state='normal', font=("Lucida", "10",
                                                                                      "bold"), fg='#335BA3',
                                       bg='#DAE3F3', command=lambda: (self.submit()))
        self.submit_button.grid(row=10, column=1, pady=(10, 10))

        self.label_error = tk.Label(self, foreground='red')
        self.success = tk.Label(self, foreground='green')
        self.label_error.grid(row=7, column=3, sticky=tk.W, padx=5)
        self.success.grid(row=7, column=3, sticky=tk.W, padx=5)

    def _callback(self, event):
        dropdownValidation = self.validateRegister.validate_form(self.fname.get(), self.lname.get(),
                                                                 self.mobile.get(),
                                                                 self.city.get(),
                                                                 self.email.get())

        if dropdownValidation['status'] is False:
            self.on_invalid(dropdownValidation['error_field'])

        self.submit_button.config(state='normal')
        self.label_error['text'] = ''
        self.start_time['menu'].delete(0, 'end')
        self.duration['menu'].delete(0, 'end')
        drop_down = self.appointmentController.dropdown_generator(self.date.get_date(),
                                                                  int(self.duration_time_init.get()))
        for opt in self.duration_time:
            self.duration['menu'].add_command(label=opt, command=tk._setit(self.duration_time_init, opt))
        for opt in drop_down:
            self.start_time['menu'].add_command(label=opt, command=tk._setit(self.option_menu_init, opt))

    def submit(self):
        formValidation = self.validateRegister.validate_form(self.fname.get(), self.lname.get(), self.mobile.get(),
                                                             self.city.get(),
                                                             self.email.get(),
                                                             self.option_menu_init.get())

        if formValidation['status']:
            customerId = self.customerController.create_customer(self.fname.get(), self.lname.get(), self.mobile.get(),
                                                                 self.city.get(),
                                                                 self.email.get())
            self.appointmentController.create_appointment(customerId, self.date.get_date(), self.option_menu_init.get(),
                                                          self.duration_time_init.get())
            self.success['text'] = 'Επιτυχημένη εγγραφή πελάτη.'
            self._delete_entry()
            self.clear_dropdowns(self)
        else:
            self.on_invalid(formValidation['error_field'])

    def _delete_entry(self):
        self.fname.delete(0, "end")
        self.lname.delete(0, "end")
        self.mobile.delete(0, "end")
        self.city.delete(0, "end")
        self.email.delete(0, "end")
        self.date.selection_set(datetime.today())
        self.option_menu_init.set(value='Eπέλεξε ραντεβού')
        self.duration_time_init.set("20")

    def clear_dropdowns(self, event):
        self.option_menu_init.set(value='Eπέλεξε ραντεβού')
        self.duration_time_init.set("20")

    def on_invalid(self, type):
        self.success['text'] = ''
        self.submit_button.config(state='disabled')
        if type == 'firstname':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο όνομα'
            self.fname['foreground'] = 'red'
        if type == 'lastname':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο επίθετο'
            self.lname['foreground'] = 'red'
        if type == 'mobile':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο αριθμό τηλεφώνου'
            self.mobile['foreground'] = 'red'
        if type == 'city':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο όνομα πόλης'
            self.city['foreground'] = 'red'
        if type == 'email':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο email'
            self.email['foreground'] = 'red'
        if type == 'start_time':
            self.label_error['text'] = 'Παρακαλώ επιλέξτε ώρα ραντεβού'

    def on_valid(self, value, type):
        self.success['text'] = ''
        self.label_error['text'] = ''
        self.submit_button.config(state='normal')

        if type == 'firstname':
            output = self.validateRegister.validate_string_input(value)
            if output:
                self.fname['foreground'] = 'black'
                return True
            else:
                return False
        if type == 'lastname':
            output = self.validateRegister.validate_string_input(value)
            if output:
                self.lname['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'mobile':
            output = self.validateRegister.validate_mobile(value)
            if output:
                self.mobile['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'city':
            output = self.validateRegister.validate_string_input(value)
            if output:
                self.city['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'email':
            output = self.validateRegister.validate_email(value)
            if output or output == '':
                self.email['foreground'] = 'black'
                return True
            else:
                return False

    def reset_dropdown_time_range(self, event):
        self.option_menu_init.set(value='Eπέλεξε ραντεβού')

    def validate_dropdown(self):
        if self.option_menu_init.get() != 'Eπέλεξε ραντεβού':
            self.submit()
        else:
            self.label_error['text'] = 'Επέλεξε σωστή ημερομηνία'
