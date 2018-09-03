import pymysql

try:

    #Creates the database
    db = pymysql.connect(host='localhost', port=3306, user='root', db='')
    cur = db.cursor()
    cur.execute('CREATE DATABASE LockerDB')

    #Creates the table
    db = pymysql.connect(host='localhost', port=3306, user='root', db='LockerDB')
    cur = db.cursor()
    sqlQuery = "CREATE TABLE UserData(ID int primary key AUTO_INCREMENT, UserID varchar(30) NOT NULL, Username varchar(255) NOT NULL, Date datetime NOT NULL)" 
    cur.execute(sqlQuery)
    
except Exception as e:
        print(e)



