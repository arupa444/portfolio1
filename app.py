from flask import Flask, render_template, request, flash, redirect, url_for, abort, jsonify, session
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

@app.route('/game')
def game():
    return render_template('game.html', profile=profile)

# ... existing routes ...

@app.route('/chat', methods=['POST'])
def chat():
    if not GENAI_KEY:
        return jsonify({'response': "AI System Offline (Missing API Key). Contact Admin."})

    user_msg = request.json.get('message', '')

    # --- CONTEXT LOGIC ---
    # Retrieve history from session or initialize empty list
    history = session.get('chat_history', [])

    # Create the prompt with history
    # We format history as a dialogue script to keep context
    conversation_so_far = ""
    for turn in history[-10:]:  # Keep last 10 turns to save tokens
        conversation_so_far += f"User: {turn['user']}\nAI: {turn['ai']}\n"

    full_prompt = f"{systemContext}\n\nCONVERSATION HISTORY:\n{conversation_so_far}\n\nCURRENT USER QUERY: {user_msg}\nAI RESPONSE:"

    try:
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        response = model.generate_content(full_prompt)
        ai_reply = response.text

        # Update History
        history.append({'user': user_msg, 'ai': ai_reply})
        session['chat_history'] = history

        return jsonify({'response': ai_reply})
    except Exception as e:
        return jsonify({'response': f"Neural Link Error: {str(e)}"})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', profile=profile), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)