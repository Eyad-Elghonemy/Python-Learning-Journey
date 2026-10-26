# -------------------------------------------------------
# -- Database => SQLite => Very Important Informations --
# -------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("train.db")

# Setting Up The Cursor
cr = db.cursor()

# SQL injection
# my_tuple = ('Pascal', '65', 3)

# Inserting Data
# cr.execute("insert into skills values (?, ?, ?)", my_tuple)

# Fetch Data From Database

# cr.execute("select * from skills order by user_id")
# cr.execute("select * from skills order by user_id asc")
# cr.execute("select * from skills order by user_id desc")
# cr.execute("select * from skills order by name desc")
# cr.execute("select * from skills order by name limit 3 offset 2")
# cr.execute("select * from skills where user_id > 1")
# cr.execute("select * from skills where user_id in (1, 2, 3)")
cr.execute("select * from skills where user_id not in (1, 2)")


# Assign Data To Variable
results = cr.fetchall()

# Loop On Results
for row in results :
    
    print(f"user ID => {row[0]}", end =" ,")        
    print(f"user Name => {row[1]}", end =" ,")
    print(f"User Id => {row[2]}")