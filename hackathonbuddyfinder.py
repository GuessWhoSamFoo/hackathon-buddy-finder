from flask import Flask, g, render_template, request, redirect, url_for, jsonify
from models import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# DISPLAY ALL THE IDEAS, uses ideas_list.html template currently
@app.route('/ideas', methods=["GET"])
def ideas_list():
    entries = show_all_ideas()
    all_columns = column_names()
    return jsonify({ 'entries': all_columns} )

# Show a from for creating a new idea (new.html), post is creating a new entry in ideas table
@app.route('/new', methods=["POST"])
def new():
    creator_name = request.form['creator_name']
    creator_role = request.form['creator_role']
    project_name = request.form['project_name']
    project_desc = request.form['project_desc']
    tags = request.form['tags']
    spots = request.form['spots']
    position_one = request.form['position_one']
    position_one_owner = None
    position_two = request.form['position_two']
    position_two_owner = None
    create_new_idea(creator_name, creator_role, project_name, project_desc, spots, tags, position_one, position_one_owner, position_two, position_two_owner)
    return render_template("", 204)
  
@app.route('/join', methods=["POST"])  
def positions():
    position_one_owner = request.form['position_one_owner']
    position_two_owner = request.form['position_two_owner']
    return render_template("", 204)

#  Display just one entry
@app.route('/ideas/<id>', methods=["GET"])
def ideas_id(id):
    one_idea = show_an_idea(id)
    return render_template("ideas_id.html", one_idea = one_idea)

    
if __name__ == "__main__":
    app.run()
