import json
import requests
import sys
from sql.db import Database

db = Database()
db.SetupSchema()
db.example()

while True:
	data = json.loads(sys.stdin.readline())
	cmd = data["cmd"]

	if (cmd == 0):
		# Add user and stats
		db.AddUser(data["name"], data["age"], data["gender"], data["email"], data["password"], data["city"])
		userId = db.GetUser(data["name"])
		db.AddStats(userId[0][0], data["bench"], data["deadlift"], data["squat"])

	elif (cmd == 1):
		# GetUser
		foundUser = db.GetUser(data["name"])
		convert = {}
		convert["name"] = foundUser[0][1]
		convert["age"] = foundUser[0][2]
		convert["gender"] = foundUser[0][3]
		convert["email"] = foundUser[0][4]
		convert["password"] = foundUser[0][5]
		convert["city"] = foundUser[0][6]
		print(json.dumps(convert))

	elif (cmd == 2):
		# GetStats
		foundUser = db.GetUser(data["name"])
		foundStats = db.GetStats(foundUser[0][1])
		convert = {}
		convert["bench"] = foundStats[0][1]
		convert["deadlift"] = foundStats[0][2]
		convert["squat"] = foundStats[0][3]
		print(json.dumps(convert))

	elif (cmd == 3):
		# ChangeStats
		db.ChangeStats(data["name"], data["bench"], data["deadlift"], data["squat"])

	elif (cmd == 4):
		# SendMessage
		sender = db.GetUser(data["sender"])
		receiver = db.GetUser(data["receiver"])
		db.SendMessage(sender[0][0], receiver[0][0], data["message"])

	elif (cmd == 5):
		# GetMessages
		user1 = db.GetUser(data["user1"])
		user2 = db.GetUser(data["user2"])
		foundMessages = db.GetMessages(user1[0][0], user2[0][0])

		jsonList = []
		for message in foundMessages:
			convert = {}
			if (message[0] == user1[0][0]):
				convert["sender"] = user1[0][1]
				convert["receiever"] = user2[0][1]
			else:
				convert["sender"] = user2[0][1]
				convert["receiever"] = user1[0][1]

			convert["message"] = message[2]
			convert["timestamp"] = message[3]
			jsonList.append(convert)

		print(json.dumps(jsonList))


db.Close()
