# MySQLServer.py  

import mysql.connector  

try:  
    # Establish a connection to the MySQL server  
    db = mysql.connector.connect(  
        host="localhost",  
        user="user",  
        password="12345"  
    )  
 
    cursor = db.cursor()  
 
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")  

    print("Database 'alx_book_store' created successfully!")  

    cursor.close()  
    db.close()  

except mysql.connector.Error as e:  
    print(f"Error: Failed to connect to the DB - {e}")