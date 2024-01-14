from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Empty list to hold user responses
responses = []

@app.route('/')
def home():
    """Shows title/instructions for survey, as well as Start"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<int:q_id>')
def questions(q_id):
    """Shows questions, in intended order, protecting against tampering with the URL."""
    if len(responses) == len(satisfaction_survey.questions):
        flash("Thank you! You have already completed the survey.")
        return redirect('/thank-you')
    if q_id == len(responses):
        question = satisfaction_survey.questions[q_id].question
        choices = satisfaction_survey.questions[q_id].choices
        return render_template('questions.html', question=question, choices=choices)
    else:
        flash("Please complete survey questions in order!")
        return redirect(f'/questions/{len(responses)}')

@app.route('/thank-you')
def thank_you():
    """Thanks user for completing survey."""
    return render_template('thank_you.html')

@app.route('/answer/', methods=['POST'])
def add_response():
    """Stores responses to each question in survey (appends to responses list)"""
    response = request.form['response']
    responses.append(response)
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thank-you')
    else:
        return redirect(f'/questions/{len(responses)}')