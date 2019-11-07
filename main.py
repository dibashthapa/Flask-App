
import session
from flask import *
from flask_mysqldb import MySQL


 
app = Flask(__name__)
mysql= MySQL(app)
app.secret_key="dibashthapa"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MyDB'

@app.route('/')
def hello_world():
   return render_template("index.html")


@app.route('/login',methods=['GET','POST'])
def login():
   if request.method=='GET':
      return render_template("login.html")
   else:
      details=request.form
      Email=details['Email']
      Password=details['Password']
      cur=mysql.connection.cursor()

      query_string = "SELECT * FROM Users WHERE Email = %s AND Password=%s"
      cur.execute(query_string, (Email,Password))
      mysql.connection.commit()
      account=cur.fetchone()
      if account:
         session['LoggedIn']=True
         session['Id']=account[0]
         session['Email']=account[1]
         return render_template("index.html",email=account[1])
      else:
         status=False
         return render_template("login.html",status=status)
@app.route('/register',methods=['GET','POST'])
def register():
   if request.method=='GET':
      return render_template("register.html")
   elif request.method=='POST':
      details = request.form
      Name = details['Name']
      Email = details['Email']
    
      Password=details['Password']
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO Users(Name, Email, Password) VALUES(%s, %s, %s)",(Name, Email, Password))
      mysql.connection.commit()
      cur.close()
      return "success"


   
if __name__ == '__main__':
   app.run(host="localhost",port=5000,debug=True)