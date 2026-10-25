# ----------------------------------------------------
# -- Database => SQLite => Create Skills App Part 1 --
# ----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("train.db")

# Setting Up The Cursor
cr = db.cursor()

# My User ID
uid = 1



def commit_and_close():
    """commit Changes And Close Conection To Database"""
    db.commit()  # Save (Commit) Changes
    db.close()  # Close Database Connection
    print("Connection To Database Closed")



# Input Message
input_message ="""

What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit the App
Choose Option :
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    
    cr.execute(f"select * from skills where user_id = {uid}")
    
    results = cr.fetchall()
    
    print(f"You Have {len(results)} Skills")
    
    if len(results)> 0 :
    
        print("Showing Skills With Progress :")
    
    for row in results :
        
       print(f"Skill => {row[0]}", end =" ,")
       print(f"Progress => {row[1]}%")
        
    
    commit_and_close()
    

def add_skills():
    
    sn = input("Write Skill Name :").strip().capitalize()
    
    cr.execute(f"select name from skills where name = '{sn}' and user_id = {uid}")
    
    results = cr.fetchone()
    
    if results == None :  #  Theres No Skill With This Name In Database
        
       print("You Can Add It :)")
       
       prog = input("Write Skill Progress :").strip()
    
       cr.execute(f"insert into skills(name, progress, user_id) values ('{sn}', '{prog}', '{uid}')")
    
    else:  #  Theres Is A Skill With This Name In Databas 
        
        print(f"You Cannot Add {sn} It's Already Existed")
        
        input_msg = input(f"Do You Want To Update {sn} Progress Y, N ?").strip().capitalize()
        
        if input_msg == "Y" :
            
            prog = input(f"Write The New Skill {sn} Progress :").strip()
    
            cr.execute(f"update skills set progress = '{prog}' where name = '{sn}' and user_id = {uid}")
            
            print(f"Skill {sn} Updated Successfully")
            
        elif input_msg == "N" :
            
            commit_and_close()
            
        else :
            
            print("Invalid Option")
    
    # print(f"You Have {len(results)} Skills")
    
    
    commit_and_close()


def delete_skills():
    
    sn = input("Write Skill Name :").strip().capitalize()
    
    cr.execute(f"delete from skills where name = '{sn}' and user_id = {uid}")
    
    commit_and_close()


def update_skills():
    
    sn = input("Write Skill Name :").strip().capitalize()
    
    prog = input(f"Write The New Skill {sn} Progress :").strip()
    
    cr.execute(f"update skills set progress = '{prog}' where name = '{sn}' and user_id = {uid}")
    
    print(f"Skill {sn} Updated Successfully")
    
    commit_and_close()





# Check If Command Is Exists
if user_input in commands_list :
    
    # print(f"Command Found {user_input}")
    
    if user_input == "s" :
        
        show_skills()
        
    elif user_input == "a" :
        
        add_skills()
        
    elif user_input == "d" :
        
        delete_skills()
        
    elif user_input == "u" :
        
        update_skills()
        
    
    else :
        
        print("App Is Closed")
        
        commit_and_close()
    
else :
    
    print(f"Sorry This Command \"{user_input}\" Is Not Found")
    