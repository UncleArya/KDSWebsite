from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from src.contact import NotificationManager


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        name = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        message = request.form["message"]
        print(name, email, phone, message)
        NotificationManager(name, subject, email, phone, message).send_email()
        return render_template("contact_submitted.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")

    if request.method == "POST":
        name = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        message = request.form["message"]
        print(name, email, phone, message)
        NotificationManager(name, email, phone, subject, message).send_email()
        return render_template("contact_submitted.html")


# To use while editing
if __name__ == "__main__":
    app.run(debug=True)
