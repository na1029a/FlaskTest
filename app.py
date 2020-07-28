from flask import Flask,render_template
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

if __name__ == '__main__':
    app.run(debug=True)
