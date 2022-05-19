from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
      return User.query.get(int(user_id))


class User(db.Model, UserMixin):
      __tablename__ = 'users'
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(200), unique=True, nullable=False)
      email = db.Column(db.String(120), unique=True, nullable=False)
      image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
      password = db.Column(db.String(60), nullable=False)
      posts = db.relationship('Post', backref='author', lazy=True)
      comments = db.relationship('Comment', backref='author', lazy=True)

      def get_reset_token(self, expires_sec=1800):
            s = Serializer(app.config['SECRET_KEY'], expires_sec)
            return s.dumps({'user_id': self.id}).decode('utf8')

      @staticmethod
      def verify_reset_token(token):
            s = Serializer(app.config['SECRET_KEY'])
            try:
                  user_id = s.loads(token)['user_id']
            except:
                  return None
            return User.query.get(user_id)

      def __repr__(self):
            return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
      __tablename__ = 'posts'
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(100), nullable=False)
      content = db.Column(db.Text, nullable=False)
      category = db.Column(db.Text, nullable=False)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
      comments = db.relationship('Comment', backref='post', lazy=True)
      
      def __repr__(self):
            return f"Post('{self.title}', '{self.content}', '{self.category}', '{self.date_posted}')"



class Comment(db.Model):
      __tablename__ = 'comments'
      id = db.Column(db.Integer, primary_key=True)
      comment = db.Column(db.Text, nullable=False)
      posted_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
      user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
      post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

      
      def save_comment(self):
            db.session.add(self)
            db.session.commit()

      @classmethod
      def get_comment(cls,id):
            comments = Comment.query.filter_by(post_id=id).all()
            return comments
      
      def __repr__(self):
            return f"Comment('{self.comment}', '{self.posted_date}')"


class Quotes:
      def __init__(self, author, quote):

            self.author = author
            self.quote = quote