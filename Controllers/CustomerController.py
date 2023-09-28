from Models.CustomerModel import *


class CustomerController:
    def __init__(self):
        self.customerModel = CustomerModel()

    def display_customers(self, search):
        customers = self.customerModel.show_customers(search)
        return customers

    def create_customer(self, fname, lname, mobile, city, email):
        customers = self.customerModel.create_customer(fname, lname, mobile, city, email)
        return customers

    def delete_customer(self, customerId):
        self.customerModel.delete_customer(customerId)
        return True


    def update_customer(self, customerId, fname, lname, mobile, city, email):
        customer = self.customerModel.update_customer(customerId, fname, lname, mobile, city, email)
        return customer
