# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Excute
# - Close
# - https://sqlite.org/download.html
# -------------------------------------------------

# Import SQLite Module

import sqlite3

# Create Database And Connect 

db = sqlite3.connect("app.db")  # db => db extention

# Create The Taples And Fields 

db.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Close Database

db.close()
