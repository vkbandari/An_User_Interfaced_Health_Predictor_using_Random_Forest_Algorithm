from flask import Flask,render_template,request,session,redirect,url_for,json
import pymysql
import time
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import confusion_matrix,accuracy_score
db = pymysql.connect(host='localhost',user='root',password='password',db='health_predictor')
cursor = db.cursor()

app = Flask(__name__)
app.secret_key = "Enter a random secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signup')
def signup():
    return render_template('signup.html',msg="signup")

@app.route('/Signup',methods=["POST","GET"])
def signup_submitted():
    if request.method == "POST":
        time1 = int(round(time.time() * 1000))
        reg_id = "Admin" + str(time1)
        now = datetime.now().strftime('%c')
        reg_id1 = "User" + str(time1)
        if request.method == "POST":
            uname = request.form['uname']
            emailid = request.form['emailid']
            password1 = request.form['password1']
            phnumber = request.form['phnumber']
            date = request.form['date']
            address = request.form['address']
            city = request.form['city']
            selected = request.form['selected']
            sql = "select email,phone_number from reg where (email='%s' or phone_number ='%s') and user_type='%s'" % (
            emailid, phnumber, selected)
            cursor.execute(sql)
            signup_results = cursor.fetchall()
            if (len(signup_results) > 0):
                if (signup_results[0][0] == emailid):
                    print("entered emailid is already exits")
                    return render_template('index.html', msg="emailid_exits")
                elif (signup_results[0][0] == phnumber):
                    print("entered phone number is already exits")
                    return render_template('signup.html', msg="phonenumber_exits")
            else:
                if (selected == "admin"):
                    sql = "insert into reg(reg_id,username,email,password,phone_number,dob,address,city,user_type,reg_timedate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                          % (reg_id, uname, emailid, password1, phnumber, date, address, city, selected, now)
                    cursor.execute(sql)
                    db.commit()
                    return render_template('signup.html', msg="successfully_registered")
                if (selected == "user"):
                    sql = "insert into reg(reg_id,username,email,password,phone_number,dob,address,city,user_type,reg_timedate) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                          % (reg_id1, uname, emailid, password1, phnumber, date, address, city, selected, now)
                    cursor.execute(sql)
                    db.commit()
                    return render_template('signup.html', msg="successfully_registered")
    return render_template('index.html')

@app.route('/Signin')
def signin():
    return render_template('index.html')

@app.route('/Signin/Submited/',methods=["POST","GET"])
def signin_submitted():
    if request.method == "POST":
        emailid = request.form['emailid']
        password1 = request.form['password1']
        selected = request.form['selected']
        sql = "select password,username from reg where email = '%s' and user_type = '%s'"%(emailid,selected)
        cursor.execute(sql)
        login_results = cursor.fetchall()
        # session['username'] = login_results[0][1]
        # username = session['username']
        # print(username)
        print(login_results,emailid,selected)
        sql1 = "select password,name from doctor_reg where email = '%s'" % (emailid)
        cursor.execute(sql1)
        doctor_results = cursor.fetchall()
        # doctorname = session['doc_name']
        if(len(login_results)>0):
            if(selected == "admin"):
                if(login_results[0][0] == password1):
                    session['admin_email'] = emailid
                    return redirect(url_for('admin_homepage'))
                else:
                    return render_template('index.html',msg="invalid_password")
            if (selected == "user"):
                if (login_results[0][0] == password1):
                    session['user_email'] = emailid
                    return redirect(url_for('user_homepage'))
                else:
                    return render_template('index.html',msg="invalid_password")
        else:
            if len(doctor_results)>0:
                if selected == "doctor":
                    if(doctor_results[0][0]==password1):
                        session['doc_email']=emailid
                        return redirect(url_for('doctor_homepage'))
                    else:
                        return render_template('index.html',msg="invalid_password")
            else:
                return render_template('index.html', msg="invalid_emailid")

            return render_template('index.html',msg="invalid_emailid")
        return render_template('index.html')
    return render_template('index.html')

@app.route('/Admin-Homepage')
def admin_homepage():
    if 'admin_email' in session:
        admin_email = session['admin_email']
        if(admin_email == None):
            return redirect(url_for('index'))
    return render_template('admin.html')

@app.route('/User-Homepage')
def user_homepage():
    if 'user_email' in session:
        user_email = session['user_email']
        if(user_email == None):
            return redirect(url_for('index'))
    return render_template('user.html')

@app.route('/Doctor-Homepage')
def doctor_homepage():
    if 'doc_email' in session:
        doc_email=session['doc_email']
        if doc_email == None:
            return redirect(url_for('index'))
    return render_template('doctor_dashboard.html')
@app.route('/Admin-Homepage/Add-Doctors/')
def add_doctors():
    return render_template('add_doctors.html')

@app.route('/Admin-Homepage/Add-Doctors/Submitted',methods=["POST","GET"])
def add_doctors_submitted():
    if request.method == "POST":
        uname = request.form['uname2']
        emailid = request.form['emailid']
        phnumber = request.form['phnumber']
        city = request.form['city']
        age = request.form['age']
        specialist = request.form['specialist']
        gender = request.form['gender']
        hname=request.form['hname']
        haddress=request.form['haddress']
        landmark=request.form['landmark']
        specification=request.form['selected']
        password='doctor@1234'
        sql = "select email,phnumber from doctor_reg where email ='%s' or phnumber ='%s'"%(emailid,phnumber)
        cursor.execute(sql)
        add_doctors_results=cursor.fetchall()
        if(len(add_doctors_results)>0):
            if(add_doctors_results[0][0] == emailid):
                return render_template('add_doctors.html',msg="emailid_exits")
            if(add_doctors_results[0][1] == phnumber):
                return render_template('add_doctors.html', msg="phone_exits")
        else:
            now = datetime.now()
            status = "active"
            sql = "insert into doctor_reg(name,email,'password',phnumber,hname,haddress,city,landmark,age,specailist,specification,gender,date_of_reg) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                  %(uname,emailid,password,phnumber,hname,haddress,city,landmark,age,specialist,specification,gender,now)
            cursor.execute(sql)
            db.commit()
            return render_template('add_doctors.html',msg="successfully_added")
        # print(uname)
    return render_template('add_doctors.html')

@app.route('/View-Doctor')
def view_doctor():
    sql = "select * from doctor_reg"
    cursor.execute(sql)
    view_doctor_results = cursor.fetchall()
    return render_template('view_doctor.html',results=view_doctor_results)

@app.route('/View-users/')
def view_user():
    sql = "select * from reg where user_type ='%s'"%('user')
    cursor.execute(sql)
    view_user_results = cursor.fetchall()
    return render_template('view_users.html', results=view_user_results)

@app.route('/Viewsuser-Doctor')
def userview_doctor():
    sql = "select * from doctor_reg"
    cursor.execute(sql)
    view_doctor_results = cursor.fetchall()
    return render_template('userview_doctor.html',results=view_doctor_results)

@app.route('/Model-performance/')
def model_performance():
    return render_template('model_performance.html',msg="csv_uploaded")

@app.route('/Model-Performance/csv_submitted',methods=["POST","GET"])
def model_performance_csv_submitted():
    if request.method == "POST":
        csvfile1 =request.files['xtrain']
        csvfile2 = request.files['xtest']
        csvfile3 = request.files['ytrain']
        csvfile4 = request.files['ytest']
        x_train = csvfile1.filename
        xtest = csvfile2.filename
        ytrain = csvfile3.filename
        ytest = csvfile4.filename
        return render_template('model_performance.html',msg="select_model",xtrain = x_train,ytrain=ytrain,xtest=xtest,ytest=ytest)
    return render_template('model_performance.html',msg="select_model")

@app.route('/Model-Performance/model_submitted/<xtrain>/<ytrain>/<xtest>/<ytest>/',methods=["POST","GET"])
def selected_model_submitted(xtrain,ytrain,xtest,ytest):
    print(xtrain,ytrain,xtest,ytest)
    if request.method == "POST":
        selected = int(request.form['selected'])
        x_train = pd.read_csv(xtrain).drop("Unnamed: 0",axis=1)
        y_train = pd.read_csv(ytrain).drop("Unnamed: 0",axis=1)
        x_test = pd.read_csv(xtest).drop("Unnamed: 0",axis=1)
        y_test = pd.read_csv(ytest).drop("Unnamed: 0",axis=1)

        if (selected == 1):
            clf = RFC(random_state=21, bootstrap=True, max_depth=5, max_features=3, min_samples_leaf=3,
                      min_samples_split=2, n_estimators=25)

            clf.fit(x_train, y_train)
            pred = clf.predict(x_test)

            accuracy = accuracy_score(pred, y_test)
            result=round(accuracy*100,2)

            print(f"Accuracy on Test dataset = {round(accuracy,2)}")

            def plot_confusion_matrix(cm, classes,
                                      normalize=False,
                                      title='Confusion matrix',
                                      cmap=plt.cm.Blues):
                """
                See full source and example:
                http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

                This function prints and plots the confusion matrix.
                Normalization can be applied by setting `normalize=True`.
                """
                plt.imshow(cm, interpolation='nearest', cmap=cmap)
                plt.title(title)
                plt.colorbar()
                tick_marks = np.arange(len(classes))
                plt.xticks(tick_marks, classes, rotation=45)
                plt.yticks(tick_marks, classes)

                if normalize:
                    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
                    print("Normalized confusion matrix")
                else:
                    print('Confusion matrix, without normalization')

                thresh = cm.max() / 2.
                for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
                    plt.text(j, i, cm[i, j],
                             horizontalalignment="center",
                             color="white" if cm[i, j] > thresh else "black")

                plt.tight_layout()
                plt.ylabel('True label')
                plt.xlabel('Predicted label')
                plt.show()

            # assigning labels to "y_test" and "pred"
            pred = pred.astype(object)
            for i, row in enumerate(pred):
                if row == 0:
                    pred[i] = "Negative"
                else:
                    pred[i] = "Positive"
            y_test = pd.Series(y_test['diagnosis'])
            # print(f"{y_test} ,{y_test.dtype}")
            for index in y_test.index:
                if y_test[index] == 0:
                    y_test[index] = "Negative"
                else:
                    y_test[index] = "Positive"

            labels = ["Positive", "Negative"]

            cm = confusion_matrix(pred, y_test, labels)

            plot_confusion_matrix(cm, classes=["Positive", "Negative"])
            return render_template('model_performance.html',msg="accuary",result_accu=result,model="Random Forest")
    return render_template('model_performance.html')

@app.route('/User/Heart-Analysis/')
def heart_analysis():
    return render_template('heart_analysis.html')

@app.route('/User/Heart-Analysis/Submitted',methods=["POST","GET"])
def heart_analysis_submitted():
    if request.method == "POST":
        list1 = []
        # csvfile = request.files['xtarin']
        #
        # x_train = csvfile.filename
        # print(x_train)
        # csvfile1 = request.files['ytarin']
        # y_train = csvfile1.filename
        # print(y_train)

        age = request.form['age']
        print(age)
        sex = request.form['sex']
        print(sex)
        chestpain = request.form['chestpain']
        print(chestpain)
        trestbps = request.form['trestbps']
        print(trestbps)
        serumcholestoral = request.form['serumcholestoral']
        print(serumcholestoral)
        fbs = request.form['fbs']
        print(fbs)
        restecg = request.form['restecg']
        print(restecg)
        thalach = request.form['thalach']
        print(thalach)
        exang = request.form['exang']
        print(exang)
        oldpeak = request.form['oldpeak']
        print("oldpeak",oldpeak)
        slope = request.form['slope']
        print(slope)
        majorvessels = request.form['majorvessels']
        print(majorvessels)
        Thal = request.form['Thal']
        print(Thal)
        list1.extend([age,sex,chestpain,trestbps,serumcholestoral,fbs,restecg,thalach,exang,oldpeak,slope,majorvessels,Thal])
        print(list1)
        x_train = pd.read_csv('x_train.csv').drop("Unnamed: 0", axis=1)
        print(x_train)
        y_train = pd.read_csv('y_train.csv').drop("Unnamed: 0", axis=1)
        print(y_train)
        clf = RFC(random_state=21, bootstrap=True, max_depth=5, max_features=3, min_samples_leaf=3, min_samples_split=2,
                  n_estimators=25)
        clf.fit(x_train, y_train.values.ravel())
        list2 = pd.DataFrame(np.array(list1).reshape(1, 13), columns=x_train.columns)
        pred = clf.predict(list2)
        predict = pred[0]
        return render_template('heart_analysis.html', msg1="predicted_successfully", results=predict)
    return render_template('heart_analysis.html')

@app.route('/User/Dengu-Analysis/')
def dengu_analysis():
    return render_template('dengu_analysis.html')

@app.route('/User/Dengu-Analysis/Submitted',methods=["POST","GET"])
def dengu_analysis_submitted():
    if request.method == "POST":
        try:
            list1 = []
            # csvfile = request.files['xtarin']
            # x_train = csvfile.filename
            # print(x_train)
            # csvfile1 = request.files['ytarin']
            # y_train = csvfile1.filename
            # print(y_train)
            skinrash = request.form['skinrash']
            chills = request.form['chills']
            jointpain = request.form['jointpain']
            vomiting = request.form['vomiting']
            fatigue = request.form['fatigue']
            highfever = request.form['highfever']
            sweating = request.form['sweating']
            headache = request.form['headache']
            nausea = request.form['nausea']
            lossofappetite = request.form['lossofappetite']
            painbehindtheeyes = request.form['painbehindtheeyes']
            backpain = request.form['backpain']
            constipation = request.form['constipation']
            Abdominalpain = request.form['Abdominalpain']
            diarrhoea = request.form['diarrhoea']
            malaise = request.form['malaise']
            toxiclook = request.form['toxiclook']
            musclepain = request.form['musclepain']
            Redspotsoverbody = request.form['Redspotsoverbody']
            bellypain = request.form['bellypain']
            list1.extend([skinrash,chills,jointpain,vomiting,fatigue,highfever,sweating,headache,nausea,lossofappetite,painbehindtheeyes,
                          backpain,constipation,Abdominalpain,diarrhoea,malaise,toxiclook,musclepain,Redspotsoverbody,bellypain])
            x_train = pd.read_csv('df_x.csv').drop("Unnamed: 0", axis=1)
            print(x_train)
            y_train = pd.read_csv('df_y.csv').drop("Unnamed: 0", axis=1)
            print(y_train)
            clf = RFC(random_state=123)
            clf.fit(x_train, y_train)
            list2 =  pd.DataFrame(np.array(list1).reshape(1, 20), columns=x_train.columns)
            pred = clf.predict(list2)
            print(pred)
            predict = pred[0]
            return render_template('dengu_analysis.html', msg1="predicted_successfully", results=predict)
        except:
            return render_template('dengu_analysis.html', msg2="Please select all options")

    return render_template('dengu_analysis.html')


@app.route('/user/book_appointment/<name>',methods=["POST","GET"])
def book_appointment(name):
    print(name)
    sql="select * from reg where email='%s'" %(session['user_email'])
    cursor.execute(sql)
    a=cursor.fetchall()
    print(a)
    sql_1="select * from doctor_reg where specification='%s'" %(name)
    cursor.execute(sql_1)
    b=cursor.fetchall()
    return render_template("book_appointment.html",result=a,doctor=b,name=name)

@app.route('/user/book_appointment1',methods=['POST','GET'])
def book_appointment1():
    if request.method=="POST":
        print("hiiiiiiiiii")
        pno = request.form['pno']
        date = request.form['date']
        print(pno,date)
        sql_q = "select pnumber from user_appointment where pnumber='%s'" % (pno)
        cursor.execute(sql_q)
        pno1 = cursor.fetchall()
        print(pno1)
        if pno1:
            return json.dumps({'status': 'OK', 'user': "Mobileno already exist", 'pass': date})
        return render_template({'status': 'OK', 'user': "mobileno", 'pass': date},msg="confirmed")
    return render_template("book_appointment.html")


@app.route('/user/appointment_submitted',methods=["POST","GET"])
def appointment_submited():
    if request.method=="POST":
        dname=request.form['dname']
        demail=request.form['demail']
        uname=request.form['uname']
        disease=request.form['disease']
        pno=request.form['pno']
        date=request.form['date']
        print(demail)

        sql="insert into user_appointment(doctor_name,doctor_email,user_name,disease,pnumber,date_of_appointment,user_email) values('%s','%s','%s','%s','%s','%s','%s')"%(dname,demail,uname,disease,pno,date,session['user_email'])
        cursor.execute(sql)
        db.commit()
        session['user']=uname
        print(session['user'])
        return render_template("book_appointment.html",msg="submitted")
    return render_template("book_appointment.html")

@app.route('/user/view_appointment',methods=["POST","GET"])
def view_appointment():
    if 'user' in session:
        name=session['user']
        sql="select * from user_appointment where user_name='%s'" %(name)
        cursor.execute(sql)
        view=cursor.fetchall()
        return render_template("view_appointment.html",resilt=view)
    return render_template("view_appointment.html")

@app.route('/doctor/View-user-appointment-details/')
def doctor_viewuserdetails():
    sql = "select * from user_appointment where doctor_email = '%s' order by date_of_appointment DESC limit 3"%(session['doc_email'])
    cursor.execute(sql)
    doctor_userdetails=cursor.fetchall()
    # print(doctor_userdetails)
    return render_template('doctor_userdetails.html',results=doctor_userdetails)

@app.route('/doctor/user-precautions/submitted/<int:id>/',methods=["POST","GET"])
def precautions_submitted(id=id):
    pid=(id)
    sql = "select *from user_appointment where a_id ='%s' "%(id)
    cursor.execute(sql)
    result=cursor.fetchall()
    if request.method == "POST":
        print("hello enttered here ")
        pname=request.form['pname']
        disease = request.form['disease']
        precautions = request.form['precautions']
        sql = "insert into paitent_precautions (username,disease,precautions,patient_a_id,user_email) values('%s','%s','%s','%s','%s')"%(pname,disease,precautions,pid,result[0][7])
        cursor.execute(sql)
        db.commit()
        return redirect(url_for('doctor_viewuserdetails'))
    return render_template('precautions.html',results=result)

@app.route('/user/doctor-Precautions/')
def doctor_precautions():
    sql = "select * from paitent_precautions where user_email = '%s'"%(session['user_email'])
    cursor.execute(sql)
    appointment_results = cursor.fetchall()
    return render_template('userprecautions.html',msg=appointment_results)

@app.route('/logout')
def logout():
    session['admin_email'] = None
    session['user_email'] = None
    session['doc_email']=None
    return redirect(url_for('index'))



app.run()
