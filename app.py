import os
from flask import Flask, render_template, request, redirect, jsonify, session
from dotenv import load_dotenv
import razorpay
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Razorpay Setup
razorpay_client = razorpay.Client(auth=(
    os.getenv("RAZORPAY_KEY_ID"),
    os.getenv("RAZORPAY_KEY_SECRET")
))

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("VelvoraX_Leads").sheet1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html",
                           key_id=os.getenv("RAZORPAY_KEY_ID"))

@app.route("/create-order", methods=["POST"])
def create_order():
    amount = int(request.form.get("amount")) * 100
    order = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })
    return jsonify(order)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        sheet.append_row([name, email, phone, message])
        return redirect("/contact")

    return render_template("contact.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form["password"] == os.getenv("ADMIN_PASSWORD"):
            session["admin"] = True
            return redirect("/admin")

    if session.get("admin"):
        records = sheet.get_all_records()
        return render_template("admin.html", leads=records)

    return '''
        <form method="POST">
            <input type="password" name="password" placeholder="Admin Password"/>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
