from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>VelvoraX</h1>
    <p>Official Super Platform of Velvoro Software Solution</p>
    """

if __name__ == "__main__":
    app.run()
