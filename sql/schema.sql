DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS STATS;
DROP TABLE IF EXISTS GYM;
DROP TABLE IF EXISTS USER_GYM;

CREATE TABLE USER (
	userId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	firstName TEXT,
	lastName TEXT,
	dateOfBirth TEXT,
	email TEXT,
	password TEXT
);

CREATE TABLE STATS (
	userId INTEGER PRIMARY KEY,
	bench REAL,
	deadlift REAL,
	squat REAL,
	FOREIGN KEY (userId) REFERENCES USER(userId)
);

CREATE TABLE GYM (
	gymId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	geoX REAL NOT NULL,
	geoY REAL NOT NULL
);

CREATE TABLE USER_GYM (
	userId INTEGER,
	gymId INTEGER,
	PRIMARY KEY (userId, gymId),
	FOREIGN KEY (userId) REFERENCES USER(userId),
	FOREIGN KEY (gymId) REFERENCES GYM(userId)
);
