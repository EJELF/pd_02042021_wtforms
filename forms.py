from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
from user import User


class UserForm(FlaskForm):

    username = StringField(
        label="Username",
        validators=[InputRequired(), EqualTo(fieldname=(user for user in User.users_list))]
    )

    email = StringField(
        label="E-mail",
        validators=[InputRequired(), Email(message="Enter valid email")]
    )
    submit = SubmitField(label="Submit")




