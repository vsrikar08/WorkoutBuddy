import sqlite3
import os

class Database():
	def __init__(self):
		self.path = self.path = os.path.abspath(os.path.dirname(__file__))
		self.db = None
		self.cursor = None

	def SetupSchema(self):
		self.db = sqlite3.connect(self.path + "\\wb.db")
		self.cursor = self.db.cursor()

		with open (self.path + "\\schema.sql", "r") as schema:
			self.cursor.executescript(schema.read())

		self.db.commit()

	def Close(self):
		self.db.close()

	def GetUser(self, first, last):
		self.cursor.execute("SELECT * FROM USER WHERE firstName LIKE ? AND lastName LIKE ?", (first, last))
		print(self.cursor.fetchall())

	def AddUser(self, first, last, dob, email, password):
		self.cursor.execute("""INSERT INTO USER 
								(firstName, lastName, dateOfBirth, email, password)
								VALUES
								(?, ?, ?, ?, ?)
							""", (first, last, dob, email, password))
		self.db.commit()
