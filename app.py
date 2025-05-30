from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import bcrypt
from functools import wraps

app = Flask(__name__)
app.secret_key = 'Shakir is cool'  

def get_db_connection():
    return mysql.connector.connect(
        host='centerbeam.proxy.rlwy.net',
        user='root',
        password='kEPKdZOjlSUsRKoRZvfBXEQIpGhCjJTT',
        database='railway',
        port=23147
    )



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('patients.html', patients=patients)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(password, user['password'].encode('utf-8')):
            session['username'] = username
            session['user_role'] = user['role']
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_role') != 'admin':
            flash("You must be admin to access this page.")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/add_patient', methods=['GET', 'POST'])
@admin_required
def add_patient():
    if request.method == 'POST':
        pname = request.form['pname']
        age = request.form['age']
        address = request.form['address']
        gender = request.form['gender']
        blood_group = request.form['blood_group']
        mobile = request.form['mobile']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO patients (pname, age, address, gender, blood_group, mobile)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (pname, age, address, gender, blood_group, mobile))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Patient added successfully.")
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/edit_patient/<int:pid>', methods=['GET', 'POST'])
@admin_required
def edit_patient(pid):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        pname = request.form['pname']
        age = request.form['age']
        address = request.form['address']
        gender = request.form['gender']
        blood_group = request.form['blood_group']
        mobile = request.form['mobile']

        cursor.execute("""
            UPDATE patients SET pname=%s, age=%s, address=%s, gender=%s, blood_group=%s, mobile=%s
            WHERE pid=%s
        """, (pname, age, address, gender, blood_group, mobile, pid))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Patient updated successfully.")
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM patients WHERE pid=%s", (pid,))
    patient = cursor.fetchone()
    cursor.close()
    conn.close()
    if not patient:
        flash("Patient not found.")
        return redirect(url_for('index'))
    return render_template('add_patient.html', patient=patient)

@app.route('/delete_patient/<int:pid>')
@admin_required
def delete_patient(pid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE pid=%s", (pid,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Patient deleted successfully.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
