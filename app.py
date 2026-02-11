from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Services Page
@app.route("/services")
def services():
    return render_template("services.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Pricing Page
@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
