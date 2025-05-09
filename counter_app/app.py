from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to use sessions

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html', count=session['count'])

@app.route('/add')
def add():
    session['count'] += 1
    return redirect(url_for('index'))

@app.route('/subtract')
def subtract():
    session['count'] -= 1
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
