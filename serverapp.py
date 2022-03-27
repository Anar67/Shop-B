#https://www.youtube.com/watch?v=759C2p3CAA4&t=1867s
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    price =db.Column(db.Integer, nullable = False) 
    isActive = db.Column(db.Boolean, default = True)
	#text = db.Column(db.Text, nullable = False)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')
	
	#return '<h1>Hello!!!! Anar</h1>'
if __name__ == "__main__":
    app.run(debug=True) #потом поменять на False 
	