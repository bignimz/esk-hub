from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from flask_login import current_user
from app.models import User

class RegistrationForm(FlaskForm):
      username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
      email = StringField('Email', validators=[DataRequired(), Email()])
      password = PasswordField('Password', validators=[DataRequired()])
      confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
      submit = SubmitField('Sign Up')

      def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()

            if user:
                  raise ValidationError('The username is taken, please enter a different username')

      def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()

            # if email:
            #       raise ValidationError('That email address is already in use, please enter a different email')


class LoginForm(FlaskForm):
      email = StringField('Email', validators=[DataRequired(), Email()])
      password = PasswordField('Password', validators=[DataRequired()])
      remember = BooleanField('Remember Me')
      submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
      username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
      email = StringField('Email', validators=[DataRequired(), Email()])
      picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
      submit = SubmitField('Update')

      def validate_username(self, username):
            if username.data != current_user.username:
                  user = User.query.filter_by(username=username.data).first()
                  if user:
                        raise ValidationError('The username is taken, please enter a different username')

      def validate_email(self, email):
            if email.data != current_user.username:
                  user = User.query.filter_by(email=email.data).first()
            # if user:
            #       raise ValidationError('The email aaddress is taken, please enter a different email address')


class RequestResetForm(FlaskForm):
      email = StringField('Email', validators=[DataRequired(), Email()])
      submit = SubmitField('Request Password Reset')

      def validate_email(self, email):
            if email.data != current_user.username:
                  user = User.query.filter_by(email=email.data).first()
            if user is None:
                  raise ValidationError('There is no account with that email address')

      
class ResetPasswordForm(FlaskForm):
      password = PasswordField('Password', validators=[DataRequired()])
      confirm_password = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password')])
      submit = SubmitField('Reset Password')