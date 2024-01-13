from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"
debug = DebugToolbarExtension(app)

@app.route('/')
def madlib_home():
    prompts = story.prompts
    return render_template('madlib_home.html', prompts=prompts)

@app.route('/story')
def gen_story():
    text = story.generate(request.args)
    return render_template('starter_story.html', text=text)