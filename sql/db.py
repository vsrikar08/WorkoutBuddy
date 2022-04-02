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

	def AddUser(self, first, last, dob, email, password):
		self.cursor.execute("""INSERT INTO USER 
								(firstName, lastName, dateOfBirth, email, password)
								VALUES
								(?, ?, ?, ?, ?)
							""", (first, last, dob, email, password))
		self.db.commit()

	def GetUser(self, first, last):
		self.cursor.execute("SELECT * FROM USER WHERE firstName LIKE ? AND lastName LIKE ?", (first, last))
		return self.cursor.fetchall()

	def AddStats(self, userId, city, bench, deadlift, squat):
		self.cursor.execute("""INSERT INTO STATS
								(userId, city, bench, deadlift, squat)
								VALUES
								(?, ?, ?, ?, ?)
							""", (userId, city, bench, deadlift, squat))
		self.db.commit()

	def GetStats(self, first, last):
		user = self.GetUser(first, last)

		self.cursor.execute("SELECT * FROM STATS WHERE userId = ?", (user[0][0],))
		return self.cursor.fetchall()