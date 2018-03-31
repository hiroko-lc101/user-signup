from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config["DEBUG"] = True

def input_space_check(string):
    if (string.count(" ") != 0):
        return True

def input_length_check(string):
    if len(string) < 3 or len(string) > 20:
        return True

@app.route("/signup", methods=["POST"])
def signup():
    # look inside the request to figure out what the user typed
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify-password"]
    email = request.form["email"]

    error = ""
    # username
    if input_space_check(username) or input_length_check(username):
        error = "1"
        username = ""
    else:
        error="0"
    # password
    if input_space_check(password) or input_length_check(password):
        error += "1"
    else:
        error += "0"
    # verify password
    if verify_password == "" or verify_password != password:
        error += "1"
    else:
        error += "0"
    password = ""
    verify_password = ""
    # email
    if email != "":
        if (email.count("@") != 1 or email.count(".") != 1 or
            input_space_check(email) or input_length_check(email)):
            error += "1"
            email = ""
        else:
            error += "0"
    else:
        error += "0"
    if error.count("1") != 0:
        return render_template("index.html", error=error, 
            username=username, password=password, 
            verify_password=verify_password, email=email)

#    return render_template("welcome.html", username=username)
    return redirect("/welcome?username=" + username)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template("index.html", error=encoded_error)

app.run()