from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['TESTING'] = True

class FlaskTests(TestCase):

    def test_display_board(self):
        """Check session / HTML"""
        with app.test_client() as client:
            resp = client.get('/board')

            "Check for session" 
            self.assertIn('BOARD_KEY', session)
            self.assertIsNone(session.get('high_score'))
            self.assertIsNone(session.get('times_played'))

            "Check for proper HTML" 
            self.assertIn(b'<p class="timer">', resp.data)
            self.assertIn(b'<form class="word-form"', resp.data)
            self.assertIn(b'<p class="score"', resp.data)
            self.assertIn(b'<p class="message"', resp.data)

    def test_check_word(self):
        """Modifies board for testing and checks word validity"""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['BOARD_KEY'] = [
                    ['B', 'O', 'A', 'R', 'D'],
                    ['B', 'O', 'A', 'R', 'D'],
                    ['B', 'O', 'A', 'R', 'D'],
                    ['B', 'O', 'A', 'R', 'D'],      
                    ['B', 'O', 'A', 'R', 'D']
                ]

        "Tests if word is valid / on board"
        resp = client.get('/words?word=board')
        self.assertEqual(resp.json['result'], 'ok')

        "Tests if word is valid / not on board"
        resp = client.get('/words?word=word')
        self.assertEqual(resp.json['result'], 'not-on-board')

        "Tests rejecting non-valid words"
        resp = client.get('/words?word=asdlkfsdf')
        self.assertEqual(resp.json['result'], 'not-word')
