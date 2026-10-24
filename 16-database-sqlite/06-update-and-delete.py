# ---------------------------------------------
# -- Database => SQLite => Ubdate and Delete --
# ---------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("train.db")

# Setting Up The Cursor
cr = db.cursor()

# Ubdate Data
# cr.execute("update users set name = 'Aseel' where user_id = 1")
# cr.execute("update users set name = 'Ali' where user_id = 2")
# cr.execute("update users set name = 'Eyad' where user_id = 3")

# Delete Data
cr.execute("delete from users where user_id = 4")

# Fetch Data
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (Commit) Changes
db.commit()

# Close Database Connection
db.close()