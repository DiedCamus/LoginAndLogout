import sqlite3
def connect_db():
	return  sqlite3.connect("user.db")
def show_db():
	coon = connect_db()
	c = coon.cursor()
	out = c.execute("SELECT * FROM USERS WHERE username='hello'")
	if out:
		print "hello exists"
	else:
		print "no user named hello"
	#for row in out:
	#	print "id = ", row[0]
	#	print "name = ", row[1]
	#	print "password = ", row[2], "\n"
	coon.close()

