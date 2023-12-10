import flask
from flask import session
from datetime import datetime
import os
import mysql.connector
host = "localhost"
user = "root"
password = "sai123"
database = "sai"
connection = mysql.connector.connect(
host=host,
user=user,
password=password,
db=database
)
cursor = connection.cursor()

app=flask.Flask(__name__)
app.secret_key = 'your_secret_key'
picFolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder
pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpeg')
pic2=os.path.join(app.config['UPLOAD_FOLDER'], 'banner1.jpeg')
pic3=os.path.join(app.config['UPLOAD_FOLDER'], 'banner2.jpeg')
pic4=os.path.join(app.config['UPLOAD_FOLDER'], 'banner3.jpeg')
pic5=os.path.join(app.config['UPLOAD_FOLDER'], 'banner4.jpeg')
pic6=os.path.join(app.config['UPLOAD_FOLDER'], 'iphone.jpeg')
pic7=os.path.join(app.config['UPLOAD_FOLDER'], 'mi.jpeg')
pic8=os.path.join(app.config['UPLOAD_FOLDER'], 'mi2.jpeg')
pic9=os.path.join(app.config['UPLOAD_FOLDER'], 'redmi.jpeg')
pic10=os.path.join(app.config['UPLOAD_FOLDER'], 'samsung.jpeg')
pic11=os.path.join(app.config['UPLOAD_FOLDER'], 'iphone2.jpeg')
pic12=os.path.join(app.config['UPLOAD_FOLDER'], 'iphone3.jpeg')
pic13=os.path.join(app.config['UPLOAD_FOLDER'], 'samsung1.jpeg')
pic14=os.path.join(app.config['UPLOAD_FOLDER'], 'samsung1.jpeg')
u1=os.path.join(app.config['UPLOAD_FOLDER'], 'user1.jpeg')
u2=os.path.join(app.config['UPLOAD_FOLDER'], 'user2.jpeg')
u3=os.path.join(app.config['UPLOAD_FOLDER'], 'user3.jpeg')
u4=os.path.join(app.config['UPLOAD_FOLDER'], 'user4.jpeg')
u5=os.path.join(app.config['UPLOAD_FOLDER'], 'user5.jpeg')
uteja=os.path.join(app.config['UPLOAD_FOLDER'], 'userteja.jpeg')
uj=os.path.join(app.config['UPLOAD_FOLDER'], 'userjawahar.jpeg')
ut=os.path.join(app.config['UPLOAD_FOLDER'], 'usertagore.jpeg')
uc=os.path.join(app.config['UPLOAD_FOLDER'], 'usserchetan.jpeg')
amazon=os.path.join(app.config['UPLOAD_FOLDER'], 'amazon.jpeg')
flipkart=os.path.join(app.config['UPLOAD_FOLDER'], 'flipkart.jpeg')
shopclues=os.path.join(app.config['UPLOAD_FOLDER'], 'shopclues.jpeg')
myntra=os.path.join(app.config['UPLOAD_FOLDER'], 'myntra.jpeg')
snapdeal=os.path.join(app.config['UPLOAD_FOLDER'], 'snapdeal.jpeg')
facebook=os.path.join(app.config['UPLOAD_FOLDER'], 'facebook.jpeg')
twitter=os.path.join(app.config['UPLOAD_FOLDER'], 'twitter.jpeg')
instagram=os.path.join(app.config['UPLOAD_FOLDER'], 'instagram.jpeg')
email="....."
password="....."
time=datetime.now()
cur_time="0:0:0"

@app.route("/")
def my_index_page():
    
    return flask.render_template("index.html",login="Login",k=pic14,user_image=pic1,b1=pic2,b2=pic3,b3=pic4,b4=pic5,s1=pic6,s2=pic7,s3=pic8,s4=pic9,s5=pic10,s6=pic11,s7=pic12,s8=pic13)


@app.route("/account")
def my_index_page1():
    return flask.render_template("index.html",login="Login",k=pic14,user_image=pic1,b1=pic2,b2=pic3,b3=pic4,b4=pic5,s1=pic6,s2=pic7,s3=pic8,s4=pic9,s5=pic10,s6=pic11,s7=pic12,s8=pic13)
@app.route("/about")
def about():
    return flask.render_template("about.html",facebook=facebook,twitter=twitter,instagram=instagram)
@app.route("/upcoming")
def upcoming():
    return flask.render_template("upcoming.html")
@app.route("/review.html",methods=['GET','POST'])
def review():
    return flask.render_template("review.html",u1=uteja,u2=uj,u3=ut,u4=uc,u5=u5,amazon=amazon,flipkart=flipkart,myntra=myntra,shopclues=shopclues,snapdeal=snapdeal)
@app.route("/topsale")
def topsale():
    return flask.render_template("topsale.html")
@app.route("/newphones")
def new_phones():
    return flask.render_template("newphones.html")
@app.route("/chat",methods=['GET', 'POST'])
def chat():
    return flask.render_template("chat.html")
@app.route("/product.html")
def product_page():
    pic14=os.path.join(app.config['UPLOAD_FOLDER'], 'product.jpeg')
    return flask.render_template("product.html",p1=pic14,logo=pic1,login="Login")
@app.route("/search",methods=['GET', 'POST'])
def search():
    return flask.render_template("search.html",login="Login",k=pic14,user_image=pic1,b1=pic2,b2=pic3,b3=pic4,b4=pic5,s1=pic6,s2=pic7,s3=pic8,s4=pic9,s5=pic10,s6=pic11,s7=pic12,s8=pic13)
@app.route("/index.html",methods=['GET', 'POST'])
def login_option():
    email =flask.request.form.get("email")
    password=flask.request.form.get("password")
    print(email,type(email))
    print(password)
    
    cursor.execute(f"select password from umlregistration where email='{email}' ")
    result=cursor.fetchone()

                
    if(result==None):
        
        return flask.render_template("login.html",sai="INVALID PASSWORD OR USERNAME")
    for x in result:
        print(x,email) 
        if x!=password:
            return flask.render_template("login.html",sai="INVALID PASSWORD OR USERNAME")
    else:
        connection.commit()
        #cur_time=time.strftime("%H:%M:%S")
       
        return flask.render_template("index.html",login=email[:len(email)-10],k=pic14,user_image=pic1,b1=pic2,b2=pic3,b3=pic4,b4=pic5,s1=pic6,s2=pic7,s3=pic8,s4=pic9,s5=pic10,s6=pic11,s7=pic12,s8=pic13)
@app.route("/login.html")
def login_page():

    return flask.render_template("login.html",sai="...")
@app.route("/register.html")
def registration_page():
    

    return flask.render_template("registration.html",regwarning=".",wrongemail=".")

@app.route("/index1.html",methods=['GET', 'POST'])
def rigister_option():
    email =flask.request.form.get("email")
    password=flask.request.form.get("password")
    conformpassword=flask.request.form.get("conformpassword")
    phone=flask.request.form.get("phone")
    if len(phone)!=10 or not phone.isnumeric():
        print(len(phone))
        return flask.render_template("registration.html",regwarning="Please Enter carefully",wrongemail=".",ph="enter correctly",pas=".")
    
    if(email[len(email)-10:]!='@gmail.com'):
        return flask.render_template("registration.html",regwarning="Please Enter carefully",wrongemail="use gmail extension",ph=".",pas=".")

    
    if len(password)<4:
        return flask.render_template("registration.html",regwarning="Please Enter carefully",wrongemail=".",ph=".",pas="atleast 4 characters")

    if password!=conformpassword:
        return flask.render_template("registration.html",regwarning="Please Enter carefully",wrongemail=".",ph=".",pas=".")
    cursor.execute(f"select email,password from umlregistration where email='{email}' ")
    result=cursor.fetchone()
    if(result!=None):
    
        return flask.render_template("registration.html",regwarning="Please Enter carefully",wrongemail="Already exist's",ph=".",pas=".")
    else:
        cursor.execute(f"insert into umlregistration values('{email}','{password}')")  
        re=cursor.fetchall()
        for i in re:
            print(re)
        connection.commit()
        return flask.render_template("index.html",login="Login",k=pic14,user_image=pic1,b1=pic2,b2=pic3,b3=pic4,b4=pic5,s1=pic6,s2=pic7,s3=pic8,s4=pic9,s5=pic10,s6=pic11,s7=pic12,s8=pic13)


if __name__=="__main__":

    app.run(debug=True)





