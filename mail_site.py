from flask import Flask, redirect, url_for, render_template, request, session
from auto_mail import send_mail
from auto_mail import process_file

app = Flask(__name__)

# Defining the home page of our site
# to do: fix validation, work on getting inputs from user (csv), remember me, sessions
app.config["SECRET_KEY"] = '0a8a8ba8c2ba57c2662af4e630ef0ebb'


@app.route("/", methods=["GET", "POST"])  # this sets the route to this page
def home():

    errors = ""
    if request.method == "POST":
        email_address = None
        email_password = None
        message = None
        subject = None
        csv_file = request.files["input_file"]

        try:
            email_address = str(request.form["email_address"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(
                request.form["email_address"])
        try:
            email_password = str(request.form["email_password"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(
                request.form["email_password"])

        try:
            subject = str(request.form["subject"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(
                request.form["subject"])
        try:
            message = str(request.form["message"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(
                request.form["message"])

        if email_address is not None and email_password is not None and message is not None and subject is not None:
            if request.form["action"] == "Send Mail":
                send_mail(email_address, email_password,
                          process_file(csv_file), subject, message)

                return render_template("email_sent.html")

    return render_template("index.html").format(errors=errors)


@app.route("/email_sent")
def sent():
    return render_template("email_sent.html")


@app.route("/how_to_use")
def instructions():
    return render_template("how_to_use.html")


if __name__ == "__main__":
    app.run(debug=True)
