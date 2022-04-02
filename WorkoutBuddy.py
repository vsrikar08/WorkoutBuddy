from sql.db import Database

db = Database()
db.SetupSchema()
db.AddUser("John", "Doe", "2/4/1920", "johndoe@gmail.com", "password1234")
db.GetUser("John", "Doe")
db.Close()
