from flask import Blueprint, render_template, session
from app.utils.auth_utils import login_required

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET'])
@login_required
def home():
    print(f"Session: {session}")  # Print session values for debugging
    return render_template('index.html')