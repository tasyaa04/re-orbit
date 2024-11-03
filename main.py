from data.users import User
from data.activities import Activity
from flask import Flask, render_template
from personality_quiz import take_quiz
from recommender import swiping

DEVELOPMENT_ENV = True
app = Flask(__name__)
@app.route('/')
def index():
    pass    # code for main window

@app.route('/hobbies')
def select_hobbies():
    pass

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()