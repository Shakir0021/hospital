from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "mysecretkey")  # fallback

# MySQL connection
try:
    db = mysql.connector.connect(
        host='centerbeam.proxy.rlwy.net',
        user='root',
        password='kEPKdZOjlSUsRKoRZvfBXEQIpGhCjJTT',
        database='railway',
        port=23147
    )
    cursor = db.cursor(dictionary=True)
    print("[✅] Connected to Railway MySQL Database")
except Exception as e:
    print("[❌] Database connection failed:", e)

# ROUTES

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/doctors")
def doctors():
    doctors = [
        {
            "name": "Dr. Ayesha Siddiqui",
            "speciality": "IVF Specialist",
            "description": "Expert in infertility treatments, IVF & reproductive health.",
            "timing": "10 AM - 2 PM"
        },
        {
            "name": "Dr. Neha Sharma",
            "speciality": "Gynecologist",
            "description": "Experienced in maternity, childbirth and women's health.",
            "timing": "4 PM - 7 PM"
        },
        {
            "name": "Dr. Firoz Khan",
            "speciality": "Gynecologist & Obstetrician",
            "description": "Specialist in high-risk pregnancies and reproductive health.",
            "timing": "9 AM - 12 PM"
        }
    ]
    return render_template("doctors.html", doctors=doctors)

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        name = request.form['name']
        contact = request.form['contact']
        department = request.form['department']
        date = request.form['date']

        try:
            cursor.execute(
                "INSERT INTO appointments (name, contact, department, date) VALUES (%s, %s, %s, %s)",
                (name, contact, department, date)
            )
            db.commit()
            flash("✅ Appointment booked successfully!", "success")
        except Exception as e:
            print("[❌] Error:", e)
            flash("❌ Failed to book appointment.", "danger")

        return redirect("/appointment")
    return render_template("appointment.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Run
if __name__ == "__main__":
    app.run(debug=True)
