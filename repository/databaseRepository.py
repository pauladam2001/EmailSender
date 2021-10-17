import sqlite3


class DatabaseRepository:
    def __init__(self):
        self.connection = sqlite3.connect('EmailAddresses.db')
        self.cursor = self.connection.cursor()
        # self.create_table()
        # self.add_address('daria.andrioaie@gmail.com', 'wife')
        # self.add_address('adam.adrian@yahoo.com', 'father')
        # self.add_address('paula_g_adam@yahoo.com', 'mother')
        self._email_list = {}
        self.create_dictionary()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE addresses (
                        address text UNIQUE,
                        nickname text UNIQUE
                        )""")

    def create_dictionary(self):
        self.cursor.execute("SELECT address, nickname FROM addresses")
        items = self.cursor.fetchall()
        for row in items:
            self._email_list[row[1]] = row[0]

    def get_addresses(self):
        self.cursor.execute("SELECT * FROM addresses")
        items = self.cursor.fetchall()
        return items

    def get_dictionary(self):
        return self._email_list

    def add_address(self, address, nickname):
        self.cursor.execute("INSERT INTO addresses VALUES (?,?)", (address, nickname))
        self.create_dictionary()
        self.connection.commit()

    def close_connection(self):
        self.connection.commit()
        self.connection.close()
