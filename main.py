from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", 
                         style = "/static/css/style.css",
                         image ='/static/img/poto.webp')

@app.route('/calc')
def calc():
  n1 = 55
  n2 = 108
  return render_template('calc.html',
                         num1=n1,
                         num2=n2)

   

app.run(debug=True)