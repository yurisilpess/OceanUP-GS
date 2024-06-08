from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

# In-memory storage for contributors
contributors = []

@app.route('/')
def index():
    return render_template('index.html', contributors=contributors, count=len(contributors))

@app.route('/contribute', methods=['POST'])
def contribute():
    name = request.form['name']
    if name:
        contributors.append(name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
