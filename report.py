import sqlite3
from datetime import datetime

class Report:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()

    def get_monthly_report(self, year, month):
        self.c.execute('SELECT * FROM transactions WHERE STRFTIME("%Y", date) = ? AND STRFTIME("%m", date) = ?', (year, month))
        transactions = self.c.fetchall()
        income = sum(transaction[1] for transaction in transactions if transaction[2] == 'Income')
        expenses = sum(transaction[1] for transaction in transactions if transaction[2] == 'Expense')
        savings = income - expenses
        return income, expenses, savings

    def get_yearly_report(self, year):
        self.c.execute('SELECT * FROM transactions WHERE STRFTIME("%Y", date) = ?', (year,))
        transactions = self.c.fetchall()
        income = sum(transaction[1] for transaction in transactions if transaction[2] == 'Income')
        expenses = sum(transaction[1] for transaction in transactions if transaction[2] == 'Expense')
        savings = income - expenses
        return income, expenses, savings
