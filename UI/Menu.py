import tkinter as tk
from Helpers.ExitQuestionHelper import ExitQuestionHelper
from PIL import ImageTk, Image


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)
        self.config(bg="white")
        self.controller = controller
        img = Image.open('image.png')
        self.tkimage = ImageTk.PhotoImage(img)
        label_image = tk.Label(self, image=self.tkimage, bg='white')
        label_image.grid(row=6,column=3, columnspan=2)

        label = tk.Label(self, text="""
                Εφαρμογή Διαχείρισης Ραντεβού Πελατών""", highlightbackground='white',
                         font=("Lucida", "16", "bold"), fg='#335BA3', bg='white', justify="center")
        label.grid(row=0, columnspan=2, padx=(10, 40), pady=10)

        label2 = tk.Label(self, text="""
        Καλώς ορίσατε στην Εφαρμογή Διαχείρισης Ραντεβού Πελατών. 
                Επιλέξτε από το μενού επιλογών την διεργασία που θέλετε να εκτελέσετε. 
                Για έξοδο πατήστε το κλείσιμο παραθύρου 'x'.""", highlightbackground='white',
                          font=("Lucida", "10", "italic"), fg='#335BA3', bg='white')
        label2.grid(row=1, columnspan=2, padx=10, pady=10)

        label_entry = tk.LabelFrame(self, bd=2, bg='#335BA3')
        label_entry.grid(row=2, columnspan=2, padx=10, pady=10)
        save_customer = tk.Button(label_entry, text="Εισαγωγή Νέου Ραντεβού", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44,
                                  command=lambda: (controller.show_frame("Register")))
        label_entry1 = tk.LabelFrame(self, bd=2, bg='#DAE3F3', height=4, width=20)
        label_entry1.grid(row=3, column=0, padx=10, pady=10)
        customer_display = tk.Button(label_entry1, text="Εμφάνιση Πελάτη", bg='#335BA3',
                                     font=("Lucida", "14", "bold"), fg='white', height=4, width=20,
                                     command=lambda: (
                                     controller.show_frame("CustomerDisplay")))
        label_entry2 = tk.LabelFrame(self, bd=2, bg='#DAE3F3', height=4, width=20)
        label_entry2.grid(row=3, column=1, padx=10, pady=10)
        search_appointment = tk.Button(label_entry2, text="Εμφάνιση Ραντεβού", bg='#335BA3',
                                       font=("Lucida", "14", "bold"), fg='white', height=4, width=20,
                                       command=lambda: (
                                       controller.show_frame("AppointmentAppearance")))
        label_entry3 = tk.LabelFrame(self, bd=2, bg='#DAE3F3', height=4, width=20)
        label_entry3.grid(row=4, column=0, padx=10, pady=10)
        appointment_reminded = tk.Button(label_entry3, text="Υπενθύμιση ραντεβού", bg='#335BA3',
                                         font=("Lucida", "14", "bold"), fg='white', height=4, width=20,
                                         command=lambda: (
                                         controller.show_frame("AppointmentReminder")))
        label_entry4 = tk.LabelFrame(self, bd=2, bg='#DAE3F3', height=4, width=20)
        label_entry4.grid(row=4, column=1, padx=10, pady=10)
        export_appointments = tk.Button(label_entry4, text="Εξαγωγή σε αρχείο Excel", bg='#335BA3',
                                        font=("Lucida", "14", "bold"), fg='white', height=4, width=20,
                                        command=lambda: (
                                        controller.show_frame("ExportAppointments")))
        label_entry5 = tk.LabelFrame(self, bd=1, bg='#969696')
        label_entry5.grid(row=5, columnspan=2, padx=2, pady=10)
        exit_button = tk.Button(label_entry5, text="'Εξοδος", font=("Lucida", "12", "bold"), fg='white', bg='#B2B2B2',
                                height=1, width=15, command=lambda: ExitQuestionHelper.on_close())

        save_customer.grid(row=1, columnspan=2, padx=10, pady=10)
        customer_display.grid(row=2, column=0, padx=10, pady=10)
        search_appointment.grid(row=2, column=1, padx=10, pady=10)
        appointment_reminded.grid(row=3, column=0, padx=10, pady=10)
        export_appointments.grid(row=3, column=1, padx=10, pady=10)
        exit_button.grid(row=5, columnspan=2, padx=5, pady=5)
