from flask import Flask, render_template, request, session # gives access to a variable called `session`
from flask_session import Session
app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file
                                                  
note = [];
@app.route('/notes', methods=["POST", "GET"])
def notes():
    if request.method == "POST":
        notes = request.form.get("note")
        note.append(notes)
    
    return render_template('index.html', notes=note)