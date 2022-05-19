from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import User
from flask_login import current_user


class PostForm(FlaskForm):
      title = StringField('Title', validators=[DataRequired()])
      content = TextAreaField('Content', validators=[DataRequired()])
      category = SelectField('Categories', choices=[('Product Post'), ('Sales Post'), ('Business Post'), ('Interview Post')], validators=[DataRequired()])
      submit = SubmitField('Add Post')


class CommentForm(FlaskForm):
      comment = TextAreaField('Comment')
      submit = SubmitField('Submit')