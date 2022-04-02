from sql.db import Database
from sql.json_test import jsonTest

db = Database()
db.SetupSchema()
db.AddUser("John", "Doe", "2/4/1920", "johndoe@gmail.com", "password1234")
db.AddStats(1, "Riverside", 100, 200, 300)
print(db.GetStats("John", "Doe"))
db.Close()
