import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(Path(__file__).resolve().parent.parent / 'discord.db')
        self.c = self.conn.cursor()

        self.CreateDatabase()

    def CreateDatabase(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (
                        idx integer,
                        username text,
                        region text,
                        UNIQUE(idx, username, region)
                        )""")

    def InsertUser(self, idx, username, region):
        with self.conn:
            self.c.execute("INSERT OR REPLACE INTO users VALUES (:idx, :username, :region)", {'idx': idx, 'username': username, 'region': region})

    def GetUserByID(self, idx):
        self.c.execute("SELECT * FROM users WHERE idx=:idx", {'idx': idx})
        return self.c.fetchone()

    def UpdateDetails(self, idx, username, region):
        with self.conn:
            return self.c.execute("""UPDATE users SET username = :username, region = :region WHERE idx=:idx""", {'idx': idx, 'username': username, 'region': region})

    def RemoveUser(self, idx):
        with self.conn:
            self.c.execute("DELETE from users WHERE idx=:idx", {'idx': idx})