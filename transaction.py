import sqlite3
from datetime import datetime

class Transaction:
    def __init__(self, id=None, amount=None, category=None, description=None, date=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()

    def add_transaction(self, amount, category, description):
        self.c.execute("INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?)", 
                       (amount, category, description, datetime.now()))
        self.conn.commit()

    def save(self):
        if self.id is None:
            self.c.execute("INSERT INTO transactions VALUES (NULL, ?, ?, ?, ?)", 
                           (self.amount, self.category, self.description, self.date))
            self.conn.commit()
            self.id = self.c.lastrowid
        else:
            self.c.execute("UPDATE transactions SET amount = ?, category = ?, description = ?, date = ? WHERE id = ?", 
                           (self.amount, self.category, self.description, self.date, self.id))
            self.conn.commit()

    def delete(self):
        if self.id is not None:
            self.c.execute("DELETE FROM transactions WHERE id = ?", (self.id,))
            self.conn.commit()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('finance.db')
        c = conn.cursor()
        c.execute("SELECT * FROM transactions")
        rows = c.fetchall()
        transactions = []
        for row in rows:
            transactions.append(cls(*row))
        return transactions

    @classmethod
    def get_by_id(cls, id):
        conn = sqlite3.connect('finance.db')
        c = conn.cursor()
        c.execute("SELECT * FROM transactions WHERE id = ?", (id,))
        row = c.fetchone()
        if row:
            return cls(*row)
        else:
            return None

    def __str__(self):
        return f"Transaction(id={self.id}, amount={self.amount}, category='{self.category}', description='{self.description}', date='{self.date}')"

# Create the transactions table if it does not exist
def create_table():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT
                )""")
    conn.commit()

create_table()
