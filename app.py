from flask import *
from flask_socketio import SocketIO, send, emit
import os
import models
from werkzeug.utils import secure_filename
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['UPLOAD_FOLDER']="static/images"
app.secret_key="xjhdjhkjhskjhdkj"
@app.route('/')
def home():
    if 'Email' in session:
        data={
               'Email':session['Email']
           }


        filename=models.get_image(data)
        if filename is not None:
            image= " | ".join(filename[0])

            return render_template("index.html",filename=image)
        else:
           return render_template("index.html")
    else:
        return render_template("base.html")

#Login For user and setting session objects
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=="POST":
        details = request.form
        data={
        "Email": details['Email'],
        "Password" :details['Password']
        }
        account = models.select_table(data)
        if account:
            session['Email'] = account[2]
            session['Name'] = account[1]
            session['Id']=account[0]
            return redirect('/')
        else:
            return redirect(url_for("/",status="loginError"))
    else:
        return "url not found"


#Resgistran for User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        details = request.form
        data={
        "Name": details['Name'],
        "Email": details['Email'],
        "Password":details['Password']

        }
    models.insert_table(data)
    return redirect("/")
@app.route('/setting')
def setting():
    if 'Email' in session:
        datas={
            "Email":session['Email'],
            "Name":session['Name']
        }


        return render_template("setting.html",datas=datas)
    else:
        return redirect("/logout")

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
            return redirect("/logout")
    else:
        return redirect("/setting")

@app.route('/logout')
def logout():
    for keys in session.keys():
        session.pop(keys)
        return redirect('/')
#
@app.route("/upload",methods=['POST','GET'])
def upload_file():
    if 'Email' in session:
        if request.method == 'POST':
            file= request.files['image']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data={
                "Email":session['Email'],
                "filename":filename
            }

            models.insert_image(data)
            return redirect('/')
        else:
           return redirect('/setting')
    else:
        return redirect('/logout')
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)




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
        filename=models.get_image(data)
    #
        image= " | ".join(filename[0])

        posts=models.get_posts(data)
        datas={
            "posts":posts,
            "name":session['Name']
        }
        if filename is not None:
           return render_template("blogs.html",datas=datas, filename=image)
        else:
            return render_template("blogs.html",data=datas)

    else:
        return redirect("/login")
@app.route('/people',methods=['GET','POST'])
def find_people():
    if request.method=='GET':
        if 'Email' in session:
            data={
                "Email":session['Email']
            }
            peoples=models.find_people(data)

            filename=models.get_image(data)
            image= " | ".join(filename[0])
            data={
                "people":peoples
            }
            if filename is None:
                return render_template("people.html",people=peoples)
            else:
                return render_template("people.html",data=data,filename=image)

        else:
            return redirect('/login')
    elif request.method=='POST':
        details=request.form
        try:
            name=details['Name']
            return redirect(url_for('chats',name=name))
        except:
            btn_name=details['button']
            name=details['name']
            return redirect(url_for('follow',btn=btn_name,name=name))

@app.route('/notification')
def notify():
   if 'Email' in session:
       data={
           "Email":session['Email']

       }
       peoples=models.find_people(data)
       return render_template("notifications.html",people=peoples)
   else:
       return redirect('/logout')

@app.route('/user/<name>')
def find_user(name):
    data={
            "Email":session['Email'],
            "Name":name
        }
    posts=models.get_posts(data)
    peoples=models.find_people(data)
    for people in peoples:
        if name==people[0]:
           return render_template("profile.html",data=data,posts=posts)
    else:
        return render_template("profile.html")

@app.route('/chats')
def chats():
    if 'Email' in session:
        if (request.args.get("name")):
            Name= request.args.get("name")
            current_user=session['Name']
            return render_template("messages.html",name=Name,user=current_user)
        else:
            return redirect('/people')
    else:
        return redirect('/login')


@socketio.on('message from user',namespace='/message')
def handleMessage(data):
    messages=data['messages']
    emit('from flask',data,broadcast=True)

@app.route('/follow',methods=['GET','POST'])
def follow():
    if 'Email' in session:
        btn= request.args.get('btn')
        name=request.args.get('name')
        username=session['Name']
        data={
    "name":name,
    "user":username
        }
        if btn=='following':
            models.add_following(data)
            return redirect('/people')
        else:
            return redirect('/people')
    else:
        return redirect("/logout")
if __name__ == '__main__':
    socketio.run(app,debug=True)
