import flask
import forms
from user import User

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "very_secret_key"


@app.route("/")
def list_of_users():
    if len(User.users_list) > 0:
        return flask.render_template("userlist.html", data=User.users_list)
    return "There is no user added.<br> Plese add user using path <em>/add_user</em>"


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    form = forms.UserForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        user = User(username=username, email=email)
        User.users_list.append(user)

        return flask.render_template("user_added.html", user=user)

    return flask.render_template("form.html", form=form)


app.run(debug=True)
