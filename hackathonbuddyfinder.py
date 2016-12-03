from flask import Flask, g, render_template
from models import *
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/ideas', methods=["GET"])
def ideas_list():
    return render_template("ideas_list.html")
    
@app.route('/ideas/new', methods=["GET","POST"])
def new():
    author = request.form['author']
    title = request.form['title']
    description = request.form['description']
    max_num = request.form['max_num']
    return render_template("new.html")
    
@app.route('/ideas/<id>', methods=["GET"])
def ideas_id(id):
    
    return render_template("ideas_id.html", id = id)

    
if __name__ == "__main__":
    app.run()
