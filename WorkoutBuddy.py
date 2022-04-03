import json
import sys
from sql.db import Database

def main():
	db = Database()
	db.SetupSchema()
	db.exampleUsers()
	db.exampleMessages()

	loop = True
	while loop:
		lines = sys.stdin.readline().split("\\n")

		for line in lines:
			data = json.loads(line)
			cmd = data["cmd"]

			if (cmd == 0):
				# Add user and stats
				db.AddUser(data["name"], data["age"], data["sex"], data["email"], data["password"], data["city"])
				userId = db.GetUser(data["name"])
				db.AddStats(userId[0][0], data["bench"], data["deadlift"], data["squat"])

			elif (cmd == 1):
				# GetUser
				foundUser = db.GetUser(data["name"])
				convert = {}
				convert["name"] = foundUser[0][1]
				convert["age"] = foundUser[0][2]
				convert["sex"] = foundUser[0][3]
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
				db.SendMessageNoTime(sender[0][0], receiver[0][0], data["content"])

			elif (cmd == 5):
				# GetMessages
				user1 = db.GetUser(data["sender"])
				user2 = db.GetUser(data["receiver"])
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

					convert["content"] = message[3]
					convert["timestamp"] = message[4]
					jsonList.append(convert)

				print(json.dumps(jsonList))

			elif (cmd == 6):
				# Category search (beginner, intermediate, heavy)
				if (data["type"] == "bench"):
					users = db.SearchCategory(0, data["weight"])
				elif (data["type"] == "deadlift"):
					users = db.SearchCategory(1, data["weight"])
				elif (data["type"] == "squat"):
					users = db.SearchCategory(2, data["weight"])

				jsonList = []
				for user in users:
					convert = {}
					convert["name"] = (db.GetUserById(user[0]))[1]
					convert["bench"] = user[1]
					convert["deadlift"] = user[2]
					convert["squat"] = user[3]

					jsonList.append(convert)

				print(json.dumps(jsonList))

			elif (cmd == 7):
				# Search for users by city
				users = db.SearchByCity(data["city"])

				jsonList = []
				for user in users:
					userStats = db.GetStats(user[1])[0]
					convert = {}
					convert["name"] = user[1]
					convert["age"] = user[2]
					convert["sex"] = user[3]
					convert["email"] = user[4]
					convert["password"] = user[5]
					convert["city"] = user[6]
					convert["bench"] = userStats[1]
					convert["deadlift"] = userStats[2]
					convert["squat"] = userStats[3]
					jsonList.append(convert)

				print(json.dumps(jsonList))

			elif (data["cmd"] == 999):
				loop = False
				break

	db.Close()

if __name__ == '__main__':
    main()