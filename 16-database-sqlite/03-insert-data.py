# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - Cursor => All Operation In SQL Done By Cursor Not The Connection Itself
# - Commit => Save All Changes
# -------------------------------------------------

# Import SQLite Module

import sqlite3

# Create Database And Connect 

db = sqlite3.connect("misr.db")  # db => db extention

# Setting Up The Cursor

cr = db.cursor()

# Create The Taples And Fields 

# cr.execute("create table if not exists users (user_id integer, name text)")

# cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data

cr.execute("insert into users(user_id, name) values(1, 'Ahmed')")

cr.execute("insert into users(user_id, name) values(2, 'Mohamed')")

cr.execute("insert into users(user_id, name) values(3, 'Ali')")

# my_list = ["Ahmed", "Ali", "Sayed", "Kamal","Enas", "Sameh", "Ibrahem", "Azab"]

# n = enumerate(my_list, start=0)

# for user_id, name in n :
    
#     cr.execute(f"insert into users (user_id, name) values ({user_id}, '{name}')")

# Save (Commit) Changes

# db.commit()


# Close Database

# db.close()
