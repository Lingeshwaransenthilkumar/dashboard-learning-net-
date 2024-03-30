from flask import Flask,render_template,url_for,request
import mysql.connector
app=Flask(__name__,template_folder='../FLASK1/template')
db=mysql.connector.connect(
    host="localhost",
    username="lingesh",
    password="Lingesh2002",
    database="mydb")
cursor=db.cursor()
@app.route('/',methods=['GET'])
def home():
    datatype=type(request.args)
    myargs=request.args
    try:
        if request.args.get('reg')=="Register":
            name=request.args.get('name')
            email=request.args.get('email')
            pwd=request.args.get('pwd')
            sql="insert into user(name,email,pass) values('{0}','{1}','{2}')".format(name,email,pwd)
            cursor.execute(sql)
            db.commit()
            return render_template("register.html")
        elif request.args.get('login')=="Login":
            email=request.args.get('email')
            pwd=request.args.get('pwd')
            sql="select * from user where email='{0}' and pass='{1}'".format(email,pwd)
            cursor.execute(sql)
            db_data=cursor.fetchall()
            print(db_data)
            return render_template("profile.html",profile_data=db_data)
        else:
            return render_template("dashboard.html",myargs=myargs)


    except Exception as e:
        return "provide valid data"        
@app.route('/about')
def about():
    return render_template("about.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")  





        




if __name__=="__main__":
    app.run(debug=True)