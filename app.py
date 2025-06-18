from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'studentName' in request.form and 'studentPassword' in request.form:
        name = request.form['studentName']
        password = request.form['studentPassword']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE name = %s AND password = %s', (name, password))
        student = cursor.fetchone()
        if student:
            session['loggedin'] = True
            session['id'] = student['id']
            session['name'] = student['name']
            return redirect('/index')
        else:
            msg = 'Incorrect username or password!'
    return render_template('login.html', msg=msg)

@app.route('/index')
def index():
    if 'loggedin' in session:
        return render_template('index.html', name=session['name'])
    return redirect('/')

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE id = %s', (session['id'],))
        student = cursor.fetchone()
        return render_template('profile.html', student=student)
    return redirect('/')

@app.route('/marks')
def marks():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT subject, mark FROM marks WHERE student_id = %s', (session['id'],))
        marks = cursor.fetchall()
        student_marks = {m['subject']: m['mark'] for m in marks}
        return render_template('marks.html', student_marks=student_marks)
    return redirect('/')

@app.route('/fees')
def fees():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM fees WHERE student_id = %s', (session['id'],))
        fee = cursor.fetchone()
        return render_template('fees.html', fee=fee)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
