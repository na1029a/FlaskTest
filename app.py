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
    
if __name__ == '__main__':
    app.run(debug=True)
