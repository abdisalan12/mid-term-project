from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/Question', methods=['GET', 'POST'])
def Question():
    if request.method == 'POST':
        age = request.form['age']
        return render_template('age.html', age=age)
    return render_template("Question.html")


@app.route('/about')
def about():
    return '''<h1>Information about this website</h1>
<h2>This website consists 4 main pages</h2>
<p>  * Home page</p>
* About page    </p>
* Question      </p>
* Contact page  </p>
<h3>The main reason of this project is to show that
we can use python to create a website</h3>'''


@app.route('/Contact')
def Contact():
	return '''<h1>You can contact the developer of this website</h1>
<p>* Example.gmail.com</p>
<p>* +00998888777666777</p>
'''

if __name__ == "__main__":
    app.run(debug=True)
