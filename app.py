from summa import keywords
from flask import Flask ,render_template ,request, url_for, redirect,g
import module1 as m
import video1 as v
import video1 as v1
import video2 as v2
import video3 as v3
import video4 as v4
import pymysql
import mlpnew2 as mlp

from flask import Flask,flash, session
from flask import Flask, flash, redirect, render_template, request, url_for
#from flask.ext.session import Session

app = Flask(__name__)
@app.before_request
def before_request():
    g.user = None
    #g.level = None
    if 'user' in session:
        g.user = session['user']
        #g.level = session['level']
        print(g.user)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/login')
def login():
    return render_template('loginask.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile')
def profile():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    cursor.execute("select tid from teacher where email=%s ", (session['email']))
    tid = cursor.fetchall()
    cursor.execute("select sid from student where tid=%s ", (tid))
    sid = cursor.fetchall()
    cursor.execute("select level from rating where sid=%s ", (sid))
    data = cursor.fetchall()
    cursor.execute("select name from student where sid=%s ", (sid))
    name = cursor.fetchall()
    cursor.execute("select email from student where sid=%s ", (sid))
    email = cursor.fetchall()
    # array=data['sid']
    # print(data)
    l = len(data)
    return render_template('profile.html',level=data,name=name,email=email,l=l)

@app.route('/logout')
def logout():
    session.pop('type', None)
    session.pop('email', None)
    session.pop('level', None)
    session.pop('login', None)
    session['login'] = "false"
    return render_template('index.html')

@app.route('/studentlogin')
def studentlogin():
    return render_template('studentlogin.html')

@app.route('/teacherlogin')
def teacherlogin():
    return render_template('teacherlogin.html')

@app.route('/registerationask')
def registerationask():
    return render_template('registerationask.html')

@app.route('/studentregister')
def studentregister():
    return render_template('studentregister.html')

@app.route('/teacherregister')
def teacherregister():
    return render_template('teacherregister.html')

@app.route('/displaypuzzles')
def displaypuzzles():
    if session['login'] == "true":
        return render_template('displaypuzzles.html')
    else:
        flash('Please login first to use the service.')
        return render_template('loginask.html')

@app.route('/insertteacher', methods=['GET','POST'])
def insertteacher():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    try:
        cursor.execute("insert into teacher (name, email, password) values (%s,%s,%s)",(name,email,password,))
        connection.commit()
    except pymysql.err.IntegrityError:
        return ("ERROR: email id not available")
    return render_template('successfulregister.html')

@app.route('/insertstudent', methods=['GET','POST'])
def insertstudent():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    try:
        cursor.execute("insert into student (name, email, password) values (%s,%s,%s)",(name,email,password,))
        connection.commit()
    except pymysql.err.IntegrityError:
        return ("ERROR: email id not available")
    return render_template('successfulregister.html')

@app.route('/studentlogincheck', methods=['GET','POST'])
def studentlogincheck():
    email = request.form.get("email")
    password = request.form.get("password")
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    data = cursor.execute("select * from student where email=%s and password=%s",(email,password,))
    #print(data)
    if(len(cursor.fetchall()) > 0):
        session['email'] = email
        session['type'] = "student"
        session['login'] = "true"
        print(session['email'])
        print(session['type'])
        cursor.execute("select sid from student where email=%s ", (email))
        sid = cursor.fetchall()
        cursor.execute("select level from rating where sid=%s ", (sid))
        data = cursor.fetchall()
        session['level']=data[0][0]
        cursor.execute("select name from student where sid=%s ", (sid))
        data1 = cursor.fetchall()
        session['name']=data1[0][0]
        print(session['name'])
        session.modified = True
        return render_template("index.html")
    else:
        print("error")


@app.route('/teacherlogincheck', methods=['GET','POST'])
def teacherlogincheck():
    email = request.form.get("email")

    password = request.form.get("password")

    #print(email, password)
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    #cursor.execute("select * from teacher where email=%s",(email,))
    #user=cursor.fetchone()
    #cursor.close()

    #if len(user) > 0:
     #   if user["password"] == password :
      #      session['name'] = user['name']
        #    session['email'] = user['email']
         #   return render_template('successfullogin.html')
        #else:
         #   return "Error password and email not match"
    #else:
     #   return "Error user not found"

    data = cursor.execute("select * from teacher where email=%s and password=%s", (email, password,))
    data1=cursor.fetchall()
    if (len(data1) > 0):
        #session['name'] = data1['name']
        session['email'] = email
        session['type'] = "teacher"
        session['login'] = "true"
        session['level'] = "teacher"
       # print(session['email'])
       # print(session['type'])
       # print(session['login'])
        session.modified = True
        return render_template("successfullogin.html")
    else:
        print("error")
    return render_template("teacherlogin.html")


@app.route('/storyfrom')
def storyfrom():
    return render_template('storyfrom.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/displaystoryvideos')
def displaystoryvideos():
    return render_template('displaystoryvideos.html')

@app.route('/butterflypuzzle')
def butterflypuzzle():
    if session['level']== "LOW":
        return render_template('butterflypuzzle.html')
    if session['level']== "NORMAL":
        return render_template('butterflypuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('butterflypuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('butterflypuzzle3.html')
    return render_template('butterflypuzzle.html')

@app.route('/homepuzzle')
def homepuzzle():
    if session['level']== "LOW":
        return render_template('homepuzzle.html')
    if session['level']== "NORMAL":
        return render_template('homepuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('homepuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('homepuzzle3.html')
    return render_template('homepuzzle.html')

@app.route('/sunflowerpuzzle')
def sunflowerpuzzle():
    if session['level']== "LOW":
        return render_template('sunflowerpuzzle.html')
    if session['level']== "NORMAL":
        return render_template('sunflowerpuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('sunflowerpuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('sunflowerpuzzle3.html')
    return render_template('sunflowerpuzzle.html')

@app.route('/elephantpuzzle')
def elephantpuzzle():
    if session['level']== "LOW":
        return render_template('elephantpuzzle.html')
    if session['level']== "NORMAL":
        return render_template('elephantpuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('elephantpuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('elephantpuzzle3.html')
    return render_template('elephantpuzzle.html')

@app.route('/treepuzzle')
def treepuzzle():
    if session['level']== "LOW":
        return render_template('treepuzzle.html')
    if session['level']== "NORMAL":
        return render_template('treepuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('treepuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('treepuzzle3.html')
    return render_template('treepuzzle.html')

@app.route('/lionpuzzle')
def lionpuzzle():
    if session['level']== "LOW":
        return render_template('lionpuzzle.html')
    if session['level']== "NORMAL":
        return render_template('lionpuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('lionpuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('lionpuzzle3.html')
    return render_template('lionpuzzle.html')

@app.route('/crabpuzzle')
def crabpuzzle():
    if session['level']== "LOW":
        return render_template('crabpuzzle.html')
    if session['level']== "NORMAL":
        return render_template('crabpuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('crabpuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('crabpuzzle3.html')
    return render_template('crabpuzzle.html')

@app.route('/fishpuzzle')
def fishpuzzle():
    if session['level']== "LOW":
        return render_template('fishpuzzle.html')
    if session['level']== "NORMAL":
        return render_template('fishpuzzle1.html')
    if session['level'] == "GOOD":
        return render_template('fishpuzzle2.html')
    if session['level'] == "EXCELLENT":
        return render_template('fishpuzzle3.html')
    return render_template('fishpuzzle.html')

@app.route('/learningmenu')
def learningmenu():
    if session['login'] == "true":
        return render_template('learningmenu.html')
    else:
        flash('Please login first to use the service.')
        return render_template('loginask.html')

@app.route('/rating')
def rating():
    return render_template('rating.html')

@app.route('/insertrating',methods=['GET','POST'])
def insertrating():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    email=request.form.get("email")
    r1 = request.form.get("radios1")
    r2 = request.form.get("radios2")
    r3 = request.form.get("radios3")
    r4 = request.form.get("radios4")
    r5 = request.form.get("radios5")
    r6 = request.form.get("radios6")
    print(session['type'])
    print(email)
    if(session['type']=="teacher"):
        uemail=session['email']
        cursor.execute("select tid from teacher where email=%s ", (session['email']))
        tid=cursor.fetchall()
        tid = cursor.execute("update student set tid=%s where email=%s ",(tid,email,))
        cursor.execute("select sid from student where email=%s ", (email))
        sid = cursor.fetchall()
        level=mlp.start([[float(r1),float(r2),float(r3),float(r4),float(r5),float(r6)]])
        cursor.execute("insert into rating (listening, reading, speaking, writing, disability, mobility,sid ,level) values (%s,%s,%s,%s,%s,%s,%s,%s)", (r1,r2,r3,r4,r5,r6,sid,level,))
        #cursor.execute("%s ",(tid,email,))
    return render_template('successfulrating.html')


@app.route('/displaylevel')
def displaylevel():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="SLchildren")
    cursor = connection.cursor()
    cursor.execute("select tid from teacher where email=%s ", (session['email']))
    tid = cursor.fetchall()
    cursor.execute("select sid from student where tid=%s ", (tid))
    sid = cursor.fetchall()
    cursor.execute("select level from rating where sid=%s ", (sid))
    data = cursor.fetchall()
    cursor.execute("select name from student where sid=%s ", (sid))
    name = cursor.fetchall()
    cursor.execute("select email from student where sid=%s ", (sid))
    email = cursor.fetchall()
    #array=data['sid']
    #print(data)
    l=len(data)

    return render_template('displaylevel.html',level=data,name=name,email=email,l=l)


@app.route('/searchkeywordssingle', methods=['GET','POST'])
def searchkeywordssingle():
    scenariodata = " "
    scenariodata = request.form.get("scenariodata")
   # print(scenariodata)

    text = scenariodata
    arr2 = ""
    #list1 = (keywords.keywords(text))
    #arr1 = list1.split("\n")
    #l = len(arr1)
    response = m.googleimagesdownload()  # class instantiation

    if session['level']== "LOW":
        arguments = {"keywords": text+" for kids", "limit": 20, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
        l2 = len(arr2)
        return render_template('displayimages.html', list=arr2, l=l2)
    if session['level']== "NORMAL":
        arguments = {"keywords": text+" drawing", "limit": 16, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
        l2 = len(arr2)
        return render_template('displayimages1.html', list=arr2, l=l2)
    if session['level']== "GOOD":
        arguments = {"keywords": text+" animated", "limit": 12, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
        l2 = len(arr2)
        return render_template('displayimages2.html', list=arr2, l=l2)
    if session['level']== "EXCELLENT":
        arguments = {"keywords": text, "limit": 8, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
        l2 = len(arr2)
        return render_template('displayimages3.html', list=arr2, l=l2)
    if session['level']== "TEACHER":
        arguments = {"keywords": text, "limit": 8, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
        l2 = len(arr2)
        return render_template('displayimages3.html', list=arr2, l=l2)

    arguments = {"keywords": text, "limit": 8, "print_urls": True, "no_download": True}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function
    arr2 = m.retrive()
    l2 = len(arr2)
    return render_template('displayimages3.html', list=arr2, l=l2)

@app.route('/searchvideosingle', methods=['GET','POST'])
def searchvideosingle():
    scenariodata = " "
    scenariodata = request.form.get("scenariodata")

    if session['level'] == "EXCELLENT":
        y=v1.YouTubeApi()
        y.search_keyword(scenariodata)
        arr2=v1.retrive1()
        l2 = len(arr2)
        return render_template('displayvideos.html', list=arr2, l=l2)

    if session['level'] == "GOOD":
        y=v2.YouTubeApi()
        y.search_keyword(scenariodata)
        arr2=v2.retrive1()
        l2 = len(arr2)
        return render_template('displayvideos.html', list=arr2, l=l2)

    if session['level'] == "NORMAL":
        y=v3.YouTubeApi()
        y.search_keyword(scenariodata)
        arr2=v3.retrive1()
        l2 = len(arr2)
        return render_template('displayvideos.html', list=arr2, l=l2)

    if session['level'] == "LOW":
        y=v4.YouTubeApi()
        y.search_keyword(scenariodata)
        arr2= v4.retrive1()
        l2 = len(arr2)
        return render_template('displayvideos.html', list=arr2, l=l2)

    y = v4.YouTubeApi()
    y.search_keyword(scenariodata)
    arr2 = v4.retrive1()
    l2 = len(arr2)
    return render_template('displayvideos.html', list=arr2, l=l2)

@app.route('/searchkeywords', methods=['GET','POST'])
def searchkeywords():
    scenariodata = request.form.get("scenariodata")
    text = ""
    text = '""' + scenariodata + '""'
    list1 = (keywords.keywords(text))
    arr1 = list1.split("\n")

    fobj = open("stopwords.txt")
    text1 = fobj.read().strip().split()
    k1 = []
    flag = 0
    for key in arr1:
        for words in text1:
            if key == words:
                flag = 1
                break
            else:
                i = 0
        if flag == 0:
            if key not in k1 and "ing" not in key:
                k1.append(key)
        flag = 0
    fobj.close()

    l = len(k1)
    response = m.googleimagesdownload()  # class instantiation
    for i in range(0,l-1):
        arguments = {"keywords": k1[i]+ " " +k1[i+1], "limit": 8, "print_urls": True, "no_download": True}  # creating list of arguments
        paths = response.download(arguments)  # passing the arguments to the function
        arr2 = m.retrive()
    l2 = len(arr2)

    return render_template('displayimages.html', list=arr2, l=l2)


@app.route('/searchkeywords1', methods=['GET','POST'])
def searchkeywords1():
    scenariodata = request.form.get("scenariodata")
    text = ""
    text = '""' + scenariodata + '""'
    list1 = (keywords.keywords(text))
    arr1 = list1.split("\n")
    #arr1=["hello"]

    fobj = open("stopwords.txt")
    text1 = fobj.read().strip().split()
    k1 = []
    flag = 0
    for key in arr1:
        for words in text1:
            if key == words:
                flag = 1
                break
            else:
                i = 0
        if flag == 0:
            if key not in k1 and "ing" not in key:
                k1.append(key)
        flag = 0
    fobj.close()

    l = len(k1)
    y = v.YouTubeApi()
   # response = m.googleimagesdownload()  # class instantiation
    for i in range(0,l-1):

##############
        if i==0:
            y.search_keyword(k1[i]+" "+k1[i+1])
        else:
            y.search_keyword(k1[i] + " story")
        arr2=v.retrive1()
    l2 = len(arr2)

############
    return render_template('displayvideos.html', list=arr2, l=l2)



if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)