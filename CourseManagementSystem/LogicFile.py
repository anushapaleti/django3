from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

from Module.FacultyModule.FacultyLogic import *
from sqlalchemy.dialects.postgresql import psycopg2

app = Flask(__name__)

app.secret_key = '123'

DATABASE = 'deepak.db'


def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


create_table()


@app.route('/')
def index():
    return render_template("Project/ProjectHomepage.html")


@app.route('/FacultyHomepage')
def FacultyHomepage():
    # Check if the user is logged in
    if 'user_id' in session:
        return render_template("Faculty/FacultyHomepage.html")
    else:
        return redirect(url_for('loginpagecall'))


@app.route('/signuppagecall')
def signuppagecall():
    return render_template('Project/Signup.html')


@app.route('/signup', methods=['POST'])
def signuplogic():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phone_number']

    # Insert user into the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, email, phone_number) VALUES (?, ?, ?, ?)',
                   (username, password, email, phone_number))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


@app.route('/loginpagecall')
def loginpagecall():
    return render_template('Project/Login.html')


@app.route('/loginlogic', methods=['POST'])
def loginlogic():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the username and password match a record in the database
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            # Store the user_id in the session upon successful login
            session['user_id'] = user[0]

            # Redirect based on the length of the username
            if len(username) == 4:
                return redirect(url_for('FacultyHomepage'))

        else:
            # Invalid credentials, show an error message
            return render_template('Project/Login.html', error='Invalid username or password')

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # Clear the user_id from the session
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/addst')
def student_form():
    return render_template('Faculty/student_Details_form.html')


@app.route('/submit_student', methods=['POST'])
def submit_student():
    name = request.form['name']
    age = request.form['age']
    phone_number = request.form['phone_number']
    aadhar_number = request.form['aadhar_number']
    email_id = request.form['email_id']
    return insert_function(name, age, phone_number, aadhar_number, email_id)


@app.route('/crud')
def crud_display():
    return render_template('Faculty/crud.html')

import psycopg2
@app.route('/view_students')
def view_students():
    conn = psycopg2.connect(
        database='CMS', user='postgres',
        password='Harika@2609',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM StudentDetails ''')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('Faculty/View_students.html', students=students)





@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    # student_id = request.form['student_id']
    # Delete student record from the database
    conn = psycopg2.connect(
        database='CMS', user='postgres',
        password='Harika@2609',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM studentdetails WHERE student_id = %s', (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('view_students'))



@app.route('/update_student/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if request.method == 'GET':
        # Get student details from database
        conn = psycopg2.connect(
            database='CMS', user='postgres',
            password='Harika@2609',
            host='127.0.0.1', port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM studentdetails WHERE student_id = %s', (student_id,))
        student_data = cursor.fetchone()  # Fetch the first (and hopefully only) record
        cursor.close()
        conn.close()

        if student_data:
            # Prepare data for template (assuming student_data is a dictionary)
            return render_template('update_student.html', student=student_data)
        else:
            return f"Student with ID {student_id} not found."

    elif request.method == 'POST':
        # Update student details in database
        updated_name = request.form['name']  # Access form data
        updated_email = request.form['email']  # Access form data

        conn = psycopg2.connect(
            database='CMS', user='postgres',
            password='Harika@2609',
            host='127.0.0.1', port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE studentdetails
            SET name = %s, email = %s
            WHERE student_id = %s
        ''', (updated_name, updated_email, student_id))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('view_students'))  # Redirect to student list view

    else:
        return "Unsupported method!"




if __name__ == '__main__':
    app.run(debug=True)
