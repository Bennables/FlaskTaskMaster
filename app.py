from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABAS_URI'] = 'sqlite:///test.db'
#database initialized with data from app
db = SQLAlchemy(app)

class Todo(db.Model):
    #I assume this is the number for the task
    id = db.Column(db.Integer, primary_key = True)
    #this is the description for the task, 200chars max
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


#settin gup rout
@app.route('/')

#temp inheritance, create one master and it'll be seen in other ones
def index():
    return render_template('index.html')

#to make sure it's ran directly from orig file rather than with import
if __name__ == "__main__":
    app.run(debug=True)

