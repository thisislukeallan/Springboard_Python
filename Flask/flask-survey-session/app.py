from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey

# key for the session:
RESPONSE_KEY = 'responses'

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Shows title/instructions for survey, as well as Start"""

    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template('home.html', title=title, instructions=instructions)

##############################################
            # Handle Sessions #
##############################################
@app.route('/start', methods=['POST'])
def create_response_sessions():
    """Initializes empty session to store responses"""

    session[RESPONSE_KEY] = []

    return redirect('/questions/0')

@app.route('/answer/', methods=['POST'])
def add_response():
    """Stores responses to each question in survey (appends to responses list)"""

    # pull response from form
    response = request.form['response']

    # add reponse to session
    responses = session[RESPONSE_KEY]
    responses.append(response)
    session['responses'] = responses

    # check if survey if any more questions : if complete redirect to thank you page
    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thank-you')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/questions/<int:q_id>')
def questions(q_id):
    """Shows questions, in intended order, protecting against tampering with the URL."""

    responses = session.get(RESPONSE_KEY)

    # check if survey is complete
    if len(responses) == len(satisfaction_survey.questions):
        flash("Thank you! You have already completed the survey.")
        return redirect('/thank-you')
    
    # make sure they are answering questions in right order / not tampering with URL
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


    
