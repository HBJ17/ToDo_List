from flask import Flask,render_template
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

