from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="student_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    if not title:
        return redirect('/add')

    cursor.execute("INSERT INTO tasks (title, status) VALUES (%s, %s)", (title, "Pending"))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)