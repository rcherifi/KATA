import unittest
import sqlite3
import bank_app

class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.connection = bank_app.create_connection()
        bank_app.create_table(self.connection)
        bank_app.create_account(self.connection, "rayen5", 100)
    
    def test_deposit(self):
        result = bank_app.deposit(self.connection, "rayen5", 50)
        self.assertEqual(result, "Deposit successful")
        account = bank_app.retrieve_account(self.connection, "rayen5")
        self.assertEqual(account["balance"], 150)
        
    def test_deposit_nonexistent_account(self):
        result = bank_app.deposit(self.connection, "nonexistent", 50)
        self.assertEqual(result, "Account does not exist")
        
    def tearDown(self):
        bank_app.close_connection(self.connection)

if __name__ == '__main__':
    unittest.main()
