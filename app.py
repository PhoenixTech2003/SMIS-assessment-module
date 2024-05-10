from flask import Flask, render_template, request
import mysql.connector

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
    




app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")