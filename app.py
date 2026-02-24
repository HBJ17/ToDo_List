from flask import Flask,render_template,request,redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("todo.db")

@app.route("/")
def index():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    db.close()
    return render_template("index.html",tasks=tasks)

@app.route("/add",method=["POST"])
def add():
    task = request.form["task"]
    db = get_db()
    db.execute("INSERT INTO tasks (task,done) VALUES (?,?)",(task,0))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/done/<int:id>")
def done(id):
    db = get_db()
    db.execute("UPDATE tasks SET done = 1 WHERE id = ?",(id,))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete():
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?",(id,))
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    db = get_db
    db.execute("""
                CREATE TABLE IF NOT EXIST tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                done INTEGER
            )
        """)
    db.close()
    app.run(debug=True)

