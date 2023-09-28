import tkinter as tk
from Controllers.CustomerController import *
from Validators.ValidateUpdateCustomerForm import *


class UpdateCustomerForm:

    def create_popup(self, customerId, customerFirstName, customerLastName, customerMobile, customerCity,
                     customerEmail):
        top = tk.Toplevel()
        top.geometry("800x300")
        top.title("Τροποποίηση Πελάτη")
        top.configure(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.customerController = CustomerController()
        self.validator = ValidateUpdateCustomerForm()

        self.title = tk.Label(top, text="Τροποποίηση Στοιχείων Πελάτη", font=("Lucida", "16", "bold"),
                              fg='#335BA3', bg='white').grid(row=0, column=1, columnspan=3, pady=10)
        self.label_comment = tk.Label(top, text="Αφού πραγματοποιήσετε τις αλλαγές στα πεδία πατήστε 'Αποθήκευση'",
                                      font=("Lucida", "10", "italic"), fg='#335BA3', bg='white').grid(row=2,
                                                                                                      column=1,
                                                                                                      columnspan=3,
                                                                                                      pady=10)

        self.fname = tk.Entry(top, width=15)
        self.fname.insert(0, customerFirstName)
        self.fname.grid(row=4, column=0, sticky="w", padx=3)
        self.fname.config(validate='focusout',
                          validatecommand=(top.register(self.on_valid), '%P', 'firstname'),
                          invalidcommand=(top.register(self.on_invalid), 'firstname'))
        self.lname = tk.Entry(top, width=18)
        self.lname.insert(0, customerLastName)
        self.lname.grid(row=4, column=1, sticky="w", padx=3)
        self.lname.config(validate='focusout', validatecommand=(top.register(self.on_valid), '%P', 'lastname'),
                          invalidcommand=(top.register(self.on_invalid), 'lastname'))
        self.mobile = tk.Entry(top, width=10)
        self.mobile.insert(0, customerMobile)
        self.mobile.grid(row=4, column=2, sticky="w", padx=3)
        self.mobile.config(validate='focusout', validatecommand=(top.register(self.on_valid), '%P', 'mobile'),
                           invalidcommand=(top.register(self.on_invalid), 'mobile'))
        self.city = tk.Entry(top, width=20)
        self.city.insert(0, customerCity)
        self.city.grid(row=4, column=3, sticky="w", padx=3)
        self.city.config(validate='focusout', validatecommand=(top.register(self.on_valid), '%P', 'city'),
                         invalidcommand=(top.register(self.on_invalid), 'city'))
        self.email = tk.Entry(top, width=25)
        self.email.insert(0, customerEmail)
        self.email.grid(row=4, column=4, sticky="w", padx=3)
        self.email.config(validate='focusout', validatecommand=(top.register(self.on_valid), '%P', 'email'),
                          invalidcommand=(top.register(self.on_invalid), 'email'))

        self.fname_label = tk.Label(top, text="Όνομα", highlightbackground='white',
                                    font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=0,
                                                                                                  sticky="w", padx=3)
        self.lastName_label = tk.Label(top, text="Επώνυμο", highlightbackground='white',
                                       font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=1,
                                                                                                     sticky="w", padx=3)
        self.mobile_label = tk.Label(top, text="Κινητό", highlightbackground='white',
                                     font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=2,
                                                                                                   sticky="w", padx=3)
        self.city_label = tk.Label(top, text="Πόλη", highlightbackground='white',
                                   font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=3,
                                                                                                 sticky="w", padx=3)
        self.email_label = tk.Label(top, text="e-mail", highlightbackground='white',
                                    font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=4,
                                                                                                  sticky="w", padx=3)

        self.label_error = tk.Label(top, foreground='red', bg="white")
        self.success = tk.Label(top, foreground='green', bg="white")
        self.label_error.grid(row=1, column=1, sticky=tk.W, padx=5)
        self.success.grid(row=11, column=1, sticky=tk.W, padx=5)

        self.update_button = tk.Button(top, state='normal', text="Αποθήκευση", font=("Lucida", "10",
                                                                                     "bold"), fg='#335BA3',
                                       bg='#DAE3F3',
                                       command=lambda: (self.update_customer(customerId)))
        self.update_button.grid(row=10, column=2, pady=20)

    def update_customer(self, customerId):
        formValidation = self.validator.validate_form(self.fname.get(), self.lname.get(), self.mobile.get(),
                                                      self.city.get(),
                                                      self.email.get())

        if formValidation['status']:
            self.customerController.update_customer(customerId, self.fname.get(), self.lname.get(),
                                                    self.mobile.get(), self.city.get(), self.email.get())

            self.success['text'] = 'Επιτυχημένη τροποποίηση πελάτη.'
        else:
            self.on_invalid(formValidation['error_field'])

    def on_invalid(self, type):
        self.success['text'] = ''
        self.update_button.config(state='disabled')

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
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο ονομα πολης'
            self.city['foreground'] = 'red'
        if type == 'email':
            self.label_error['text'] = 'Παρακαλώ εισάγετε έγκυρο email'
            self.email['foreground'] = 'red'

    def on_valid(self, value, type):
        self.success['text'] = ''
        self.label_error['text'] = ''
        self.update_button.config(state='normal')

        if type == 'firstname':
            output = self.validator.validate_string_input(value)
            if output:
                self.fname['foreground'] = 'black'
                return True
            else:
                return False
        if type == 'lastname':
            output = self.validator.validate_string_input(value)
            if output:
                self.lname['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'mobile':
            output = self.validator.validate_mobile(value)
            if output:
                self.mobile['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'city':
            output = self.validator.validate_string_input(value)
            if output:
                self.city['foreground'] = 'black'
                return True
            else:
                return False

        if type == 'email':
            output = self.validator.validate_email(value)
            if output or output == '':
                self.email['foreground'] = 'black'
                return True
            else:
                return False
