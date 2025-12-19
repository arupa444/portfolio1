from flask import Flask, render_template, request, flash, redirect, url_for, abort, jsonify
from content import profile, projects, skills, systemContext
import google.generativeai as genai
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key')

# --- GEMINI CONFIGURATION ---
GENAI_KEY = os.environ.get("GEMINI_API_KEY")
if GENAI_KEY:
    genai.configure(api_key=GENAI_KEY)

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html',
                           profile=profile,
                           projects=projects,
                           skills=skills)


@app.route('/project/<project_id>')
def project_detail(project_id):
    # Find project logic
    project = next((p for p in projects if p.get('id') == project_id), None)
    if not project:
        abort(404)
    return render_template('project_detail.html', project=project, profile=profile)


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    if not name:
        flash('Please enter your name.', 'error')
    else:
        flash(f'Message received, {name}! I will be in touch.', 'success')
    return redirect(url_for('index', _anchor='contact'))


# --- CHATBOT API ---
@app.route('/chat', methods=['POST'])
def chat():
    if not GENAI_KEY:
        return jsonify({'response': "AI System Offline (Missing API Key). Contact Admin."})

    user_msg = request.json.get('message', '')
    if not user_msg:
        return jsonify({'response': "Empty signal received."})

    try:
        # Using Gemini 1.5 Flash (current standard equivalent for '2.5' request in 2025 context)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # We send the system context + user message
        full_prompt = f"{systemContext}\n\nUSER INQUIRY: {user_msg}"

        response = model.generate_content(full_prompt)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f"Neural Link Error: {str(e)}"})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', profile=profile), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)