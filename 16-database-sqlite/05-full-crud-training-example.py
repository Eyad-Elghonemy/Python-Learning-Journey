# --------------------------------------------------
# -- Database => SQLite => Training On Everything --
# --------------------------------------------------

import sqlite3


def get_all_data():
    
    try :
        
        # Connect to Database
        
        db = sqlite3.connect("train.db")
        
        
        # print Success Message
        print("Connected To Database Successfully")
        
        # Setting Up The Cursor
        cr = db.cursor()
        
        # Fetch Data From Database
        cr.execute("select * from users")
        
        # Assign Data To Variable
        results = cr.fetchall()
        
        # Print Number Of Rows
        print(f"Database Has {len(results)} Rows")
        
        # Printing Message
        print("Showing Data")
        
        # Loop On Results
        for row in results:
            
            print(f"user ID => {row[0]}", end =" ,")
            
            print(f"user Name => {row[1]}")
    
    except sqlite3.Error as er:
        
        print(f"Error Reading data {er}")
        
    finally :
        
        if (db) :
            
            # Close Connection To The Database
            db.close()
            
            print("Connection To Database Closed")
    


get_all_data()