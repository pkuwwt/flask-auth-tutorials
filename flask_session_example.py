from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
# Check Configuration section for more details
app.config['SECRET_KEY'] = 'aaaaaaaaaaaaaaaaaa'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

if __name__ == '__main__':
    app.run(debug=True)
