from database import *


class CustomerModel:
    def create_customer(self, fname, lname, mobile, city, email):
        user_data = [fname, lname, mobile, city, email]

        customer = conDatabase.execute("SELECT * FROM customers WHERE email=? AND mobile=? LIMIT 1",
                                       (email, mobile)).fetchone()

        if customer:
            customerId = customer[0]
        else:
            cur = conDatabase.cursor()
            cur.execute('INSERT INTO customers(fname,lname,mobile,city,email) VALUES (?,?,?,?,?)', user_data)
            conDatabase.commit()
            customerId = cur.lastrowid
            cur.close()

        return customerId



    def show_customers(self, search):
        query = "SELECT * FROM customers "
        if search:
            query = query + "WHERE email LIKE ? OR mobile LIKE ? OR fname LIKE ? OR lname LIKE ? OR city LIKE ?"
            customers = conDatabase.execute(query, (
                '%' + search + '%', '%' + search + '%', '%' + search + '%', '%' + search + '%',
                '%' + search + '%',)).fetchall()
        else:
            customers = conDatabase.execute(query).fetchall()

        return customers

    def delete_customer(self, customerId):
        conDatabase.execute("DELETE FROM customers WHERE id=? ",
                            (customerId,))
        conDatabase.commit()

    def show_customer(self, search):
        query = 'SELECT id,email,mobile FROM customers '

        if search:
            query = query + 'WHERE mobile LIKE ? OR email LIKE ?'
            customer = conDatabase.execute(query,('%' + search + '%', '%' + search + '%',)).fetchall()
        else:
            customer = conDatabase.execute(query).fetchall()

        return customer

    def update_customer(self, customerId, fname, lname, mobile, city, email):
        query = """UPDATE customers SET fname = ?, lname= ?, mobile = ?, city = ?, email= ?  WHERE id = ?"""
        params = (fname, lname, mobile, city, email, customerId)
        conDatabase.execute(query, params)
        conDatabase.commit()
