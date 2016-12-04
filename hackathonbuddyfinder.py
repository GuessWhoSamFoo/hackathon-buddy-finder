from flask import Flask, g, render_template, request, redirect, url_for
from models import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# DISPLAY ALL THE IDEAS, uses ideas_list.html template currently
@app.route('/ideas', methods=["GET"])
def ideas_list():
    entries = show_all_ideas()
    return render_template("ideas_list.html", entries=entries)

# Show a from for creating a new idea (new.html), post is creating a new entry in ideas table
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

#  Display just one entry
@app.route('/ideas/<id>', methods=["GET"])
def ideas_id(id):
    one_idea = show_an_idea(id)
    return render_template("ideas_id.html", one_idea = one_idea)

    
if __name__ == "__main__":
    app.run()
