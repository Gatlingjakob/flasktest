from flask import Flask, render_template
import mysql.connector

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="bets"
	)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 10 MINUTE")

myresult = mycursor.fetchall()
print myresult, type(myresult)
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", data=myresult)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)