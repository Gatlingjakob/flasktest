from flask import Flask, render_template
import mysql.connector
<<<<<<< HEAD
import pandas as pd
=======
>>>>>>> 4630f4b22cc0ae407558b517cebcfb710fdf73aa

mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
<<<<<<< HEAD
	  passwd="password",
	  database="flaskapp"
=======
	  passwd="",
	  database="bets"
>>>>>>> 4630f4b22cc0ae407558b517cebcfb710fdf73aa
	)

mycursor = mydb.cursor()

<<<<<<< HEAD
df = pd.read_sql('SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 8 HOUR', con=mydb)
df = df[["HT_Name", "AT_Name", "HT_Score", "AT_Score", "MatchTime", "HT_Wins", "Draw", "AT_Wins"]]
df = df.iterrows()

#mycursor.execute("SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 4 HOUR")

#myresult = mycursor.fetchall()
#print (myresult, type(myresult))
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", data=df)
=======

mycursor.execute("SELECT * FROM BettingData WHERE Time >= NOW() - INTERVAL 10 MINUTE")

myresult = mycursor.fetchall()
print myresult, type(myresult)
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", data=myresult)
>>>>>>> 4630f4b22cc0ae407558b517cebcfb710fdf73aa
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)