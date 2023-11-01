import sqlite3
con=sqlite3.connect("library.db")
cur=con.cursor()
#execute query
cur.execute("""CREATE TABLE BOOK(ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,Pages INTEGERS )""")
#INSERT is used to add data in table
cur.execute("""INSERT INTO BOOK(Title,Author,Pages) VALUES ( 'comics','Dilden','120'),
            ('Billibil','DR.Ashyam','300'),('Great lawyer','Sheehan','250')""")

#UPDATE IS USED TO UPDATE DATA (VALUES) 
cur.execute("""UPDATE BOOK SET Pages='130',Title='Canen' WHERE Author ='Dilden'""")
cur.execute("""UPDATE BOOK SET Title='Laweni' WHERE Author ='Sheehan'""")
#if we dont use WHERE all the rows get updated 


#DELETE is used to delete single or multiple records (not all table)
cur.execute("DELETE FROM BOOK WHERE Author ='DR.Ashyam'")#delete the second row 

#DELETE * all the record of table (GETTING EROR BUT TABLE DELETED)
# cur.execute("DELETE * FROM BOOK ")#delete the all record 



# #SELECT *  is used to read the data from table
cur.execute("SELECT * FROM BOOK ")
result=cur.fetchall()#fetchall used for all rows & fetchone used for one row
for row in result:#if we dont use for loop output will be shown in tuple not in table
      print(row)
con.commit()  # save data

# print("Table Created")
con.close()

