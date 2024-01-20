from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

# key for the session:
BOARD_KEY = 'board'

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/board')
def display_board():
    """ Builds and displays Boggle game board. """
    board = boggle_game.make_board()
    session['BOARD_KEY'] = board
    high_score = session.get("high_score", 0)
    times_played = session.get("times_played", 0)

    return render_template('board.html', board=board, high_score=high_score, times_played=times_played)

@app.route('/words')
def check_word():
    """Checks if word is in word list"""
    word = request.args['word']
    board = session['BOARD_KEY']
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route('/store-score', methods=['POST'])
def store_score():
    """Stores score in the session and checks if new high score."""
    data = request.json
    score = data['score']

    high_score = session.get("high_score", 0)
    times_played = session.get("times_played", 0)

    session['high_score'] = max(score, high_score)
    session['times_played'] = times_played + 1

    return jsonify(newRecord = score > high_score)
    