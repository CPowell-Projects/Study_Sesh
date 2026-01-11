from flask import Flask, render_template, request
from datetime import date
app = Flask(__name__)

assignments = []

@app.route("/", methods=["GET","POST"])
def home():
    error = None
    if request.method == "POST":
        if "delete_index" in request.form:
            index = int(request.form["delete_index"])
            if 0 <= index < len(assignments):
                assignments.pop(index)

        else:
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
            assignments.sort(
                
            key = lambda assignments: date.fromisoformat(assignments["due"])
    )
    return render_template("assignments.html", assignments = assignments, error=error)

if __name__ == "__main__":
    app.run(debug=True)
 
