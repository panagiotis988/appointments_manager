from Models.AppointmentModel import *


class ValidateExport:

    def validate_date(self, date):
        appointmentModel = AppointmentModel()
        appointment = appointmentModel.get_appointment(date)

        if appointment:
            return True
