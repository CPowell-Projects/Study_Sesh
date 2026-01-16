from flask import Flask, render_template, request, redirect, url_for
from datetime import date
import json
import os
DATA_FILE = "assignments.json"
app = Flask(__name__)

if os.path.exists(DATA_FILE):
    try:
        with open (DATA_FILE, "r" ) as f:
            assignments = json.load(f)
    except json.JSONDecodeError:
        assignments = []
    else:
        assignments =[]
def save_assignments():
    with open(DATA_FILE, "w") as f:
        json.dump(assignments, f, indent=2)

@app.route("/", methods=["GET","POST"])
def home():
    error = None
    acton = None
    if request.method == "POST":
        action = request.form.get("action")
        if action == "delete":
            index = int(request.form["delete_index"])
            if 0 <= index < len(assignments):
                assignments.pop(index)
                save_assignments()
                return redirect(url_for("home"))
        
        elif action == "add":
            course = request.form["course"]
            due = request.form["due"]
            today = date.today()
            due_date =date.fromisoformat(due)
            if due_date < today:
                error = "Cannot input date earlier than today"
            else: assignments.append({
                 "course": course,
                 "due": due

        })
        save_assignments()
        if error is None:
            return redirect(url_for("home"))
        assignments.sort(
                
            key=lambda assignment: date.fromisoformat(assignments["due"])
    )
    return render_template("assignments.html", assignments = assignments, error=error)

if __name__ == "__main__":
    app.run(debug=True)
 
