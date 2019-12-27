import mysql.connector
  #host="localhost",
  #user="root",
  #passwd="88645684",
  #database="API"
# host="remotemysql.com",
#  user="gYdL5jxd1B",
#  passwd="QsEmI5HWGt",
#  database="gYdL5jxd1B"
mydb = mysql.connector.connect(
 host="remotemysql.com",
 user="gYdL5jxd1B",
 passwd="QsEmI5HWGt",
 database="gYdL5jxd1B"


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


def update_form(data):
  query="UPDATE `Users` SET `Name` = %s, `Email` = %s WHERE `Users`.`id` = %s"
  values=(data['Name'],data['Email'],data['Id'])  
  mycursor.execute(query,values)
  mydb.commit()
#
def add_posts(data):
  query="INSERT INTO Posts (Email,Post) VALUES(%s,%s)"
  values=(data['email'],data['post'])
  mycursor.execute(query,values)
  mydb.commit()
  
def get_posts(data):
  query="SELECT Post ,title FROM Posts WHERE Email='%s'"
  mycursor.execute(query%(data['Email']))
  return mycursor.fetchall()


def find_people(data):
  query="SELECT Name,image FROM Users WHERE NOT Email='%s'"
  mycursor.execute(query%(data['Email']))
  return mycursor.fetchall()


def insert_image(data):
  query="UPDATE Users SET image=%s WHERE Email=%s"
  values=(data['filename'],data['Email'])
  mycursor.execute(query,values)
  mydb.commit()

def get_image(data):
  query="SELECT image FROM Users WHERE Email='%s'"
  mycursor.execute(query%(data['Email']))
  return mycursor.fetchall()



