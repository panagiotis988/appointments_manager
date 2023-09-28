from database import *
from tkinter import messagebox
from datetime import timedelta
from datetime import datetime


class AppointmentModel:

    def create_appointment(self, customerId, date, start_time, end_time):
        appointment_data = [customerId, str(date), str(start_time), str(end_time)]

        conDatabase.execute(
            'INSERT OR REPLACE INTO appointments(customer_id,date,start_time,end_time) VALUES (?,?,?,?)',
            appointment_data)
        conDatabase.commit()

    def delete_appointment(self, appointmentId):
        conDatabase.execute("DELETE FROM appointments WHERE id=? ",
                            (appointmentId,))
        conDatabase.commit()

    def get_appointments_by_day(self, date):
        appointments = conDatabase.execute(
            "SELECT customers.fname, customers.lname, customers.mobile, customers.email, customers.city,"
            "appointments.date, appointments.start_time, appointments.end_time "
            "FROM appointments "
            "INNER JOIN customers "
            "ON appointments.customer_id = customers.id "
            "WHERE appointments.date=?",
            (date,)).fetchall()

        return appointments

    def get_appointment(self, date):
        appointment = conDatabase.execute("SELECT * FROM appointments WHERE date=? LIMIT 1",
                                          (date,)).fetchone()

        return appointment

    def get_appointment_date(self, date):
        appointment_date = conDatabase.execute(
            'SELECT start_time,end_time FROM appointments WHERE  date = ? ORDER BY start_time',
            (date,)).fetchall()
        return appointment_date

    def get_appointment_by_date(self, date):
        appointments = conDatabase.execute("SELECT * FROM appointments INNER JOIN customers "
                                           "ON appointments.customer_id = customers.id WHERE date = ? AND customers.email"
                                           " IS NOT NULL AND customers.email <>  '' ",
                                           (date,)).fetchall()
        return appointments

    def show_appointments(self, state_calendar, date, start_time, end_time, search):
        query = "SELECT * FROM appointments INNER JOIN customers ON appointments.customer_id = customers.id "

        if state_calendar == 'True':
            query = query + "WHERE (date = ? AND start_time >= ? AND end_time <= ?) "
        elif state_calendar == 'False':
            query = query + "WHERE ( start_time >= ? AND end_time <= ?) "

        if search and state_calendar == 'True':
            query = query + "AND (email LIKE ? OR mobile LIKE ?) ORDER BY appointments.start_time"
            appointments = conDatabase.execute(query, (
                date, start_time, end_time, '%' + search + '%', '%' + search + '%',)).fetchall()

        elif search and state_calendar == 'False':
            query = query + "AND (email LIKE ? OR mobile LIKE ?) ORDER BY appointments.start_time"
            appointments = conDatabase.execute(query, (
                start_time, end_time, '%' + search + '%', '%' + search + '%',)).fetchall()

        elif search == '' and state_calendar == 'True':
            query = query + "ORDER BY appointments.start_time"
            appointments = conDatabase.execute(query, (date, start_time, end_time,)).fetchall()
        else:
            query = query + "ORDER BY appointments.start_time"
            appointments = conDatabase.execute(query, (start_time, end_time,)).fetchall()

        return appointments

    def update_appointment(self, appointmnetId, date, start_time, end_time):
        query = 'UPDATE appointments SET date = ?, start_time = ?, end_time = ? WHERE id = ?'
        params = (date, start_time, end_time, appointmnetId)
        conDatabase.execute(query, params)
        conDatabase.commit()
