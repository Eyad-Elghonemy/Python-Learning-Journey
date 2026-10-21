# ------------------------------------------------------
# -- Database => SQLite => Retrive Data From Database --
# ------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of query result. It returns all the rows
# -             as a list of tuples. An empty list returned if there is no record to fetch.
# - fetchmany(size) =>
# - Retrive = fetch
# ------------------------------------------------------

import sqlite3

db = sqlite3.connect("app.db")

# Setting Up The Cursor

cr = db.cursor()

# Create The Taples And Fields 

cr.execute("create table if not exists users (user_id integer, name text)")

cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data

# cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")
# cr.execute("insert into users(user_id, name) values(2, 'Mohamed')")
# cr.execute("insert into users(user_id, name) values(3, 'Ali')")


# Fetch Data
cr.execute("select user_id, name from users")
cr.execute("select * from users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# print(cr.fetchall())

print(cr.fetchmany(4))

# print(cr.fetchone()) # => None

# 



# Save (Commit) Changes

db.commit()


# Close Database

db.close()
