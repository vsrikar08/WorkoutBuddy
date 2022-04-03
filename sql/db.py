import csv
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

	def GetUserById(self, userId):
		self.cursor.execute("SELECT * FROM USER WHERE userId = ?", (userId,))
		return self.cursor.fetchone()

	def AddStats(self, userId, bench, deadlift, squat):
		self.cursor.execute("""INSERT INTO STATS
								(userId, bench, deadlift, squat)
								VALUES
								(?, ?, ?, ?)
							""", (userId, bench, deadlift, squat))
		self.db.commit()

	def GetStats(self, name):
		user = self.GetUser(name)

		self.cursor.execute("SELECT * FROM STATS WHERE userId = ?", (user[0][0],))
		return self.cursor.fetchall()

	def ChangeStats(self, name, bench, deadlift, squat):
		user = self.GetUser(name)

		self.cursor.execute("""UPDATE STATS SET bench = ?, deadlift = ?, squat = ? WHERE userId = ?""", (bench, deadlift, squat, user[0][0]))
		self.db.commit()

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

	def SearchCategory(self, type, weight):
		if (type == 0):
			if (weight >= 0 and weight <= 100):
				self.cursor.execute("SELECT * FROM STATS WHERE bench > 0 AND bench <= 100")
			elif (weight > 100 and weight <= 200):
				self.cursor.execute("SELECT * FROM STATS WHERE bench > 100 AND bench <= 200")
			elif (weight > 200):
				self.cursor.execute("SELECT * FROM STATS WHERE bench > 200")

			return self.cursor.fetchall()

		elif (type == 1):
			if (weight >= 0 and weight <= 200):
				self.cursor.execute("SELECT * FROM STATS WHERE deadlift > 0 AND deadlift <= 200")
			elif (weight > 200 and weight <= 300):
				self.cursor.execute("SELECT * FROM STATS WHERE deadlift > 200 AND deadlift <= 300")
			elif (weight > 300):
				self.cursor.execute("SELECT * FROM STATS WHERE deadlift > 300")

			return self.cursor.fetchall()
				
		elif (type == 2):
			if (weight >= 0 and weight <= 300):
				self.cursor.execute("SELECT * FROM STATS WHERE squat > 0 AND squat <= 300")
			elif (weight > 300 and weight <= 400):
				self.cursor.execute("SELECT * FROM STATS WHERE squat > 300 AND squat <= 400")
			elif (weight > 400):
				self.cursor.execute("SELECT * FROM STATS WHERE squat > 400")

			return self.cursor.fetchall()

		else:
			return None

	def SearchByCity(self, city):
		self.cursor.execute("SELECT * FROM USER WHERE city = ?", (city,))
		return self.cursor.fetchall()
				

	def example(self):
		with open (self.path + "\\example_set.csv", "r") as file:
			reader = csv.reader(file, delimiter = ",")

			header = next(reader)
			for row in reader:
				self.AddUser(row[0], row[1], row[2], row[3], row[4], row[5])
				user = self.GetUser(row[0])
				self.AddStats(user[0][0], row[6], row[7], row[8])
