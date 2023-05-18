from flask import Flask, render_template

app = Flask(__name__)

#settin gup rout
@app.route('/')

#temp inheritance, create one master and it'll be seen in other ones
def index():
    return render_template('index.html')

#to make sure it's ran directly from orig file rather than with import
if __name__ == "__main__":
    app.run(debug=True)

