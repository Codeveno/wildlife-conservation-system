from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/species")
def species():
    return render_template("species.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

if __name__ == "__main__":
    app.run(debug=True)