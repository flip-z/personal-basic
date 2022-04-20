
from flask import Flask, render_template, url_for, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4e895d495ab39301b88457d72968508'

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/rd2l', methods=['GET','POST'])
def scout():
	return render_template('rd2l.html')

@app.route('/me', methods=['GET', 'POST'])
def me():
	return render_template('me.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=False)
