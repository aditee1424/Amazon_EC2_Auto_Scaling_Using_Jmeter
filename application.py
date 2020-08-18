from flask import Flask, render_template, request
import os
import pymysql

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = '' 

host = ''
user = ''
password = ''
database = ''
 
connection = pymysql.connect(host, user, password, database)

@application.route('/', methods=['GET','POST'])
def index():
  print("hello inside index")
  return render_template('home.html')

@application.route('/home', methods=['GET'])
def home():
  teachername = request.args.get('teacher')
  connection = pymysql.connect(host, user, password, database)
  if connection:
   print('database succes')

  cursor = connection.cursor()
  sql = "INSERT into Teacher (name) values (%s);"
  cursor.execute(sql,(teachername))
  connection.commit()

  sql1="select name from Teacher;"
  cursor.execute(sql1)
  result=cursor.fetchone()
  connection.commit()

  cursor.close()
  connection.close()
  return render_template('home.html',result=result)

@application.route('/question', methods=['GET'])
def question():
  question = request.args.get('question')
  connection = pymysql.connect(host, user, password, database)
  if connection:
   print('database succes')

  cursor = connection.cursor()
  sql = "INSERT into Teacher (question) values (%s);"
  cursor.execute(sql,(question))
  connection.commit()

  cursor.close()
  connection.close()
  return render_template('home.html')

@application.route('/studentname', methods=['GET'])
def studentname():
  connection = pymysql.connect(host, user, password, database)
  if connection:
   print('database succes')

  cursor = connection.cursor()
  sql2="select name from Student;"
  cursor.execute(sql2)
  result2=cursor.fetchall()
  connection.commit()

  cursor.close()
  connection.close()
  return render_template('home.html',result2=result2)

@application.route('/answer', methods=['GET'])
def answer():
  connection = pymysql.connect(host, user, password, database)
  if connection:
   print('database succes')

  cursor = connection.cursor()
  sql2="select answer from Student;"
  cursor.execute(sql2)
  answer=cursor.fetchall()
  connection.commit()

  cursor.close()
  connection.close()
  return render_template('home.html',answer=answer)

@application.route('/grades', methods=['GET'])
def grades():
  student = request.args.get('student')
  grades = request.args.get('grades')
  connection = pymysql.connect(host, user, password, database)
  if connection:
   print('database succes')

  cursor = connection.cursor()
  sql2="Update Student set grades=%s where name=%s;"
  cursor.execute(sql2,(grades,student))
  connection.commit()

  cursor.close()
  connection.close()
  return render_template('home.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0')
