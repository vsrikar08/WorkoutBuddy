import os
import sqlite3
import time

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

	def AddUser(self, name, age, gender, email, password, city):
		self.cursor.execute("""INSERT INTO USER 
								(name, age, gender, email, password, city)
								VALUES
								(?, ?, ?, ?, ?, ?)
							""", (name, age, gender, email, password, city))
		self.db.commit()

	def GetUser(self, name):
		self.cursor.execute("SELECT * FROM USER WHERE name LIKE ?", (name,))
		return self.cursor.fetchall()

	def AddStats(self, userId, bench, deadlift, squat):
		self.cursor.execute("""INSERT INTO STATS
								(userId, bench, deadlift, squat)
								VALUES
								(?, ?, ?, ?)
							""", (userId, bench, deadlift, squat))
		self.db.commit()

	def GetStats(self, first, last):
		user = self.GetUser(first, last)

		self.cursor.execute("SELECT * FROM STATS WHERE userId = ?", (user[0][0],))
		return self.cursor.fetchall()

	def SendMessage(self, usr1, usr2, message):
		self.cursor.execute("""INSERT INTO MESSAGE
								(senderId, receiverId, message, time, status)
								VALUES
								(?, ?, ?, ?, ?)
							""", (usr1, usr2, message, time.time(), "Unread"))
		self.db.commit()

	def GetMessages(self, usr1, usr2):
		self.cursor.execute("""SELECT * FROM MESSAGE WHERE 
								(senderId = ? AND receiverId = ?) 
								OR 
								(senderId = ? AND receiverId = ?)
							""", (usr1, usr2, usr2, usr1));
		return self.cursor.fetchall();

	def example(self):
		self.AddUser("John Doe", 27, "Male", "johndoe@gmail.com", "password1234", "Riverside")
		self.AddStats(1, 150, 300, 200)

		self.AddUser("Jane Doe", 22, "Female", "janedoe@gmail.com", "orange12", "Riverside")
		self.AddStats(2, 100, 200, 150)