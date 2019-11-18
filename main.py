from flask import *
import os
from flask_mysqldb import MySQL
from werkzeug import secure_filename
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
mysql = MySQL(app)
socketio = SocketIO(app, cors_allowed_origins="*")

app.secret_key = "dibashthapa"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'MyDB'
app.config['UPLOAD_FOLDER']='images'

users=[]

@app.route('/')
def home():
    if 'Name' in session:
        print(session['Name'])
        if(request.args.get("Name")):
            return render_template("index.html",Status=True,Name=session['Name'])
        elif(request.args.get("filename")):
            if ('filename' in session):
                print(session['filename'])
                return render_template("profile.html",filename=session['filename'],Name=session['Name'])
            

    else:
        return render_template("base.html")

    

#Login For user and setting session objects
@app.route('/login/<name>', methods=['GET', 'POST'])
def login(name):
    
        if request.method == 'GET':
            if request.args.get("name")=="student":
                return render_template("login.html")
        else:
            if request.args.get("name")=="student":
                details = request.form
                Email = details['Email']
                Password = details['Password']
                cur = mysql.connection.cursor()
                query_string = "SELECT * FROM Users WHERE Email = %s AND Password=%s"
                cur.execute(query_string, (Email, Password))
                mysql.connection.commit()
                account = cur.fetchone()
                if account:
                    session['Email'] = account[2]
                    session['Name'] = account[1]
                    return redirect(url_for('home',Name=account[1]))
                else:
                    return render_template("login.html", status=False)
          
                

#Resgistran for User
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
        session['filename']=filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("run_profile",filename=filename))
    else:
        return redirect(request.url)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/profile")
def run_profile():
    if request.args.get("filename"):
        filename=request.args.get("filename")
        return redirect(url_for("home",filename=filename))
    else:
        return render_template("profile.html")


if __name__ == '__main__':
    socketio.run(app,debug=True)