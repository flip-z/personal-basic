
from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4e895d495ab39301b88457d72968508'

db_name = 'sidequest.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

questdb = SQLAlchemy(app)

class Quest(questdb.Model):
    __tablename__ = 'quests'
    id = questdb.Column(questdb.Integer, primary_key=True)
    name = questdb.Column(questdb.String)
    description = questdb.Column(questdb.String)

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

@app.route('/sidequest', methods=['GET', 'POST'])
def sidequest():


	if request.method == 'POST':
		if request.form.get('action1') == 'VALUE1':
			pass # do something
		elif  request.form.get('action2') == 'VALUE2':
			pass # do something else
		else:
			pass # unknown
	elif request.method == 'GET':
		try:
			quests = Quest.query.order_by(Quest.name).all()
			return render_template('sidequest.html', quests=quests)
		except Exception as e:
			# e holds description of the error
			error_text = "<p>The error:<br>" + str(e) + "</p>"
			hed = '<h1>Something is broken.</h1>'
			return hed + error_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=False)
