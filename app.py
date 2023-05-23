from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from requests import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#database initialized with data from app

db = SQLAlchemy(app)



class Todo(db.Model):
    #I assume this is the number for the task
    id = db.Column(db.Integer, primary_key = True)
    #this is the description for the task, 200chars max
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r' % self.id

app.app_context().push()

#settin gup rout
#post get means we can send data rather than only get
@app.route('/',methods= ['POST','GET'])

#temp inheritance, create one master and it'll be seen in other ones
def index():
    if request.method == "POST":
        pass
    else:
        pass

    return render_template('index.html')

#to make sure it's ran directly from orig file rather than with import
if __name__ == "__main__":
    app.run(debug=True)

