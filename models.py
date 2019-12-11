import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="88645684",
  database="API"
)
mycursor = mydb.cursor()



def insert_table(data):
 
  sql="INSERT INTO Users (Name, Email, Password) VALUES(%s, %s, %s)"
  values=(data["Name"], data["Email"], data["Password"])
  mycursor.execute(sql,values)
  mydb.commit()
  
def select_table(data):
  query_string = "SELECT * FROM Users WHERE Email = %s AND Password=%s"
  mycursor.execute(query_string,(data['Email'],data['Password']))
  
  return mycursor.fetchone()




#
