import tkinter as tk
from Helpers.CalendarFormatter import *
from Controllers.AppointmentController import *
from Controllers.CustomerController import *


class UpdateAppointmentUpForm:

    def create_popup(self, appointmentId, date, start_time, end_time):
        top = tk.Toplevel()
        top.geometry("700x500")
        top.title("Τροποποίηση ραντεβού")
        top.configure(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.CustomerController = CustomerController()
        self.AppointmentController = AppointmentController()

        format = "%H:%M"
        self.title = tk.Label(top, text="Τροποποίηση του Ραντεβού", font=("Lucida", "16", "bold"),
                              fg='#335BA3', bg='white').grid(row=0, column=1, columnspan=3, pady=10)
        self.label_comment = tk.Label(top, text="Αφού πραγματοποιήσετε τις αλλαγές πατήστε 'Τροποποίηση'",
                                      font=("Lucida", "10", "italic"), fg='#335BA3', bg='white').grid(row=2, column=1,
                                                                                                      pady=10)

        start_time_format = datetime.strptime(start_time, format)
        end_time_format = datetime.strptime(end_time, format)
        diff = end_time_format - start_time_format
        diff_minutes = int(diff.seconds / 60)

        self.option_menu_init = tk.StringVar(value=start_time)
        self.duration_time_init = tk.StringVar(value=str(diff_minutes))
        self.duration_time = [10, 20, 30, 40, 50, 60]

        self.start_time_value = []
        date_convert = datetime.strptime(date, '%Y-%m-%d')
        date_today = datetime.now()
        self.date = MyCalendar(top, allowed_weekdays=(
            calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY),
                               weekendbackground='red', weekendforeground='red',
                               othermonthbackground='gray95', othermonthwebackground='gray95',
                               othermonthforeground='black', othermonthweforeground='black',
                               font="Lucida 10", selectmode='day',
                               cursor="hand1", date_pattern='yyyy-mm-dd',
                               selectforeground='green', year=date_convert.year, month=date_convert.month,
                               day=date_convert.day, mindate=date_today, locale='el')

        self.date.grid(row=7, column=1)
        self.date.bind("<<CalendarSelected>>", self.clear_dropdowns)

        tk.Label(top, text="Διάρκεια ραντεβού", font=("Lucida", "11", "bold"), fg='#335BA3',
                 bg='white').grid(row=8, column=0, pady=10)
        tk.Label(top, text="Ώρα έναρξης", font=("Lucida", "11", "bold"), fg='#335BA3',
                 bg='white').grid(row=9, column=0, pady=10)

        self.duration = tk.OptionMenu(top, self.duration_time_init, *self.duration_time)
        self.duration.config(font=("Lucida", "10", "bold"), fg='white', bg='#335BA3', width=20)
        self.duration.grid(row=8, column=1)
        self.duration.bind('<Button-1>', self.reset_dropdown_time_range)

        self.start_time = tk.OptionMenu(top, self.option_menu_init, self.start_time_value)
        self.start_time.config(font=("Lucida", "10", "bold"), fg='white', bg='#335BA3', width=20)
        self.start_time.grid(row=9, column=1)
        self.start_time['direction'] = 'flush'
        self.start_time.bind('<Button-1>', self._callback)

        tk.Button(top, text="Τροποποίηση", font=("Lucida", "10", "bold"), fg='#335BA3', bg='#DAE3F3',
                  command=lambda: (self.validate_dropdown(appointmentId))).grid(row=10, column=1)
        self.success = tk.Label(top, foreground='green', bg='white')
        self.success.grid(row=11, column=1)

        self.label_error = tk.Label(top, foreground='red', bg='white')
        self.label_error.grid(row=12, column=1, sticky=tk.W, padx=5)

    def _callback(self, event):
        self.label_error['text'] = ''
        self.success['text'] = ''
        self.duration['menu'].delete(0, 'end')
        self.start_time['menu'].delete(0, 'end')

        drop_down = self.AppointmentController.dropdown_generator(self.date.get_date(),
                                                                  int(self.duration_time_init.get()))

        for opt in self.duration_time:
            self.duration['menu'].add_command(label=opt, command=tk._setit(self.duration_time_init, opt))
        for opt in drop_down:
            self.start_time['menu'].add_command(label=opt, command=tk._setit(self.option_menu_init, opt))

    def submit(self, appointmentId):
        self.AppointmentController.update_appointment(appointmentId, self.date.get_date(), self.option_menu_init.get(),
                                                      self.duration_time_init.get())
        self.success['text'] = 'Επιτυχημένη τροποποίηση ραντεβού.'
        self.label_error['text'] = ''

    def reset_dropdown_time_range(self, event):
        self.option_menu_init.set(value='Eπέλεξε ραντεβού')

    def validate_dropdown(self, appointmentId):
        if self.option_menu_init.get() != 'Eπέλεξε ραντεβού':
            self.submit(appointmentId)
        else:
            self.label_error['text'] = 'Επέλεξε ώρα ραντεβού'

    def clear_dropdowns(self, event):
        self.option_menu_init.set(value='Eπέλεξε ραντεβού')
        self.duration_time_init.set("20")
