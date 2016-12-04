from flask import Flask, g, render_template, request, redirect, url_for
from models import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/ideas', methods=["GET"])
def ideas_list():
    entries = show_all_ideas()
    return render_template("ideas_list.html", entries=entries)
    
@app.route('/new', methods=["GET","POST"])
def new():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        description = request.form['description']
        max_num = request.form['max_num']
        # Adds new row to database
        create_new_idea(author, title, description, max_num)
        return redirect("/")
    return render_template("new.html")
    
@app.route('/ideas/<id>', methods=["GET"])
def ideas_id(id):
    
    return render_template("ideas_id.html", id = id)

    
if __name__ == "__main__":
    app.run()
