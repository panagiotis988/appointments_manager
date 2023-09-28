from UI.UpdateCustomerForm import *


class CustomerDisplay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.config(bg="white")

        self.CustomerController = CustomerController()
        self.UpdateForm = UpdateCustomerForm()
        self.label_list = []
        self.controller = controller

        self.title = tk.Label(self, text="Εμφάνιση Πελατών", highlightbackground='white',
                              font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')
        self.title.grid(row=0, column=3, pady=(10, 10))
        self.search_label = tk.Label(self, text="Αναζήτηση", highlightbackground='white',
                                     font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=3, column=3,
                                                                                                   pady=10)
        self.search = tk.Entry(self, width=40)
        self.search.grid(row=3, column=4, padx=10, pady=10)
        self.label_comment = tk.Label(self, text="Εισάγετε όνομα ή επίθετο ή κινητό ή email",
                                      font=("Lucida", "10", "italic"), fg='#335BA3', bg='white').grid(row=4, column=4,
                                                                                                      pady=2)

        self.fname_label = tk.Label(self, text="Όνομα", highlightbackground='white',
                                    font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=6, column=0,
                                                                                                  padx=20, pady=2)
        self.lastName_label = tk.Label(self, text="Επώνυμο", highlightbackground='white', font=("Lucida", "12", "bold"),
                                       fg='#335BA3', bg='white').grid(row=6, column=1, padx=20, pady=2)

        self.mobile_label = tk.Label(self, text="Κινητό", highlightbackground='white', font=("Lucida", "12", "bold"),
                                     fg='#335BA3', bg='white')
        self.mobile_label.grid(row=6, column=2, padx=20, pady=2)
        self.city_label = tk.Label(self, text="Πόλη", highlightbackground='white',
                                   font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=6, column=3,
                                                                                                 padx=2, pady=2)
        self.email_label = tk.Label(self, text="e-mail", highlightbackground='white',
                                    font=("Lucida", "12", "bold"), fg='#335BA3', bg='white').grid(row=6, column=4,
                                                                                                  padx=2)

        self.menu = tk.Button(self, text="<<Επιστροφή στο Αρχικό Μενού", font=("Lucida", "10", "bold"), fg='white',
                              bg='#335BA3',
                              command=lambda: (controller.show_frame("Menu"), self.clean_records()))
        self.menu.grid(row=2, column=3)
        tk.Button(self, text="Εμφάνιση Αποτελεσμάτων", font=("Lucida", "10", "bold"), fg='#335BA3', bg='#DAE3F3',
                  command=lambda: (self.display())).grid(row=5, column=3, pady=20)

    def display(self):
        self.clean_records()
        customers = self.CustomerController.display_customers(self.search.get())

        counter = 8

        for customer in customers:
            self.fname = tk.Label(self, text=customer[1], font=("Lucida", "11", "italic"),
                                  fg='#335BA3', bg='white')
            self.fname.grid(row=counter, column=0)
            self.lname = tk.Label(self, text=customer[2], font=("Lucida", "11", "italic"),
                                  fg='#335BA3', bg='white')
            self.lname.grid(row=counter, column=1)
            self.mobile = tk.Label(self, text=customer[3], font=("Lucida", "11", "italic"),
                                   fg='#335BA3', bg='white')
            self.mobile.grid(row=counter, column=2)
            self.city = tk.Label(self, text=customer[4], font=("Lucida", "11", "italic"),
                                 fg='#335BA3', bg='white')
            self.city.grid(row=counter, column=3)
            self.email = tk.Label(self, text=customer[5], font=("Lucida", "11", "italic"),
                                  fg='#335BA3', bg='white')
            self.email.grid(row=counter, column=4)
            self.delete = tk.Button(self, text='Διαγραφή', bg='#335BA3', font=("Lucida", "10", "bold"), fg='white',
                                    command=lambda customerId=customer[0]: self.delete_customer(customerId))
            self.delete.grid(row=counter, column=8, padx=3)
            self.update = tk.Button(self, text='Τροποποίηση', bg='#335BA3', font=("Lucida", "10", "bold"), fg='white',
                                    command=lambda customerId=customer[0],
                                                   customerFirstName=customer[1],
                                                   customerLastName=customer[2],
                                                   customerMobile=customer[3],
                                                   customerCity=customer[4],
                                                   customerEmail=customer[5],
                                    : [self.UpdateForm.create_popup(customerId,
                                                                    customerFirstName, customerLastName, customerMobile,
                                                                    customerCity,
                                                                    customerEmail), self.clean_records()])
            self.update.grid(row=counter, column=9, padx=3)
            self.label_list.extend(
                [self.fname, self.lname, self.mobile, self.city, self.email, self.delete, self.update])

            counter = counter + 1

    def delete_customer(self, customerId):
        self.CustomerController.delete_customer(customerId)
        self.clean_records()
        self.display()

    def clean_records(self):
        for label in self.label_list:
            label.destroy()
