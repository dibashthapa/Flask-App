from flask import *
import os
import models 
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="images"
app.secret_key="xjhdjhkjhskjhdkj"
@app.route('/')
def home():
    if 'Name' in session:
        if(request.args.get("Name")):
            return render_template("index.html",Status=True,Name=session['Name'])
       
    else:   
        return render_template("base.html")

#Login For user and setting session objects
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'GET':
            return render_template("login.html")
        else:
            details = request.form
            data={
            
             "Email": details['Email'],
            "Password" :details['Password']
            }
            account = models.select_table(data)
            print(account)
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
        data={
        "Name": details['Name'],
        "Email": details['Email'],
        "Password":details['Password']
        }


        models.insert_table(data)
        return redirect("/login")
@app.route('/setting')
def setting():
    if 'Email' in session or 'Name' in session:
        datas={
            "Email":session['Email'],
            "Name":session['Name']
        }
      
        
        return render_template("setting.html",datas=datas)
    else:
        return render_template("base.html")
#
#@app.route("/upload",methods=['POST','GET'])
#def upload_file():
#    if request.method == 'POST':
#        file= request.files['image']
#        filename = secure_filename(file.filename)
#        session['filename']=filename
#        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#        return redirect(url_for("run_profile",filename=filename))
#    else:
#        return redirect(request.url)
#
#
#@app.route('/upload/<filename>')
#def send_image(filename):
#    return send_from_directory("images", filename)
#
#@app.route("/profile")
#def run_profile():
#    if request.args.get("filename"):
#        filename=request.args.get("filename")
#        return redirect(url_for("home",filename=filename))
#    else:
#        return render_template("profile.html")
#
#
if __name__ == '__main__':
    app.run(debug=True)
