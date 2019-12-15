from flask import *
import os
import models 
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="images"
app.secret_key="xjhdjhkjhskjhdkj"
@app.route('/')
def home():
    if 'Email' in session:
        if(request.args.get("Name")):
            return render_template("index.html",Status=True,Name=session['Name'])
        else:
            return render_template("index.html")
       
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
                session['Id']=account[0]
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
@app.route('/setting/update',methods=['GET','POST'])
def updatesetting():
    if request.method=="POST":
        if 'Email' in session:
            details=request.form
            data={
            "Name":details['Name'],
           "Email":details['Email'],
            "Id":session['Id']
            }
            
            models.update_form(data)
            return redirect("/setting")
        else:
            return redirect("/login")
    else:
        return redirect("/setting")

@app.route('/logout')
def logout():
    for keys in session.keys():
        session.pop(keys)
        return redirect('/')
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
@app.route('/add',methods=['GET','POST'])
def add_post():
    if request.method=='POST':
        if 'Email' in session:
            details=request.form
            data={
            "post":details['post'],
            "email":session['Email']
            }
            
            models.add_posts(data)
            return redirect('/')
    else:
        return redirect("/blogs")
@app.route('/blogs')
def get_post():
    if 'Email' in session:
        data={
            "Email":session['Email']
        }
        
        posts=models.get_posts(data)
        datas={
            "posts":posts,
            "name":session['Name']
        }
        return render_template("blogs.html",datas=datas)
    else:
        return redirect("/login")
@app.route('/people')
def find_people():
    if 'Email' in session:
        data={
            "Email":session['Email']
        }
        peoples=models.find_people(data)
        
        return render_template("people.html",people=peoples)
    else:
        return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)
