import os
import secrets
from PIL import Image
from flask_mail import Message
from app import app

# Function to save picture
def save_picture(form_picture):
      random_hex = secrets.token_hex(8)
      _, f_ext = os.path.splitext(form_picture.filename)
      picture_fn = random_hex + f_ext
      picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
      
      form_picture.save(picture_path)
      return picture_fn


def send_reset_email(user):
      token = user.get_reset_token()
      msg = Message('Password Reset Request', sender='noreply@gmail.com', recipients=[user.email])
      msg.body = f' To reset your password, visit the following link'
      {url_for('reset_token', token=token, _external=True)}
      mail.send(msg)