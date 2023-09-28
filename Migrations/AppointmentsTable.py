def appointments_table(conDatabase):
    appointment = conDatabase.cursor()
    appointment.execute("CREATE TABLE IF NOT EXISTS appointments("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "customer_id INTEGER,"
                        "date DATE NOT NULL,"
                        "start_time TIME NOT NULL,"
                        "end_time TIME NOT NULL,"
                        "FOREIGN KEY(customer_id) REFERENCES customers(id)  ON DELETE CASCADE); ")
    conDatabase.commit()
