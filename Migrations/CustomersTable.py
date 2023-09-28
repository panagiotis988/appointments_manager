def customers_table(conDatabase):
    customer = conDatabase.cursor()
    customer.execute("CREATE TABLE IF NOT EXISTS customers("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "fname TEXT NOT NULL,"
                     "lname TEXT NOT NULL,"
                     "mobile INTEGER NOT NULL,"
                     "city TEXT,"
                     "email TEXT);")
    conDatabase.commit()
