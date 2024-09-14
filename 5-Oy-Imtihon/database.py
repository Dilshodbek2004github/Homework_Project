import mysql.connector

from os import system
system("cls")

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '2004'
        )
        self.cursor = self.db.cursor()
        self.setup()

    def setup(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS HOSPITAL;")
        self.cursor.execute("USE HOSPITAL;")
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS USERS(
ID INT AUTO_INCREMENT PRIMARY KEY,
NAME VARCHAR(64) NOT NULL,
SURNAME VARCHAR(64) NOT NULL,
AGE INT NOT NULL,
USERNAME VARCHAR(100) NOT NULL UNIQUE,
PASSWORD VARCHAR(100) NOT NULL UNIQUE                            
);
""")
    def insert_user(self, name, surname, age, username, password):
        self.cursor.execute("""
INSERT INTO USERS (NAME, SURNAME, AGE, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s);
""", (name, surname, age, username, password))
        self.db.commit()
    
    def check_user(self, username, password):
        self.cursor.execute("""
SELECT * FROM USERS WHERE USERNAME = %s AND PASSWORD = %s;
""", (username, password))
        return self.cursor.fetchone()
    
        
        