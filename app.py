from flask import Flask, render_template, request, flash, redirect, url_for
from content import profile, skills, experience, projects
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html',
                           profile=profile,
                           skills=skills,
                           experience=experience,
                           projects=projects)


@app.route('/contact', methods=['POST'])
def contact():
    # In a real deployment, integrate SendGrid or SMTP here
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Mock Validation
    if not name or not email or not message:
        flash('Please fill out all fields.', 'error')
        return redirect(url_for('index', _anchor='contact'))

    # Success Animation Trigger via Flash
    flash(f'System: Message received from {name}. I will respond shortly.', 'success')
    return redirect(url_for('index', _anchor='contact'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)