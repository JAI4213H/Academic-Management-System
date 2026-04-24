from flask import Flask,request,url_for, redirect, render_template,session

app = Flask(__name__)
app.secret_key = "supersecret124r152"




teachers = {
    "teacher1": "pass123",
    "john_sir": "maths@123",
    "ai_prof": "ml2026",
    "physics_guru": "quantum456"
}
students_password = {
    "jai": "1234",
    "rahul": "pass567",
    "ananya": "secure999",
    "rohit": "abc123"
}
students_marks = {
    "jai": {
        "maths": 95,
        "science": 88,
        "english": 90
    },
    "rahul": {
        "maths": 70,
        "science": 75,
        "english": 80
    },
    "ananya": {
        "maths": 98,
        "science": 92,
        "english": 94
    },
    "rohit": {
        "maths": 60,
        "science": 65,
        "english": 70
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login/teacher", methods = ["POST", "GET"])
def teacherlogin():
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in teachers and password == teachers[username]:
            session["user"] = username
            return redirect(url_for("dash"))
        else:
            return render_template("teacher_login.html", error="Invalid credentials")
    else:
        return render_template("teacher_login.html")
        
        
    
    
    
@app.route("/login/student", methods = ["POST", "GET"])
def studentlog():
        
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in students_password and password == students_password[username]:
            session["user"] = username
            return redirect(url_for("studentdash"))
        
        else:
            return render_template("teacher_login.html", error="Invalid credentials")
    else:
        
        return render_template("student_login.html")
    
    
@app.route("/studentdash")
def studentdash():
    name = session["user"]
    maths = students_marks[name]['maths']
    science = students_marks[name]['science']
    english = students_marks[name]['english']
    return render_template("stuDashboard.html", name = name,maths = maths,science = science,english = english)































if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    