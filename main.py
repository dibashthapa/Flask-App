from flask import *
import os
from flask_mysqldb import MySQL
from werkzeug import secure_filename
from flask_socketio import SocketIO, send, emit
# import code for encoding urls and generating md5 hashes
import urllib, hashlib

app = Flask(__name__)
mysql = MySQL(app)

app.secret_key = "dibashthapa"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MyDB'
app.config['UPLOAD_FOLDER']='images'

users=[]

@app.route('/')
def home():
    
    if request.args.get('Name'):
        Name = request.args.get('Name')
        return render_template("index.html", Status=True, Name=Name)
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

@app.route("/upload",methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        file= request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        return render_template("index.html",filename=filename)
    else:
        return render_template("index.html")


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)






if __name__ == '__main__':
    app.run(debug=True)
