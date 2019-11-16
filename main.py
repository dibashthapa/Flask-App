from flask import *
from flask_mysqldb import MySQL
from flask_socketio import SocketIO, send, emit
# import code for encoding urls and generating md5 hashes
import urllib, hashlib

app = Flask(__name__)
mysql = MySQL(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.secret_key = "dibashthapa"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MyDB'

 

users=[]

@app.route('/')
def home():
    
    if request.args.get('Name'):
        Name = request.args.get('Name')
        return render_template("chats.html", Status=True, Name=Name)
    else:
        return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        details = request.form
        Email = details['Email']
        Password = details['Password']
        cur = mysql.connection.cursor()

        query_string = "SELECT * FROM Users WHERE Email = %s AND Password=%s"
        cur.execute(query_string, (Email, Password))
        mysql.connection.commit()
        account = cur.fetchone()
        if account:

            session['LoggedIn'] = True
            session['Email'] = account[2]
            session['Name'] = account[1]
            # return render_template("chats.html", Status=session['LoggedIn'], Name=account[1])
            return redirect(url_for('home',Name=account[1]))

        else:
            session['LoggedIn'] = False
            return render_template("login.html", status=session['LoggedIn'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        details = request.form
        Name = details['Name']
        Email = details['Email']

        Password = details['Password']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Users(Name, Email, Password) VALUES(%s, %s, %s)", (Name, Email, Password))
        mysql.connection.commit()
        cur.close()
        return redirect("/login")
@app.route("/profile")
def profile():
    pass
@socketio.on("typing",namespace='/message')
def send_typing(data):
    print(data['names'],"is typing...")
    emit('data typing',data,broadcast=True)
    



@socketio.on('message from user',namespace='/message')
def handleMessage(data):
    messages=data['messages']
  
    print(messages)
     
  
    emit('from flask',data,broadcast=True)





if __name__ == '__main__':
    socketio.run(app,debug=True)
