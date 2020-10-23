import pyodbc
from cffi import model
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)
def get_db_connection():
    conn = pyodbc.connect("Driver= {SQL Server Native Client 11.0};"
                          'Server=new-front.database.windows.net;'
                          'Database=parcticeDB;'
                          "uid=admin001;"
                          "pwd=WelcomeAgent001;"
                          'Trusted_Connection=No;'
                          'Encrypt=Yes;')
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    title = ""
    if request.method == 'POST':
        conn = get_db_connection()
        roll = request.form["rollNo"]
        posts = conn.execute('SELECT * from dbo.Students where rollNo=?', (roll)).fetchall()
        conn.close()
        return render_template('output.html',posts = posts)
    else:
        return render_template('index.html')


def connect(roll):


    conn.close()

if __name__ == '__main__':
    app.run()