from UI.UpdateAppointmentForm import *
from UI.UpdateCustomerForm import *
from Helpers.TimeFormatter import *

class AppointmentAppearance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.CustomerController = CustomerController()
        self.AppointmentController = AppointmentController()
        self.UpdateForm = UpdateAppointmentUpForm()
        self.controller = controller
        self.label_list = []
        timeLists = TimeFormatter.format('07:00', '20:00', 30, '%H:%M')
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Εμφάνιση Ραντεβού", font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')
        self.label.grid(row=1, column=1)

        self.menu = tk.Button(self, text="<<Επιστροφή στο Αρχικό Μενού", font=("Lucida", "10", "bold"),
                              fg='white', bg='#335BA3', command=lambda: (
                                  controller.show_frame("Menu"), self.clean_records(), self.clear_spinbox(),
                                  self.date.selection_set(datetime.today())))
        self.menu.grid(row=2, column=1, pady=5)

        self.date = MyCalendar(self, allowed_weekdays=(
            calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY),
                               weekendbackground='red', weekendforeground='red',
                               othermonthbackground='gray95', othermonthwebackground='gray95',
                               othermonthforeground='black', othermonthweforeground='black',
                               font="Lucid 10", selectmode='day', date_pattern='yyyy-mm-dd',
                               selectforeground='green', mindate=datetime.now(), locale='el')
        self.date.grid(row=10, column=1)

        self.var = tk.StringVar()
        self.var.set('False')

        self.disable_button_label = tk.Label(self,
            text= '''Ενεργοποιήστε το ημερολόγιο για εμφάνιση λίστας ραντεβού συγκεκριμένης ημερομηνίας''' ,
                         font=("Lucida", "10", "italic"), fg='#335BA3', bg='#EAEAEA')
        self.disable_button_label.grid(row=9, column=0, columnspan=3, sticky="w", pady=(5, 10))
        self.disable_calendar = tk.Checkbutton(self, command=self.check_button, variable=self.var, onvalue='True',
                                               offvalue='False', text='Απενεργοποιημένο',
                                               font=("Lucida", "10", "bold italic"),bg='#C0C0C0', fg='white')
        self.disable_calendar.grid(row=10, column=2, sticky='e', padx=10)

        self.search_label = tk.Label(self, text="Αναζήτηση", font=("Lucida", "12",
                      "bold"), fg='#335BA3', bg='white').grid(row=3, column=0)

        self.search = tk.Entry(self, width=40)
        self.search.grid(row=3, column=1)
        label_comm = tk.Label(self, text="Εισάγετε όνομα ή επίθετο ή κινητό ή email",
                                 font=("Lucida", "10", "italic"), fg='#335BA3', bg='white')
        label_comm.grid(row=4, column=1, pady=2)

        self.start_time_label = tk.Label(self, text="Ώρα έναρξης", font=("Lucida", "11", "bold"), bg='white',
                                         fg='#335BA3')
        self.start_time_label.grid(row=6, column=0)
        self.start_time = tk.Spinbox(self, font="Lucida 11",bg='white', fg='#335BA3',
                                     textvariable=timeLists.get('start_init'),
                                     values=timeLists.get('time_list'),
                                     wrap=True, width=5)
        self.start_time.grid(row=6, column=1, pady=5)

        self.end_time_label = tk.Label(self, text="Ώρα λήξης", font=("Lucida", "11", "bold"), bg='white',
                                       fg='#335BA3').grid(row=7, column=0)
        self.end_time = tk.Spinbox(self, font="Lucida 11", bg='white', fg='#335BA3',
                                   textvariable=timeLists.get('end_init'),
                                   values=timeLists.get('reversed_list'),
                                   wrap=True, width=5)
        self.end_time.grid(row=7, column=1, pady=5)

        tk.Button(self, text="Εμφάνιση Αποτελεσμάτων", font=("Lucida", "10", "bold"), fg='#335BA3',
                  bg='#DAE3F3',command=self.display).grid(row=12, column=1, pady=(10, 10))

        self.dates_label = tk.Label(self, text="Ημερομηνία", font = ("Lucida", "11", "bold"), bg = 'white',
                                    fg='#335BA3').grid(row=14, column=0, padx=2)
        self.start_time_label = tk.Label(self, text="Ώρα Έναρξης", font = ("Lucida", "11", "bold"), bg = 'white',
                                         fg = '#335BA3').grid(row=14, column=1, padx=2)
        self.end_time_label = tk.Label(self, text="Ώρα Λήξης", font = ("Lucida", "11", "bold"), bg = 'white',
                                       fg = '#335BA3').grid(row=14, column=2)

        self.email_label = tk.Label(self, text="Κινητό", font=("Lucida", "11", "bold"), bg = 'white',
                                    fg = '#335BA3').grid(row=14, column=3)
        self.email_label = tk.Label(self, text="E-mail", font=("Lucida", "11", "bold"), bg = 'white',
                                    fg = '#335BA3').grid(row=14, column=4, padx=(20, 20))


    def check_button(self):

        if self.var.get() == 'False':
            self.disable_calendar['bg'] = 'red'
            self.disable_calendar['text'] = 'Απενεργοποιημένο'
        else:
            self.disable_calendar['bg'] = 'green'
            self.disable_calendar['text'] = 'Ενεργοποιημένο!'

    def display(self):
        self.clean_records()

        appointments = self.AppointmentController.display_appointments(self.var.get(), self.date.get_date(),
                                                                       self.start_time.get(),
                                                                       self.end_time.get(), self.search.get())

        self.clean_records()
        counter = 16
        for appointment in appointments:
            self.dates_display = tk.Label(self, text=appointment[2], font=("Lucida", "10", "italic"),
                                          fg='#335BA3', bg='white')
            self.dates_display.grid(row=counter, column=0, padx=2, pady=2)
            self.start_times_display = tk.Label(self, text=appointment[3], font=("Lucida", "10", "italic"),
                                                fg='#335BA3', bg='white')
            self.start_times_display.grid(row=counter, column=1, padx=2, pady=2)
            self.end_times_display = tk.Label(self, text=appointment[4], font=("Lucida", "10", "italic"),
                                              fg='#335BA3', bg='white')
            self.end_times_display.grid(row=counter, column=2, padx=2, pady=2)
            self.mobile_display = tk.Label(self, text=appointment[8], font=("Lucida", "10", "italic"),
                                           fg='#335BA3', bg='white')
            self.mobile_display.grid(row=counter, column=3, padx=(0, 10), pady=2)
            self.email_display = tk.Label(self, text=appointment[10], font=("Lucida", "10", "italic"),
                                          fg='#335BA3', bg='white')
            self.email_display.grid(row=counter, column=4, padx=(10,10), pady=2)

            self.delete_display = tk.Button(self, text='Διαγραφή', bg='#335BA3',
                                     font=("Lucida", "10", "bold"), fg='white',
                                            command=lambda appointmentId=appointment[0]: self.delete_appointment(
                                                appointmentId))
            self.delete_display.grid(row=counter, column=10, padx=2, pady=2)
            self.update_display = tk.Button(self, text='Τροποποίηση', bg='#335BA3', font=("Lucida", "10", "bold"),
                                            fg='white', command=lambda appointmentId=appointment[0],
                                                           date=appointment[2],
                                                           start_time=appointment[3],
                                                           end_time=appointment[4]: [
                                                self.UpdateForm.create_popup(appointmentId, date, start_time,
                                                                             end_time), self.clean_records()])
            self.update_display.grid(row=counter, column=11, padx=2, pady=2)

            self.label_list.extend(
                [self.dates_display, self.start_times_display, self.end_times_display, self.mobile_display,
                 self.email_display,
                 self.delete_display, self.update_display])

            counter += 1

    def clean_records(self):
        for label in self.label_list:
            label.destroy()

    def delete_appointment(self, appointmentId):
        self.AppointmentController.delete_appointment(appointmentId)
        self.clean_records()
        self.display()

    def clear_spinbox(self):
        self.start_time.delete(0, "end")
        self.end_time.delete(0, "end")
        self.start_time.insert(0, '07:00')
        self.end_time.insert(0, '20:00')
