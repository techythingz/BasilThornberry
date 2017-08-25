import psycopg2
from flask import Flask
from flask import render_template
from flask import request 
from flask import session 
from flask import url_for, redirect, escape
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/basil")
def showIndex():
	return render_template('index.html')

@app.route("/connect")
def showadded():
	return render_template('connect.html')

@app.route("/addstuff", methods=['POST'])
def addStuff():

	session['databasename'] = request.form['dbname']
	session['host'] = request.form['hostname']
	session['user'] = request.form['username']
	session['password'] = request.form['password']
	session['port'] = request.form['port']
	return connektBasilR()
	#return render_template("othertest.html")

@app.route("/test")
def testHTML():
    return render_template('test.html')

@app.route("/showdata", methods=['POST'])
def showData():
	session['chosentable']=request.form['chosentable']
	connektBasil(request.form['chosentable'])
	return render_template("othertest.html")

def connektBasilR():
	mydatabase = session['databasename']
	myuser = session['user'] 
	mypassword = session['password'] 
	myhost = session['host']
	myport = session['port']

	theList = []

	try:
	    conn = psycopg2.connect(database=mydatabase, user=myuser, password=mypassword, host=myhost, port=myport)
	except:
	    return "Unable to connect to the database" 
	cursor = conn.cursor()
	cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
	alltables = cursor.fetchall()
	oneTable = cursor.fetchone();
	return "%s" % oneTable

def connektBasil(tablename):
	mydatabase = session['databasename']
	myuser = session['user'] 
	mypassword = session['password'] 
	myhost = session['host']
	myport = session['port']

	theList = []

	try:
	    conn = psycopg2.connect(database=mydatabase, user=myuser, password=mypassword, host=myhost, port=myport)
	except:
	    return "Unable to connect to the database" 
	cursor = conn.cursor()
	cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
	alltables = cursor.fetchall()
	table = tablename

	for oneTable in alltables:
  		stripped = "%s" % oneTable
  		theList.append(stripped)
  	
  	showsql="select * from "+table
	cursor.execute(showsql)
	colnames = [desc[0] for desc in cursor.description]
	values = cursor.fetchall()

	cursor.close()	    	    
	session['alltables']=theList
	session['colnames']=colnames
	session['values']=values

