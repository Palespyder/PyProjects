from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for, session
from app.models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials (replace with actual validation logic)
        if username == 'admin' and password == 'password':
            session['logged_in'] = True  # Set session variable
            session['user_id'] = 'username'
            flash('Login successful!', 'success')
            return redirect(url_for('home_bp.home'))  # Redirect to home page
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')    
    

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    # Implement registration logic
    return jsonify({'message': 'Registration successful'})
