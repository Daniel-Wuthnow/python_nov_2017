from flask import Flask, render_template, request, redirect, session, flash
import md5
import re
import os, binascii
app = Flask(__name__)
password = 'password'
hashed_password = md5.new(password).hexdigest()
print hashed_password
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'mydb')

app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
	errors = False
	if len(request.form['first_name']) < 2:
		errors = True
		flash('First Name not Valid', 'f_name')
	if len(request.form['last_name']) < 2:
		errors = True
		flash('Last Name not Valid', 'l_name')
	if len(request.form['email']) < 1:
		errors = True
		flash("You need to have an email", "email")
	elif not EMAIL_REGEX.match(request.form['email']):
		errors = True
		flash('Invalid Email Address!', "email")
	if len(request.form['password']) < 8:
		errors = True
		flash('Password is not Valid', 'password')
	if request.form['password'] != request.form['password_comp']:
		errors = True
		flash('Passwords do not match', 'password_comp')
	if request.form['action'] == 'reg' and errors == False:
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email = request.form['email']
		password = request.form['password']
		salt = binascii.b2a_hex(os.urandom(15))
		hashed_pw = md5.new(password + salt).hexdigest()
		insert_query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"
		print insert_query
		query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'hashed_pw': hashed_pw, 'salt':salt}
		print query_data
		mysql.query_db(insert_query, query_data)
		return redirect('/')
	else:
		return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	if request.form['action'] == 'login':
		password = request.form['password']
		email = request.form['email']
		#log_reg_query = "SELECT * FROM log_reg where log_reg.email = :email AND log_reg.password = :password"
		users_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
		query_data = { 'email': email}
		# print query_data
		users = mysql.query_db(users_query, query_data)
		# print users
		if len(users) != 0:
			encrypted_password = md5.new(password + users[0]['salt']).hexdigest()
			if users[0]['password'] == encrypted_password:
				session['user'] = request.form['email']
				session['first_name'] = users[0]['first_name']
				session['last_name'] = users[0]['last_name']
				session['id'] = users[0]['id']
				return redirect('/wall')
			else:
				flash("Invalid Password", 'password_log')
				return redirect('/')
		else:
			flash("Invalid Email", 'email_log')
			return redirect('/')

@app.route('/message', methods=['GET', 'POST'])
def message():
	users_id = "SELECT id FROM users where users.email = '"+ session['user'] +"'"
	temp = mysql.query_db(users_id)
	print temp

	message = request.form['message']
	print message
	message_query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :users_id)"

	query_data = { 
		'message': message,
		'users_id': temp[0]['id']
	}
	mysql.query_db(message_query, query_data)
	return redirect('/wall')

@app.route('/comment', methods=['POST'])
def comment():
	comment = request.form['comment']
	comment_query = "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :messages_id, :users_id)"
	query_data = {
		'comment': comment,
		'messages_id': request.form['post_id'],
		'users_id': session['id']
	}
	
	mysql.query_db(comment_query, query_data)
	return redirect('/wall')

@app.route('/wall', methods=['GET'])
def wall():
	query = "SELECT users.id, concat(users.first_name,' ', users.last_name) as name, messages.message as message, date_format(messages.created_at, '%Y %M %D') as message_date, messages.id as message_id, comments.id as comment_id, comments.comment as comment, date_format(comments.created_at, '%Y %M %D') as comment_date FROM USERS left join messages on users.id = messages.user_id left join comments on messages.id = comments.message_id ORDER BY message_id desc, comment_id asc"
	#"SELECT a.id as user_id, concat(a.first_name,' ', a.last_name) as post_name, date_format(messages.created_at, '%Y %M %D') as post_date, c.id as comment_id, c.comment as comment, date_format(c.created_at, '%Y %M %D') as comment_date, concat(d.first_name,' ', d.last_name) as comment_name FROM users a "
	#join messages b on a.id = b.users_id "
	#left join comments c on b.id = c.messages_id left join users    d on d.id = c.users_id order by post_id, comment_id"
	messages = mysql.query_db(query)
	# print messages
	return render_template('success.html', messages=messages)

@app.route('/logout', methods=['POST'])
def logout():
	print "test"
	session.clear()
	return redirect('/')


app.run(debug=True)