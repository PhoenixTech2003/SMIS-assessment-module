from flask import Flask, render_template, request
import mysql.connector


list_of_programs = ['BIS', 'BIT']
list_of_classes = ['BIS3','BIT3']
list_of_gender = ['M','F']



def insert_student(first_name, last_name, program_id, gender, class_id, reg_no):
    db = mysql.connector.connect(
        host = "localhost",
        user ="chiyembekezo",
        password = "Alphawolf@20",
        database = "smis_assessment_module"
    )
    cursor = db.cursor()

    query = "INSERT INTO student(student_id,program_id,class_id,first_name, last_name, gender) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (reg_no, program_id, class_id, first_name, last_name,gender)

    cursor.execute(query, values)
    db.commit()

    db.close()


def select_all_students():
    db = mysql.connector.connect(
        host = "localhost",
        user ="chiyembekezo",
        password = "Alphawolf@20",
        database = "smis_assessment_module"
    )

    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM student ORDER BY class_id"
    cursor.execute(query)

    result = cursor.fetchall()
    db.close()

    return result
    




app = Flask(__name__)

@app.route('/')
def hello_world():
    record = select_all_students()
    gender = list_of_gender
    classes = list_of_classes
    programs = list_of_programs
    return render_template("index.html", record = record, gender=gender, classes= classes, programs=programs)

@app.route("/add_student")
def add_student():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    reg_no = request.args.get('reg_no')
    program_id = request.args.get('program')
    classes = request.args.get('class')
    gender = request.args.get('gender')
    insert_student(first_name.upper(), last_name.upper(), program_id, gender, classes, reg_no.upper())
    record = select_all_students()
    return render_template("index.html", record = record)


