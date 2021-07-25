from flask import Flask, render_template, request, url_for, session, g
from werkzeug.utils import redirect
import auth_model

app = Flask(__name__)

username = ''
app.secret_key = 'homEWO1rk3'

@app.before_request
def before_request():
	g.user = None
	if 'username' in session:
		g.user = auth_model.find_username(session['user_id'])

# The Static Pages
@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
	return render_template("about.html")

@app.route('/termsOfUse', methods=['GET'])
def terms():
	return render_template("terms_of_use.html")

@app.route('/privacy', methods=['GET'])
def privacy():
	return render_template("privacy.html")

@app.route('/dashboard', methods=['GET'])
def dashboard():
	return render_template("dashboard.html")

# The Authentication Routes
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == ['POST']:
		session.pop('user_id', None)

		user_id = auth_model.signup(
			username=request.form["username"],
			email=request.form["email"],
			password=request.form["password"]
			)
		
		session['user_id'] = user_id
		
		return redirect(url_for('dashboard'))
	return render_template("signup.html")
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == ['POST']:
		return
	return render_template("login.html")

if __name__ == '__main__':
	app.run(port=4000, debug=True)
