# WorkoutBuddy
Example JSON commands that can be sent to the Python interface. Multiple commands can be sent at once by appending a "\n" between each preceding command.

// Command 0: Add user and their stats
- {"cmd":0,"name":"Gary Oak","age":24,"sex":"Male","email":"gary_prof_oak@gmail.com","password":"passABC","city":"Riverside","bench":145,"squat":200,"deadlift":250}

// Command 1: Get user based on their name
- {"cmd":1,"name":"Gary Oak"}

// Command 2: Get user stats based on their name
- {"cmd":2,"name":"Gary Oak"}

// Command 3: Modify user's stats
- {"cmd":3,"name":"Gary Oak", "bench":147,"squat":203,"deadlift":259}

// Command 4: Send message format
- {"cmd":4,"sender":"Gary Oak", "receiver": "Jane Doe", "content":"Hi! Want to work out some time?"}

- {"cmd":4,"sender":"Jane Doe", "receiver": "Gary Oak", "content":"I'd love to! What time works best for you?"}

// Command 5: Get all messages between two users
- {"cmd":5,"sender":"Jane Doe", "receiver": "Gary Oak"}

// Command 6: Search for users with a similar weight class
- {"cmd":6,"type":"bench","weight":145}

// Command 7: Get all users in the city of Riverside
- {"cmd":7,"city":"Riverside"}

// Command 999: Close the database
- {"cmd":999}

### What is this?

The backend database for http://workoutbuddy.tech/. 

### How to use this?

Run WorkoutBuddy.py and type any of the commands above additionally after command 0 (Gary Oak is intentionally not in the database at the start). After that depending on what the user wants as shown in the options menu above, you can choose what you want to do. 

### How was this built?

The database is based on SQLite3 and the interface that connects to it is Python 3. All functionality uses native Python libraries. We also use js for the front end and connect it to the backend through requests. So when we enter in data we store that data in the sql database and depending on what the user wants we retreive stuff from the database to give to the front end. 


