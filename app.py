from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "meditrack.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    medicines = conn.execute("SELECT * FROM medicines").fetchall()
    conn.close()
    return render_template("index.html", medicines=medicines)


@app.route("/add", methods=["GET", "POST"])
def add_medicine():
    if request.method == "POST":
        name = request.form["name"]
        quantity = request.form["quantity"]
        expiry_date = request.form["expiry_date"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO medicines (name, quantity, expiry_date) VALUES (?, ?, ?)",
            (name, quantity, expiry_date),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)