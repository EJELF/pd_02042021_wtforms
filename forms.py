from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, ValidationError
from user import User


class UserForm(FlaskForm):

    username = StringField(
        label="Username:",
        validators=[InputRequired()]
    )

    email = StringField(
        label="E-mail:",
        validators=[InputRequired(), Email(message="Enter valid email")]
    )
    submit = SubmitField(label="Submit")

    def validate_username(self, username):
        for user in User.users_list:
            if user.username == self.username.data:
                raise ValidationError(
                    f"User with username {self.username.data } already exists!"
                )


