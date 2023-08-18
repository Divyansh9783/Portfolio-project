from flask import Flask,render_template,request,redirect,url_for

import pymysql as sql

def db_connect():
    db=sql.connect(host='localhost',port=3306,user='root',password="",database='python')
    cursor=db.cursor()
    return db,cursor


app=Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/aftersubmit/",methods=['GET','POST'])
def aftersubmit():
    if request.method=="GET":
        return redirect(url_for('contact'))
    else:
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        db,cursor=db_connect()
        cmd=f"select  * from flask_data where email='{email}'"
        cursor.execute(cmd)
        data=cursor.fetchall()
        if data:
            msg="This email already exist"
            return render_template('contact.html',msg=msg)
        
        
    

        else:
           
           cursor.execute(cmd)
           
           cmd=f"insert into flask_data values('{name}','{email}','{phone}','{message}')"
           
           db.commit()
           
           db.close()
           msg="details are send sucessfully"
           return render_template('contact.html',msg=msg)

    
@app.route('/Resume/')
def resume():
    return send_static_file('resume.pdf')


app.run(debug=True)


