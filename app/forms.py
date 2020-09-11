from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    signIn = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired()])
    # email = StringField('Email', validators = [Email()])
    # password = PasswordField('Password', validators=[DataRequired()] )
    # password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')] )
    # submit = SubmitField('Register')

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username).first()
    #     if user is not None:
    #         raise ValidationError('Please choose a different username')
    
    # def validate_email(self, email):
    #     user = User.query.filter_by(username=email).first()
    #     if user is not None:
    #         raise ValidationError('Please choose a different email')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
		