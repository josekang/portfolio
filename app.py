
from flask import Flask, render_template, url_for, redirect, flash, request
from myproject import ContactForm
from myproject import mail
from flask_mail import Message
from myproject import app

#home route
@app.route("/", methods = ["GET", "POST"])
def home():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required")
            return render_template("home.html", form = form)

        else:
            msg = Message(form.subject.data, sender = "contact@example.com", recipients = ["josekangethe2@gmail.com"])
            msg.body = """
            From: %s &lt;%s&gt;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template("home.html", success = True)

    elif request.method == "GET":
        return render_template("home.html", form = form)


    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
