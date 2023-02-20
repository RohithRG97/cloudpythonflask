from flask import Flask, render_template
import pypyodbc as odbc
 
app = Flask(__name__)

server = 'cloudsqlserver01.database.windows.net'
database = 'DemoDB'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cloudsqlserver001.database.windows.net,1433;Database=DemoDB;Uid=RohithGurram;Pwd={Demodbgrr@#4};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)

@app.route('/')


def home():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT * FROM dbo.earthquake_data")

    #if resultValue > 0:
    data = cur.fetchall()
    return render_template('home.html', data=data)
    

@app.route('/register')
def register():
    return render_template('register.html')