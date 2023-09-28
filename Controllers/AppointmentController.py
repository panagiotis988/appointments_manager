from Models.AppointmentModel import *
from Models.CustomerModel import *
from xlsxwriter import Workbook
import time
from datetime import datetime


class AppointmentController:
    def __init__(self):
        self.appointmentModel = AppointmentModel()
        self.customerModel = CustomerModel()

    def create_appointment(self, customerId, date, start_time, duration):
        end_time = (datetime.strptime(str(start_time), "%H:%M") + timedelta(minutes=int(duration))).strftime("%H:%M")

        customers = self.appointmentModel.create_appointment(customerId, date, start_time, end_time)
        return customers

    def delete_appointment(self, appointmentId):
        self.appointmentModel.delete_appointment(appointmentId)
        return True

    def export_xlsx(self, date):
        headers = {
            'fname': 'Όνομα',
            'lname': 'Επίθετο',
            'mobile': 'Τηλέφωνο',
            'email': 'Email',
            'city': 'Πόλη',
            'date': 'Ημέρα ραντεβόυ',
            'start_time': 'Ώρα έναρξης ραντεβού',
            'end_time': 'Ώρα λήξης ραντεβού',
        }

        appointments = self.appointmentModel.get_appointments_by_day(date)

        formatted_appointments = []
        for appointment in appointments:
            formatted_appointments.append({"fname": appointment[0],
                                           "lname": appointment[1],
                                           "mobile": appointment[2],
                                           "email": appointment[3],
                                           "city": appointment[4],
                                           "date": appointment[5],
                                           "start_time": appointment[6],
                                           "end_time": appointment[7]})

        timestamp = time.mktime(datetime.now().timetuple())

        with Workbook("Δεδομένα των ραντεβού" + str(timestamp) + ".xlsx") as workbook:
            worksheet = workbook.add_worksheet()
            worksheet.write_row(row=0, col=0, data=headers.values())
            header_keys = list(headers.keys())
            for index, item in enumerate(formatted_appointments):
                row = map(lambda field_id: item.get(field_id, ''), header_keys)
                worksheet.write_row(row=index + 1, col=0, data=row)

    def dropdown_generator(self, date, duration):

        format = "%H:%M"
        start_day = datetime.strptime("07:00", format)
        end_day = datetime.strptime("20:00", format)
        diff = end_day - start_day
        diff_minutes = int(diff.seconds / 60)

        day_time_lapse = []
        delete_from_dropdown = []

        for seq in range(0, diff_minutes, 10):
            split_time = (start_day + timedelta(minutes=seq)).strftime(format)
            day_time_lapse.append(split_time)

        held_appointments = self.appointmentModel.get_appointment_date(date)
        if held_appointments:

            for i in range(len(held_appointments)):
                appointment_end_time = held_appointments[i][1]
                last_free_time = (datetime.strptime(held_appointments[i][0], format) - timedelta(
                    minutes=duration - 10)).strftime(format)
                appointment_start_time_format = datetime.strptime(last_free_time, format)
                ap_end_time_format = datetime.strptime(appointment_end_time, format)
                diff = ap_end_time_format - appointment_start_time_format
                diff_minutes = int(diff.seconds / 60)

                for seq in range(0, diff_minutes, 10):
                    split_time = (appointment_start_time_format + timedelta(minutes=seq)).strftime(format)
                    delete_from_dropdown.append(split_time)
        drop_down = [time for time in day_time_lapse if time not in delete_from_dropdown]

        return drop_down

    def getAllAppointmentsByDay(self, date):
        appointments = self.appointmentModel.get_appointment_by_date(date)

        return appointments

    def display_appointments(self, state_calendar, date, start_time, end_time, search):

        display_appointments = self.appointmentModel.show_appointments(state_calendar, date, start_time, end_time,
                                                                       search)

        return display_appointments

    def update_appointment(self, appointmnetId, date, start_time, duration):
        end_time = (datetime.strptime(str(start_time), "%H:%M") + timedelta(minutes=int(duration))).strftime("%H:%M")

        self.appointmentModel.update_appointment(appointmnetId, date, start_time, end_time)
