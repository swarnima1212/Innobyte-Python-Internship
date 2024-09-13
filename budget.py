import sqlite3

class Budget:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()

    def set_budget(self, category, amount):
        self.c.execute("INSERT OR REPLACE INTO budgets VALUES (?, ?)", (category, amount))
        self.conn.commit()

    def get_budget(self, category):
        self.c.execute("SELECT amount FROM budgets WHERE category=?", (category,))
        row = self.c.fetchone()
        if row:
            return row[0]
        else:
            return 0

    def get_all_budgets(self):
        self.c.execute("SELECT * FROM budgets")
        rows = self.c.fetchall()
        budgets = {}
        for row in rows:
            budgets[row[0]] = row[1]
        return budgets
