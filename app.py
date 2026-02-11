from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        mobile = request.form["mobile"]
        service = request.form["service"]

        # 🔹 Google Form Integration (Replace with your form link)
        google_form_url = "YOUR_GOOGLE_FORM_RESPONSE_URL"

        form_data = {
            "entry.1234567890": name,
            "entry.0987654321": mobile,
            "entry.1111111111": service
        }

        requests.post(google_form_url, data=form_data)

        return redirect("/")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
