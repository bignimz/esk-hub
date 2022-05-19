from flask import Blueprint, render_template, request
from app.models import Pitch

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
      page = request.args.get('page', 1, type=int)
      pitches = Pitch.query.order_by(Pitch.date_posted.desc()).paginate(page=page, per_page=6)
      return render_template('index.html', pitches=pitches)


@main.route('/about')
def about():
      return render_template('about.html')