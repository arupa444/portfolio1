from flask import Flask, render_template, request, flash, redirect, url_for, abort
from content import profile, projects, skills
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html',
                           profile=profile,
                           projects=projects,
                           skills=skills)

@app.route('/project/<project_id>')
def project_detail(project_id):
    # Find the project with the matching ID
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        abort(404)
    return render_template('project_detail.html', project=project, profile=profile)

@app.route('/contact', methods=['POST'])
def contact():
    # Mock contact form logic
    name = request.form.get('name')
    if not name:
        flash('Please enter your name.', 'error')
    else:
        flash(f'Message received, {name}! I will be in touch.', 'success')
    return redirect(url_for('index', _anchor='contact'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)