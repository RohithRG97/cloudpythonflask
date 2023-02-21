from flask import Flask, render_template, request, url_for
import pypyodbc as odbc
 
app = Flask(__name__)

server = 'cloudsqlserver01.database.windows.net'
database = 'DemoDB'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cloudsqlserver001.database.windows.net,1433;Database=DemoDB;Uid=RohithGurram;Pwd={Demodbgrr@#4};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)


@app.route('/',  methods =["GET", "POST"])
def gfg():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        pop_range1 = request.form.get("prange1")
        pop_range2 = request.form.get("prange2")
        n_value = request.form.get("nval")
        
        cur = conn.cursor()
        sql1 = "select top "+n_value+" city, population from dbo.quiz2 where population >=" + pop_range1 +" AND POPULATION <= "+ pop_range2 + "ORDER BY POPULATION"
        cur.execute(sql1)
        data = cur.fetchall()

        sql2 = "select top "+n_value+" city, population from dbo.quiz2 where population >=" + pop_range1 +" AND POPULATION <= "+ pop_range2 + "ORDER BY POPULATION DESC"
        cur.execute(sql2)
        data2 = cur.fetchall()
        
        cur.close()

        return render_template("cities.html", citiesmin=data, citiesmax=data2)
    

    #return render_template('earthquake_range.html', rangedata = data) 

@app.route('/test')
def test():
    return 'Welcome Welcome Welcome'

@app.route('/home', methods = ['POST', 'GET'])
def route():
    if request.method == 'POST':
        range1 = request.form['range1']
        range2 = request.form['range2']

        return "The range is" + range1 + " and " + range2


if __name__ == "__main__":
    app.run(debug=True)

