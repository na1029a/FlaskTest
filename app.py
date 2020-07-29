from flask import Flask,render_template,redirect,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/hello')    
def greet():
    return render_template('index.html')

@app.route('/top')
def top():
    return "これがトップページや"


@app.route('/hello/<text>')    
def namehello(text):
    return text + "さんこんにちは"    

@app.route('/index')    
def index():
    name = "ashihara"
    age = 19
    addres = "幸町"
    return render_template('index.html',user_name = name,user_address = addres,user_age = age)
    
    
@app.route('/weather')
def weather():
    weather = "ハレのちユキ"
    return render_template('weather.html',today_weather = weather)    

@app.route('/dbtest')    
def dbtest():
    #dbと接続
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    #SQLの命令をかく
    c.execute("SELECT name,age,address FROM user WHERE id = 1")
    user_info = c.fetchone()
    #DBの終了
    print(user_info)
    return render_template('dbtest.html',db_userinfo = user_info)


#TODOアプリ
@app.route('/add')
def add_get():
    return render_template('add.html')

@app.route('/add',methods = ['post'])
def app_post():
    py_task = request.form.get("task")
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("INSERT INTO task VALUES (null,?)",(py_task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/list')
def task_list():
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("SELECT id , task FROM task")   
    task_list_py = []
    for row in c.fetchall():
        task_list_py.append({"id":row[0],"task":row[1]})
    c.close()
    print(task_list_py)
    return render_template("tasklist.html",task_list = task_list_py)

@app.errorhandler(404)
def notfound(code):
    return "404 Not Found😯"
    
if __name__ == '__main__':
    app.run(debug=True)
