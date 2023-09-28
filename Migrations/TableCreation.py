from Migrations.AppointmentsTable import appointments_table
from Migrations.CustomersTable import customers_table


def sql_table(conDatabase):
    appointments_table(conDatabase)
    customers_table(conDatabase)
